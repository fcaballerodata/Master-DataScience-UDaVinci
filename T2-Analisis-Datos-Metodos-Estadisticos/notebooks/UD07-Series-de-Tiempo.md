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
