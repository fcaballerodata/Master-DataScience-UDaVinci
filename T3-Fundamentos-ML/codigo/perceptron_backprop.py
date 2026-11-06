import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

# 1) Perceptrón simple con la regla de aprendizaje (hardlim), desde cero
def hardlim(n): return (n >= 0).astype(int)
def entrenar_perceptron(X, t, epocas=100, seed=0):
    rng = np.random.default_rng(seed); w = rng.normal(size=X.shape[1]); b = rng.normal()
    for ep in range(1, epocas + 1):
        err_total = 0
        for p, tt in zip(X, t):
            a = hardlim(np.array(w @ p + b)); e = tt - a
            w = w + e * p; b = b + e; err_total += abs(e)      # regla: w_nuevo = w + e·p ; b_nuevo = b + e
        if err_total == 0: return w, b, ep
    return w, b, None
X = np.array([[0,0],[0,1],[1,0],[1,1]])
for nombre, t in [("AND",[0,0,0,1]),("OR",[0,1,1,1]),("XOR",[0,1,1,0])]:
    w,b,ep = entrenar_perceptron(X, np.array(t))
    pred = hardlim(X @ w + b)
    print(nombre, "convergió en época" if ep else "NO converge en 100 épocas", ep or "", "| aciertos", int((pred==np.array(t)).sum()),"/4")

# 2) Backpropagation desde cero (MLP 2-3-1, sigmoide, pérdida cuadrática) + verificación numérica del gradiente
sig = lambda z: 1/(1+np.exp(-z))
def init(seed=1):
    r = np.random.default_rng(seed); return dict(W1=r.normal(0,1,(2,3)), b1=np.zeros(3), W2=r.normal(0,1,(3,1)), b2=np.zeros(1))
def forward(P, X):
    h = sig(X @ P["W1"] + P["b1"]); y = sig(h @ P["W2"] + P["b2"]); return h, y
def loss(P, X, t): return 0.5*np.mean((forward(P, X)[1].ravel()-t)**2)
def grads(P, X, t):
    h, y = forward(P, X); n = len(X)
    d2 = (y.ravel()-t)[:,None]*y*(1-y)/n          # error en la salida
    d1 = (d2 @ P["W2"].T)*h*(1-h)                  # error propagado hacia atrás
    return dict(W2=h.T@d2, b2=d2.sum(0), W1=X.T@d1, b1=d1.sum(0))
tx = np.array([0,1,1,0]); P = init()
g = grads(P, X, tx); eps = 1e-6; maxdif = 0
for k in P:
    for idx in np.ndindex(P[k].shape):
        P[k][idx] += eps; lp = loss(P, X, tx); P[k][idx] -= 2*eps; lm = loss(P, X, tx); P[k][idx] += eps
        maxdif = max(maxdif, abs((lp-lm)/(2*eps) - g[k][idx]))
print("máx. diferencia gradiente analítico vs numérico:", f"{maxdif:.2e}")
hist=[]
for it in range(1, 20001):
    g = grads(P, X, tx)
    for k in P: P[k] -= 2.0*g[k]
    if it in (1,1000,5000,20000): hist.append((it, round(loss(P,X,tx),5)))
print("pérdida por iteración:", hist, "| predicciones:", forward(P,X)[1].ravel().round(3), "->", (forward(P,X)[1].ravel()>.5).astype(int))

# 3) Datos reales: perceptrón simple vs MLP (estandarizado)
Xc,yc = load_breast_cancer(return_X_y=True)
a,b_,c,d = train_test_split(Xc,yc,test_size=.25,random_state=42,stratify=yc)
p1 = make_pipeline(StandardScaler(), Perceptron(random_state=42)).fit(a,c)
p2 = make_pipeline(StandardScaler(), MLPClassifier((16,),max_iter=2000,random_state=42)).fit(a,c)
print("breast cancer prueba: perceptrón", round(p1.score(b_,d),4), "| MLP", round(p2.score(b_,d),4))
