"""Actividad ML S10 · Experimento del artículo: diagnóstico de cáncer de mama (Breast Cancer Wisconsin, datos reales de scikit-learn).
Compara regresión logística (sin capa oculta), MLP (16,) y MLP (32,16): exactitud, precisión, recall, AUC, AP, Log Loss y CV-AP. Semilla 42.
"""
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score, learning_curve
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, roc_auc_score, average_precision_score, log_loss, recall_score, precision_score, accuracy_score
d=load_breast_cancer(); X=d.data; y=1-d.target  # 1 = maligno
print(X.shape, y.mean())
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,stratify=y,random_state=42)
models={'Logística (sin capa oculta)':make_pipeline(StandardScaler(),LogisticRegression(max_iter=2000)),
'MLP (16,)':make_pipeline(StandardScaler(),MLPClassifier(hidden_layer_sizes=(16,),alpha=1e-2,max_iter=2000,random_state=42)),
'MLP (32,16)':make_pipeline(StandardScaler(),MLPClassifier(hidden_layer_sizes=(32,16),alpha=1e-2,max_iter=2000,random_state=42))}
cv=StratifiedKFold(5,shuffle=True,random_state=42)
for n,m in models.items():
    cvap=cross_val_score(m,Xtr,ytr,cv=cv,scoring='average_precision').mean()
    m.fit(Xtr,ytr); p=m.predict_proba(Xte)[:,1]; pr=(p>=.5).astype(int)
    tn,fp,fn,tp=confusion_matrix(yte,pr).ravel()
    print(f"{n:30s} trainacc {m.score(Xtr,ytr):.3f} testacc {accuracy_score(yte,pr):.3f} prec {precision_score(yte,pr):.3f} rec {recall_score(yte,pr):.3f} AUC {roc_auc_score(yte,p):.3f} AP {average_precision_score(yte,p):.3f} LL {log_loss(yte,p):.3f} CVAP {cvap:.3f} | VN{tn} FP{fp} FN{fn} VP{tp}")
