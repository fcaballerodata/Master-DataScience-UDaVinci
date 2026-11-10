"""UD10 ML · Interpretación de resultados: medidas de error (MSE, MAE, RMSE, RMSLE, R², Log Loss),
error aceptable (benchmark y tolerancia ±20 %) y diagnóstico con curvas de aprendizaje y residuos.
Clasificación: Breast Cancer Wisconsin (real, scikit-learn). Regresión: montos de facturación SIMULADOS."""
import numpy as np, warnings; warnings.filterwarnings("ignore")
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, StratifiedKFold, learning_curve
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.dummy import DummyRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.compose import TransformedTargetRegressor
from sklearn.metrics import (accuracy_score, log_loss, roc_auc_score, average_precision_score,
                             mean_absolute_error, mean_squared_error, r2_score)

# A. Clasificación: la exactitud no basta; Log Loss mide la calidad de las probabilidades
d = load_breast_cancer(); X, y = d.data, 1 - d.target            # 1 = maligno
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.25, stratify=y, random_state=42)
print("== A. Clasificación (cáncer de mama, real) ==")
for n, m in {"Random Forest": RandomForestClassifier(300, random_state=42),
             "Logística": make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)),
             "Naive Bayes": GaussianNB()}.items():
    p = m.fit(Xtr, ytr).predict_proba(Xte)[:, 1]
    print(f"{n:14s} acc {accuracy_score(yte, p >= .5):.3f} | LogLoss {log_loss(yte, p):.3f} | "
          f"AUC {roc_auc_score(yte, p):.3f} | AP {average_precision_score(yte, p):.3f}")

# B. Regresión (SIMULADA): medidas de error y benchmark
rng = np.random.default_rng(42); n = 3000
x1 = rng.uniform(0, 10, n); x2 = rng.integers(0, 3, n)
monto = np.exp(8 + .25*x1 + .4*x2 + rng.normal(0, .35, n))*(1 + .04*(x1 - 5)**2)
Z = np.c_[x1, x2]
Ztr, Zte, mtr, mte = train_test_split(Z, monto, test_size=.25, random_state=42)
def rmsle(a, b): return np.sqrt(np.mean((np.log1p(a) - np.log1p(np.clip(b, 0, None)))**2))
modelos = {"Media (benchmark)": DummyRegressor(),
           "Lineal": LinearRegression(),
           "MLP (32,16)": TransformedTargetRegressor(
               make_pipeline(StandardScaler(), MLPRegressor(hidden_layer_sizes=(32, 16), max_iter=3000, random_state=42)),
               transformer=StandardScaler())}
print("\n== B. Regresión (simulada) ==")
res = {}
for nm, m in modelos.items():
    pr = m.fit(Ztr, mtr).predict(Zte); res[nm] = pr
    mse = mean_squared_error(mte, pr)
    dentro = np.mean(np.abs(pr - mte)/mte <= .20)
    corr = np.corrcoef(mte - pr, (pr - pr.mean())**2)[0, 1]
    print(f"{nm:18s} MAE {mean_absolute_error(mte, pr):9.0f} | MSE {mse:.3e} | RMSE {np.sqrt(mse):9.0f} | "
          f"RMSLE {rmsle(mte, pr):.3f} | R2 {r2_score(mte, pr):6.3f} | ±20%: {dentro:.1%} | corr(res,(pred-media)^2) {corr:+.3f}")
print("predicciones negativas del lineal:", int((res["Lineal"] < 0).sum()), "de", len(mte))
# Efecto de un outlier (una predicción x0.3) en MAE vs RMSE, MLP
pr = res["MLP (32,16)"].copy(); i = int(np.argmax(mte)); pr2 = pr.copy(); pr2[i] *= .3
for etiqueta, q in [("sin outlier", pr), ("con outlier", pr2)]:
    print(f"MLP {etiqueta}: MAE {mean_absolute_error(mte, q):.0f} | RMSE {np.sqrt(mean_squared_error(mte, q)):.0f}")
print(f"RMSLE 100 vs 150: {rmsle(np.array([100.]), np.array([150.])):.3f} | 10,000 vs 10,050: {rmsle(np.array([10000.]), np.array([10050.])):.3f}")

# C. Curvas de aprendizaje: sobreajuste vs subajuste
print("\n== C. Curvas de aprendizaje (cáncer de mama, 5-fold) ==")
cv = StratifiedKFold(5, shuffle=True, random_state=42)
for nm, est, cols in [("Árbol sin límite", DecisionTreeClassifier(random_state=42), slice(None)),
                      ("Logística con 2 variables", make_pipeline(StandardScaler(), LogisticRegression()), [3, 4])]:
    ts, tr_s, va_s = learning_curve(est, X[:, cols], y, cv=cv, train_sizes=np.linspace(.1, 1, 6))
    print(f"{nm:26s} train {tr_s.mean(1)[-1]:.3f} | validación {va_s.mean(1)[-1]:.3f}")
