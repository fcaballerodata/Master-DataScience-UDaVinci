# UD5 — Fundamentos de las RNA

**Asignatura:** Fundamentos de Machine Learning
**Trimestre:** T3 — 2026 | Semana 5

---

## 📌 Resumen ejecutivo (repaso rápido de 30 segundos)

- Una RNA se compone de **capas** (entrada, ocultas, salida) unidas por **pesos** ajustables.
- Los pesos **empiezan al azar** y el entrenamiento los ajusta comparando la respuesta de la red con el resultado conocido.
- Mejor **muchos ejemplos y ajuste lento**: la red debe generalizar, no memorizar.
- Una neurona calcula una **suma ponderada** y reconoce el patrón si supera un **umbral**.
- Tú defines la arquitectura y la tasa de ajuste; **la red aprende los pesos**.

---

> Una aclaración sobre el material: en la copia del PDF usada, las páginas sobre capas y funcionamiento (6 a 9) salieron con el texto revuelto, y el mapa conceptual no se ve. Se reconstruyó lo legible y se marca con **[reconstrucción]** lo que quedó parcialmente ilegible, y con **[complemento]** lo que se agrega como apoyo.

---

## 🗺️ Ruta de estudio

1. Por qué importan las RNA (aplicaciones)
2. Elementos: neuronas, capas y pesos
3. Estructura: las tres capas
4. Funcionamiento: pesos, entrenamiento, tasa de ajuste y umbral
5. Ejemplo aplicado + código (Python y R)
6. Resumen

---

## 1. Por qué importan las RNA

Las RNA imitan la estructura de las neuronas biológicas (UD2) para procesar y aprender de los datos. El material destaca cuatro sectores:

| Sector | Aplicación |
|---|---|
| **Medicina** | Análisis de imágenes para detectar enfermedades con gran precisión |
| **Industria** | Mantenimiento predictivo: identificar patrones de fallo antes de que ocurran |
| **Finanzas** | Predicción de comportamientos del mercado y detección de fraude |
| **Conducción autónoma y robótica** | Interpretar el entorno y decidir en tiempo real |

---

## 2. Elementos de las RNA

### 🟢 En palabras simples
Una RNA es un conjunto de unidades simples organizadas en **capas** y unidas por conexiones que tienen un **peso**. Los datos entran por un lado, se transforman al pasar de capa en capa, y por el otro lado sale el resultado.

### 🔵 Definición técnica
Una red neuronal incluye tres tipos de capas: una **capa de entrada** (unidades que representan los datos de entrada), una o más **capas ocultas** y una **capa de salida** (una o varias unidades con los resultados previstos). Las unidades se conectan mediante **pesos que pueden variar**.

**Cómo aprende (según el material):** analiza registros uno por uno, genera una predicción para cada uno y **ajusta los pesos cuando la predicción es incorrecta**. Repite el proceso muchas veces, mejorando, hasta cumplir uno o más criterios de finalización.

> 🔎 **Conexiones con lo que ya sabes:**
> - UD2: las entradas son las dendritas, y el **peso** es la sinapsis.
> - UD3: la arquitectura y la tasa de aprendizaje son *hiperparámetros*.
> - UD4: si los datos fluyen en un solo sentido, es una red **feedforward**.

---

## 3. Estructura: las tres capas

| Capa | Función | Detalle según el material |
|---|---|---|
| **Entrada** | Recibe los datos iniciales | No contiene neuronas artificiales que procesen; solo recibe los datos |
| **Ocultas** | Procesan la información | No son visibles desde fuera (ni entradas ni salidas). Su número varía según la complejidad del problema; las redes más complejas usan más |
| **Salida** | Entrega el resultado final | El número de neuronas de salida depende del problema a resolver |

> 💡 **Idea clave:** el material describe el recorrido como "de izquierda a derecha": entrada → ocultas → salida.

⚠️ **Error común:** pensar que tú defines los pesos. Tú defines la arquitectura (cuántas capas y neuronas) y la tasa de ajuste; los **pesos los aprende la red** durante el entrenamiento.

---

## 4. Funcionamiento

### 4.1 El entrenamiento, paso a paso

1. Los pesos se asignan **de forma aleatoria** al inicio (en el ejemplo del material, entre -1 y 1) **[reconstrucción]**.
2. Se presentan ejemplos con **resultado conocido**.
3. La red genera una respuesta y se **compara** con el resultado conocido.
4. Esa comparación **retroalimenta** a la red, que ajusta los pesos poco a poco.
5. Terminado el entrenamiento, se aplica a **casos nuevos** donde el resultado no se conoce.

**Ejemplo de una neurona (material) [reconstrucción]:** los pesos de las entradas *activas* (valor 1) se refuerzan y los de las *inactivas* (valor 0) se reducen. Es una regla simplificada para enseñar la idea; la regla formal basada en el error la verás en el perceptrón (UD8) **[complemento]**.

### 4.2 La tasa de ajuste
Podría parecer que ajustar los pesos rápido acelera el aprendizaje, pero **no suele ser efectivo en redes con muchas neuronas**. Incluso con una sola neurona, es mejor entrenar con **muchos ejemplos y ajuste lento** que con pocos ejemplos y ajuste rápido.

> 🔎 Es la misma lógica de UD3: pocos datos y ajustes bruscos favorecen que la red memorice (sobreajuste) en lugar de generalizar.

### 4.3 Reconocer un patrón: el umbral
Una neurona entrenada puede reconocer patrones. Ante un patrón nuevo produce una salida; **si supera un umbral específico, el patrón se reconoce; si es menor, no**. Es el mecanismo de la neurona biológica de UD2 (suma de impulsos frente al umbral de activación).

### 🔵 Fundamento técnico: la suma ponderada
*Concepto → intuición → fórmula → ejemplo → aplicación.*

- **Intuición:** cada señal de entrada "vota" con más o menos fuerza según su peso; se suman los votos y se compara con un umbral.
- **Fórmula:** `z = w1·x1 + w2·x2 + w3·x3 + b`, y la neurona responde 1 si `z > 0`, y 0 si no. (`b`, el sesgo, equivale a mover el umbral **[complemento]**.)
- **Ejemplo numérico** con los pesos que aprende el código de abajo (`w = [0.25, 0.28, 0.32]`, `b = -0.51`):

| Cliente (frecuente, gasto alto, reciente) | z | Resultado |
|---|---|---|
| (1, 1, 0) | 0.25 + 0.28 + 0 − 0.51 = **0.02** | 1 → VIP |
| (1, 0, 0) | 0.25 − 0.51 = **−0.26** | 0 → no VIP |
| (0, 1, 1) | 0.28 + 0.32 − 0.51 = **0.09** | 1 → VIP |

---

## 5. Ejemplo aplicado + código

**Problema de negocio:** clasificar un cliente como VIP si cumple **al menos 2 de 3 señales** (compra frecuente, gasto alto, compra reciente). Entrenamos **una sola neurona desde cero**, para ver los pesos y el umbral en acción.

### Python

```python
import numpy as np
from itertools import product
from sklearn.neural_network import MLPClassifier

X = np.array(list(product([0, 1], repeat=3)))   # las 8 combinaciones posibles
y = (X.sum(axis=1) >= 2).astype(int)            # VIP si cumple al menos 2 de 3

rng = np.random.default_rng(42)
w = rng.uniform(-1, 1, size=3)   # pesos iniciales aleatorios entre -1 y 1
b = rng.uniform(-1, 1)           # sesgo (mueve el umbral)
lr = 0.1                         # tasa de ajuste

for epoca in range(1, 101):
    errores = 0
    for xi, yi in zip(X, y):
        salida = 1 if (w @ xi + b) > 0 else 0   # ¿supera el umbral?
        error = yi - salida
        if error != 0:                           # solo se ajusta si se equivoca
            w = w + lr * error * xi
            b = b + lr * error
            errores += 1
    if errores == 0:
        break

print("Épocas:", epoca, "| pesos:", w.round(2), "| sesgo:", round(b, 2))

# Estructura de capas en scikit-learn
mlp = MLPClassifier(hidden_layer_sizes=(4,), max_iter=3000, random_state=42).fit(X, y)
print("Capas:", mlp.n_layers_)
print("Pesos entrada->oculta:", mlp.coefs_[0].shape)
print("Pesos oculta->salida:", mlp.coefs_[1].shape)
```

**Salida real al ejecutarlo:** pesos iniciales `[0.55, -0.12, 0.72]` y sesgo `0.39`; la neurona llegó a **0 errores en 8 épocas**, con pesos finales `[0.25, 0.28, 0.32]`, sesgo `-0.51` y **8 de 8 aciertos**. La red de scikit-learn tiene **3 capas**, con pesos de forma `(3, 4)` (3 entradas × 4 neuronas ocultas = 12 pesos) y `(4, 1)` (4 pesos hacia la salida).

**Cómo leerlo:** empezó con pesos al azar, se equivocó, se ajustó solo cuando fallaba, y terminó con tres pesos parecidos y un umbral que exige que se sumen al menos dos señales. Nadie le dijo "2 de 3": lo aprendió de los ejemplos.

### R

```r
set.seed(42)
X <- as.matrix(expand.grid(c(0, 1), c(0, 1), c(0, 1)))
y <- as.numeric(rowSums(X) >= 2)

w  <- runif(3, -1, 1)   # pesos iniciales aleatorios
b  <- runif(1, -1, 1)   # sesgo
lr <- 0.1

for (epoca in 1:100) {
  errores <- 0
  for (i in 1:nrow(X)) {
    salida <- as.numeric(sum(w * X[i, ]) + b > 0)
    error  <- y[i] - salida
    if (error != 0) {
      w <- w + lr * error * X[i, ]
      b <- b + lr * error
      errores <- errores + 1
    }
  }
  if (errores == 0) break
}
print(list(epocas = epoca, pesos = round(w, 2), sesgo = round(b, 2)))
```

⚠️ **No pude ejecutar el código de R aquí** (mi entorno no tiene R); es el equivalente directo del de Python. Los números serán distintos porque R genera otros valores aleatorios, pero la lógica es la misma.

---

## 6. Explicación del código, por partes

### Paso 1: los datos
```python
X = np.array(list(product([0, 1], repeat=3)))
y = (X.sum(axis=1) >= 2).astype(int)
```
- `product([0, 1], repeat=3)` genera las 8 combinaciones posibles de tres valores 0/1. Cada **fila es un cliente** y cada **columna una señal** (compra frecuente, gasto alto, compra reciente).
- `X.sum(axis=1)` suma cada fila, o sea, cuántas señales tiene activas. Con `>= 2` queda verdadero/falso, y `.astype(int)` lo vuelve 1/0.
- `y` es el **resultado conocido**: `[0 0 0 1 0 1 1 1]`.

### Paso 2: el punto de partida
```python
rng = np.random.default_rng(42)
w = rng.uniform(-1, 1, size=3)
b = rng.uniform(-1, 1)
lr = 0.1
```
- `default_rng(42)` fija la semilla: salen los mismos números al azar cada vez que lo corres.
- `w` son los **3 pesos**, uno por señal, al azar entre -1 y 1. `b` es el **sesgo**, que mueve el umbral.
- `lr` es la **tasa de ajuste**: qué tan grande es cada corrección.

### Paso 3: el ciclo de entrenamiento
```python
for epoca in range(1, 101):
    errores = 0
    for xi, yi in zip(X, y):
        salida = 1 if (w @ xi + b) > 0 else 0
        error = yi - salida
        if error != 0:
            w = w + lr * error * xi
            b = b + lr * error
            errores += 1
    if errores == 0:
        break
```
- Una **época** es una pasada completa por los 8 ejemplos; `errores` cuenta cuántas veces falló en esa pasada.
- `w @ xi + b` es la **suma ponderada** (`w1·x1 + w2·x2 + w3·x3 + b`). Si es mayor que 0, la salida es 1: ese es el **umbral**.
- `error = yi - salida` puede valer:
  - **0**: acertó.
  - **+1**: debía ser VIP y dijo que no, así que hay que subir pesos.
  - **-1**: dijo VIP y no lo era, así que hay que bajarlos.
- `if error != 0` ajusta **solo cuando se equivoca**, como dice el material.
- `w + lr * error * xi`: como `xi` vale 0 o 1, **solo cambian los pesos de las señales que estaban activas**. `b` se mueve en el mismo sentido.
- `if errores == 0: break` es el **criterio de finalización**: una pasada completa sin fallar.

#### Una época real, con los números de la ejecución
Pesos iniciales `[0.55, -0.12, 0.72]` y sesgo `0.39`. Con ellos la neurona decía "VIP" para los 8 clientes, así que fallaba en 4:

| Cliente | z | Dijo | Era | Qué cambió |
|---|---|---|---|---|
| (0,0,0) | +0.39 | 1 | 0 | Solo el sesgo (0.39 → 0.29). Con todas las entradas en 0, ningún peso se mueve |
| (0,0,1) | +1.01 | 1 | 0 | `w3` baja de 0.72 a 0.62 y el sesgo a 0.19 |
| (0,1,0) | +0.07 | 1 | 0 | `w2` baja de -0.12 a -0.22 y el sesgo a 0.09 |
| (1,0,0) | +0.64 | 1 | 0 | `w1` baja de 0.55 a 0.45 y el sesgo a -0.01 |

Los otros 4 clientes los acertó y no tocó nada. Tras 8 épocas (la octava ya sin errores) quedó en `[0.25, 0.28, 0.32]` y sesgo `-0.51`.

### Paso 4: la red de scikit-learn
```python
mlp = MLPClassifier(hidden_layer_sizes=(4,), max_iter=3000, random_state=42).fit(X, y)
```
- Es una red con **3 entradas → 1 capa oculta de 4 neuronas → 1 salida**. `n_layers_ = 3` cuenta entrada, oculta y salida.
- `coefs_[0]` tiene forma `(3, 4)`: cada una de las 3 entradas conectada a cada una de las 4 neuronas ocultas, **12 pesos**. `coefs_[1]` es `(4, 1)`: **4 pesos** hacia la salida.
- `max_iter` es el máximo de iteraciones, otro criterio de finalización.

---

## 7. Respuestas a las preguntas de comprensión

### Pregunta 1 · Entradas, pesos y umbral
- **Las 3 entradas** son las señales del cliente: compra frecuente, gasto alto y compra reciente (1 = la cumple).
- **Los pesos** indican cuánto cuenta cada señal en la decisión. Quedaron parecidos (`0.25`, `0.28`, `0.32`): las tres pesan casi igual, y por eso la regla "al menos 2 de 3" funciona.
- **El umbral** es el corte. Con sesgo `-0.51`, la neurona dice VIP solo si la suma de pesos activos supera 0.51:
  - Una sola señal suma como máximo `0.32`, no alcanza.
  - Dos señales suman al menos `0.53` (`0.25 + 0.28`), sí superan el corte.

El umbral quedó entre lo que suma una señal y lo que suman dos. Nadie le dijo "2 de 3": lo aprendió de los ejemplos. Nota que el margen es estrecho (`0.53` frente a `0.51`), porque el entrenamiento se detiene en cuanto deja de fallar, no busca los pesos ideales.

### Pregunta 2 · Por qué no importa empezar con pesos al azar
Porque los pesos iniciales son solo un punto de partida: la red todavía no sabe nada, así que cualquiera sirve. Lo que importa es que cada error empuja los pesos en la dirección correcta. En el ejemplo, los pesos iniciales hacían que **todos** fueran VIP, y con 8 épocas de correcciones terminó acertando los 8. El segundo peso empezó negativo (`-0.12`) y terminó positivo (`0.28`): los datos le "enseñaron" que un gasto alto suma.

**[Complemento]** En redes con capas ocultas el azar además es necesario: si todos los pesos empezaran iguales, las neuronas ocultas se comportarían igual y aprenderían lo mismo. La aleatoriedad las hace distintas.

---

### Pregunta 3 · Pocos ejemplos con ajuste rápido o muchos con ajuste lento
Es mejor **muchos ejemplos y ajuste lento**: se busca que la red **generalice** y no que memorice. El material lo justifica con que el ajuste rápido no suele funcionar bien en redes con muchas neuronas, y la conexión con el sobreajuste de UD3 (memorizar los datos de entrenamiento) es la lectura correcta.

---

### Pregunta de repaso · Por qué solo cambió `w3`

La línea clave es:

```python
w = w + lr * error * xi
```

Para el cliente `(0,0,1)`, con `error = -1` y `lr = 0.1`, el cambio de cada peso es `lr × error × su entrada`:

| Peso | Cálculo | Cambio |
|---|---|---|
| `w1` | 0.1 × (-1) × **0** | 0 |
| `w2` | 0.1 × (-1) × **0** | 0 |
| `w3` | 0.1 × (-1) × **1** | **-0.1** (0.72 → 0.62) |

Si la entrada vale 0, el cambio vale 0. Y tiene lógica: esa señal no estaba activa, así que **no contribuyó** a la respuesta equivocada (aportaba 0 a la suma). Solo `x3` empujó la suma hacia arriba, y por eso solo `w3` se corrige. La corrección cae donde estuvo la "responsabilidad".

El sesgo `b` sí cambió siempre (0.29 → 0.19) porque se ajusta con `lr * error`, sin multiplicar por ninguna entrada; es como una entrada fija en 1. En `(0,0,0)` pasó lo mismo: con todas las entradas en 0, ningún peso se movió y solo se movió el sesgo.

Esto conecta con el material: ahí se dice que se ajustan los pesos de las entradas **activas**. La versión del código es más precisa, porque además usa el **signo del error** para decidir el sentido:
- `error = -1` (dijo VIP y no lo era): los pesos de las entradas activas **bajan**.
- `error = +1` (debía ser VIP y no lo dijo): **suben**.

La regla formal la verás en el perceptrón (UD8).

---

## 🧠 Lo que debes recordar

1. Una RNA se compone de **capas** (entrada, ocultas, salida) unidas por **pesos** ajustables.
2. La capa de entrada recibe los datos; las ocultas procesan (no son visibles desde fuera); la salida entrega el resultado.
3. Los pesos **empiezan al azar** y el entrenamiento los ajusta comparando la respuesta de la red con el resultado conocido.
4. Se ajustan **poco a poco**: mejor muchos ejemplos y ajuste lento, para que la red generalice en vez de memorizar.
5. Una neurona calcula una **suma ponderada** y reconoce el patrón si supera un **umbral**.
6. Los pesos se corrigen **solo cuando hay error**, y solo en proporción a las entradas que estaban activas.
7. Tú defines la arquitectura y la tasa de ajuste; **la red aprende los pesos**.
