"""Playbook de clustering: diagnostica los datos y sugiere un algoritmo inicial."""
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import skew
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN, MeanShift, estimate_bandwidth
from sklearn.mixture import GaussianMixture
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import silhouette_score, adjusted_rand_score

def _knee_eps(Xs, min_samples):
    """eps = punto del codo en la curva de distancias al k-ésimo vecino (el más alejado de la recta)."""
    d = np.sort(NearestNeighbors(n_neighbors=min_samples).fit(Xs).kneighbors(Xs)[0][:, -1])
    x = np.arange(len(d)); p1, p2 = np.array([0, d[0]]), np.array([len(d)-1, d[-1]])
    v = (p2 - p1) / np.linalg.norm(p2 - p1)
    dist = np.abs((np.c_[x, d] - p1) @ np.array([-v[1], v[0]]))
    return float(d[dist.argmax()]), d

def _eps_meseta(Xs, ms, kd):
    """Prueba un rango de eps y toma la meseta más larga donde el nº de grupos (>=2) se mantiene estable con poco ruido."""
    grid = np.geomspace(np.quantile(kd, 0.5), 4 * np.quantile(kd, 0.99), 40); runs = []
    for e in grid:
        lab = DBSCAN(eps=e, min_samples=ms).fit_predict(Xs)
        k = len(set(lab)) - (1 if -1 in lab else 0); runs.append((e, k, float((lab == -1).mean())))
    best, cur = [], []
    for e, k, nz in runs:
        if k >= 2 and nz <= 0.10 and (not cur or cur[-1][1] == k): cur.append((e, k, nz))
        else:
            if len(cur) > len(best): best = cur
            cur = [(e, k, nz)] if (k >= 2 and nz <= 0.10) else []
    if len(cur) > len(best): best = cur
    return float(np.median([b[0] for b in best])) if len(best) >= 3 else None

def _solape_convexo(Z, lab):
    """% de puntos de OTROS grupos que caen dentro de la envolvente convexa de cada grupo (en 2D). Alto = grupos no convexos."""
    from scipy.spatial import Delaunay
    ids = [g for g in set(lab) if g != -1]; tot = inside = 0
    for g in ids:
        P = Z[lab == g]
        if len(P) < 4: continue
        h = Delaunay(P); others = Z[(lab != g) & (lab != -1)]
        inside += int((h.find_simplex(others) >= 0).sum()); tot += len(others)
    return inside / tot if tot else 0.0

def diagnostico_clustering(df, cols=None, k_range=range(2, 9), seed=42, grafico=None):
    # ---- Paso 1: preparar ----
    X = df[cols] if cols else df.select_dtypes("number")
    X = X.dropna().reset_index(drop=True)
    Xs = StandardScaler().fit_transform(X); n, d = Xs.shape
    # ---- Paso 2: explorar ----
    out_share = float((np.abs(Xs) > 3).any(axis=1).mean())
    med = np.median(Xs, axis=0); mad = np.median(np.abs(Xs - med), axis=0) * 1.4826 + 1e-9
    rob_out = float((np.abs((Xs - med) / mad) > 3.5).any(axis=1).mean())   # z robusto (mediana/MAD): no se infla con los atípicos
    sk = float(np.nanmax(np.abs(skew(Xs, axis=0))))
    cm = np.corrcoef(Xs.T) if d > 1 else np.array([[1.]])
    maxcorr = float(np.max(np.abs(cm - np.eye(d)))) if d > 1 else 0.0
    # ---- Paso 5: parámetros (k) ----
    ks = list(k_range)
    km_sil = {k: silhouette_score(Xs, KMeans(k, n_init=10, random_state=seed).fit_predict(Xs)) for k in ks}
    k_km = max(km_sil, key=km_sil.get)
    bic = {k: GaussianMixture(k, covariance_type="full", n_init=3, random_state=seed).fit(Xs).bic(Xs) for k in ks}
    k_gmm = min(bic, key=bic.get)
    ms_n = max(5, 2 * d)
    eps_knee, kd = _knee_eps(Xs, ms_n)
    eps = _eps_meseta(Xs, ms_n, kd) or eps_knee
    db = DBSCAN(eps=eps, min_samples=ms_n).fit_predict(Xs)
    k_db = len(set(db)) - (1 if -1 in db else 0); noise = float((db == -1).mean())
    # ---- Paso 3: diagnóstico de forma (acuerdo entre algoritmos) ----
    km_lab = KMeans(k_km, n_init=10, random_state=seed).fit_predict(Xs)
    gm_lab = GaussianMixture(k_gmm, covariance_type="full", n_init=3, random_state=seed).fit_predict(Xs)
    ari_km_gmm = adjusted_rand_score(km_lab, gm_lab) if k_gmm > 1 else np.nan
    ok = db != -1
    ari_km_db = adjusted_rand_score(km_lab[ok], db[ok]) if k_db >= 2 and ok.sum() > 10 else np.nan
    Z2 = PCA(2, random_state=seed).fit_transform(Xs) if d > 2 else (Xs if d == 2 else np.c_[Xs, np.zeros(n)])
    solape = _solape_convexo(Z2, db) if k_db >= 2 else 0.0
    # ---- Paso 4: decisión ----
    razones = []
    if k_db >= 2 and noise < 0.30 and solape > 0.05:
        rec = "DBSCAN"; razones.append(f"Los grupos no son convexos: {solape:.0%} de los puntos de otros grupos caen dentro de la envolvente de un grupo (DBSCAN halla {k_db} grupos, {noise:.0%} ruido).")
    elif k_db >= 2 and noise >= 0.02 and not np.isnan(ari_km_db) and ari_km_db >= 0.9:
        rec = "DBSCAN (o K-Means tras retirar atípicos)"; razones.append(f"DBSCAN marca {noise:.0%} de filas como ruido (puntos aislados) y fuera de ellos coincide con K-Means (ARI={ari_km_db:.2f}): hay atípicos que arrastrarían a K-Means.")
    elif not np.isnan(ari_km_gmm) and ari_km_gmm < 0.8 and k_gmm >= 2:
        rec = "GMM"; razones.append(f"Grupos convexos pero K-Means y GMM discrepan (ARI={ari_km_gmm:.2f}): elípticos o traslapados; BIC sugiere k={k_gmm}.")
    else:
        rec = "K-Means"; razones.append(f"Grupos convexos, sin atípicos relevantes y K-Means≈GMM (ARI={ari_km_gmm:.2f}); silhouette máx. {km_sil[k_km]:.2f} en k={k_km}.")
    res = dict(n=n, d=d, atipicos_z3=round(out_share, 3), atipicos_zrobusto=round(rob_out, 3), asimetria_max=round(sk, 2), corr_max=round(maxcorr, 2),
               k_silhouette=k_km, silhouette=round(km_sil[k_km], 3), k_bic_gmm=k_gmm,
               dbscan_eps=round(eps, 3), dbscan_min_samples=ms_n, dbscan_grupos=k_db, dbscan_ruido=round(noise, 3),
               ari_kmeans_gmm=None if np.isnan(ari_km_gmm) else round(ari_km_gmm, 3),
               ari_kmeans_dbscan=None if np.isnan(ari_km_db) else round(ari_km_db, 3), solape_convexo=round(solape, 3),
               recomendacion=rec, razones=razones)
    if grafico:
        Z = PCA(2, random_state=seed).fit_transform(Xs) if d > 2 else (Xs if d == 2 else np.c_[Xs, np.zeros(n)])
        fig, ax = plt.subplots(1, 4, figsize=(18, 4))
        ax[0].scatter(Z[:, 0], Z[:, 1], s=8); ax[0].set_title("Paso 2: forma de los datos (PCA 2D)")
        ax[1].plot(ks, [km_sil[k] for k in ks], "o-"); ax[1].set_title("Silhouette K-Means vs k"); ax[1].set_xlabel("k")
        ax[2].plot(ks, [bic[k] for k in ks], "o-"); ax[2].set_title("BIC GMM vs k (menor = mejor)"); ax[2].set_xlabel("k")
        ax[3].plot(kd); ax[3].axhline(eps, ls="--", c="r"); ax[3].set_title(f"k-distancia (eps≈{eps:.2f})")
        plt.tight_layout(); fig.savefig(grafico, dpi=110); plt.close(fig)
    return res
