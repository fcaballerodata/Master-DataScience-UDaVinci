# 📈 UD4 — Regresión Lineal Simple y Múltiple

**Asignatura:** Análisis de Datos y Métodos Estadísticos  
**Semana:** S4 (29 Jun – 4 Jul 2026)

---

## 🎯 Conceptos clave

La regresión lineal es una técnica paramétrica para predecir una variable continua dependiente a partir de una o más variables independientes. Origen: Francis Galton (1886), estudio de la estatura de padres e hijos.

---

## 1. Regresión Lineal Simple

Una variable independiente (X) predice una variable dependiente (Y).

**Ejemplo:** en una clínica veterinaria, ¿el número de mascotas atendidas (X) predice los ingresos diarios (Y) de una sede?

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

**Ejemplo:** predecir el costo de una consulta veterinaria (Y) usando especie, peso, tipo de procedimiento y sede (X1, X2, X3, X4).

### Pasos

1. Matriz de correlación entre variables independientes y la dependiente
2. Identificar variables con mayor correlación con Y
3. Construir el modelo
4. Evaluar con F-Test, R² y coeficientes Beta

### ⚠️ Multicolinealidad

Ocurre cuando dos o más variables independientes están correlacionadas entre sí (no solo con Y). Ejemplo: "peso" y "talla" de una mascota probablemente estén muy correlacionados — esto infla artificialmente los coeficientes. Solución: identificar y eliminar la variable redundante.

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

# ── 2. REGRESIÓN SIMPLE — Clínica veterinaria ─────────────────
np.random.seed(42)
mascotas_dia = np.array([10, 15, 12, 20, 18, 25, 14, 22, 16, 19])
ingresos_dia = mascotas_dia * 45000 + np.random.normal(0, 30000, 10)

X = mascotas_dia.reshape(-1, 1)
y = ingresos_dia

modelo = LinearRegression()
modelo.fit(X, y)
print(f"Intercepto: {modelo.intercept_:.2f} | Coef: {modelo.coef_[0]:.2f}")
print(f"R²: {modelo.score(X, y):.4f}")
print(f"Predicción 20 mascotas: {modelo.predict([[20]])[0]:.0f}")

# Visualización + residuos
plt.scatter(mascotas_dia, ingresos_dia, color='steelblue')
plt.plot(mascotas_dia, modelo.predict(X), color='red')
plt.xlabel("N° mascotas/día"); plt.ylabel("Ingresos")
plt.title("Regresión Lineal Simple")
plt.show()

# ── 3. REGRESIÓN MÚLTIPLE ──────────────────────────────────────
datos = pd.DataFrame({
    'peso':         [5, 22, 3, 35, 8, 15, 28, 4, 18, 30],
    'duracion_min': [20, 35, 15, 50, 25, 30, 45, 18, 32, 48],
    'es_cirugia':   [0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
    'costo':        [50, 120, 40, 200, 60, 80, 180, 35, 90, 195]
})

X_multi = sm.add_constant(datos[['peso', 'duracion_min', 'es_cirugia']])
modelo_multi = sm.OLS(datos['costo'], X_multi).fit()
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
mascotas_dia <- c(10, 15, 12, 20, 18, 25, 14, 22, 16, 19)
ingresos_dia <- mascotas_dia * 45000 + rnorm(10, 0, 30000)

modelo <- lm(ingresos_dia ~ mascotas_dia)
summary(modelo)
predict(modelo, newdata = data.frame(mascotas_dia = 20))

plot(mascotas_dia, ingresos_dia, col="steelblue", pch=19)
abline(modelo, col="red", lwd=2)

# ── 3. REGRESIÓN MÚLTIPLE ──────────────────────────────────────
datos <- data.frame(
  peso = c(5, 22, 3, 35, 8, 15, 28, 4, 18, 30),
  duracion_min = c(20, 35, 15, 50, 25, 30, 45, 18, 32, 48),
  es_cirugia = c(0, 1, 0, 1, 0, 0, 1, 0, 0, 1),
  costo = c(50, 120, 40, 200, 60, 80, 180, 35, 90, 195)
)

modelo_multi <- lm(costo ~ peso + duracion_min + es_cirugia, data = datos)
summary(modelo_multi)
cor(datos)
```

---

## 🗺️ Mapa mental

```
UD4: REGRESIÓN LINEAL SIMPLE Y MÚLTIPLE
│
├── Simple
│     ├── 1 X → predice Y
│     ├── Residuo = Observado − Predicho
│     └── Mínimos Cuadrados (MCO)
│
├── Bondad de Ajuste
│     ├── RSE → error promedio
│     ├── Test F → p<0.05 = significativo
│     └── R² → % variabilidad explicada
│
├── Condiciones
│     └── Linealidad, normalidad, homocedasticidad, sin outliers, independencia
│
├── Correlación (r)
│     └── -1 a +1: dirección y fuerza
│
└── Múltiple
      ├── Varias X → predicen Y
      ├── ⚠️ Multicolinealidad → X's correlacionadas entre sí
      └── F-Test, R², Coeficientes Beta
```

---

## 📚 Referencias

Gutiérrez González, E., & Panteleeva, O. V. (2016). *Estadística inferencial 1 para ingeniería y ciencias*. Grupo Editorial Patria.

Montgomery, D. C., & Runger, G. C. (2010). *Probabilidad y estadística aplicadas a la ingeniería* (2.ª ed.). Limusa Wiley.
