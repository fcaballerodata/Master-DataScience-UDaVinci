"""UD09 Minería · (1) MLP con optimizadores sgd/adam/lbfgs en cáncer de mama; (2) red de Hopfield desde cero (N=100): recuperación con ruido, capacidad y energía.
"""
import numpy as np, time, warnings; warnings.filterwarnings("ignore")
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score
X, y = load_breast_cancer(return_X_y=True); y = 1 - y
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.25, stratify=y, random_state=42)
print("== MLP por optimizador (cáncer de mama, 1=maligno) ==")
base = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)).fit(Xtr, ytr)
print(f"logística: train {base.score(Xtr,ytr):.3f} prueba {base.score(Xte,yte):.3f} recall {recall_score(yte, base.predict(Xte)):.3f}")
for solver in ("sgd", "adam", "lbfgs"):
    m = make_pipeline(StandardScaler(), MLPClassifier((16,), solver=solver, max_iter=2000, random_state=42))
    t0 = time.time(); m.fit(Xtr, ytr); dt = time.time() - t0; r = m[-1]
    print(f"{solver:6s} iter {r.n_iter_:4d} | pérdida final {r.loss_:.4f} | train {m.score(Xtr,ytr):.3f} prueba {m.score(Xte,yte):.3f} recall {recall_score(yte,m.predict(Xte)):.3f} | {dt:.2f}s")
m = make_pipeline(StandardScaler(), MLPClassifier((16,), solver="adam", max_iter=2000, random_state=42)).fit(Xtr, ytr)
lc = m[-1].loss_curve_; print("pérdida adam (iter 1, 10, 50, última):", [round(lc[i],4) for i in (0, 9, 49, len(lc)-1)])
print("sin estandarizar adam:", round(MLPClassifier((16,), max_iter=2000, random_state=42).fit(Xtr,ytr).score(Xte,yte),3))
print("semillas adam (prueba):", [round(make_pipeline(StandardScaler(), MLPClassifier((16,), max_iter=2000, random_state=s)).fit(Xtr,ytr).score(Xte,yte),3) for s in range(5)])
# ---------- Hopfield ----------
print("\n== Hopfield (N=100 neuronas binarias ±1) ==")
def entrenar(P): N = P.shape[1]; W = P.T @ P / N; np.fill_diagonal(W, 0); return W
def energia(W, s): return -0.5 * s @ W @ s
def recuperar(W, s, rng, max_barridos=50):
    s = s.copy(); E = [energia(W, s)]
    for _ in range(max_barridos):
        cambio = False
        for i in rng.permutation(len(s)):
            nuevo = 1 if W[i] @ s >= 0 else -1
            if nuevo != s[i]: s[i] = nuevo; cambio = True
        E.append(energia(W, s))
        if not cambio: break
    return s, E
rng = np.random.default_rng(42); N = 100
for k in (3, 10, 20):
    P = rng.choice([-1, 1], size=(k, N)); W = entrenar(P); ok = 0; ens = 0; mono = True
    for rep in range(20):
        p = P[rep % k]; s = p.copy(); flip = rng.choice(N, 10, replace=False); s[flip] *= -1   # 10% ruido
        r, E = recuperar(W, s, rng); ok += int((r == p).all()); mono &= all(np.diff(E) <= 1e-9)
    print(f"{k:2d} patrones: recupera exacto {ok}/20 | energía nunca sube: {mono} | k/N = {k/N:.2f}")
