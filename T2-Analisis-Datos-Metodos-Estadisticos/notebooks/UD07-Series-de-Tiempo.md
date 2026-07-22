# 📈 UD7 — Series de Tiempo

**Asignatura:** Análisis de Datos y Métodos Estadísticos
**Semana:** S7

---

## 1. Componentes de una serie de tiempo

| Componente | Qué es | Ejemplo |
|---|---|---|
| **Tendencia** | Comportamiento a largo plazo (crece o decrece) | La clínica crece 5% anual en consultas |
| **Estacionalidad** | Fluctuación periódica que se repite en un lapso fijo | Más consultas en diciembre-enero y primavera |
| **Ciclos** | Desviaciones largas de la tendencia, sin periodo fijo | Recesión económica que reduce visitas por 2-3 años |
| **Movimiento irregular** | Lo que sobra tras quitar tendencia+estacionalidad+ciclos — ruido | Pico inesperado por un brote local |

**Advertencia:** los meses no son homogéneos (distinto número de días/fines de semana), y hay ciclicidad que no coincide con el calendario — no sacar conclusiones apresuradas de una sola gráfica.

---

## 2. Gráfico de secuencia

Primer paso obligatorio antes de modelar: graficar `xt` vs. tiempo para detectar tendencia, estacionalidad y heterocedasticidad.

```python
import pandas as pd
import matplotlib.pyplot as plt

serie = pd.Series(consultas, index=fechas)
serie.plot(figsize=(10,4), marker="o", markersize=3)
```
```r
serie <- ts(consultas, start = c(2023, 1), frequency = 12)
plot(serie)
```

---

## 3. Métodos de pronóstico y suavización

| Situación | Método |
|---|---|
| Sin tendencia, sin estacionalidad | Promedio móvil |
| Con tendencia, sin estacionalidad | Suavización exponencial doble (Holt) |
| Con tendencia y estacionalidad | Método de Winters (Holt-Winters) |
| Solo describir componentes | Descomposición |

### Descomposición
```python
from statsmodels.tsa.seasonal import seasonal_decompose
resultado = seasonal_decompose(serie, model="additive", period=12)
resultado.plot()
```
```r
decompose(serie, type = "additive")
```

### Promedio móvil
```python
serie.rolling(window=3).mean()
```
```r
library(zoo); rollmean(serie, k=3, fill=NA)
```

### Suavización exponencial doble (Holt)
```python
from statsmodels.tsa.holtwinters import Holt
Holt(serie).fit().forecast(6)
```
```r
HoltWinters(serie, gamma = FALSE)
```

### Método de Winters
```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing
ExponentialSmoothing(serie, trend="add", seasonal="add", seasonal_periods=12).fit().forecast(6)
```
```r
HoltWinters(serie)
```

---

## 4. ARIMA y correlación

| Concepto | Qué hace |
|---|---|
| Diferenciación | Elimina tendencia/estacionalidad para volver la serie estacionaria |
| Desfase (lag) | Compara un valor con otro k periodos atrás |
| Autocorrelación (ACF) | Correlación de la serie consigo misma en distintos desfases — guía componente MA |
| Autocorrelación parcial (PACF) | Correlación en desfase k controlando desfases intermedios — guía componente AR |

```python
from statsmodels.tsa.arima.model import ARIMA
ARIMA(serie, order=(1,1,1)).fit()
```
```r
arima(serie, order = c(1,1,1))
```

---

## 📚 Referencias

Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). *Time Series Analysis: Forecasting and Control* (5.ª ed.). Wiley.

---

## 🗺️ Way of Work — Análisis de Series de Tiempo

Checklist reutilizable para cualquier serie de tiempo (consultas, ventas, cualquier variable con fecha). Es un diagnóstico progresivo: cada paso indica qué buscar y qué hacer con lo que se encuentra.

```
PASO 1 — Graficar y describir la serie          (10 min)
         Visualizar antes de modelar nada
PASO 2 — Descomponer la serie                    (10 min)
         Separar tendencia, estacionalidad, residuo
PASO 3 — Evaluar estacionariedad                 (10-15 min)
         ¿La serie es estable en el tiempo?
PASO 4 — Elegir el método según el diagnóstico   (5 min)
         Tabla de decisión según lo que encontraste
PASO 5 — Ajustar el modelo                       (10-15 min)
         Entrenar con los datos históricos
PASO 6 — Validar el modelo                       (10-15 min)
         ¿Los residuos son ruido blanco? ¿Qué tan preciso es?
PASO 7 — Pronosticar e interpretar               (5-10 min)
         Proyección + intervalo de confianza + sanity check
```

### PASO 1 — Graficar y describir la serie

Graficar `xt` vs. tiempo, sin tocar nada más todavía.

| Pregunta | Cómo se ve |
|---|---|
| ¿Hay tendencia? | La serie sube o baja de forma sostenida |
| ¿Hay estacionalidad? | Se repite un patrón similar cada cierto periodo fijo |
| ¿Hay heterocedasticidad? | La amplitud de las fluctuaciones cambia según el nivel |
| ¿Hay outliers/quiebres? | Picos o caídas que no encajan con el patrón general |

```python
serie.plot(figsize=(10,4), marker="o", markersize=3)
```
```r
plot(serie, main = "Serie original")
```

**Antes de seguir:** si hay un outlier claramente causado por un evento externo conocido, decidir si corregirlo/interpolarlo o dejarlo — un valor extremo puede distorsionar el análisis posterior.

### PASO 2 — Descomponer la serie

```python
from statsmodels.tsa.seasonal import seasonal_decompose
resultado = seasonal_decompose(serie, model="additive", period=12)
resultado.plot()
```
```r
descomposicion <- decompose(serie, type = "additive")
plot(descomposicion)
```

**Decisión clave — ¿aditiva o multiplicativa?**

| Si observas... | Usa modelo |
|---|---|
| Amplitud estacional constante sin importar el nivel | Aditivo |
| Amplitud estacional proporcional al nivel | Multiplicativo |

**Qué revisar:** tendencia (¿confirma lo visto? ¿lineal, curva, plana?), patrón estacional (¿consistente año con año?), residuo (debería verse como ruido aleatorio — si aún muestra forma, revisar la periodicidad usada).

### PASO 3 — Evaluar estacionariedad

Una serie es **estacionaria** si su media, varianza y autocorrelación no cambian con el tiempo — la mayoría de métodos clásicos (especialmente ARIMA) lo requieren.

**Prueba formal — Dickey-Fuller Aumentada (ADF):**

```python
from statsmodels.tsa.stattools import adfuller
resultado_adf = adfuller(serie)
print(f"Estadístico ADF: {resultado_adf[0]:.3f} | p-valor: {resultado_adf[1]:.4f}")
# H0: la serie NO es estacionaria. Si p < 0.05 → se rechaza H0 → SÍ es estacionaria
```
```r
library(tseries)
adf.test(serie)  # p < 0.05 → estacionaria
```

**Si NO es estacionaria → diferenciar:**

```python
serie_diferenciada = serie.diff().dropna()
adfuller(serie_diferenciada)  # volver a probar
```
```r
serie_diferenciada <- diff(serie)
adf.test(serie_diferenciada)
```

Repetir hasta que el p-valor de ADF sea < 0.05. El número de veces diferenciado es el parámetro **d** de ARIMA(p,d,q).

### PASO 4 — Elegir el método según el diagnóstico

| Diagnóstico | Método recomendado |
|---|---|
| Sin tendencia, sin estacionalidad | Promedio móvil |
| Con tendencia, sin estacionalidad | Suavización exponencial doble (Holt) |
| Con tendencia y con estacionalidad | Método de Winters (Holt-Winters) |
| Serie estacionaria/diferenciada, se busca más flexibilidad | ARIMA (apoyado en ACF/PACF) |
| Solo se quiere describir componentes | Descomposición (Paso 2) |

**Si se usa ARIMA, mirar ACF/PACF de la serie diferenciada:**

```python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
plot_acf(serie_diferenciada)
plot_pacf(serie_diferenciada)
```
```r
acf(serie_diferenciada)
pacf(serie_diferenciada)
```

| Qué se observa | Sugiere |
|---|---|
| PACF se corta abruptamente en p, ACF decae lento | AR(p) |
| ACF se corta abruptamente en q, PACF decae lento | MA(q) |
| Ambos decaen gradualmente | Modelo mixto ARMA(p,q) |

### PASO 5 — Ajustar el modelo

Dividir en **entrenamiento** y **prueba** (ej. últimos 6 meses) — nunca entrenar y validar con los mismos datos.

```python
train = serie[:-6]
test = serie[-6:]

from statsmodels.tsa.holtwinters import ExponentialSmoothing
modelo = ExponentialSmoothing(train, trend="add", seasonal="add", seasonal_periods=12).fit()
```
```r
train <- window(serie, end = c(2025, 6))
test <- window(serie, start = c(2025, 7))
modelo <- HoltWinters(train)
```

### PASO 6 — Validar el modelo

**a) Diagnóstico de residuos** (deben verse como ruido blanco):

```python
residuos = modelo.resid
plot_acf(residuos)  # no debería haber barras significativas
```
```r
checkresiduals(modelo)  # requiere library(forecast)
```

**b) Precisión contra el set de prueba:**

```python
pronostico_test = modelo.forecast(6)
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

mae = mean_absolute_error(test, pronostico_test)
rmse = np.sqrt(mean_squared_error(test, pronostico_test))
mape = np.mean(np.abs((test - pronostico_test) / test)) * 100
```
```r
pronostico_test <- predict(modelo, n.ahead = 6)
mae <- mean(abs(test - pronostico_test))
rmse <- sqrt(mean((test - pronostico_test)^2))
mape <- mean(abs((test - pronostico_test) / test)) * 100
```

**Interpretación de MAPE:**

| MAPE | Calidad del modelo |
|---|---|
| < 10% | Excelente |
| 10-20% | Bueno |
| 20-50% | Aceptable, con reservas |
| > 50% | Pobre — reconsiderar método |

### PASO 7 — Pronosticar e interpretar

Reentrenar con **todos** los datos (no solo entrenamiento) y generar el pronóstico final con intervalo de confianza.

```python
modelo_final = ExponentialSmoothing(serie, trend="add", seasonal="add", seasonal_periods=12).fit()
pronostico_final = modelo_final.forecast(6)
```

**Sanity check final antes de entregar cualquier pronóstico:**
- ¿El pronóstico tiene sentido con el conocimiento del negocio?
- ¿El intervalo de confianza es razonable, o tan ancho que no sirve para decidir?
- ¿Hay algún evento futuro conocido (campaña, apertura de sucursal) que el modelo no puede anticipar por no estar en los datos históricos?

