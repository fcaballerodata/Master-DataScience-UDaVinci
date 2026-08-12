# 🤖 UD10 — Técnicas Clásicas de Clasificación y Predicción

**Asignatura:** Análisis de Datos y Métodos Estadísticos
**Semana:** S10

---

## 1. Árboles de Decisión

**Para qué sirve:** clasifica/predice dividiendo los datos en subgrupos cada vez más homogéneos mediante reglas "si/entonces", sin estimar una ecuación (Gironés Roig et al., 2017, Cap. 13).

**Cómo se aplica:** se elige la variable y punto de corte que maximiza la reducción de impureza (entropía/ganancia de información); se repite recursivamente hasta una regla de parada; la estructura final tiene nodos, ramas y hojas.

**Qué considerar:** riesgo de sobreajuste (controlar con poda); la entropía y ganancia de información son el criterio matemático de cada corte; sensible a variables irrelevantes.

```python
from sklearn.tree import DecisionTreeClassifier, plot_tree
modelo = DecisionTreeClassifier(max_depth=3, criterion="entropy", random_state=42)
modelo.fit(X_train, y_train)
plot_tree(modelo, feature_names=X_train.columns, filled=True)
precision = modelo.score(X_test, y_test)
```

**Way of Work:**
1. Preparar datos (limpiar, decidir si discretizar variables continuas).
2. Dividir en train/test.
3. Entrenar con un criterio de impureza (entropía o Gini) y una cota de profundidad conservadora.
4. Evaluar con matriz de confusión — comparar precisión train vs. test para detectar sobreajuste.
5. Podar si hace falta.
6. Visualizar el árbol final y verificar sentido de negocio.

---

## 2. K-NN (k vecinos más cercanos)

**Para qué sirve:** clasifica una instancia según la clase mayoritaria entre sus k vecinos más cercanos, usando una métrica de distancia. Es un método "perezoso": memoriza los datos y decide al momento de predecir.

**Cómo se aplica:** se elige k y una métrica de distancia; se calculan distancias de la nueva instancia a todos los puntos de entrenamiento; se asigna la clase mayoritaria entre los k más cercanos.

**Qué considerar:** k pequeño es sensible al ruido, k grande suaviza demasiado; **escalado de variables obligatorio** (Gironés Roig et al., 2017, Cap. 10); costoso computacionalmente con datasets grandes.

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

escalador = StandardScaler()
X_train_esc = escalador.fit_transform(X_train)
modelo = KNeighborsClassifier(n_neighbors=5)
modelo.fit(X_train_esc, y_train)
```

**Way of Work:**
1. Escalar/normalizar todas las variables numéricas.
2. Elegir la métrica de distancia adecuada (euclídea para numéricas, Hamming para categóricas).
3. Probar varios valores de k con validación cruzada.
4. Elegir el k con mejor equilibrio entre precisión y estabilidad.
5. Evaluar tiempo de cómputo en datasets grandes.

---

## 3. Redes Bayesianas

**Para qué sirve:** modelan dependencia probabilística entre variables mediante un grafo dirigido; permiten razonar hacia adelante y hacia atrás (inferir causa dado un resultado observado).

**Cómo se aplica:** se define la estructura del grafo; se estiman probabilidades condicionales de cada nodo dado sus padres; se usa la regla de Bayes para propagar evidencia.

**Qué considerar:** definir bien la estructura es lo más difícil; existen redes bayesianas dinámicas (incorporan el tiempo); requieren datos suficientes por cada probabilidad condicional.

```python
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

modelo = BayesianNetwork([("Edad", "EnfermedadRenal"), ("EnfermedadRenal", "DietaEspecial")])
# ... definir CPDs y agregar al modelo
inferencia = VariableElimination(modelo)
```

**Way of Work:**
1. Mapear las variables relevantes y su relación de dependencia conceptualmente.
2. Definir la estructura del grafo (validada con conocimiento experto).
3. Estimar probabilidades condicionales con datos históricos.
4. Validar con casos conocidos (inferencia adelante/atrás con resultados esperables).
5. Actualizar la red con nuevos datos/evidencia.

---

## 4. Cadenas de Markov

**Para qué sirve:** modelan sistemas que cambian de estado con el tiempo, donde el siguiente estado depende únicamente del estado actual (propiedad de Markov).

**Cómo se aplica:** se definen los estados posibles; se construye una matriz de transición; se proyecta el estado futuro multiplicando el estado actual por la matriz.

**Qué considerar:** verificar que la propiedad "sin memoria" sea razonable; la matriz debe estimarse con suficientes datos por estado.

```python
import numpy as np
matriz_transicion = np.array([[0.80, 0.20], [0.60, 0.40]])
estado_actual = np.array([1, 0])
for mes in range(1, 4):
    estado_actual = estado_actual @ matriz_transicion
```

**Way of Work:**
1. Definir claramente los estados posibles (mutuamente excluyentes y exhaustivos).
2. Verificar el supuesto "sin memoria".
3. Estimar la matriz de transición con frecuencias históricas.
4. Validar que cada fila sume 1.
5. Proyectar y comparar contra la intuición del negocio.

---

## 5. Redes Neuronales Artificiales (RNA)

**Para qué sirve:** modelo inspirado en neuronas biológicas, capaz de aprender patrones complejos no lineales ajustando pesos iterativamente (Gironés Roig et al., 2017, Cap. 12).

**Cómo se aplica:** se define la arquitectura (entrada, capas ocultas, salida); cada conexión tiene un peso; se entrena con backpropagation, ajustando pesos para minimizar el error, repitiendo en épocas.

**Qué considerar:** requiere normalizar los datos; necesita más datos que métodos clásicos; riesgo de sobreajuste (regularización, early stopping); es un modelo "caja negra".

```python
from sklearn.neural_network import MLPClassifier
modelo = MLPClassifier(hidden_layer_sizes=(8,), max_iter=1000, random_state=42)
modelo.fit(X_train_esc, y_train)
```

**Way of Work:**
1. Normalizar/escalar todas las variables de entrada.
2. Empezar con una arquitectura simple (una capa oculta pequeña).
3. Dividir en train/validación/test.
4. Monitorear la curva de error (detener si el error de validación empieza a subir).
5. Evaluar con matriz de confusión y comparar contra un modelo más simple.

---

## 6. Naive Bayes (Clasificador Bayesiano)

**Para qué sirve:** clasificador probabilístico basado en el Teorema de Bayes, que asume independencia entre atributos dado el valor de la clase. A pesar de esa simplificación, funciona bien en la práctica (Gironés Roig et al., 2017, Cap. 14).

**Cómo se aplica:** P(clase|atributos) ∝ P(clase) × ∏ P(atributo_i|clase). Se estima probabilidad previa de cada clase y de cada atributo dado cada clase; se clasifica eligiendo la clase de mayor probabilidad.

**Qué considerar:** el supuesto de independencia rara vez es 100% cierto, pero el modelo suele ser robusto; ideal como modelo baseline rápido; funciona bien con datasets pequeños.

```python
from sklearn.naive_bayes import CategoricalNB
modelo = CategoricalNB()
modelo.fit(X_train, y_train)
probabilidades = modelo.predict_proba(X_test)
```

**Way of Work:**
1. Verificar tipo de atributos (categóricos → CategoricalNB; numéricos → GaussianNB).
2. No preocuparse en exceso por la independencia real entre atributos.
3. Usarlo como modelo baseline rápido antes de modelos más complejos.
4. Evaluar con matriz de confusión, prestando atención a clases minoritarias.
5. Revisar las probabilidades de salida (`predict_proba`), no solo la clase predicha.

---

## 📋 Resumen — ¿cuál técnica usar?

| Situación | Técnica recomendada |
|---|---|
| Necesitas explicar la decisión con reglas claras | Árboles de decisión |
| Pocos datos, quieres algo rápido y simple | Naive Bayes |
| Relaciones causales/de dependencia explícitas | Redes Bayesianas |
| El problema evoluciona en el tiempo por estados | Cadenas de Markov |
| Patrones complejos, no lineales, con suficientes datos | Redes Neuronales |
| Clasificación por similitud/vecindad, dataset pequeño-mediano | K-NN |

---

## 📚 Referencias

Gironés Roig, J., Casas Roma, J., Minguillón Alfonso, J., & Caihuelas Quiles, R. (2017). *Minería de datos: Modelos y algoritmos* (Capítulos 2, 4, 5, 10, 12, 13 y 14). Editorial UOC.

Guía de la Unidad 10 — Universidad DaVinci (2026). Técnicas clásicas de clasificación y predicción.
