"""UD09 ML · Construcción de una RNA. Datos mixtos simulados (churn): preparación (estandarizar, one-hot, ordinal, binaria), topologías, activaciones, regularización y early stopping, comparadas con CV (average precision). Los datos son SIMULADOS.
"""
import numpy as np, pandas as pd, warnings; warnings.filterwarnings("ignore")
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import average_precision_score
rng = np.random.default_rng(42); n = 4000
df = pd.DataFrame({
 "frecuencia": rng.poisson(4, n), "monto": rng.lognormal(11, 1, n),
 "canal": rng.choice(["web","tienda","app"], n), "plan": rng.choice(["pequeño","mediano","grande"], n),
 "usa_app": rng.integers(0, 2, n)})
z = (-1 + 0.9*(df.frecuencia>=6) - 0.8*(df.frecuencia<=1)*(df.usa_app==0) + 0.6*(df.canal=="app")
     + 0.5*(df.plan=="grande") + 0.7*(np.log(df.monto)>11.5)*(df.frecuencia>=3) + rng.normal(0,.6,n))
y = (z > 0.4).astype(int); print("tasa positiva", round(y.mean(),3))
Xtr, Xte, ytr, yte = train_test_split(df, y, test_size=.25, stratify=y, random_state=42)
def prep(escalar=True, ohe=True):
    return ColumnTransformer([
      ("num", StandardScaler() if escalar else "passthrough", ["frecuencia","monto"]),
      ("nom", OneHotEncoder() if ohe else OrdinalEncoder(), ["canal"]),
      ("ord", OrdinalEncoder(categories=[["pequeño","mediano","grande"]]), ["plan"]),
      ("bin", "passthrough", ["usa_app"])])
def modelo(h=(16,), act="relu", alpha=1e-4, es=False, escalar=True, ohe=True, seed=42):
    return Pipeline([("p", prep(escalar, ohe)), ("m", MLPClassifier(h, activation=act, alpha=alpha, early_stopping=es, max_iter=800, random_state=seed))])
def ev(nombre, m):
    cv = cross_val_score(m, Xtr, ytr, cv=5, scoring="average_precision").mean(); m.fit(Xtr, ytr)
    print(f"{nombre:34s} CV-AP {cv:.3f} | train acc {m.score(Xtr,ytr):.3f} | test acc {m.score(Xte,yte):.3f} | test AP {average_precision_score(yte, m.predict_proba(Xte)[:,1]):.3f}")
print("-- topología (capas/neuronas)")
for h in [(), (2,), (16,), (32,16), (128,128,128)]:
    if h==(): 
        from sklearn.linear_model import LogisticRegression
        ev("sin capas ocultas (logística)", Pipeline([("p",prep()),("m",LogisticRegression(max_iter=1000))]))
    else: ev(f"MLP {h}", modelo(h))
print("-- activación"); [ev(f"(16,) {a}", modelo((16,),a)) for a in ("relu","tanh","logistic")]
print("-- regularización (128,128,128)"); ev("alpha=1e-4", modelo((128,128,128),alpha=1e-4)); ev("alpha=1.0", modelo((128,128,128),alpha=1.0)); ev("early_stopping", modelo((128,128,128),es=True))
print("-- datos"); ev("sin estandarizar", modelo((16,),escalar=False)); ev("canal como entero (0,1,2)", modelo((16,),ohe=False))
print("-- semillas (16,)"); print([round(modelo((16,),seed=s).fit(Xtr,ytr).score(Xte,yte),3) for s in range(5)])
