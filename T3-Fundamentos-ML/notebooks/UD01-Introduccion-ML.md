# UD1 — Introducción al Machine Learning

**Asignatura:** Fundamentos de Machine Learning
**Trimestre:** T3 — 2026

## 1. Concepto clave

El Machine Learning (ML) es una rama de la Inteligencia Artificial en la que un algoritmo construye un modelo matemático a partir de datos de entrenamiento, ajustando sus parámetros internos para identificar patrones, y usa ese modelo para hacer predicciones sobre datos nuevos — sin que cada regla haya sido programada manualmente.

**Diferencia con programación tradicional:**

| Programación tradicional | Machine Learning |
|---|---|
| Tú escribes las reglas (`si X entonces Y`) | El algoritmo *encuentra* las reglas a partir de ejemplos |
| Datos + Reglas → Resultados | Datos + Resultados (ejemplos) → Reglas (modelo) |

**La bifurcación fundamental de todo problema de ML:**

> ¿Tengo una variable objetivo (etiqueta) en mis datos históricos?
> - **Sí** → problema **supervisado** → Clasificación o Regresión
> - **No** → problema **no supervisado** → Clustering (agrupamiento)

## 2. Términos y definiciones

- **Clasificación:** predecir una categoría (ej. ¿cancela o no cancela?)
- **Regresión:** predecir un valor numérico continuo (ej. ¿cuánto va a vender?)
- **Clustering (agrupamiento):** encontrar grupos naturales sin etiquetas previas
- **Reducción de dimensionalidad:** simplificar datos con muchas variables sin perder información relevante
- **Variable objetivo (target):** lo que el modelo intenta predecir
- **Variables predictoras (features):** los datos que el modelo usa para predecir
- **TensorFlow / PyTorch:** frameworks de deep learning
- **Scikit-learn:** librería de referencia para ML clásico (clasificación, regresión, clustering)

**Breve línea de tiempo:**
1950 (Turing) → 1957 (perceptrón, Rosenblatt) → 1980-90s (redes neuronales, SVM, árboles) → 2006 (término "deep learning", Hinton) → 2012 (AlexNet, explosión del deep learning moderno)

## 3. Ejemplos de código ejecutable

### Ejemplo 1 — Clasificación supervisada (churn)

**Problema de negocio:** predecir si un cliente va a cancelar su servicio, usando antigüedad y número de quejas.

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.DataFrame({
    "antiguedad_meses": [24, 3, 36, 2, 18, 1, 30, 5],
    "quejas":           [0, 3, 0, 4, 1, 5, 0, 2],
    "cancelo":          [0, 1, 0, 1, 0, 1, 0, 1]
})

X = data[["antiguedad_meses", "quejas"]]
y = data["cancelo"]

modelo = LogisticRegression()
modelo.fit(X, y)

nuevo_cliente = [[4, 3]]
prediccion = modelo.predict(nuevo_cliente)
print("¿Cancela?", "Sí" if prediccion[0] == 1 else "No")
```

```r
library(tidyverse)

datos <- tibble(
  antiguedad_meses = c(24, 3, 36, 2, 18, 1, 30, 5),
  quejas           = c(0, 3, 0, 4, 1, 5, 0, 2),
  cancelo          = c(0, 1, 0, 1, 0, 1, 0, 1)
)

modelo <- glm(cancelo ~ antiguedad_meses + quejas, data = datos, family = "binomial")
nuevo_cliente <- tibble(antiguedad_meses = 4, quejas = 3)
predict(modelo, nuevo_cliente, type = "response")
```

### Ejemplo 2 — Clustering no supervisado (segmentación RFM)

**Problema de negocio:** agrupar clientes según comportamiento de compra (Recencia, Frecuencia, Monto), sin etiquetas previas.

```python
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.DataFrame({
    "recencia_dias":      [5, 200, 10, 150, 3, 180, 20, 220],
    "frecuencia_compras": [30, 2, 25, 3, 40, 1, 20, 2],
    "monto_total":        [4500, 300, 3800, 250, 6000, 150, 3200, 200]
})

X_scaled = StandardScaler().fit_transform(data)
modelo = KMeans(n_clusters=3, random_state=42, n_init=10)
data["segmento"] = modelo.fit_predict(X_scaled)
print(data)
```

```r
library(tidyverse)

datos <- tibble(
  recencia_dias        = c(5, 200, 10, 150, 3, 180, 20, 220),
  frecuencia_compras    = c(30, 2, 25, 3, 40, 1, 20, 2),
  monto_total           = c(4500, 300, 3800, 250, 6000, 150, 3200, 200)
)

datos_escalados <- scale(datos)
set.seed(42)
modelo <- kmeans(datos_escalados, centers = 3, nstart = 10)
datos$segmento <- modelo$cluster
```

## 4. Conexión con experiencia real (Movet, Rappi)

- **Movet:** segmentación de clientes con RFM (recencia de visitas, frecuencia, gasto) para identificar clientes VIP, en riesgo de abandono, o inactivos.
- **Rappi:** ejemplo de problema supervisado de clasificación — predecir churn de usuarios con base en frecuencia de pedidos y quejas registradas.
- Flujo mental a interiorizar: **problema de negocio → datos → modelo → predicción → decisión**.

## 5. Preguntas de repaso

1. ¿Cuál es la diferencia entre un problema supervisado y uno no supervisado?
2. ¿Por qué "clasificar clientes" en lenguaje de negocio no siempre significa usar un algoritmo de Clasificación en ML?
3. ¿Por qué es necesario escalar los datos (`StandardScaler`) antes de aplicar K-Means, pero no antes de una regresión logística simple con dos variables en escalas similares?

## 6. Referencias

Material oficial de la Unidad 1 — Universidad DaVinci, asignatura Fundamentos de Machine Learning.
