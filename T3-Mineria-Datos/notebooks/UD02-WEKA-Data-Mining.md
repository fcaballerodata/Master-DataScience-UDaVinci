# UD2 — WEKA y Data Mining

**Asignatura:** Minería de Datos
**Trimestre:** T3 — 2026 | Semana 2

---

## 📌 Resumen ejecutivo (repaso rápido de 30 segundos)

- **WEKA** (Waikato Environment for Knowledge Analysis): software libre en Java para minería de datos sin código, de la Universidad de Waikato (Nueva Zelanda).
- Formato de datos propio: **`.arff`** (cabecera `@RELATION` + `@ATTRIBUTE` tipados + `@DATA`).
- 4 técnicas soportadas: clasificación, regresión, selección de atributos, clustering.
- **Siempre correr un baseline (`ZeroR`)** antes de evaluar cualquier modelo real.
- 5 interfaces: **Explorer** (principal), **Experimenter** (comparación estadística), **KnowledgeFlow** (visual/diagramas), **Workbench** (todo integrado), **Simple CLI** (comandos).
- Evaluar con `Cross-validation` o `Percentage split` — **nunca solo con `Use training set`** (evaluación optimista, el modelo "ya vio la respuesta").
- Selección de atributos = **Attribute Evaluator** (mide calidad) + **Search Method** (cómo explora combinaciones).

---

## 1. ¿Qué es WEKA?

### 1.1 Definición

WEKA (**Wai**kato **E**nvironment for **K**nowledge **A**nalysis) es un conjunto de librerías Java desarrollado por la Universidad de Waikato (Nueva Zelanda), que implementa un extenso conjunto de algoritmos de minería de datos, bajo **licencia de software libre (GPL)**. Soporta las tareas propias del proceso de minería de datos: preprocesamiento, clasificación, regresión, clustering, visualización y selección de atributos.

Al estar desarrollado en Java, es **portable**: se ejecuta en cualquier máquina que tenga instalada la máquina virtual de Java (Windows, Linux, Mac).

### 1.2 Instalación

**Único requisito:** tener instalada la máquina virtual de Java. Se verifica con:

```bash
java -version
```

Si no está instalada, se descarga desde [java.com](https://www.java.com/es/download/) — o se usa la versión de WEKA que ya incluye la máquina virtual de Java integrada. Versión estable de referencia del material: **WEKA 3.8**.

### 1.3 Ventajas destacadas por el material

- Software libre (GPL) — alternativa gratuita a herramientas comerciales similares (SAS Miner, Clementine).
- Interfaz intuitiva, accesible para quienes inician en minería de datos.
- Extensa colección de algoritmos ya implementados.
- Portable (Java).
- Permite añadir extensiones/paquetes adicionales.
- Acceso a bases de datos vía SQL (conexión JDBC — Java Database Connectivity).
- Ofrece API para ser usado por terceros (integrable en otros sistemas).

### 1.4 El formato de datos ARFF

WEKA carga los datos desde ficheros de texto plano tipo `.arff`, con 3 secciones:

```
@RELATION iris

@ATTRIBUTE sepallength  REAL
@ATTRIBUTE sepalwidth   REAL
@ATTRIBUTE petallength  REAL
@ATTRIBUTE petalwidth   REAL
@ATTRIBUTE class  {Iris-setosa,Iris-versicolor,Iris-virginica}

@DATA
5.1,3.5,1.4,0.2,Iris-setosa
4.9,3.0,1.4,0.2,Iris-setosa
```

| Sección | Qué contiene |
|---|---|
| `@RELATION` | Nombre del conjunto de datos. Útil para grandes volúmenes: se pueden declarar varias relaciones (ej. `@RELATION dia_1`, `@RELATION dia_2`) y hacer minería solo de subconjuntos concretos |
| `@ATTRIBUTE` | Nombre y tipo de cada columna (`REAL`, o lista de categorías posibles entre `{ }`) |
| `@DATA` | Los registros, uno por línea, separados por comas, en el mismo orden que los atributos declarados |

> 🔎 **Equivalencia con pandas:** un archivo `.arff` es conceptualmente igual a un DataFrame — filas = instancias, columnas = atributos — pero con los **tipos de dato declarados explícitamente** en la cabecera, más parecido a `df.dtypes` o a un schema declarado que a un CSV plano sin tipado.

WEKA también puede conectarse a bases de datos vía **JDBC** y procesar directamente los datos que devuelve una consulta SQL — el mismo principio que conectar Python a Snowflake.

---

## 2. Técnicas de Data Mining en WEKA

### 2.1 Los 4 tipos de algoritmos

| Técnica | Qué hace |
|---|---|
| **Clasificación** | Dada una serie de elementos etiquetados, predice la etiqueta de elementos nuevos |
| **Regresión** | Predice variables continuas basándose en otras características del conjunto de datos |
| **Selección de atributos** | Encuentra qué atributos son los más relevantes (detalle en sección 4) |
| **Clusterización / Agrupamiento** | Identifica grupos con características similares |

Son las mismas 4 categorías fundamentales del Machine Learning ya trabajadas en Fundamentos de ML UD1 — WEKA no introduce conceptos nuevos, ofrece una forma visual de aplicarlos.

### 2.2 Ejemplo guiado — dataset Iris (clasificación), paso a paso

El material usa el dataset clásico **Iris** (mediciones de flores, prediciendo la especie) para comparar 4 clasificadores, en orden de sofisticación creciente:

**Paso 1 — Baseline con `ZeroR`**

`ZeroR` es un clasificador deliberadamente simple: predice siempre la clase mayoritaria (ignora todas las variables predictoras). Con Iris (3 clases balanceadas, ~33% cada una), acierta solo el **33%**.

> ⚠️ **Por qué es obligatorio correrlo primero:** el % de acierto de cualquier modelo posterior **debe superar claramente** este baseline, o el modelo no está aportando valor real. Si un modelo "sofisticado" apenas supera al `ZeroR`, es señal de que las variables usadas no tienen relación real con lo que se quiere predecir, o hay un error en el proceso.

**Paso 2 — Clasificador `PART` (genera reglas)**

Resultado: **97.33%** de aciertos. Al ser un algoritmo basado en reglas, WEKA muestra las reglas exactas generadas:

```
Si petalwidth <= 0.6: Iris-setosa (50.0)
Si petalwidth <= 1.7 AND petallength <= 4.9: Iris-versicolor (48.0/1.0)
En otro caso: Iris-virginica (52.0/3.0)
```

Se puede verificar en la pestaña "Visualize" que `petalwidth` y `petallength` son, efectivamente, los atributos que mejor separan visualmente las clases.

**Paso 3 — Árbol de decisión `J48`** (implementación de árboles de decisión en WEKA)

Clasifica correctamente con buena precisión y **se puede visualizar el árbol gráficamente** con un clic (clic derecho sobre el resultado → "Visualize tree"). También permite visualizar los errores de clasificación directamente ("Visualize classifier errors").

**Paso 4 — Regresión logística** (pestaña "functions")

Mejor resultado del ejemplo: **98.6%** de aciertos, con matriz de confusión aún más limpia.

> 🔎 **Por qué `PART` y `J48` dan resultados tan parecidos:** en Minería de Datos UD1 se vio que las reglas de inducción se pueden derivar directamente de un árbol de decisión — `PART` construye reglas usando una lógica de particionamiento muy similar a la de `J48`. No es coincidencia.

### 2.3 El mismo ejercicio, en Python (equivalencia directa)

```python
from sklearn.datasets import load_iris
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

X, y = load_iris(return_X_y=True)

# Paso 1: baseline (equivalente a ZeroR)
baseline = DummyClassifier(strategy="most_frequent")
print("Baseline (ZeroR):", cross_val_score(baseline, X, y, cv=5).mean())

# Paso 3: árbol de decisión (equivalente a J48)
arbol = DecisionTreeClassifier(random_state=42)
print("Árbol (J48):", cross_val_score(arbol, X, y, cv=5).mean())

# Paso 4: regresión logística
logreg = LogisticRegression(max_iter=200)
print("Regresión logística:", cross_val_score(logreg, X, y, cv=5).mean())
```

### 2.4 En R

```r
library(rpart)
library(nnet)  # para multinom (regresión logística multiclase)

data(iris)

# Árbol de decisión (equivalente a J48)
arbol <- rpart(Species ~ ., data = iris, method = "class")

# Regresión logística multinomial
modelo_log <- multinom(Species ~ ., data = iris)
```

---

## 3. Interfaces de WEKA

### 3.1 Las 5 interfaces

| Interfaz | Para qué sirve |
|---|---|
| **Explorer** | Interfaz principal para análisis exploratorio: cargar datos, filtrar, clasificar, agrupar, visualizar |
| **Experimenter** | Experimentos avanzados: correr varios algoritmos sobre varios datasets de forma automatizada (secuencial o paralela), repetir ensayos, comparar resultados con pruebas estadísticas de significancia |
| **KnowledgeFlow** | Entorno visual tipo diagrama de flujo — se conectan componentes (fuente de datos, filtros, clasificadores, evaluadores) arrastrando y soltando |
| **Workbench** | Integra Explorer + Experimenter + KnowledgeFlow + Simple CLI en un único espacio de trabajo (desde WEKA 3.8) |
| **Simple CLI** | Consola de comandos para ejecutar las clases Java de WEKA manualmente — se mantiene por compatibilidad histórica (antes de que existiera interfaz gráfica) |

### 3.2 Detalle del Explorer — pestaña por pestaña

| Pestaña | Función | Relación con el proceso KDD (UD1) |
|---|---|---|
| **Preprocess** | Cargar datos (archivo, URL, base de datos, generación sintética) y aplicar filtros (supervisados / no supervisados; sobre instancias o sobre atributos) | Etapas 1-5 (selección, limpieza, integración, transformación, reducción) |
| **Classify** | Algoritmos de clasificación y regresión | Etapa 6 |
| **Cluster** | Algoritmos de agrupamiento | Etapa 6 |
| **Associate** | Reglas de asociación (algoritmo por defecto: `Apriori`) | Etapa 6 |
| **Select attributes** | Selección de atributos (ver sección 4) | Etapa 5 |
| **Visualize** | Gráficos de resultados | Etapas 7-8 (interpretación) |

### 3.3 Filtros en Preprocess

- **Filtros no supervisados:** se aplican de forma independiente al proceso de clasificación posterior (ej. eliminar duplicados, normalizar, eliminar columnas/filas).
  - **Filtrado horizontal (sobre atributos):** elimina o transforma columnas.
  - **Filtrado vertical (sobre instancias):** elimina o transforma filas (registros).
- Los filtros se pueden aplicar en cascada (uno sobre el resultado del anterior) y deshacer con el botón "Undo".
- Los datos filtrados se pueden guardar como nuevo fichero ARFF para operaciones posteriores.

### 3.4 Modos de evaluación en "Classify"

| Modo | Descripción | Confiabilidad |
|---|---|---|
| **Use training set** | Evalúa el modelo sobre el mismo conjunto con el que se entrenó | ⚠️ Optimista — poco confiable (el modelo "ya vio la respuesta") |
| **Supplied test set** | Evalúa con un conjunto de datos independiente, cargado aparte | Confiable si el conjunto de test es representativo |
| **Cross-validation** | Validación cruzada — se realizan tantas evaluaciones como indique el parámetro `Folds` | ✅ La más rigurosa y recomendada |
| **Percentage split** | Divide los datos en dos grupos según un porcentaje (%): uno para entrenar, el resto para evaluar | Confiable, más simple que cross-validation |

> ⚠️ **Por qué `Use training set` es poco confiable:** al evaluar sobre los mismos datos usados para entrenar, el modelo puede estar **memorizando** en vez de **generalizando** — obtiene buenos resultados en esos datos específicos, pero eso no garantiza que funcione bien con datos nuevos que no ha visto. Este concepto se profundiza formalmente en unidades posteriores de Fundamentos de ML (sobreajuste / *overfitting*).

### 3.5 Aplicación destacada — Bayes Net Editor

Dentro de las herramientas de WEKA (menú "Tools" → "Bayes net editor") se puede construir y visualizar una **red bayesiana**. El material menciona como ejemplo: calcular la probabilidad de accidentes de tráfico a partir de variables como días festivos y época del año — aplicando directamente el mecanismo de prior → evidencia → posterior ya estudiado en Minería de Datos UD1 (Bloque 3).

### 3.6 Otras utilidades del menú "Tools"

- **Package manager:** instalar o desinstalar paquetes/extensiones de WEKA.
- **ArffViewer:** visualizar uno o varios ficheros ARFF en formato tabla; permite editar y eliminar atributos (columnas) e instancias (filas) directamente.
- **SQLViewer:** ejecutar consultas SQL independientes contra una base de datos conectada vía JDBC.

---

## 4. Selección de Atributos

### 4.1 Dos tipos de selección

| Tipo | Dónde se aplica | Característica |
|---|---|---|
| **No supervisada** | Filtros de la pestaña "Preprocess" | Se realiza de forma independiente al proceso de clasificación posterior — no usa la variable objetivo (clase) |
| **Supervisada** | Pestaña "Select attributes" | Busca atributos evaluando específicamente su capacidad de **discriminar la clase** (variable objetivo) |

### 4.2 Los 2 componentes de la selección supervisada

1. **Método de Evaluación (Attribute Evaluator):** función que determina la calidad de un conjunto de atributos para discriminar la clase.
2. **Método de Búsqueda (Search Method):** forma de recorrer las posibles combinaciones de atributos.

### 4.3 Por qué se necesita un método de búsqueda inteligente

Evaluar exhaustivamente **todas** las combinaciones posibles de atributos es un **problema combinatorio inabordable** a medida que crece el número de atributos — el mismo tipo de explosión combinatoria que resolvían los algoritmos genéticos frente al problema del vendedor viajero (Minería de Datos UD1, Bloque 3).

| Método de búsqueda | Cómo funciona |
|---|---|
| **ExhaustiveSearch** | Prueba todas las combinaciones posibles — muy costoso, solo viable con pocos atributos |
| **ForwardSelection** | Empieza sin atributos y va añadiendo, uno por uno, el que más mejora el resultado, hasta que añadir más empeora la situación |
| **BestSearch** | Búsqueda por escalada: explora combinaciones cercanas a la mejor encontrada, con posibilidad de retroceder (backtracking) si es necesario |

### 4.4 Tipos de método de evaluación

| Tipo | Cómo mide la calidad | Costo computacional |
|---|---|---|
| **Wrapper** | Usa directamente un clasificador real, midiendo su tasa de error sobre el subconjunto de atributos propuesto | Alto (entrena un clasificador por cada combinación evaluada), pero muy preciso y detecta interacciones complejas entre atributos |
| **No-wrapper** (ej. `CfsSubsetEval`) | Evalúa la calidad basándose en correlación entre atributos y con la clase, sin entrenar un clasificador completo | Más rápido, menos exhaustivo |

### 4.5 Selección de atributos vs. Reducción de dimensionalidad

| | Selección de atributos | Reducción de dimensionalidad (ej. PCA) |
|---|---|---|
| **Qué hace** | Elige un subconjunto de las columnas originales | Transforma las variables en nuevas combinaciones |
| **Variables originales** | Se conservan tal cual | Se pierden como tales (se combinan) |
| **Interpretabilidad** | Alta — sigues sabiendo qué variable original es cuál | Menor — las nuevas variables son combinaciones matemáticas |

---

## 5. Glosario de la unidad

| Término | Definición breve |
|---|---|
| **WEKA** | Software libre en Java para minería de datos, de la Universidad de Waikato |
| **ARFF** | Formato de archivo de datos propio de WEKA (`@RELATION`, `@ATTRIBUTE`, `@DATA`) |
| **JDBC** | Java Database Connectivity — conexión de WEKA a bases de datos vía SQL |
| **ZeroR** | Clasificador baseline que siempre predice la clase mayoritaria |
| **PART** | Algoritmo de clasificación basado en reglas |
| **J48** | Implementación de árboles de decisión en WEKA |
| **Cross-validation** | Modo de evaluación robusto con múltiples particiones (*folds*) de los datos |
| **Attribute Evaluator** | Función que mide la calidad de un subconjunto de atributos |
| **Search Method** | Estrategia para recorrer combinaciones de atributos |
| **Wrapper** | Método de evaluación de atributos que usa un clasificador real para medir calidad |
| **Explorer / Experimenter / KnowledgeFlow / Workbench / Simple CLI** | Las 5 interfaces de WEKA |

---

## 6. Preguntas de repaso

1. ¿Cuáles son las 3 secciones de un archivo `.arff` y qué contiene cada una?
2. ¿Por qué es obligatorio correr `ZeroR` antes de evaluar cualquier modelo de clasificación real?
3. ¿Qué interfaz de WEKA usarías para comparar estadísticamente 5 algoritmos sobre 3 datasets distintos, y cuál para construir un flujo de análisis arrastrando componentes visualmente?
4. ¿Por qué `Use training set` es una evaluación poco confiable, y qué alternativas existen?
5. ¿Cuál es la diferencia entre selección de atributos supervisada y no supervisada?
6. ¿Por qué `ExhaustiveSearch` deja de ser viable cuando el número de atributos crece?
7. Distingue selección de atributos de reducción de dimensionalidad en términos de si las variables originales se conservan o se transforman.

---

## 7. Referencias

- Material oficial de la Unidad 2 — Universidad DaVinci, asignatura Minería de Datos.
- Alpaydin, E. (2021). *Aprendizaje automático*. MIT Press.
- Bobadilla, J. (2021). *Aprendizaje automático y aprendizaje profundo: usando Python, Scikit y Keras*. Ediciones Zhou.
- **Complemento externo (citado directamente en el material oficial):** sitio oficial de WEKA — [ml.cms.waikato.ac.nz/weka](https://ml.cms.waikato.ac.nz/weka/).
- **Complemento externo:** documentación de [scikit-learn `DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html) y [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html), usados como equivalente de `ZeroR` y `J48` en los ejemplos de código Python.
