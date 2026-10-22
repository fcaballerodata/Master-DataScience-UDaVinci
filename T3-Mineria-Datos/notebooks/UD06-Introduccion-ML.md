# UD06 · Introducción al Machine Learning — Minería de Datos (T3)

> **Fuente:** guía académica "Unidad 6 – Introducción al Machine Learning" (LMS UDaVinci, 24 pp.). El texto del PDF viene con partes mezcladas al extraerse; lo que no se leyó con claridad está marcado **[verificar]**.
> **Estado:** notebook de estudio. La fase de preguntas de comprensión **aún no se ha hecho** para esta unidad.

---

## 1. Resumen ejecutivo

- **ML** = rama de la IA que ajusta modelos matemáticos con datos, sin reglas escritas a mano. Aprender = **optimización estadística para reducir el error**, no comprensión humana (frase textual de la guía).
- **Cuatro enfoques:** supervisado, no supervisado, por refuerzo y semisupervisado (híbrido).
- **Supervisado:** clasificación (categoría) y regresión (valor continuo).
- **No supervisado:** clustering y reducción de dimensionalidad.
- **ML vs Deep Learning:** DL aprende las características solo, con redes de muchas capas; necesita más datos y cómputo y es menos interpretable.
- **Futuro:** AutoML, IA explicable, datos no estructurados/tiempo real, aprendizaje federado.

## 2. Ruta de estudio

1. Qué es ML y cómo aprende (ciclo iterativo)
2. Clasificación por tipo de aprendizaje
3. Algoritmos por tarea
4. ML vs Deep Learning
5. Futuro
6. Código + aplicación a BI

## 3. Qué es ML y cómo aprende

🟢 **Simple:** el modelo hace una predicción, mide cuánto se equivocó, ajusta sus parámetros y repite hasta que el error es aceptable.

🔵 **Técnico:** etapas según la guía: (1) recopilar y preparar datos (corregir errores, quitar inconsistencias, elegir variables), (2) elegir algoritmo, (3) entrenar, (4) evaluar con **datos no usados antes** (generalización), (5) ajustar parámetros o cambiar el enfoque.

💡 **BI:** es el mismo ciclo del KDD de la Unidad 1; ML es la etapa de "minería", no todo el proceso.

⚠️ **Cuidado:** si se ajustan parámetros mirando el conjunto de prueba, se contamina la evaluación. Para eso se usa validación cruzada y se toca la prueba una sola vez.

## 4. Clasificación de algoritmos (según la guía)

| Enfoque | Datos | Objetivo | Ejemplo de la guía |
|---|---|---|---|
| Supervisado | Etiquetados | Predecir salida conocida | Spam, precios |
| No supervisado | Sin etiquetas | Hallar estructura | Segmentación de clientes |
| Refuerzo | Interacción con entorno | Maximizar recompensa | Robótica, videojuegos |
| Semisupervisado | Pocos etiquetados + muchos sin etiquetar | Aprovechar ambos | Etiquetar es costoso |

**Refuerzo — elementos:** entorno, estados, acciones, recompensas y **política** (qué acción tomar en cada estado). Dilema **exploración vs explotación**: probar cosas nuevas vs repetir lo que ya funcionó.

**Algoritmos por tarea:**
- Clasificación: asigna categoría. Regresión: predice valor continuo.
- Clustering (k-means, DBSCAN) y reducción de dimensionalidad.
- Refuerzo: Q-learning, Deep Q-Networks **[verificar nombres exactos en el PDF]**.
- Árboles de decisión, redes neuronales, K-means aparecen en la actividad de completar huecos.

⚠️ **Dos puntos imprecisos de la guía (para no repetirlos en entregas):**
1. En el ejercicio de huecos dice "algoritmo de **correlación**… hacer predicciones". Lo técnicamente correcto es **regresión** (la correlación mide asociación, la regresión predice).
2. Dice que el aprendizaje por refuerzo "es un tipo de aprendizaje profundo". No: es un **paradigma** de aprendizaje; se combina con redes profundas (Deep RL), pero no es lo mismo.
Si la plataforma califica con la respuesta de la guía, usa la de la guía allí; en trabajos escritos usa la precisa y explica la diferencia.

## 5. ML vs Deep Learning

| Aspecto | ML clásico | Deep Learning |
|---|---|---|
| Características | Selección/preparación manual | Las aprende en capas |
| Datos | Funciona con pocos/moderados | Requiere grandes volúmenes |
| Tipo de dato | Estructurado (tablas) | No estructurado (imagen, audio, texto) |
| Cómputo | Moderado | Alto (hardware especializado) |
| Interpretabilidad | Mayor | Menor ("caja negra") |
| Usos | Tendencias, anomalías, apoyo a decisión | Voz, visión, traducción, PLN |

💡 **BI:** para tablas de clientes/ventas en Snowflake, lo habitual es ML clásico; DL se justifica con texto, imagen o audio (Unidades 4–5).

## 6. Futuro (según la guía)

AutoML (automatiza selección de algoritmo y parámetros) · IA explicable (crítica en salud, finanzas, legal) · datos no estructurados y en tiempo real (sensores, IoT, redes) · aprendizaje federado (entrenar sin centralizar datos, protege privacidad).

## 7. Python (probado)

```python
import numpy as np
from sklearn.datasets import load_breast_cancer, load_diabetes, make_blobs
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, r2_score, mean_absolute_error, silhouette_score
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA

# --- Supervisado: CLASIFICACIÓN (3 modelos, de más a menos interpretable) ---
X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.25, random_state=42, stratify=y)
modelos = {
 "logreg": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
 "arbol":  DecisionTreeClassifier(max_depth=3, random_state=42),
 "mlp":    make_pipeline(StandardScaler(), MLPClassifier((32,16), max_iter=1000, random_state=42)),
}
for n, m in modelos.items():
    cv = cross_val_score(m, Xtr, ytr, cv=5).mean()   # validación SIN tocar la prueba
    m.fit(Xtr, ytr)
    print(n, round(cv,4), round(accuracy_score(yte, m.predict(Xte)),4))

# --- Supervisado: REGRESIÓN ---
Xd, yd = load_diabetes(return_X_y=True)
a,b,c,d = train_test_split(Xd, yd, test_size=.25, random_state=42)
p = LinearRegression().fit(a,c).predict(b)
print("R2", round(r2_score(d,p),4), "MAE", round(mean_absolute_error(d,p),2))

# --- No supervisado: CLUSTERING ---
Xb,_ = make_blobs(n_samples=300, centers=3, random_state=42)
for k in range(2,6):
    print(k, round(silhouette_score(Xb, KMeans(k, n_init=10, random_state=42).fit_predict(Xb)),3))
print(set(DBSCAN(eps=.9, min_samples=5).fit_predict(Xb)))   # -1 = ruido

# --- No supervisado: REDUCCIÓN DE DIMENSIONALIDAD ---
Xs = StandardScaler().fit_transform(X)
pc = PCA(2).fit(Xs)
print(pc.explained_variance_ratio_.round(3), pc.explained_variance_ratio_.sum().round(3))
```

**Resultados obtenidos al ejecutarlo:**

| Prueba | Resultado |
|---|---|
| Regresión logística | CV 0.9695 · prueba 0.986 |
| Árbol (prof. 3) | CV 0.9297 · prueba 0.9441 |
| Red neuronal (MLP) | CV 0.9812 · prueba 0.965 |
| Regresión lineal (diabetes) | R² 0.4849 · MAE 41.55 |
| Silhouette k=2,3,4,5 | 0.705 / **0.848** / 0.664 / 0.49 |
| DBSCAN | etiquetas {0,1,2,-1} (3 grupos + ruido) |
| PCA 2 componentes | 44.3 % + 19.0 % = 63.2 % de la varianza |

**Lectura:** la regresión logística (simple e interpretable) igualó o superó a la red neuronal en esta tabla pequeña; coincide con la idea de la guía de que el enfoque depende del problema, los datos y los recursos. El silhouette más alto en k=3 coincide con los 3 grupos con que se generaron los datos. El *accuracy* de prueba entre modelos difiere poco: con 143 casos de prueba, una diferencia de 1–2 puntos son 1–3 casos; no es evidencia fuerte.

## 8. R (no probado — R no está disponible en mi entorno)

```r
# Clasificación y regresión
modelo <- glm(Species ~ ., data = subset(iris, Species != "setosa"), family = binomial)
reg    <- lm(mpg ~ wt + hp, data = mtcars)
summary(reg)
# Clustering y PCA
set.seed(42)
km  <- kmeans(scale(iris[,1:4]), centers = 3, nstart = 10)
pca <- prcomp(iris[,1:4], scale. = TRUE); summary(pca)
```

## 9. Aplicación real (BI)

Con una tabla de clientes de una cadena de tiendas (frecuencia, ticket promedio, meses activos, sede):
- **Clasificación:** ¿el cliente se irá el próximo trimestre? (sí/no) → campañas de retención.
- **Regresión:** ¿cuánto comprará el próximo mes? → pronóstico de demanda.
- **Clustering:** segmentar sin etiquetas (estandarizar antes) → perfiles para marketing.
- **PCA:** reducir 30 métricas a 2–3 ejes para visualizar en Power BI.
- **Refuerzo:** recomendador que aprende de la respuesta del cliente (caso avanzado).
Los resultados del modelo pueden volver a Snowflake como una columna de segmento/probabilidad y consumirse en Power BI.

## 10. Preguntas de comprensión (pendientes)

Cuando quieras, hacemos la fase de 2–3 preguntas y las corrijo. Aquí no hay respuestas tuyas todavía.

## 🧠 Lo que debes recordar

1. ML = optimización estadística del error; no es "entender".
2. Supervisado (etiquetas) · no supervisado (sin etiquetas) · refuerzo (recompensa) · semisupervisado (pocas etiquetas + muchas sin).
3. Clasificación = categoría; regresión = número continuo.
4. Clustering y PCA piden variables estandarizadas.
5. Nunca ajustes con el conjunto de prueba: valida con CV.
6. Tablas → ML clásico primero; DL para imagen, audio y texto.
7. Correlación ≠ regresión; refuerzo ≠ deep learning (aunque se combinan).

## Referencias (APA 7)

Universidad DaVinci. (s. f.). *Unidad 6 – Introducción al Machine Learning* [Guía académica]. LMS UDaVinci. https://lms.udavinci.edu.mx

Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830.

*Bibliografía de la asignatura (consultar para ampliar; no se leyó su contenido aquí):* Alpaydin (2021); Bobadilla (2021); Zhou (2021).
