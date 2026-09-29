# UD3 — Características de las RNA

**Asignatura:** Fundamentos de Machine Learning
**Trimestre:** T3 — 2026 | Semana 3

---

## 📌 Resumen ejecutivo (repaso rápido de 30 segundos)

- 3 propiedades fundamentales de toda RNA: **Aprender** (ajustar pesos sinápticos con ejemplos), **Generalizar** (funcionar bien con datos nuevos/con ruido), **Abstraer** (quedarse con lo esencial).
- 4 errores comunes: **sobreajuste** (overfitting), **subajuste** (underfitting), datos insuficientes/mal preprocesados, mala selección de hiperparámetros.
- Ventajas: adaptabilidad, relaciones complejas, aprendizaje general. Desventajas: requieren muchos datos, baja interpretabilidad ("caja negra"), alto costo computacional.
- No existe "la mejor técnica" en abstracto: SVM, árboles, Random Forest, regresión y Naive Bayes pueden superar a una RNA en contextos con pocos datos o donde se necesita interpretabilidad.
- Métricas más allá del accuracy: precision, recall, F1-score, ROC-AUC — la elección depende del costo relativo de falsos positivos vs. falsos negativos en el problema de negocio.

---

## 1. Las 3 propiedades fundamentales de las RNA

### 1.1 Por qué estas 3 propiedades y no otras

La RNA copia el mecanismo de la neurona biológica (UD2: entrada → suma → activación). Esa similitud estructural con el cerebro le da 3 capacidades muy particulares que la distinguen de otras técnicas de ML.

### 1.2 Aprender

La RNA adquiere conocimiento **a partir de ejemplos, sin necesidad de programación explícita**. Se materializa mediante el ajuste progresivo de los **pesos sinápticos** (las conexiones entre neuronas) a medida que se expone repetidamente a los datos. Al modificar esos pesos, el sistema evoluciona para reducir sus errores y mejorar sus predicciones — es un proceso **dinámico y continuo**.

> 🔎 Esto es literalmente lo que hace `.fit()` en `MLPClassifier` (UD2): cada ejecución ajusta los pesos sinápticos.

### 1.3 Generalizar

Es la capacidad de aplicar el conocimiento adquirido a **casos nuevos** o a datos con variaciones respecto a los usados en el entrenamiento. Aunque los datos de entrada tengan ruido, deformaciones o pequeñas diferencias, la red puede seguir dando respuestas precisas porque identifica los elementos esenciales que permanecen constantes.

> ⚠️ En la práctica real, los datos casi nunca son idénticos a los del entrenamiento. Un modelo que no generaliza bien es un modelo inútil fuera del laboratorio, aunque tenga excelente desempeño con los datos que ya conoce.

### 1.4 Abstraer

Capacidad de identificar las **características esenciales** de un conjunto de datos, incluso cuando no muestran semejanzas aparentes a simple vista. Las arquitecturas más profundas (redes orientadas a extracción de características) son especialmente eficaces para esto: reducen la complejidad, eliminan lo irrelevante, y se concentran solo en lo que realmente importa para la tarea.

### 💡 Ejemplo integrador
Reconocimiento de escritura a mano: **aprende** viendo miles de dígitos escritos por distintas personas; **generaliza** cuando reconoce un "7" escrito por alguien cuya letra nunca vio antes; **abstrae** cuando identifica que lo esencial de un "7" es la línea horizontal + diagonal, ignorando el grosor del trazo o la inclinación.

---

## 2. Errores comunes al implementar RNA

### 2.1 Sobreajuste (overfitting)

El modelo aprende **demasiado bien** los detalles y el ruido específico del conjunto de entrenamiento, perdiendo la capacidad de generalizar a datos nuevos.

> 🔎 Es la misma razón por la que `Use training set` en WEKA (Minería de Datos UD2) da una evaluación optimista — el modelo puede estar memorizando en vez de aprender el patrón real.

### 2.2 Subajuste (underfitting)

Ocurre cuando el modelo es **demasiado simple** para capturar la complejidad real de los datos, resultando en mal rendimiento tanto en entrenamiento como en prueba. Es el error opuesto al sobreajuste.

### 2.3 Datos insuficientes o mal preprocesados

Entrenar con conjuntos de datos muy pequeños, o sin limpiar/normalizar adecuadamente, introduce ruido y sesgos, afectando el rendimiento del modelo.

> 🔎 Corresponde a las etapas 2-4 del proceso KDD (Minería de Datos UD1): limpieza, integración, transformación. El 80% del trabajo real sigue siendo preparación de datos, incluso con RNA.

### 2.4 Mala selección de hiperparámetros

Parámetros como la **tasa de aprendizaje**, el **tamaño del batch**, y la **arquitectura de la red** (número de capas y neuronas — `hidden_layer_sizes` en el código de UD2) deben elegirse y ajustarse cuidadosamente. Una mala elección lleva a un rendimiento pobre.

### 2.5 Sobreajuste vs. subajuste — tabla comparativa

| | Sobreajuste (overfitting) | Subajuste (underfitting) |
|---|---|---|
| **Causa** | Modelo demasiado complejo / memoriza | Modelo demasiado simple |
| **En entrenamiento** | Rendimiento excelente | Rendimiento pobre |
| **En datos nuevos** | Rendimiento pobre | Rendimiento pobre |

> 💡 El sobreajuste es engañoso: *parece* que el modelo funciona muy bien, hasta que lo pruebas con datos que nunca vio.

### 2.6 ¿Qué tan grande debe ser "un gran volumen de datos"? (complemento — no está en el material oficial)

No existe un umbral universal. Lo que importa es la relación entre:
- **La complejidad de la red** (cuántos pesos/parámetros hay que ajustar — más capas y neuronas = más parámetros)
- **La cantidad de datos disponibles**

Si una red tiene, por ejemplo, 100 pesos que ajustar y solo se le dan 12 ejemplos, no hay suficiente información para determinar esos valores de forma confiable — el modelo termina memorizando esos 12 casos en vez de aprender un patrón generalizable (sobreajuste).

**Órdenes de magnitud de referencia (guía general, no regla fija):**
- Un `MLPClassifier` pequeño (pocas neuronas) puede funcionar razonablemente con cientos de registros.
- Redes más profundas (deep learning) suelen necesitar miles o millones de ejemplos.

**Forma correcta de saberlo en la práctica:** comparar el rendimiento en entrenamiento vs. en datos de prueba. Una brecha grande es señal de que faltan datos o que la red es demasiado compleja para los datos disponibles.

---

## 3. Ventajas y Desventajas

| Ventajas | Desventajas |
|---|---|
| **Capacidad de aprendizaje general** — aprenden patrones sin ser explícitamente programadas para cada caso | **Requieren grandes volúmenes de datos** — necesario para evitar el sobreajuste |
| **Adaptabilidad** — se ajustan a cambios en el entorno o en los datos de entrada, robustas ante variaciones y ruido | **Dificultad en la interpretación** — a mayor complejidad, más difícil entender por qué toma una decisión ("caja negra") |
| **Potencial para representar relaciones complejas** — capturan relaciones no lineales que otras técnicas no logran modelar eficazmente | **Demanda de tiempo y recursos computacionales** — costoso entrenar y ejecutar, especialmente en tiempo real o hardware limitado |

---

## 4. Comparación de las RNA con otras técnicas

| Técnica | Qué hace | Ventaja frente a RNA |
|---|---|---|
| **SVM (Máquinas de Vectores de Soporte)** | Dividen el conjunto de datos en subconjuntos mediante kernels, manejando datos no lineales en espacios de alta dimensión | Eficaces con conjuntos de datos más pequeños |
| **Árboles de Decisión** | Basados en características específicas para hacer predicciones | Fáciles de interpretar; manejan datos categóricos y numéricos |
| **Random Forests** | Conjunto de árboles de decisión que combinan múltiples modelos | Mejoran precisión y generalizan bien (aunque menos interpretables que un solo árbol) |
| **Regresión Lineal / Logística** | Modelan la relación entre variables de entrada y salida | Simplicidad e interpretabilidad |
| **Naive Bayes** | Método probabilístico que asume independencia entre características, útil en clasificación de texto | Eficiente en tiempo de entrenamiento |

**Conclusión del material:** las RNA ofrecen una capacidad poderosa para aprender patrones estructurados y complejos, pero a menudo a costa de requerir más datos y recursos computacionales que estas otras técnicas, que suelen ser más simples e interpretables. **La elección depende del objetivo del proyecto y la naturaleza de los datos.**

---

## 5. Ejemplos de código ejecutable

### 5.1 Comparando RNA vs. otras técnicas en el mismo problema

**Problema de negocio:** churn de clientes (antigüedad + quejas → cancela), comparando regresión logística, árbol de decisión y RNA.

```python
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score

X = np.array([
    [24, 0], [3, 3], [36, 0], [2, 4], [18, 1], [1, 5], [30, 0], [5, 2],
    [20, 1], [4, 4], [28, 0], [6, 3]
])
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])

modelos = {
    "Regresión Logística": LogisticRegression(),
    "Árbol de Decisión": DecisionTreeClassifier(random_state=42),
    "RNA (MLP)": MLPClassifier(hidden_layer_sizes=(4,), max_iter=2000, random_state=42)
}

for nombre, modelo in modelos.items():
    score = cross_val_score(modelo, X, y, cv=3).mean()
    print(f"{nombre}: {score:.2%}")
```

Con un dataset tan pequeño (12 registros), la RNA probablemente **no** supere a la regresión logística o al árbol — demostración práctica de la desventaja "requieren grandes volúmenes de datos".

### 5.2 Comparando modelos con métricas más allá del accuracy

`accuracy` puede ser engañoso, sobre todo con clases desbalanceadas. `cross_validate` permite pedir varias métricas a la vez:

```python
import pandas as pd
from sklearn.model_selection import cross_validate

metricas = ["accuracy", "precision", "recall", "f1", "roc_auc"]

resultados = []
for nombre, modelo in modelos.items():
    scores = cross_validate(modelo, X, y, cv=3, scoring=metricas)
    fila = {"Modelo": nombre}
    for m in metricas:
        fila[m] = scores[f"test_{m}"].mean()
    resultados.append(fila)

tabla = pd.DataFrame(resultados).round(3)
print(tabla)
```

| Métrica | Qué te dice | Cuándo priorizarla |
|---|---|---|
| **Accuracy** | % total de aciertos | Clases balanceadas |
| **Precision** | De los que predijo "cancela", ¿cuántos realmente cancelaron? | Costo alto de **falso positivo** (ej. gastar en retención de quien no se iba a ir) |
| **Recall** | De los que realmente cancelaron, ¿cuántos detectó el modelo? | Costo alto de **falso negativo** (ej. dejar ir a un cliente sin intentar retenerlo) |
| **F1-score** | Balance entre precision y recall | Cuando importan ambos por igual |
| **ROC-AUC** | Qué tan bien separa el modelo las dos clases, en todos los umbrales | Comparar modelos de forma más robusta que con un umbral fijo |

### R

```r
library(nnet)
library(rpart)

datos <- data.frame(
  antiguedad = c(24, 3, 36, 2, 18, 1, 30, 5, 20, 4, 28, 6),
  quejas     = c(0, 3, 0, 4, 1, 5, 0, 2, 1, 4, 0, 3),
  cancelo    = as.factor(c(0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1))
)

modelo_log   <- glm(cancelo ~ antiguedad + quejas, data = datos, family = "binomial")
modelo_arbol <- rpart(cancelo ~ antiguedad + quejas, data = datos, method = "class")
modelo_rna   <- nnet(cancelo ~ antiguedad + quejas, data = datos, size = 4, maxit = 2000)
```

### ⚠️ Error común
Usar una RNA "porque es más avanzada", sin considerar el tamaño del dataset disponible. Con pocos datos, un modelo simple e interpretable (regresión, árbol) casi siempre rinde igual o mejor que una RNA — y encima se puede explicar por qué.

---

## 6. Glosario de la unidad

| Término | Definición breve |
|---|---|
| **Sobreajuste (overfitting)** | El modelo memoriza el ruido del entrenamiento y pierde capacidad de generalizar |
| **Subajuste (underfitting)** | El modelo es demasiado simple para capturar la complejidad real de los datos |
| **Hiperparámetro** | Configuración del modelo elegida antes del entrenamiento (tasa de aprendizaje, arquitectura, tamaño de batch) |
| **SVM** | Máquinas de Vectores de Soporte — técnica que separa datos usando kernels |
| **Random Forest** | Conjunto de árboles de decisión combinados |
| **Naive Bayes** | Método probabilístico que asume independencia entre variables |
| **Precision** | Proporción de positivos predichos que son realmente positivos |
| **Recall** | Proporción de positivos reales que el modelo detectó |
| **F1-score** | Media armónica entre precision y recall |
| **ROC-AUC** | Área bajo la curva ROC — mide capacidad de separación entre clases |

---

## 7. Preguntas de repaso

1. Describe las 3 propiedades fundamentales de las RNA con un ejemplo propio (no el de escritura a mano).
2. Un modelo obtiene 99% de precisión en entrenamiento y 60% en datos nuevos — ¿sobreajuste o subajuste? ¿Por qué?
3. ¿Cuáles son los 4 errores comunes al implementar RNA?
4. Con un dataset de 50 registros, ¿recomendarías RNA o una técnica más simple? Justifica con la tabla de comparación.
5. ¿Cuándo priorizarías recall sobre precision en un problema de churn, y viceversa?
6. ¿Por qué no existe un número fijo de registros que determine si tienes "suficientes datos" para una RNA?

---

## 8. Referencias

- Material oficial de la Unidad 3 — Universidad DaVinci, asignatura Fundamentos de Machine Learning.
- Bibliografía oficial de la asignatura: Burkov, A.; Géron, A.; Müller, A. C. & Guido, S.; Kelleher, J. D. et al.
- **Complemento externo:** documentación de [scikit-learn — `model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html) para las métricas de evaluación (precision, recall, F1, ROC-AUC).
