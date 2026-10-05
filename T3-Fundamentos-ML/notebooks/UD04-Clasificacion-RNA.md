# UD4 — Clasificación de las RNA

**Asignatura:** Fundamentos de Machine Learning
**Trimestre:** T3 — 2026 | Semana 4

---

## 📌 Resumen ejecutivo (repaso rápido de 30 segundos)

- Las RNA se pueden clasificar de **dos formas distintas** (no mezclarlas): por **arquitectura** (cómo está construida) y por **tarea** (qué problema resuelve).
- **Por arquitectura:** Feedforward (sin ciclos, uso general) · RNN (con ciclos y memoria a corto plazo, para secuencias) · CNN (filtros convolucionales, para imágenes/video).
- **Por tarea:** Aproximación de funciones · Clustering · Predicción · Clasificación.
- Supervisado: aproximación de funciones, predicción, clasificación. **No supervisado:** clustering (redes competitivas, p. ej. Kohonen/SOM).
- **Predicción** = valor continuo (salida lineal) · **Clasificación** = categoría discreta (sigmoide si es binaria, softmax si es multiclase).

---

## 1. Clasificación por arquitectura

La forma en que las neuronas se conectan determina para qué tipo de problema es más adecuada cada red.

| Arquitectura | Cómo fluye la información | Ideal para |
|---|---|---|
| **Feedforward** | En una sola dirección: entrada → capas ocultas → salida, **sin ciclos** | Clasificación, predicción y análisis de datos estructurados |
| **RNN (Recurrentes)** | Pueden **formar ciclos**: la salida de un paso se reutiliza como entrada del siguiente, lo que da "memoria a corto plazo" | Secuencias: series temporales, texto, traducción automática, reconocimiento de voz, predicción de eventos |
| **CNN (Convolucionales)** | Usan filtros y capas convolucionales que extraen características automáticamente de datos con estructura de cuadrícula | Visión por computadora: imágenes, video, detección de objetos, clasificación de imágenes |

> 🔎 `MLPClassifier` y `MLPRegressor` de scikit-learn (usados en UD2 y UD3) son redes **feedforward**.

> ⚠️ **Error común:** pensar que "más avanzado" (CNN, RNN) es automáticamente mejor. La elección depende del **tipo de dato**: sin estructura de secuencia ni de imagen, una feedforward simple suele ser más rápida y suficiente (mismo principio de UD3: no usar una RNA compleja cuando una técnica simple basta).

---

## 2. Clasificación por tarea

### 2.1 Aproximación de funciones

- Aprendizaje **supervisado**.
- Sirve cuando existe una relación entre entradas y salidas pero es demasiado compleja para describirla con una fórmula explícita.
- Usa capas ocultas y funciones de activación no lineales (sigmoide, ReLU, tangente hiperbólica) para capturar **no linealidad**.
- Se entrena con **retropropagación**: ajusta los pesos para minimizar el error.
- Generaliza bien a datos nuevos si está bien entrenada.
- **Ejemplo:** modelar cómo el precio de una vivienda depende de ubicación, tamaño, antigüedad y estado, sin una fórmula simple que lo describa.

### 2.2 Clustering

- Aprendizaje **no supervisado** (no hay etiquetas).
- Se usan **redes competitivas**, como las **Redes de Kohonen (Mapas Auto-organizativos, SOM)**: las neuronas *compiten* entre sí para activarse ante una entrada.
- **Auto-organización:** la red se ajusta para que datos similares queden representados en zonas cercanas del espacio de salida.
- Ayuda también a la **reducción de dimensionalidad** (visualizar datos con muchas variables).

**Kohonen vs. K-Means (UD1):** ambos agrupan datos similares sin etiquetas, con mecanismos distintos.

| | K-Means | Red de Kohonen (SOM) |
|---|---|---|
| **Mecanismo** | Distancias matemáticas a centroides | Competencia entre neuronas: la "ganadora" (la más parecida a la entrada) ajusta sus pesos para parecerse aún más, y las vecinas se ajustan un poco menos |
| **Resultado** | Grupos de datos parecidos | Grupos de datos parecidos, organizados además en un mapa donde lo similar queda cerca |

### 2.3 Predicción

- Aprendizaje **supervisado**.
- Usa datos históricos para estimar valores o tendencias futuras.
- Buena capacidad de generalización y **manejo de relaciones no lineales**, donde una regresión lineal simple se queda corta.
- Usos comunes: sistemas de recomendación, detección de anomalías, predicción de eventos futuros.

### 2.4 Clasificación

- Aprendizaje **supervisado**.
- Asigna **etiquetas discretas** (categorías), a diferencia de la predicción, que estima valores continuos.
- Función de activación **sigmoide** para clasificación **binaria** (2 clases) y **softmax** para **multiclase**.
- Bien entrenada, clasifica correctamente datos nuevos no vistos.

### 2.5 Predicción vs. Clasificación

| | Predicción | Clasificación |
|---|---|---|
| **Qué devuelve** | Un valor continuo | Una categoría discreta |
| **Ejemplo** | ¿Cuánto gastará este cliente el próximo mes? | ¿Este cliente cancela o no cancela? |
| **Activación típica de la salida** | Lineal | Sigmoide (binaria) / Softmax (multiclase) |

> 🔎 Es la misma bifurcación Regresión vs. Clasificación de UD1, aplicada ahora a cómo se configura la **capa de salida** de la red.

### 2.6 Resumen cruzado de tareas

| Tarea | Tipo de aprendizaje | Salida | Ejemplo |
|---|---|---|---|
| Aproximación de funciones | Supervisado | Valor/función no lineal | Precio de vivienda |
| Clustering | No supervisado | Grupos | Segmentación de clientes |
| Predicción | Supervisado | Valor continuo | Gasto del próximo mes |
| Clasificación | Supervisado | Categoría | Cancela / no cancela |

---

## 3. Ejemplos de código ejecutable

**Problema de negocio:** con los mismos datos de clientes, resolver una tarea de **clasificación** (¿cancela?) y una de **predicción** (¿cuánto gasta?) con redes feedforward.

### Python

```python
import numpy as np
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.preprocessing import StandardScaler

# Variables: antiguedad (meses), quejas
X = np.array([[24, 0], [3, 3], [36, 0], [2, 4], [18, 1], [1, 5], [30, 0], [5, 2]])
y_cancelo = np.array([0, 1, 0, 1, 0, 1, 0, 1])
y_gasto = np.array([4500, 300, 5800, 250, 3200, 150, 5100, 900])

# --- CLASIFICACIÓN: salida discreta ---
clasif = MLPClassifier(hidden_layer_sizes=(4,), max_iter=2000, random_state=42)
clasif.fit(X, y_cancelo)
print("¿Cancela? (1 = sí):", clasif.predict([[4, 3]]))

# --- PREDICCIÓN: salida continua ---
# Escalamos X y el objetivo: con valores en miles y una red tan pequeña,
# sin escalar el MLPRegressor converge mal y da estimaciones poco confiables.
sx, sy = StandardScaler().fit(X), StandardScaler().fit(y_gasto.reshape(-1, 1))
reg = MLPRegressor(hidden_layer_sizes=(4,), max_iter=5000, random_state=42)
reg.fit(sx.transform(X), sy.transform(y_gasto.reshape(-1, 1)).ravel())

pred_escalada = reg.predict(sx.transform([[4, 3]])).reshape(-1, 1)
print("Gasto estimado:", sy.inverse_transform(pred_escalada).ravel())
```

**Qué observar:** el código es casi idéntico; cambia la clase (`MLPClassifier` vs `MLPRegressor`), que define si la salida es una categoría (con sigmoide/softmax) o un valor continuo. En una ejecución de referencia, la clasificación dio `1` (cancela) y la predicción de gasto dio alrededor de 640 (valor orientativo; con tan pocos datos puede variar).

> ⚠️ **Lección práctica:** sin escalar, el `MLPRegressor` de este mismo ejemplo dio un gasto estimado de ~88, claramente fuera de lo razonable frente a clientes similares del dataset (300 y 900), y con aviso de no convergencia. Las RNA son sensibles a la escala de las variables: **escalar suele ser necesario**, sobre todo cuando el objetivo está en miles.

### R

```r
library(nnet)

datos <- data.frame(
  antiguedad = c(24, 3, 36, 2, 18, 1, 30, 5),
  quejas     = c(0, 3, 0, 4, 1, 5, 0, 2),
  cancelo    = as.factor(c(0, 1, 0, 1, 0, 1, 0, 1)),
  gasto      = c(4500, 300, 5800, 250, 3200, 150, 5100, 900)
)

# Clasificación
modelo_clasif <- nnet(cancelo ~ antiguedad + quejas, data = datos, size = 4, maxit = 2000)

# Predicción: linout = TRUE indica salida continua (no clasificación).
# Se escala el objetivo para facilitar la convergencia.
datos$gasto_esc <- as.numeric(scale(datos$gasto))
modelo_pred <- nnet(gasto_esc ~ antiguedad + quejas, data = datos,
                    size = 4, linout = TRUE, maxit = 2000)
```

---

## 4. Glosario de la unidad

| Término | Definición breve |
|---|---|
| **Feedforward** | Red cuya información fluye en un solo sentido, sin ciclos |
| **RNN (Red Neuronal Recurrente)** | Red con ciclos que le dan memoria a corto plazo; para secuencias |
| **CNN (Red Neuronal Convolucional)** | Red con filtros convolucionales para datos tipo imagen o video |
| **Aproximación de funciones** | Tarea supervisada: aprender una relación no lineal compleja entre entradas y salidas |
| **Red competitiva** | Red donde las neuronas compiten por activarse ante una entrada |
| **Red de Kohonen / SOM** | Mapa auto-organizativo: red competitiva para clustering y reducción de dimensionalidad |
| **Auto-organización** | Ajuste de la red para que datos similares queden en zonas cercanas del espacio de salida |
| **Sigmoide** | Función de activación para clasificación binaria |
| **Softmax** | Función de activación para clasificación multiclase |
| **Retropropagación** | Algoritmo que ajusta los pesos minimizando el error |

---

## 5. Preguntas de repaso

1. ¿Cuál es la diferencia entre clasificar una RNA por arquitectura y clasificarla por tarea? Da un ejemplo de cada una.
2. ¿Qué arquitectura usarías para predecir la siguiente palabra de una oración, y por qué?
3. ¿Qué tareas son supervisadas y cuál es no supervisada?
4. ¿Qué función de activación de salida usarías para predecir un gasto mensual y cuál para decidir si un cliente es VIP?
5. ¿En qué se parecen y en qué se diferencian las Redes de Kohonen y K-Means?
6. ¿Por qué suele ser necesario escalar las variables al entrenar una RNA de regresión?

---

## 6. Referencias

- Material oficial de la Unidad 4 — Universidad DaVinci, asignatura Fundamentos de Machine Learning.
- Bibliografía oficial de la asignatura: Burkov, A.; Géron, A.; Müller, A. C. & Guido, S.; Kelleher, J. D. et al.
- **Complemento externo:** documentación de scikit-learn — [`MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html), [`MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html) y [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html).
