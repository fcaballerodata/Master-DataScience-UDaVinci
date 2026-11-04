import numpy as np, time, warnings; warnings.filterwarnings("ignore")
from sklearn.datasets import load_breast_cancer, make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix

X, y = load_breast_cancer(return_X_y=True)          # 0 = maligno, 1 = benigno
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.25, stratify=y, random_state=42)
modelos = {
 "Naive Bayes":   GaussianNB(),
 "SVM (rbf)":     make_pipeline(StandardScaler(), SVC()),
 "KNN (k=5)":     make_pipeline(StandardScaler(), KNeighborsClassifier(5)),
 "Árbol":         DecisionTreeClassifier(random_state=42),
 "Random Forest": RandomForestClassifier(300, random_state=42),
}
print("modelo | CV(train) | train | test | recall maligno(test)")
for n, m in modelos.items():
    cv = cross_val_score(m, Xtr, ytr, cv=5).mean(); m.fit(Xtr, ytr); p = m.predict(Xte)
    print(f"{n:14s} {cv:.4f} {m.score(Xtr,ytr):.4f} {accuracy_score(yte,p):.4f} {recall_score(yte,p,pos_label=0):.4f}")
# KNN sin escalar vs escalado
k0 = KNeighborsClassifier(5).fit(Xtr,ytr).score(Xte,yte); print("KNN sin escalar", round(k0,4))
# Árbol: profundidad vs sobreajuste
print("prof | train | test")
for d in (1,2,3,5,10,None):
    t = DecisionTreeClassifier(max_depth=d, random_state=42).fit(Xtr,ytr); print(d, round(t.score(Xtr,ytr),3), round(t.score(Xte,yte),3))
# Matriz de confusión del mejor
m = modelos["Random Forest"]; print("matriz confusión RF [[VN, FP],[FN, VP]] (0=maligno):\n", confusion_matrix(yte, m.predict(Xte)))
# KNN: elegir k con validación cruzada
print("k -> CV:", {k: round(cross_val_score(make_pipeline(StandardScaler(),KNeighborsClassifier(k)),Xtr,ytr,cv=5).mean(),3) for k in (1,3,5,11,21,51)})
# Naive Bayes: sobreconfianza
for n in ("Naive Bayes","Random Forest"):
    pr = modelos[n].predict_proba(Xte).max(1); alta = pr>.99
    acc = (modelos[n].predict(Xte)[alta]==yte[alta]).mean()
    print(n, "predicciones con prob>0.99:", int(alta.sum()),"/",len(yte), "| acierto en ellas:", round(acc,3))
# Desbalance: accuracy engañosa
Xi, yi = make_classification(n_samples=5000, weights=[.95,.05], n_informative=5, random_state=42, flip_y=.01)
a,b,c,d = train_test_split(Xi,yi,test_size=.25,stratify=yi,random_state=42)
for n, mm in [("Siempre 'no' (Dummy)", DummyClassifier(strategy="most_frequent")), ("Random Forest", RandomForestClassifier(300,random_state=42)), ("RF class_weight=balanced", RandomForestClassifier(300,random_state=42,class_weight="balanced"))]:
    p = mm.fit(a,c).predict(b); print(f"{n:24s} acc {accuracy_score(d,p):.3f} precisión {precision_score(d,p,zero_division=0):.3f} recall {recall_score(d,p):.3f} F1 {f1_score(d,p):.3f}")
print("proporción clase 1 en prueba:", round(d.mean(),3))
