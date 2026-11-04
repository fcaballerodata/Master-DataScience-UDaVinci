# UD08 · El perceptrón — Fundamentos de Machine Learning (T3)

> **Fuentes:** guía académica de la unidad (11 pp.), listado de Recursos y Bibliografía de la asignatura (no tratan el perceptrón en particular) y fuentes primarias verificadas (sección Referencias).
> **Convención:** **[guía]** = sale de la guía · **[complemento]** = fuente externa o práctica habitual · **[propio]** = prueba que ejecuté yo.
> **Código:** [`perceptron_backprop.py`](../codigo/perceptron_backprop.py) · [`traza_or.py`](../codigo/traza_or.py)

---

## 1. Resumen ejecutivo

- **Perceptrón:** una neurona artificial. Multiplica cada entrada por un peso, suma todo más un sesgo (*bias*) y responde 1 o 0 según si la suma llega al umbral.
- **Aprende corrigiendo errores:** si acierta, no cambia nada; si se equivoca, ajusta pesos y sesgo.
- **Límite:** separa con **una recta**. Aprende AND y OR, no XOR.
- **Perceptrón multicapa (MLP):** varias capas con activaciones no lineales. Resuelve lo que el simple no puede.
- **Backpropagation:** algoritmo para entrenar el MLP. Forward → backward → descenso de gradiente.

## 2. Fundamentos técnicos

### 2.1 Historia **[guía]**
McCulloch y Pitts (1943): suma ponderada comparada con un umbral. Rosenblatt (finales de los 50): añade una **regla de aprendizaje**. Minsky y Papert muestran que no implementa ciertas funciones elementales. En los 80, los perceptrones multicapa con reglas de aprendizaje superan esa limitación.

### 2.2 Estructura **[guía]**
- Salida de la red: **a = hardlim(Wp + b)**.
- **W** es la matriz de pesos (S neuronas × R entradas); la fila *iw* es el vector de pesos de la neurona i.
- Cada neurona: **aᵢ = hardlim(ᵢwᵀp + bᵢ)**, con hardlim(n) = 1 si n ≥ 0 y 0 si no.
- Cada neurona divide el espacio de entrada en **dos regiones**; la frontera es una recta (o un plano).

### 2.3 Regla de aprendizaje **[complemento]**
Con error **e = t − a** (t = respuesta correcta, a = respuesta del perceptrón):

| Situación | e | Qué pasa |
|---|---|---|
| Acierta | 0 | No cambia nada |
| Dijo 0 y debía ser 1 | +1 | w = w + p ; b = b + 1 |
| Dijo 1 y debía ser 0 | −1 | w = w − p ; b = b − 1 |

Fórmula general: **w_nuevo = w + e·p** y **b_nuevo = b + e**.

🔑 El perceptrón **no calcula una función de pérdida**: solo mira el error de cada ejemplo (0, +1 o −1). La función de pérdida aparece en el MLP.

### 2.4 Por qué AND y OR sí, XOR no
- En AND y OR existe una recta que deja cada clase de su lado: son **linealmente separables**.
- En XOR, (0,0) y (1,1) son una clase y (0,1) y (1,0) la otra. Ninguna recta las separa, así que los pesos nunca se estabilizan.
- Si el problema es linealmente separable, la regla converge **[guía]**.

### 2.5 MLP **[guía]**
Capa de entrada, una o más capas ocultas con activación no lineal (ReLU, sigmoide) y capa de salida (valor continuo en regresión; probabilidad o clase en clasificación).
- Sin activaciones no lineales, varias capas equivaldrían a una sola.
- A diferencia del perceptrón con `hardlim` (solo 0 o 1), el MLP puede dar un **valor continuo**.

### 2.6 Backpropagation **[guía]**
Aprendizaje supervisado basado en **descenso de gradiente** para reducir una **función de pérdida**.
1. **Forward pass:** los datos se propagan hasta la salida y se obtiene la predicción.
2. **Backward pass:** se mide el error en la salida, se reparte hacia atrás y se calcula el **gradiente** de la pérdida respecto a cada peso (cuánto cambia la pérdida si muevo ese peso).
3. **Descenso de gradiente:** cada peso se mueve un poco en la dirección que baja la pérdida; se repite.

⚠️ La guía lo llama "red Backpropagation", pero es un **algoritmo de entrenamiento**, no una arquitectura. La arquitectura es el MLP.

*Autoevaluación de la guía:* son correctas "utiliza el cálculo de gradientes para actualizar los pesos" y "propaga el error desde la salida hacia las capas anteriores".

## 3. Ejemplos sencillos
- **Perceptrón:** ¿aprobar un crédito? Con 2 variables que se separan con una recta (ingreso alto y deuda baja → aprobar).
- **Falla en XOR:** "comprar si el cliente es nuevo **o** de alto valor, pero no si es ambas cosas" no se separa con una recta.
- **MLP:** con una capa oculta aprende esa combinación.
- **Backpropagation:** como un equipo que se equivocó en un pronóstico y repasa hacia atrás cuánto aportó cada eslabón al error.

## 4. Python (ejecutado) **[propio]**

### 4.1 El perceptrón aprende AND, OR y XOR
```python
import numpy as np
hardlim = lambda n: (n >= 0).astype(int)

def entrenar_perceptron(X, t, epocas=100, seed=0):
    rng = np.random.default_rng(seed); w = rng.normal(size=X.shape[1]); b = rng.normal()
    for ep in range(1, epocas + 1):
        err_total = 0
        for p, tt in zip(X, t):
            e = tt - hardlim(np.array(w @ p + b))
            w = w + e * p; b = b + e; err_total += abs(e)   # w_nuevo = w + e·p ; b_nuevo = b + e
        if err_total == 0: return w, b, ep
    return w, b, None
```
Una **época** es una pasada por los 4 ejemplos.

| Prueba | Resultado |
|---|---|
| AND | converge en la época 6 |
| OR | converge en la época 4 |
| XOR | **no converge** en 100 épocas (2/4 aciertos en el último intento) |

**Seguimiento de OR** con w = [0, 0] y b = 0 (`traza_or.py`):

| Época | Qué pasa | Pesos al final |
|---|---|---|
| 1 | (0,0): dijo 1, debía ser 0 → b = −1. (0,1): dijo 0, debía ser 1 → sube w₂ | w = [0, 1], b = 0 |
| 2 | (0,0): se equivoca → b = −1. (1,0): dijo 0, debía ser 1 → sube w₁ | w = [1, 1], b = 0 |
| 3 | (0,0): aún se equivoca → b = −1 | w = [1, 1], b = −1 |
| 4 | **0 errores** → termina | w = [1, 1], b = −1 |

Comprobación: con w = [1, 1] y b = −1, la suma es −1 para (0,0) → 0, y 0 o 1 para los demás → 1. Es OR.

**Lectura:** "converge en la época N" = necesitó N vueltas para encontrar una recta que separa bien. En XOR esa recta no existe, así que nunca llega a 0 errores.

### 4.2 Backpropagation desde cero (MLP 2-3-1, sigmoide, pérdida cuadrática)
```python
sig = lambda z: 1/(1+np.exp(-z))
def forward(P, X):
    h = sig(X @ P["W1"] + P["b1"]); y = sig(h @ P["W2"] + P["b2"]); return h, y
def grads(P, X, t):
    h, y = forward(P, X); n = len(X)
    d2 = (y.ravel()-t)[:,None]*y*(1-y)/n        # error en la salida
    d1 = (d2 @ P["W2"].T)*h*(1-h)               # error propagado hacia atrás
    return dict(W2=h.T@d2, b2=d2.sum(0), W1=X.T@d1, b1=d1.sum(0))
# bucle: for it in range(20000): g = grads(P,X,t); P[k] -= 2.0*g[k]   (2.0 = tasa de aprendizaje)
```

| Resultado | Qué significa |
|---|---|
| Gradiente analítico vs numérico: máx. diferencia **2.3e-11** | Calculé el gradiente con la fórmula y moviendo cada peso un poquito. Coinciden: el cálculo hacia atrás está bien. |
| Pérdida 0.128 → 0.006 → 0.0003 → 0.00006 (iter. 1, 1.000, 5.000, 20.000) | La pérdida baja: la red aprende. |
| Predicciones 0.011, 0.992, 0.987, 0.011 | Con corte en 0.5 quedan **0, 1, 1, 0** = XOR. |

Las tres líneas clave: `forward` predice; `d2` es el error en la salida; `d1` es ese error repartido hacia la capa oculta según cuánto aportó cada neurona.

### 4.3 Datos reales: cáncer de mama (569 casos; 143 en prueba)
Perceptrón simple 0.965 vs MLP 0.972 de accuracy en prueba. La diferencia es de 1 caso de 143: no es evidencia fuerte. **El MLP no siempre vale la pena** cuando el problema es casi lineal.

## 5. R (no probado: R no está disponible en mi entorno)
```r
hardlim <- function(n) as.integer(n >= 0)
perceptron <- function(X, t, epocas = 100) {
  set.seed(0); w <- rnorm(ncol(X)); b <- rnorm(1)
  for (ep in 1:epocas) {
    err <- 0
    for (i in 1:nrow(X)) {
      e <- t[i] - hardlim(sum(w * X[i, ]) + b)
      w <- w + e * X[i, ]; b <- b + e; err <- err + abs(e)
    }
    if (err == 0) return(list(w = w, b = b, epoca = ep))
  }
  list(w = w, b = b, epoca = NA)
}
X <- matrix(c(0,0, 0,1, 1,0, 1,1), ncol = 2, byrow = TRUE)
perceptron(X, c(0,0,0,1))   # AND
```

## 6. Aplicación real (BI)
Con una tabla de clientes (frecuencia, monto, meses activos) para predecir si volverán a comprar:
1. **Línea base:** perceptrón simple o regresión logística (fáciles de explicar). Sirve cuando más compras recientes siempre significan más probabilidad (relación casi recta).
2. **MLP:** cuando importan combinaciones ("pocas compras pero muy recientes y de monto alto") o cuando quiero predecir **cuánto gastará** (salida continua).
3. **Validar** sin tocar el conjunto de prueba hasta el final (UD6).
4. **Si la ganancia es pequeña,** quedarse con el modelo simple: más interpretable y barato.

## 7. Puntos de la guía que conviene manejar con cuidado
1. Backpropagation es un **algoritmo de entrenamiento**, no una arquitectura.
2. La guía muestra las fórmulas pero no desarrolla el cálculo de los gradientes (regla de la cadena); lo verifiqué numéricamente.
3. El perceptrón converge solo si el problema es linealmente separable.

## 8. Preguntas de comprensión y respuestas corregidas

**1. ¿Cómo aprende el perceptrón y por qué AND y OR sí, XOR no?**
Calcula el error por ejemplo (e = t − a). Si acierta, no cambia; si se equivoca, aplica w = w + e·p y b = b + e. AND y OR son linealmente separables; XOR no, así que los pesos no se estabilizan.

**2. ¿Qué ocurre en forward y backward, y qué se minimiza?**
Forward: se predice. Backward: se reparte el error hacia atrás y se calculan gradientes. Con descenso de gradiente se mueven los pesos para minimizar la **función de pérdida**.

**3. Perceptrón simple vs MLP, con ejemplo de BI.**
El MLP añade capas ocultas con activación no lineal y resuelve problemas no lineales; además puede dar valores continuos. Simple: ¿vuelve o no?, con relación casi recta. MLP: combinaciones complejas o predecir cuánto gastará.

## 🧠 Lo que debes recordar
1. **Perceptrón** = pesos + sesgo + umbral (`hardlim`): suma ponderada ≥ 0 → 1; si no → 0.
2. **Regla de aprendizaje:** e = t − a; si e = 0 no cambia; si no, **w = w + e·p** y **b = b + e**.
3. Solo separa con **una recta**: aprende AND y OR, no XOR.
4. **MLP** = capas ocultas + activación no lineal; resuelve problemas no lineales y puede dar valores continuos.
5. **Backpropagation:** forward → backward (gradientes) → ajustar pesos con **descenso de gradiente** para bajar la **función de pérdida**.
6. Backpropagation es un **algoritmo de entrenamiento**, no una arquitectura.
7. Si el problema es casi lineal, un modelo simple rinde casi igual que un MLP.

## Referencias (APA 7)
- McCulloch, W. S., & Pitts, W. (1943). A logical calculus of the ideas immanent in nervous activity. *The Bulletin of Mathematical Biophysics, 5*, 115–133. https://doi.org/10.1007/BF02478259
- Minsky, M., & Papert, S. (1988). *Perceptrons: An introduction to computational geometry* (ed. ampliada). MIT Press. (Obra original publicada en 1969.)
- Rosenblatt, F. (1958). The perceptron: A probabilistic model for information storage and organization in the brain. *Psychological Review, 65*(6), 386–408.
- Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors. *Nature, 323*, 533–536. *(Pendiente confirmar página final y lista completa de autores antes de usarla en una entrega.)*
- Universidad DaVinci. (s. f.). *El perceptrón* [Guía académica, Unidad 8]. Fundamentos de Machine Learning. LMS UDaVinci.
