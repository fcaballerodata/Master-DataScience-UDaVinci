# Actividad Integradora 2 — UD6 a UD10

**Asignatura:** Análisis de Datos y Métodos Estadísticos
**Semana:** S10

Cuatro entregables: (1a) Series de tiempo — IVE y desestacionalización, (1b) ANOVA, (1c) Prueba no paramétrica, (2) Resumen de artículo científico, (3) Redes neuronales con TensorFlow. El desarrollo numérico completo (tablas paso a paso) está en el documento Word entregado; aquí se documentan los resultados clave y el **Way of Work en Python** de cada técnica, para repetir el proceso en futuros ejercicios.

---

## Resultados clave

**1a — IVE:** T1=1.1226, T2=1.1136, T3=0.8658, T4=0.8980 (esquema multiplicativo, CMA 2x4).

**1b — ANOVA (3 tratamientos de rehabilitación):** F=1.0956 < F crítico=3.9823 (p=0.3682) → no se rechaza H₀, sin diferencia significativa entre tratamientos.

**1c — Mann-Whitney (tensión y peso de glándula suprarrenal):** U=112, p=0.0782 → no se rechaza H₀, sin evidencia suficiente de que la tensión aumente el peso (resultado cercano al umbral).

**2 — Resumen:** Vélez Evans, M. I. (2006). *El proceso de toma de decisiones como un espacio para el aprendizaje en las organizaciones*. Revista Ciencias Estratégicas, 14(16), 153-169.

**3 — Redes neuronales (TensorFlow):** los 3 ejercicios de conversión de unidades (pies→metros, litros→onzas, pulgadas→cm) resueltos con una neurona simple; los pesos aprendidos coincidieron con los factores de conversión reales (0.3048, 33.814, 2.54).

---

## 🗺️ Way of Work — Índices de Variación Estacional y Desestacionalización (Python)

```
PASO 1 — Cargar la serie en pandas, ordenada cronológicamente
PASO 2 — Calcular la tendencia (Media Móvil Centrada 2xN, N=periodo estacional)
PASO 3 — Eliminar la tendencia: Serie ÷ Tendencia = Estacional × Irregular
PASO 4 — Promediar S×I por periodo (trimestre/mes) para eliminar el irregular
PASO 5 — Normalizar para que los índices sumen N (o promedien 1.0)
PASO 6 — Desestacionalizar: Serie ÷ IVE correspondiente
```

```python
import pandas as pd
import numpy as np

# PASO 1: cargar serie (ejemplo trimestral, N=4)
serie = pd.Series([1598,1703,939,1230, 1001,893,793,1419, 2636,1663,2311,1393, 2191,4343,2133,3393])
N = 4  # periodo estacional (4=trimestral, 12=mensual)

# PASO 2: tendencia con media movil centrada 2xN
pesos = np.array([0.5] + [1]*(N-1) + [0.5]) / N
cma = [np.nan]*(N//2)
for t in range(N//2, len(serie)-N//2):
    ventana = serie[t-N//2 : t+N//2+1].values
    cma.append(np.dot(ventana, pesos))
cma.extend([np.nan]*(N//2))
cma = pd.Series(cma)

# PASO 3: eliminar tendencia (esquema multiplicativo)
si = serie / cma

# PASO 4: promediar por periodo estacional
etiquetas_periodo = [i % N for i in range(len(serie))]
df = pd.DataFrame({'periodo': etiquetas_periodo, 'SI': si})
promedios = df.groupby('periodo')['SI'].mean()

# PASO 5: normalizar (factor de ajuste)
factor = N / promedios.sum()
ive = promedios * factor

# PASO 6: desestacionalizar
ive_serie = pd.Series([ive[p] for p in etiquetas_periodo])
desestacionalizada = serie / ive_serie
```

**Alternativa automática (misma lógica, ya empaquetada):**
```python
from statsmodels.tsa.seasonal import seasonal_decompose
resultado = seasonal_decompose(serie, model="multiplicative", period=4)
resultado.trend      # equivalente al Paso 2
resultado.seasonal   # equivalente al Paso 5 (IVE)
serie / resultado.seasonal   # equivalente al Paso 6
```

**Qué revisar en cada paso:** en el Paso 2 se pierden los primeros y últimos N/2 datos (no tienen suficientes vecinos); en el Paso 5, verificar que los IVE sumen exactamente N antes de continuar.

---

## 🗺️ Way of Work — ANOVA de un factor (Python)

```
PASO 1 — Organizar los datos por grupo (listas o columnas separadas)
PASO 2 — Calcular el estadístico F y el p-valor
PASO 3 — (Opcional) Desglosar la tabla ANOVA manualmente para el reporte
PASO 4 — Comparar F vs. F crítico, o el p-valor vs. α
PASO 5 — Interpretar en el contexto del problema
```

```python
import numpy as np
from scipy import stats

grupo1 = [21, 23, 59, 38, 78]
grupo2 = [44, 72, 65, 43, 79]
grupo3 = [39, 46, 61, 49]

# PASO 2: F y p-valor directos
f_stat, p_value = stats.f_oneway(grupo1, grupo2, grupo3)

# PASO 3: desglose manual (para mostrar SC, GL, MC en el reporte)
grupos = [grupo1, grupo2, grupo3]
gran_media = np.mean([x for g in grupos for x in g])
sc_entre = sum(len(g) * (np.mean(g) - gran_media)**2 for g in grupos)
sc_dentro = sum(sum((x - np.mean(g))**2 for x in g) for g in grupos)
gl_entre = len(grupos) - 1
gl_dentro = sum(len(g) for g in grupos) - len(grupos)
mc_entre = sc_entre / gl_entre
mc_dentro = sc_dentro / gl_dentro
F = mc_entre / mc_dentro

# PASO 4: valor crítico de tabla
f_critico = stats.f.ppf(0.95, gl_entre, gl_dentro)
decision = "Rechazar H0" if p_value < 0.05 else "No rechazar H0"
```

**Qué revisar:** verificar que `f_stat` (de `scipy`) coincida con el `F` calculado manualmente — si no coincide, hay un error en el desglose manual. El p-valor es la forma más directa de decidir; el F crítico es la forma "de tabla" tradicional — ambas deben dar la misma conclusión.

---

## 🗺️ Way of Work — Pruebas No Paramétricas (Python)

```
PASO 1 — Verificar el tipo de comparación (muestras pareadas o independientes)
PASO 2 — Elegir la prueba (signo/Wilcoxon si son pareadas, Mann-Whitney si son independientes)
PASO 3 — Definir la hipótesis alterna (bilateral o unilateral) según la pregunta
PASO 4 — Ejecutar la prueba y obtener el estadístico + p-valor
PASO 5 — Interpretar respecto a la mediana, no a la media
```

```python
from scipy.stats import mannwhitneyu, wilcoxon, shapiro

# PASO 1-2: ejemplo con dos muestras INDEPENDIENTES de distinto tamaño -> Mann-Whitney
tratados = [3.8, 6.8, 8.0, 3.6, 3.9, 4.5, 3.9, 4.5, 3.9, 5.9, 6.0, 5.7, 5.6, 4.5]
control  = [4.2, 4.8, 4.8, 2.3, 6.5, 4.9, 3.6, 2.4, 3.2, 4.9, 4.0, 3.8]

# (Opcional) verificar normalidad, solo como contexto -- no es obligatorio para decidir usar la prueba
shapiro(tratados), shapiro(control)

# PASO 3-4: alternative='greater' porque H1 es unilateral ("tratados > control")
resultado = mannwhitneyu(tratados, control, alternative='greater')
print(f"U = {resultado.statistic}, p-valor = {resultado.pvalue:.4f}")

# Si en cambio fueran muestras PAREADAS (mismo sujeto antes/después):
# resultado = wilcoxon(antes, despues, alternative='greater')
```

**Qué revisar:** el parámetro `alternative` debe reflejar exactamente cómo está planteada H1 (`'two-sided'`, `'greater'` o `'less'`) — usar el incorrecto cambia el p-valor. Si scipy reporta empates entre valores, automáticamente aplica la aproximación normal con corrección; no es necesario calcularlo aparte salvo que se quiera mostrar el desglose.

---

## 🗺️ Way of Work — Redes Neuronales con TensorFlow (Python)

```
PASO 1 — Preparar los datos de entrenamiento (pares entrada-salida)
PASO 2 — Definir la arquitectura del modelo (capas, neuronas)
PASO 3 — Compilar (función de pérdida + optimizador)
PASO 4 — Entrenar (fit) y revisar la curva de pérdida
PASO 5 — Predecir con datos nuevos (nunca vistos en entrenamiento)
PASO 6 — Revisar los pesos aprendidos para confirmar que el modelo generalizó
```

```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# PASO 1: datos de entrenamiento (el factor real solo se usa para GENERAR los ejemplos)
entradas = np.array([0, 1, 3, 5, 10, 15, 20, 25, 30, 50, 75, 100], dtype=float)
salidas = entradas * 0.3048  # ej. pies -> metros

# PASO 2: arquitectura -- una sola neurona (equivalente a regresión lineal)
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

# PASO 3: compilar
modelo.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mean_squared_error')

# PASO 4: entrenar
historial = modelo.fit(entradas, salidas, epochs=1000, verbose=False)
plt.plot(historial.history['loss'])  # debe caer y aplanarse -> convergencia

# PASO 5: predecir con un valor nuevo
resultado = modelo.predict(np.array([12.0]), verbose=False)

# PASO 6: revisar peso y sesgo aprendidos
peso, sesgo = capa.get_weights()
print(f"Peso: {peso[0][0]:.4f} (real: 0.3048) | Sesgo: {sesgo[0]:.4f} (real: 0)")
```

**Qué revisar:** si el peso aprendido NO se acerca al valor real esperado (como pasó en el primer intento del Ejercicio 2 de esta actividad, que se quedó en 29.28 en vez de 33.814), el modelo **no convergió** — subir el número de `epochs` y/o ajustar la tasa de aprendizaje del optimizador (`Adam(lr)`) suele resolverlo. Siempre graficar la curva de pérdida: si sigue bajando al final del entrenamiento, hacen falta más épocas.

---

## 📚 Referencias

Anderson, D. R., Sweeney, D. J., & Williams, T. A. (2008). *Estadística para administración y economía* (10.ª ed.). Cengage Learning.

Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). *Time Series Analysis: Forecasting and Control* (5.ª ed.). Wiley.

Gironés Roig, J., Casas Roma, J., Minguillón Alfonso, J., & Caihuelas Quiles, R. (2017). *Minería de datos: Modelos y algoritmos*. Editorial UOC.

Vélez Evans, M. I. (2006). El proceso de toma de decisiones como un espacio para el aprendizaje en las organizaciones. *Revista Ciencias Estratégicas*, 14(16), 153-169.

Ringa Tech. (2021, 7 de julio). *Tu primera red neuronal en Python y Tensorflow* [Video]. YouTube. https://www.youtube.com/watch?v=iX_on3VxZzk
