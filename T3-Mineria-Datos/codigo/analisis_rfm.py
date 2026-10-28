"""Análisis RFM de una base de clientes: limpieza, transformación y segmentación con K-Means.
Uso:  python analisis_rfm.py ruta/BaseClientes.csv
Columnas esperadas: partner_vat_num, fecha_primera_compra, fecha_ultima_compra, fecha_corte,
                    dias_ultima_compra, numero_compras, monto_total (texto con "$").
NOTA: la base real contiene identificadores de clientes y NO se incluye en el repositorio."""
import sys, warnings; warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, adjusted_rand_score

df = pd.read_csv(sys.argv[1], encoding="utf-8-sig", dtype=str)           # utf-8-sig quita el BOM del encabezado
df["M"] = df.monto_total.str.replace(r"[^\d.\-]", "", regex=True).astype(float)   # "$330100" -> 330100.0
df["R"] = df.dias_ultima_compra.astype(int); df["F"] = df.numero_compras.astype(int)
for c in ["fecha_primera_compra", "fecha_ultima_compra", "fecha_corte"]: df[c] = pd.to_datetime(df[c])

# --- Auditoría ---
print("filas:", len(df), "| IDs duplicados:", df.partner_vat_num.duplicated().sum())
print("recencia inconsistente con la fecha de corte:", ((df.fecha_corte - df.fecha_ultima_compra).dt.days != df.R).sum())
print("primera compra posterior a la última:", (df.fecha_primera_compra > df.fecha_ultima_compra).sum())
bad = df.partner_vat_num.str.len() > 12; print("IDs mal formados (>12 dígitos):", bad.sum())
print("monto = 0:", (df.M <= 0).sum(), "| clientes con una sola compra:", round((df.F == 1).mean(), 3))
print("asimetría R, F, M:", df[["R", "F", "M"]].skew().round(2).to_dict())

# --- Limpieza ---
d = df[(df.M > 0) & (~bad)].copy(); print("filas tras limpiar:", len(d))

# --- Visualización: antes y después del logaritmo ---
fig, ax = plt.subplots(2, 3, figsize=(13, 6))
for i, (c, n) in enumerate([("R", "recencia"), ("F", "frecuencia"), ("M", "monto")]):
    ax[0, i].hist(d[c], bins=50); ax[0, i].set_title(f"{n} (original)")
    ax[1, i].hist(np.log1p(d[c]), bins=50, color="C1"); ax[1, i].set_title(f"log(1+{n})")
plt.tight_layout(); plt.savefig("hist_rfm_clientes.png", dpi=110); plt.close()

# --- Transformar, estandarizar y comparar k (silhouette con muestra de 6000 por memoria) ---
X = d[["R", "F", "M"]].astype(float).copy(); X["F"] = np.log1p(X.F); X["M"] = np.log1p(X.M)
Xs = StandardScaler().fit_transform(X)
idx = np.random.default_rng(42).choice(len(d), 6000, replace=False)
print("silhouette por k:", {k: round(silhouette_score(Xs[idx], KMeans(k, n_init=10, random_state=42).fit(Xs).labels_[idx]), 3) for k in range(2, 8)})

# --- Segmentación final (k elegido por criterio de negocio) y estabilidad ---
K = 4; lab = KMeans(K, n_init=10, random_state=42).fit_predict(Xs); d["segmento"] = lab
print(d.groupby("segmento").agg(n=("M", "size"), R=("R", "median"), F=("F", "median"), M=("M", "median"))
        .round(0).assign(pct=lambda x: (x.n / x.n.sum() * 100).round(1)).to_string())
print("estabilidad (ARI vs otras semillas):", [round(adjusted_rand_score(lab, KMeans(K, n_init=10, random_state=s).fit_predict(Xs)), 3) for s in (1, 7, 123)])
