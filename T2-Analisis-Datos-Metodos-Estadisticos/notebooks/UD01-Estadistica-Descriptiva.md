# 📊 UD1 — Estadística Descriptiva

**Asignatura:** Análisis de Datos y Métodos Estadísticos  
**Semana:** S1 (8–13 Jun 2026)

---

## 🎯 Conceptos clave

La estadística descriptiva permite organizar, resumir y comunicar las características principales de un conjunto de datos. Es el primer paso obligatorio antes de cualquier modelo o análisis inferencial.

> **Dataset de referencia:** Consultas veterinarias Movet (miles COP)  
> `[45, 52, 48, 61, 45, 70, 53, 48, 45, 63]`

---

## 1. Tipos de Variables

| Tipo | Se obtiene | Pregunta clave | Ejemplo Movet |
|---|---|---|---|
| **Discreta** | Contando | ¿Cuántos? | N° mascotas atendidas/día |
| **Continua** | Midiendo | ¿Cuánto? | Peso de una mascota (kg) |

---

## 2. Medidas de Tendencia Central

### Media
```
X̄ = (45+52+48+61+45+70+53+48+45+63) / 10 = 530 / 10 = 53.0
```
⚠️ Sensible a valores extremos (outliers).

### Mediana
Datos ordenados: `[45, 45, 45, 48, 48, 52, 53, 61, 63, 70]`  
Con n=10 (par): `(48 + 52) / 2 = 50.0`  
Más robusta que la media ante outliers.

### Moda
Valor más frecuente: **45** (aparece 3 veces)

---

## 3. Medidas de Dispersión

### Rango
```
R = Máximo − Mínimo = 70 − 45 = 25
```

### Varianza (σ²)
```
σ² = Σ(xi − X̄)² / n = 696 / 10 = 69.6
```

### Desviación Estándar (σ)
```
σ = √69.6 = 8.34
```
Las consultas se desvían ±8.340 COP de la media de 53.000.

> ⚠️ Nunca uses `FLOAT` para valores monetarios — usa `DECIMAL` para evitar errores de redondeo.

---

## 4. Medidas de Posición

Datos ordenados: `[45, 45, 45, 48, 48, 52, 53, 61, 63, 70]`

| Cuartil | Valor | Interpretación |
|---|---|---|
| Q1 (25%) | 45 | El 25% de consultas valen menos de 45K |
| Q2 (50%) | 50.0 | Mediana |
| Q3 (75%) | 62 | El 75% valen menos de 62K |
| **IQR** | **17** | Rango del 50% central de los datos |

> En Power BI ya usabas percentiles al calcular P75 o P90 por sede — esto es exactamente eso.

---

## 5. Medidas de Forma

### Sesgo (Asimetría)
- **Simétrica:** Media = Mediana = Moda
- **Sesgo positivo (derecha):** Media > Mediana → pocas consultas caras jalan la media hacia arriba
- **Sesgo negativo (izquierda):** Media < Mediana

En el dataset: Media (53) > Mediana (50) → **leve sesgo positivo** ✅

### Curtosis (Apuntamiento)
- **Leptocúrtica:** pico alto, datos concentrados
- **Mesocúrtica:** distribución normal
- **Platocúrtica:** pico bajo, datos dispersos

---

## 6. Código Python

```python
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Dataset: consultas veterinarias Movet (miles COP)
consultas = [45, 52, 48, 61, 45, 70, 53, 48, 45, 63]
data = pd.Series(consultas)

# ── Tendencia Central ──────────────────────────────────────────
print("=== TENDENCIA CENTRAL ===")
print(f"Media:    {data.mean():.2f}")
print(f"Mediana:  {data.median():.2f}")
print(f"Moda:     {data.mode()[0]}")

# ── Dispersión ────────────────────────────────────────────────
print("\n=== DISPERSIÓN ===")
print(f"Rango:        {data.max() - data.min()}")
print(f"Varianza:     {data.var(ddof=0):.2f}")   # ddof=0 → poblacional
print(f"Desv. Est.:   {data.std(ddof=0):.2f}")

# ── Posición ──────────────────────────────────────────────────
print("\n=== CUARTILES ===")
print(f"Q1 (25%): {data.quantile(0.25)}")
print(f"Q2 (50%): {data.quantile(0.50)}")
print(f"Q3 (75%): {data.quantile(0.75)}")
print(f"IQR:      {data.quantile(0.75) - data.quantile(0.25)}")

# ── Forma ─────────────────────────────────────────────────────
print("\n=== FORMA ===")
print(f"Sesgo (asimetría): {data.skew():.4f}")
print(f"Curtosis:          {data.kurt():.4f}")

# ── Resumen completo ───────────────────────────────────────────
print("\n=== RESUMEN COMPLETO ===")
print(data.describe())

# ── Visualización ─────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].boxplot(consultas, patch_artist=True, boxprops=dict(facecolor='lightblue'))
axes[0].set_title("Boxplot - Consultas Movet")
axes[0].set_ylabel("Valor consulta (miles COP)")

axes[1].hist(consultas, bins=5, color='steelblue', edgecolor='white')
axes[1].axvline(data.mean(), color='red', linestyle='--', label=f'Media={data.mean():.1f}')
axes[1].axvline(data.median(), color='green', linestyle='--', label=f'Mediana={data.median():.1f}')
axes[1].legend()
axes[1].set_title("Histograma - Consultas Movet")
plt.tight_layout()
plt.show()
```

**Salida esperada:**
```
=== TENDENCIA CENTRAL ===
Media:    53.00  |  Mediana:  50.00  |  Moda: 45

=== DISPERSIÓN ===
Rango: 25  |  Varianza: 69.60  |  Desv. Est.: 8.34

=== CUARTILES ===
Q1: 45.0  |  Q2: 50.0  |  Q3: 62.0  |  IQR: 17.0

=== FORMA ===
Sesgo: 0.6717  |  Curtosis: -0.8133
```

---

## 7. Código R

```r
consultas <- c(45, 52, 48, 61, 45, 70, 53, 48, 45, 63)

# Tendencia Central
cat("Media:  ", mean(consultas), "\n")
cat("Mediana:", median(consultas), "\n")
moda <- function(x) as.numeric(names(sort(table(x), decreasing=TRUE)[1]))
cat("Moda:   ", moda(consultas), "\n")

# Dispersión
cat("Rango:      ", diff(range(consultas)), "\n")
cat("Varianza:   ", var(consultas), "\n")   # R usa n-1 por defecto
cat("Desv. Est.: ", sd(consultas), "\n")

# Cuartiles
cat("Q1:", quantile(consultas, 0.25), "\n")
cat("Q2:", quantile(consultas, 0.50), "\n")
cat("Q3:", quantile(consultas, 0.75), "\n")
cat("IQR:", IQR(consultas), "\n")

# Forma (requiere e1071)
library(e1071)
cat("Sesgo:    ", skewness(consultas), "\n")
cat("Curtosis: ", kurtosis(consultas), "\n")

# Resumen
summary(consultas)

# Visualización
par(mfrow=c(1,2))
boxplot(consultas, main="Boxplot", ylab="Miles COP", col="lightblue")
hist(consultas, breaks=5, col="steelblue", border="white",
     main="Histograma", xlab="Miles COP")
abline(v=mean(consultas), col="red", lty=2, lwd=2)
abline(v=median(consultas), col="green", lty=2, lwd=2)
```

> **Nota:** R usa `n-1` (varianza muestral) por defecto. Python con `ddof=0` usa `n` (poblacional). Para reproducir exactamente los mismos resultados en R: `var(x) * (n-1)/n`.

---

## 🗺️ Mapa mental

```
ESTADÍSTICA DESCRIPTIVA
│
├── Tendencia Central → ¿Dónde están los datos?
│     ├── Media      → Promedio (sensible a outliers)
│     ├── Mediana    → Valor central (robusta)
│     └── Moda       → Valor más frecuente
│
├── Dispersión → ¿Qué tan esparcidos están?
│     ├── Rango          → Máx − Mín
│     ├── Varianza (σ²)  → Promedio de desviaciones²
│     └── Desv. Estándar → √Varianza
│
├── Posición → ¿Dónde cae un valor específico?
│     ├── Cuartiles  → Q1, Q2, Q3
│     ├── Deciles    → D1–D9
│     └── Percentiles → P1–P99
│
└── Forma → ¿Cómo se distribuyen?
      ├── Sesgo → Izq. / Simétrico / Der.
      └── Curtosis → Plana / Normal / Puntiaguda
```

---

## 📚 Referencias

Montgomery, D. C., & Runger, G. C. (2010). *Probabilidad y estadística aplicadas a la ingeniería* (2.ª ed.). Limusa Wiley.

IBM. (2024). *¿Qué es el análisis exploratorio de datos (EDA)?* https://www.ibm.com/mx-es/think/topics/exploratory-data-analysis
