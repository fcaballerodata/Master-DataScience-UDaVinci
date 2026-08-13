# 📈 UD4 — Regresión Lineal Simple y Múltiple

**Asignatura:** Análisis de Datos y Métodos Estadísticos
**Semana:** S4 (29 Jun – 4 Jul 2026)

---

## 📌 Aplicación profesional

**¿Para qué sirve?** Cuantificar y predecir la relación entre variables numéricas: qué tanto cambia Y cuando cambia X, y qué tan bien esa relación permite predecir valores futuros o desconocidos.

**¿Cómo se usa?** Se ajusta una línea (simple, con una X) o un hiperplano (múltiple, con varias X) que minimice el error de predicción, y se evalúa qué tan confiable es ese ajuste (R², significancia de coeficientes) antes de usarlo para predecir.

**¿En qué casos lo vas a usar como Data Analyst / Data Scientist?**
- **Forecasting de ventas:** predecir ingresos futuros según gasto en publicidad, temporada, tráfico web.
- **Pricing:** entender qué atributos de un producto explican su precio (ej. modelos hedónicos de precios inmobiliarios).
- **Diagnóstico de negocio:** cuantificar cuánto impacta cada variable operativa (headcount, horas extra, inversión en marketing) sobre un resultado (ventas, satisfacción, rotación).
- Es también la base conceptual de modelos más avanzados de Machine Learning (regresión regularizada, GLM, incluso la primera capa de una red neuronal es literalmente una regresión lineal).

---

## 🎯 Conceptos clave

La regresión lineal es una técnica paramétrica para predecir una variable continua dependiente a partir de una o más variables independientes. Origen: Francis Galton (1886), estudio de la estatura de padres e hijos.

---

## 1. Regresión Lineal Simple

Una variable independiente (X) predice una variable dependiente (Y).

**Ejemplo:** ¿el gasto en publicidad (X) predice las ventas mensuales (Y) de una tienda?

### Residuos

```
Residuo = Valor observado − Valor esperado (predicho)
```

Método de ajuste: **Mínimos Cuadrados (MCO)** — minimiza la suma del cuadrado de cada residuo (penaliza más los errores grandes).

---

## 2. Bondad de Ajuste

| Medida | Qué mide | Interpretación |
|---|---|---|
| **Error Estándar Residual (RSE)** | Desviación promedio predicción vs realidad | Menor RSE = mejor ajuste |
| **Test F** | H₀: todos los coeficientes = 0 | p < 0.05 → modelo significativo |
| **R² (determinación)** | % de variabilidad de Y explicada | 0 a 1; más cerca de 1 = mejor |

---

## 3. Condiciones del modelo

| Supuesto | Verificación |
|---|---|
| Linealidad | Scatterplot X vs Y |
| Normalidad de residuos | Histograma de residuos |
| Homocedasticidad | Scatterplot residuos vs predicción |
| Sin outliers de alta influencia | Inspección visual |
| Independencia | Relevante en series de tiempo |

---

## 4. Coeficiente de Correlación (r) — Ejemplo paso a paso

| Venta Helado (X) | Temperatura °F (Y) |
|---|---|
| 3 | 70 |
| 6 | 75 |
| 9 | 80 |

```
X̄ = 6 | Ȳ = 75
Desviaciones X: -3, 0, 3
Desviaciones Y: -5, 0, 5

Numerador = (-3)(-5)+(0)(0)+(3)(5) = 30
Denominador = √[(9+0+9)(25+0+25)] = √900 = 30

r = 30/30 = 1.0  → Correlación perfecta positiva
```

> En datos reales, r = 1.0 exacto es casi imposible — siempre revisar el scatterplot, no solo el número.

---

## 5. Regresión Lineal Múltiple

Varias variables independientes predicen una sola variable dependiente.

**Ejemplo ilustrativo — Precio de una vivienda:** predecir el precio de venta (Y) usando metros cuadrados, número de habitaciones, y antigüedad de la propiedad (X1, X2, X3) — el ejemplo clásico de regresión múltiple en analítica de negocio/bienes raíces.

### Pasos

1. Matriz de correlación entre variables independientes y la dependiente
2. Identificar variables con mayor correlación con Y
3. Construir el modelo
4. Evaluar con F-Test, R² y coeficientes Beta

### ⚠️ Multicolinealidad

Ocurre cuando dos o más variables independientes están correlacionadas entre sí (no solo con Y). Ejemplo: en un modelo de precios de vivienda, "metros cuadrados totales" y "número de habitaciones" suelen estar muy correlacionados entre sí — esto infla artificialmente los coeficientes. Solución: identificar y eliminar la variable redundante, o usar técnicas de regularización (Ridge/Lasso).

### Métricas

| Métrica | Interpretación |
|---|---|
| F-Test | p < 0.05 → al menos una variable es significativa |
| R² | % de variabilidad de Y explicada por el conjunto |
| Coeficiente Beta (β) | Intensidad y dirección del efecto individual |

---

## 6. Código Python

```python
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# ── 1. COEFICIENTE DE CORRELACIÓN ─────────────────────────────
ventas_helado = np.array([3, 6, 9])
temperatura   = np.array([70, 75, 80])
r, p_valor = stats.pearsonr(ventas_helado, temperatura)
print(f"r = {r:.4f}")

# ── 2. REGRESIÓN SIMPLE — Gasto en publicidad vs Ventas ────────
np.random.seed(42)
gasto_publicidad = np.array([10, 15, 12, 20, 18, 25, 14, 22, 16, 19])  # miles $
ventas = gasto_publicidad * 4.5 + np.random.normal(0, 3, 10)  # miles $

X = gasto_publicidad.reshape(-1, 1)
y = ventas

modelo = LinearRegression()
modelo.fit(X, y)
print(f"Intercepto: {modelo.intercept_:.2f} | Coef: {modelo.coef_[0]:.2f}")
print(f"R²: {modelo.score(X, y):.4f}")
print(f"Predicción con $20k de publicidad: {modelo.predict([[20]])[0]:.1f}")

# Visualización + residuos
plt.scatter(gasto_publicidad, ventas, color='steelblue')
plt.plot(gasto_publicidad, modelo.predict(X), color='red')
plt.xlabel("Gasto en publicidad (miles $)"); plt.ylabel("Ventas (miles $)")
plt.title("Regresión Lineal Simple")
plt.show()

# ── 3. REGRESIÓN MÚLTIPLE — Precio de vivienda ──────────────────
datos = pd.DataFrame({
    'metros_cuadrados': [50, 120, 35, 200, 80, 150, 90, 45, 110, 180],
    'habitaciones':     [1, 3, 1, 4, 2, 3, 2, 1, 3, 4],
    'antiguedad_anios': [20, 5, 30, 2, 15, 8, 12, 25, 6, 3],
    'precio_miles':     [80, 220, 55, 380, 140, 260, 155, 70, 210, 340]
})

X_multi = sm.add_constant(datos[['metros_cuadrados', 'habitaciones', 'antiguedad_anios']])
modelo_multi = sm.OLS(datos['precio_miles'], X_multi).fit()
print(modelo_multi.summary())
print("\nMatriz de correlación:")
print(datos.corr())
```

---

## 7. Código R

```r
# ── 1. COEFICIENTE DE CORRELACIÓN ─────────────────────────────
ventas_helado <- c(3, 6, 9)
temperatura   <- c(70, 75, 80)
r <- cor(ventas_helado, temperatura)
cat("r =", round(r, 4), "\n")

# ── 2. REGRESIÓN SIMPLE ────────────────────────────────────────
set.seed(42)
gasto_publicidad <- c(10, 15, 12, 20, 18, 25, 14, 22, 16, 19)
ventas <- gasto_publicidad * 4.5 + rnorm(10, 0, 3)

modelo <- lm(ventas ~ gasto_publicidad)
summary(modelo)
predict(modelo, newdata = data.frame(gasto_publicidad = 20))

plot(gasto_publicidad, ventas, col="steelblue", pch=19)
abline(modelo, col="red", lwd=2)

# ── 3. REGRESIÓN MÚLTIPLE — Precio de vivienda ──────────────────
datos <- data.frame(
  metros_cuadrados = c(50, 120, 35, 200, 80, 150, 90, 45, 110, 180),
  habitaciones = c(1, 3, 1, 4, 2, 3, 2, 1, 3, 4),
  antiguedad_anios = c(20, 5, 30, 2, 15, 8, 12, 25, 6, 3),
  precio_miles = c(80, 220, 55, 380, 140, 260, 155, 70, 210, 340)
)

modelo_multi <- lm(precio_miles ~ metros_cuadrados + habitaciones + antiguedad_anios, data = datos)
summary(modelo_multi)
cor(datos)
```

---

## 🗺️ Way of Work — Regresión Lineal (Simple y Múltiple)

```
PASO 1 — Explorar la relación con un scatterplot antes de modelar nada
PASO 2 — Calcular la correlación (r) entre cada X y la Y
PASO 3 — Ajustar el modelo (simple o múltiple)
PASO 4 — Verificar los supuestos (linealidad, normalidad, homocedasticidad)
PASO 5 — Evaluar bondad de ajuste (R², Test F, significancia de coeficientes)
PASO 6 — Revisar multicolinealidad si es regresión múltiple
PASO 7 — Predecir e interpretar los coeficientes en el contexto del negocio
```

1. **Explorar visualmente primero:** un scatterplot revela relaciones no lineales que el coeficiente r no captura bien.
2. **Correlación:** te da una primera pista de qué variables vale la pena incluir en el modelo.
3. **Ajustar el modelo:** `LinearRegression` (sklearn) para uso predictivo rápido, `statsmodels.OLS` cuando necesitas el detalle estadístico completo (p-valores, intervalos de confianza de los coeficientes).
4. **Verificar supuestos:** un R² alto con supuestos violados (ej. heterocedasticidad) puede ser engañoso — revisa siempre el gráfico de residuos.
5. **Evaluar bondad de ajuste:** no te quedes solo con R² — revisa también si los coeficientes individuales son significativos (p<0.05).
6. **Multicolinealidad:** calcula la matriz de correlación entre las X — si dos variables tienen correlación >0.8 entre sí, considera eliminar una.
7. **Interpretar en contexto:** un coeficiente estadísticamente significativo pero con efecto pequeño puede no ser accionable para el negocio — siempre traduce el coeficiente a magnitudes reales (ej. "$1,000 adicionales en publicidad generan ~$4,500 en ventas").

---

## 📚 Referencias

Gutiérrez González, E., & Panteleeva, O. V. (2016). *Estadística inferencial 1 para ingeniería y ciencias*. Grupo Editorial Patria.

Montgomery, D. C., & Runger, G. C. (2010). *Probabilidad y estadística aplicadas a la ingeniería* (2.ª ed.). Limusa Wiley.

