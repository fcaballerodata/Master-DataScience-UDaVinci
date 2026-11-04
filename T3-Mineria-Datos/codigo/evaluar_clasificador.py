import numpy as np, warnings; warnings.filterwarnings("ignore")
from sklearn.datasets import load_breast_cancer, make_classification
from sklearn.model_selection import train_test_split, cross_val_predict, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (confusion_matrix, classification_report, precision_score, recall_score, f1_score,
                             accuracy_score, roc_auc_score, average_precision_score, precision_recall_curve)
# --- Caso 1: cáncer de mama (clase positiva = maligno = 0 -> la volvemos 1) ---
X, y = load_breast_cancer(return_X_y=True); y = 1 - y            # 1 = maligno (lo que queremos detectar)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.25, stratify=y, random_state=42)
rf = RandomForestClassifier(300, random_state=42).fit(Xtr, ytr)
p = rf.predict_proba(Xte)[:, 1]; pred = (p >= .5).astype(int)
tn, fp, fn, tp = confusion_matrix(yte, pred).ravel(); print("VN,FP,FN,VP =", tn, fp, fn, tp)
print("accuracy", round((tp+tn)/len(yte),3), "| precisión", round(tp/(tp+fp),3), "| recall", round(tp/(tp+fn),3),
      "| especificidad", round(tn/(tn+fp),3), "| F1", round(f1_score(yte,pred),3))
print("umbral -> FP, FN, precisión, recall")
for u in (.1,.3,.5,.7,.9):
    q = (p >= u).astype(int); t_n,f_p,f_n,t_p = confusion_matrix(yte,q).ravel()
    print(f"  {u}: FP={f_p} FN={f_n} precisión={t_p/(t_p+f_p):.3f} recall={t_p/(t_p+f_n):.3f}")
# costo hipotético: FN cuesta 10, FP cuesta 1
costos = {u: 10*((p<u)&(yte==1)).sum() + 1*((p>=u)&(yte==0)).sum() for u in np.arange(.05,.96,.05)}
mejor = min(costos, key=costos.get); print("umbral de costo mínimo (FN=10, FP=1):", round(mejor,2), "costo", costos[mejor], "| costo con 0.5:", costos[min(costos,key=lambda u:abs(u-.5))])
print("ROC-AUC", round(roc_auc_score(yte,p),4), "| AP (área PR)", round(average_precision_score(yte,p),4))
# --- Caso 2: desbalance 5% ---
Xi, yi = make_classification(n_samples=5000, weights=[.95,.05], n_informative=5, random_state=42, flip_y=.01)
a,b,c,d = train_test_split(Xi,yi,test_size=.25,stratify=yi,random_state=42)
for nombre, m in [("RF", RandomForestClassifier(300,random_state=42)), ("LogReg", make_pipeline(StandardScaler(),LogisticRegression(max_iter=1000)))]:
    pp = m.fit(a,c).predict_proba(b)[:,1]
    print(nombre, "ROC-AUC", round(roc_auc_score(d,pp),3), "| AP", round(average_precision_score(d,pp),3), "| AP de un modelo al azar ≈", round(d.mean(),3))
# --- Validación cruzada estratificada con varias métricas ---
cvp = cross_val_predict(RandomForestClassifier(300,random_state=42), Xi, yi, cv=StratifiedKFold(5,shuffle=True,random_state=42), method="predict_proba")[:,1]
print("CV 5 pliegues (desbalanceado): AP", round(average_precision_score(yi,cvp),3), "ROC-AUC", round(roc_auc_score(yi,cvp),3))
