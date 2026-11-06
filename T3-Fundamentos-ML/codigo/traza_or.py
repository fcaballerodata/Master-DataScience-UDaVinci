"""Traza paso a paso de la regla del perceptrón en OR (w=[0,0], b=0)."""
import numpy as np
hardlim = lambda n: int(n >= 0)
X = np.array([[0,0],[0,1],[1,0],[1,1]]); t = np.array([0,1,1,1])
w = np.zeros(2); b = 0.0
for ep in range(1, 10):
    errores = 0
    for p, tt in zip(X, t):
        a = hardlim(w @ p + b); e = tt - a
        if e != 0: errores += 1; print(f"  época {ep} p={p} t={tt} a={a} e={e:+d} -> ", end="")
        w = w + e*p; b = b + e
        if e != 0: print(f"w={w} b={b}")
    print(f"época {ep}: errores={errores} | w={w} b={b}")
    if errores == 0: break
