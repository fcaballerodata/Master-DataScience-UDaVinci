# UD6 — Mecanismos de aprendizaje

**Asignatura:** Fundamentos de Machine Learning
**Trimestre:** T3 — 2026 | Semana 6

---

## 📌 Resumen ejecutivo (repaso rápido de 30 segundos)

- El **mecanismo de aprendizaje** responde a una pregunta: ¿qué le doy a la red para que aprenda? Ejemplos con respuesta, datos sin respuesta o una mezcla.
- **Supervisado:** datos con etiqueta; la red aprende a **predecir** la salida de datos nuevos (clasificación, regresión).
- **No supervisado:** datos sin etiqueta; la red **descubre estructura** (clústeres, reducción de dimensiones, anomalías).
- **Híbrido:** pre-entrenamiento no supervisado + ajuste fino supervisado; útil cuando **etiquetar es caro** y hay pocas etiquetas.
- **Estandariza antes de usar distancias** (etapa 2 del no supervisado) y **no ajustes hiperparámetros con el conjunto de prueba** (fuga de datos).

---

> Una aclaración sobre el material: en la copia del PDF usada (11 páginas), el mapa conceptual y los elementos multimedia no se ven; el contenido legible está completo. Se marca con **[rigor]** una observación metodológica sobre el texto y con **[complemento]** lo que se agrega como apoyo y no está en el material oficial.

---

## 🗺️ Ruta de estudio

1. Qué es un mecanismo de aprendizaje
2. Entrenamiento no supervisado (6 etapas)
3. Entrenamiento supervisado (5 etapas)
4. Entrenamiento híbrido (3 etapas)
5. Comparación y conexión con lo visto (UD1–UD5 y la Actividad Integradora)
6. Código en Python
7. Código en R
8. Aplicación real
9. Respuestas a las preguntas de comprensión
10. Lo que debes recordar

**Conexión con lo anterior:** en UD1 viste supervisado y no supervisado como tipos de ML y en UD4 las tareas de las RNA (clasificación, clustering…). Aquí ves el **proceso paso a paso** de cada mecanismo y un tercero, el híbrido.

---

## 1. Qué es un mecanismo de aprendizaje

### 🟢 En palabras simples
Es la forma en que una red adquiere conocimiento a partir de los datos. Según lo que tengas, eliges uno de tres caminos.

### 🔵 Definición técnica
Los mecanismos de aprendizaje determinan cómo las RNA adquieren conocimiento: en el **supervisado**, a partir de ejemplos con respuestas conocidas; en el **no supervisado**, identificando patrones sin información previa sobre los resultados; y en los **híbridos**, combinando ambas estrategias (Unidad 6).

| | No supervisado | Supervisado | Híbrido |
|---|---|---|---|
| **Datos** | Sin etiquetas | Con etiquetas (respuesta correcta) | Pocos etiquetados + muchos sin etiquetar |
| **Meta** | Descubrir patrones, estructuras o relaciones ocultas | Predecir la salida de datos nuevos | Aprovechar las ventajas de ambos |
| **Tareas típicas** | Clustering, reducción de dimensionalidad, detección de anomalías | Clasificación, regresión | Pocas etiquetas o estructura compleja |
| **Cómo se evalúa** | Métricas internas (cohesión y separación) o validación de un experto | Precisión, exactitud, *recall* en datos de prueba | Combina ambas |

### 💡 Ejemplo (BI)
Supervisado es entrenar con un reporte donde ya sabes qué clientes se fueron. No supervisado es explorar una tabla **sin** esa columna para ver qué grupos aparecen solos.

---

## 2. Entrenamiento no supervisado (6 etapas)

El modelo se entrena con datos **no etiquetados**: no se conoce la "respuesta" de cada entrada. Su objetivo es descubrir patrones, estructuras o relaciones ocultas sin una guía externa (Unidad 6).

| # | Etapa | Qué se hace |
|---|---|---|
| 1 | Recolección de datos no etiquetados | Reunir, por ejemplo, una base de clientes sin clasificar por tipo |
| 2 | Preparación y preprocesamiento | Limpieza, normalización, valores atípicos, faltantes, **estandarización de variables** |
| 3 | Selección del algoritmo | Agrupar: k-means, DBSCAN, jerárquico. Reducir dimensiones: PCA, t-SNE |
| 4 | Entrenamiento del modelo | Se asigna cada muestra a un clúster según su similitud con las demás |
| 5 | Evaluación e interpretación | Sin etiquetas: métricas internas o validación del conocimiento experto |
| 6 | Ajuste y optimización | Por ejemplo, cambiar el número de clústeres en k-means |

**Ejercicio del PDF ("Ordena los pasos del entrenamiento no supervisado"):** el orden correcto es el de la tabla, de la etapa 1 a la 6.

### 🔵 Fundamento técnico: k-means y la distancia
K-means agrupa por **distancia** (euclídea). Si una variable tiene valores enormes (gasto en miles de pesos) y otra pequeños (compras de 1 a 10), la primera domina la distancia y la segunda casi no cuenta. Por eso se estandariza (media 0, desviación 1) **antes** de agrupar.

### ⚠️ Error común
Pensar que "sin etiquetas" significa "sin preparar los datos". La estandarización y la limpieza son parte del proceso. El problema de escala se **nota** en la etapa 5 (todos los grupos se distinguen solo por gasto), pero se **resuelve** en la etapa 2.

---

## 3. Entrenamiento supervisado (5 etapas)

Se usa un conjunto de datos **etiquetados** para entrenar un modelo de predicción: ejemplos de entrada junto con su salida correcta, para que aprenda a predecir la salida de datos nuevos no vistos (Unidad 6).

| # | Etapa | Qué se hace |
|---|---|---|
| 1 | Recopilación de datos etiquetados | Cada muestra con su resultado asociado |
| 2 | División del conjunto de datos | Entrenamiento (enseña) y prueba (evalúa al final) |
| 3 | Entrenamiento del modelo | Se ajustan los parámetros internos para minimizar el error entre predicción y etiqueta, con optimizadores como el descenso de gradiente |
| 4 | Evaluación del modelo | Con el conjunto de prueba: qué tan bien generaliza a datos nuevos (precisión, exactitud, *recall*) |
| 5 | Ajuste de hiperparámetros | Modificar hiperparámetros o cambiar el algoritmo para mejorar y reducir el *overfitting* |

### ⚠️ [rigor] Dos matices importantes sobre el PDF
1. **La etapa 5 dice que el ajuste se basa "en el rendimiento del modelo en el conjunto de prueba".** Eso es una **fuga de información**: si ajustas mirando la prueba, deja de ser independiente y su resultado sale más optimista de lo real. La documentación de scikit-learn lo describe así: aun evaluando en prueba, "todavía existe el riesgo de sobreajustar al conjunto de prueba porque los parámetros pueden ajustarse" (scikit-learn developers, s. f.-a). Lo correcto es ajustar con un conjunto de **validación** (o validación cruzada) y usar la **prueba una sola vez, al final**.
2. **El PDF habla de dos conjuntos; en la práctica son tres:** entrenamiento (aprende), validación (ajusta) y prueba (se usa una vez, para informar el resultado). Es lo que hiciste en la Actividad Integradora con `validation_split=0.1`.

### 💡 Conexión con la Actividad Integradora
- Dividiste 80/20 estratificado y reservaste 10 % del entrenamiento como validación → los tres conjuntos.
- `StandardScaler` se ajustó **solo con el entrenamiento** → la misma lógica de evitar fuga de datos, aplicada al preprocesamiento.

---

## 4. Entrenamiento híbrido (3 etapas)

Combina los dos enfoques para aprovechar las ventajas de ambos, sobre todo cuando los datos etiquetados son limitados o la estructura de los datos es compleja (Unidad 6).

| # | Etapa | Qué se hace |
|---|---|---|
| 1 | Pre-entrenamiento no supervisado | La red aprende características útiles de los datos sin etiquetas (clústeres, representaciones más compactas) |
| 2 | Entrenamiento supervisado | Ajuste fino con los datos etiquetados disponibles |
| 3 | Combinación de información | Lo aprendido en el pre-entrenamiento enriquece el entrenamiento supervisado y mejora la generalización |

### [complemento] Vocabulario de la literatura
Cuando hay **pocas etiquetas y muchos datos sin etiquetar**, la literatura habla de **aprendizaje semisupervisado**, y el "pre-entrenar y luego afinar" es la base del aprendizaje profundo actual. Se usa aquí solo como apoyo para entender el concepto.

### ⚠️ Error común
Pensar que el híbrido se usa "cuando conozco el comportamiento de algunos clientes". Se usa cuando las **etiquetas son escasas o caras**. Si tienes etiquetas suficientes, basta el supervisado.

---

## 5. Comparación: ¿cuál uso?

| Situación | Mecanismo |
|---|---|
| Tengo la respuesta correcta para muchos casos y quiero predecir | Supervisado |
| No tengo respuesta y quiero explorar o segmentar | No supervisado |
| Tengo millones de registros y pocos con respuesta confirmada | Híbrido |

**Contraste que se confunde:** el *clustering* (no supervisado) **descubre** grupos; la *clasificación* (supervisado) **asigna** a grupos que ya conoces.

---

## 6. Ejemplos con código (Python)

Los tres ejemplos se ejecutaron sin errores. Los datos de clientes son sintéticos, con semilla fija.

### 6.1 No supervisado: segmentar clientes

```python
import numpy as np, pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

rng = np.random.default_rng(42)
g = lambda n, m, s: rng.normal(m, s, size=(n, 3))
X = pd.DataFrame(np.vstack([g(100,[10,200,2],[2,40,.5]),
                            g(100,[40,800,8],[5,120,1.5]),
                            g(100,[25,450,5],[4,70,1])]),
                 columns=["dias_desde_compra", "gasto_mensual", "compras_mes"])

Xs = StandardScaler().fit_transform(X)            # etapa 2: estandarizar
for k in range(2, 7):                              # etapas 3-6: probar k
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(Xs)
    print(k, round(silhouette_score(Xs, km.labels_), 3), round(km.inertia_, 1))

km = KMeans(n_clusters=3, n_init=10, random_state=42).fit(Xs)
X["cluster"] = km.labels_
print(X.groupby("cluster").mean().round(1))
print(PCA(n_components=2).fit(Xs).explained_variance_ratio_.round(3))
```

**Resultado real:**

| k | Silhouette | Inercia |
|---|---|---|
| 2 | 0,586 | 270,1 |
| **3** | **0,640** | 103,3 |
| 4 | 0,543 | 85,6 |
| 5 | 0,536 | 75,5 |
| 6 | 0,439 | 66,3 |

El *silhouette* (qué tan separados quedan los grupos; más alto es mejor) alcanza su máximo con k = 3. Con k = 3 salen grupos de 98, 100 y 102 clientes:

| Clúster | Días desde la compra | Gasto mensual | Compras al mes |
|---|---|---|---|
| 0 (gasto alto) | 40,3 | 787,3 | 8,2 |
| 1 (gasto bajo) | 9,9 | 199,5 | 2,0 |
| 2 (gasto medio) | 24,8 | 453,4 | 4,9 |

Los dos primeros componentes de PCA explican **96,9 %** de la varianza (92,1 % + 4,8 %).

### 6.2 Supervisado: ajustar hiperparámetros sin tocar la prueba

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

d = load_breast_cancer()
Xtr, Xte, ytr, yte = train_test_split(d.data, d.target, test_size=0.2,
                                      random_state=42, stratify=d.target)
pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000))
gs = GridSearchCV(pipe, {"logisticregression__C": [0.01, 0.1, 1, 10, 100]},
                  cv=5, scoring="accuracy").fit(Xtr, ytr)     # ajuste con CV, no con la prueba
print(gs.best_params_, round(gs.best_score_, 4), round(gs.score(Xte, yte), 4))
```

**Resultado real:** mejor `C = 0.1`, exactitud en validación cruzada **0,9802** y en prueba **0,9737**. El modelo sin ajustar (`C = 1`) sacó **0,9825** en prueba.

> **Lección honesta:** ajustar con validación cruzada **no garantiza** mejorar la prueba. Con 114 casos de prueba, la diferencia (0,9737 vs. 0,9825) es de **un paciente**. Lo importante es que la decisión se tomó **sin mirar la prueba**.

### ⚠️ Cuidado con la métrica del ajuste
En este conjunto la clase 1 es **benigno** y la clase 0 es **maligno**. Si pones `scoring="recall"`, el ajuste optimiza la detección de benignos: elige `C = 0.01` con recall de validación 1,0, y en prueba la exactitud baja a 0,947 y solo se detectan 37 de 42 malignos (recall 0,881 de la clase 0). Si el costo está en **no detectar un maligno**, hay que optimizar el *recall* de la clase maligna, no el de la clase 1. La métrica se elige por el costo del error, no por defecto.

### 6.3 Híbrido: 50 etiquetas frente a muchos datos sin etiqueta (dígitos escritos a mano)

```python
from sklearn.datasets import load_digits
from sklearn.semi_supervised import LabelSpreading

X, y = load_digits(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)
idx = np.random.default_rng(0).choice(len(Xtr), 50, replace=False)   # solo 50 etiquetas
Xl, yl = Xtr[idx], ytr[idx]

# a) Solo supervisado con 50 etiquetas
sup = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000)).fit(Xl, yl)

# b) Pre-entrenamiento no supervisado (KMeans con TODOS los datos, sin etiquetas) + supervisado
km = KMeans(n_clusters=100, n_init=3, random_state=0).fit(Xtr)
hyb = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000)).fit(km.transform(Xl), yl)

# c) Semisupervisado: propaga las 50 etiquetas al resto (los no etiquetados llevan -1)
yy = np.full(len(Xtr), -1); yy[idx] = yl
ls = LabelSpreading(kernel="knn", n_neighbors=7).fit(Xtr, yy)
```

Por convención, las muestras no etiquetadas se marcan con `-1` en `y` (scikit-learn developers, s. f.-b).

**Resultado real** (5 selecciones distintas de 50 etiquetas, exactitud en el conjunto de prueba):

| Selección | Solo supervisado | KMeans + supervisado | LabelSpreading |
|---|---|---|---|
| 1 | 0,800 | 0,867 | 0,928 |
| 2 | 0,807 | 0,885 | 0,913 |
| 3 | 0,804 | 0,859 | 0,906 |
| 4 | 0,793 | 0,802 | 0,898 |
| 5 | 0,783 | 0,857 | 0,941 |
| **Promedio** | **0,797** | **0,854** | **0,917** |

Con las **mismas 50 etiquetas**, aprovechar los datos sin etiqueta sube la exactitud entre 6 y 12 puntos. Ese es el valor del híbrido cuando etiquetar es caro.

> Nota técnica: al ejecutar `LabelSpreading` con pocas etiquetas, scikit-learn puede mostrar una advertencia `RuntimeWarning: invalid value encountered in divide`. En esta corrida no afectó los resultados.

---

## 7. Código en R

> ⚠️ **No probado.** El entorno de trabajo no tiene R; revisar al ejecutarlo.

```r
set.seed(42)

# No supervisado: k-means + silhouette + PCA
X  <- scale(iris[, 1:4])
km <- kmeans(X, centers = 3, nstart = 25)
library(cluster)
mean(silhouette(km$cluster, dist(X))[, "sil_width"])
summary(prcomp(X))

# Supervisado: regresión logística con división entrenamiento/prueba
idx <- sample(nrow(mtcars), 0.8 * nrow(mtcars))
mod <- glm(am ~ wt + hp, data = mtcars[idx, ], family = binomial)
pred <- as.numeric(predict(mod, mtcars[-idx, ], type = "response") > 0.5)
mean(pred == mtcars$am[-idx])
```

---

## 8. Aplicación real

**Caso: retención de clientes en una plataforma de domicilios.**

- **No supervisado:** segmentar a los clientes por frecuencia, gasto y recencia para descubrir grupos que nadie había definido. Se muestran en Power BI para marketing.
- **Supervisado:** con el historial de quiénes abandonaron, predecir quién se va a ir (*churn*). Se evalúa con el *recall* de los que abandonan, no solo con la exactitud.
- **Híbrido:** hay millones de clientes pero pocos con una etiqueta confiable de abandono (para saber si alguien abandonó hay que esperar meses). Se aprende primero la estructura de todos y luego se afina con los etiquetados.

⚠️ **Error típico:** presentar los grupos del clustering como "la verdad". Son una lectura de los datos que un experto debe validar.

---

## 9. Explicación del código, por partes

- **Estandarizar (`StandardScaler`)**: pone todas las variables en la misma escala para que ninguna domine la distancia.
- **Probar varios `k` con *silhouette***: en no supervisado no hay "respuesta correcta", así que se compara qué tan bien separados quedan los grupos. Es la etapa 6 (ajuste) en acción.
- **`GridSearchCV` con `cv=5`**: prueba cada valor de `C` con validación cruzada **dentro del entrenamiento**; la prueba no se toca hasta el final.
- **`make_pipeline`**: encadena el escalado y el modelo para que el escalado se ajuste solo con la parte de entrenamiento de cada partición (sin fuga).
- **`km.transform`**: convierte cada dato en su distancia a los 100 centros, una representación aprendida **sin etiquetas** que luego usa el modelo supervisado.
- **`-1` en `LabelSpreading`**: marca lo no etiquetado; el algoritmo propaga las pocas etiquetas por la estructura de los datos.

---

## 10. Respuestas a las preguntas de comprensión

### Pregunta 1 · Escala de las variables
*Quieres agrupar clientes por gasto (en miles de pesos) y número de compras (de 1 a 10) con k-means, sin preparar los datos. ¿Qué problema aparece y en qué etapa se resuelve?*

**Respuesta correcta:** el problema es la **escala**. K-means agrupa por distancia: el gasto, con valores enormes, domina y las compras casi no influyen; los grupos salen formados prácticamente solo por gasto. Se **nota** en la etapa 5 (evaluación e interpretación) pero se **resuelve en la etapa 2 (preparación y preprocesamiento)**, estandarizando. Los clientes repetidos y los datos faltantes también se arreglan en la etapa 2, pero son otro problema: duplicados y faltantes, no diferencia de escala.

### Pregunta 2 · Validación y prueba
*Alguien ajusta los hiperparámetros mirando el rendimiento en el conjunto de prueba hasta que sube. ¿Qué está mal y cómo lo harías bien?*

**Respuesta correcta:** es **fuga de datos**: la prueba deja de ser independiente y su resultado sale más optimista de lo que será con datos nuevos. Se ajusta con un conjunto de **validación** (o validación cruzada) y la **prueba se usa una sola vez, al final**, sin tomar decisiones con ella.

### Pregunta 3 · Cuándo usar el híbrido
*¿En qué situación preferirías un entrenamiento híbrido en vez de uno solo supervisado?*

**Respuesta correcta:** cuando las **etiquetas son escasas o caras** y hay muchos datos sin etiquetar. Conocer el comportamiento de algunos clientes no basta: si hay etiquetas suficientes, el supervisado sirve. Ejemplo: millones de clientes en varias sedes, pero pocos con el desenlace confirmado (el abandono se sabe meses después). Se aprende la estructura de todos y se afina con los pocos etiquetados.

---

## 🧠 Lo que debes recordar

1. **Supervisado** usa etiquetas para predecir. **No supervisado** descubre estructura sin etiquetas. **Híbrido** combina pocos etiquetados con muchos sin etiquetar.
2. **Etapas del no supervisado, en orden:** recolección, preprocesamiento, selección del algoritmo, entrenamiento, evaluación e interpretación, ajuste.
3. **Estandariza antes de usar distancias.** Sin eso, la variable de mayor magnitud decide los grupos. Se resuelve en la etapa 2, aunque lo notes en la 5.
4. **Los tres conjuntos tienen un rol distinto:** entrenamiento enseña, validación ajusta y prueba se usa una sola vez al final. Ajustar con la prueba es fuga de datos y da un resultado demasiado optimista.
5. **El PDF dice que el ajuste se basa en la prueba.** Hay que matizarlo: lo correcto es hacerlo con validación.
6. **Usa el híbrido cuando etiquetar es caro o lento**, no solo cuando conoces algunos casos.
7. **Los grupos del clustering son una lectura de los datos** que un experto debe validar, no una verdad.

---

## 📚 Referencias

Universidad DaVinci. (s. f.). *Mecanismos de aprendizaje* [Material de la Unidad 6]. Fundamentos de Machine Learning. LMS Universidad DaVinci.

scikit-learn developers. (s. f.-a). *3.1. Cross-validation: evaluating estimator performance*. https://scikit-learn.org/stable/modules/cross_validation.html

scikit-learn developers. (s. f.-b). *LabelSpreading*. https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html

**Bibliografía de la asignatura (lectura complementaria, no usada para citar datos puntuales):**
- Burkov, A. (2019). *The hundred-page machine learning book*.
- Géron, A. (2023). *Aprende machine learning con Scikit-learn, Keras y TensorFlow* (3.ª ed.). Anaya Multimedia.
- Guido, S., & Müller, A. C. (2016). *Introduction to machine learning with Python: A guide for data scientists*. O'Reilly Media.
- Kelleher, J. D., Mac Namee, B., & D'Arcy, A. (2015). *Fundamentals of machine learning for predictive data analytics: Algorithms, worked examples, and case studies*. MIT Press.
