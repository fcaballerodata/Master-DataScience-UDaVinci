# 🎲 UD2 — Distribuciones de Probabilidad

**Asignatura:** Análisis de Datos y Métodos Estadísticos  
**Semana:** S2 (15–20 Jun 2026)

---

## 🎯 Conceptos clave

Las distribuciones de probabilidad modelan la frecuencia esperada de los valores de una variable. Son el puente entre los datos observados y las inferencias sobre la población.

---

## 1. Tipos de Variables

| Tipo | Se obtiene | Ejemplo Movet |
|---|---|---|
| **Discreta** | Contando | N° de quejas/día, N° emergencias/noche |
| **Continua** | Midiendo | Peso mascota (kg), tiempo de espera (min) |

> **Regla rápida:** "¿Cuántos?" → discreta. "¿Cuánto?" → continua.

---

## 2. Distribución de Poisson (Discreta)

**Modela:** número de veces que ocurre un evento en un intervalo fijo, dado un promedio histórico (λ).

**Casos de uso en Movet:**
- N° de quejas por día (λ = 8)
- N° de emergencias veterinarias por noche
- N° de cancelaciones de citas por sede al mes

**Ejemplo:** Si el promedio histórico es λ = 8 quejas/día:
```
P(X = 15) = 0.0348   → 3.48% de probabilidad de exactamente 15 quejas
P(X ≥ 15) = 0.0835   → 8.35% de probabilidad de 15 o más quejas
```

---

## 3. Distribución Normal (Continua)

**Modela:** variables continuas simétricas alrededor de una media. Definida por μ (media) y σ (desviación estándar).

**Regla clave:** en variables continuas, la probabilidad de un punto exacto = 0. Siempre se trabaja con **rangos**:
```
P(peso = 25.0 kg exactamente) = 0
P(24.5 kg ≤ peso ≤ 25.5 kg) = área bajo la curva entre esos puntos
```

> La probabilidad es el **área bajo la curva**, no la altura de una barra.

---

## 4. Muestreo y Distribución Muestral

### El problema del muestreo
Con 50.000 registros en Movet, no analizas todos — tomas una **muestra representativa**.

**Métodos:**
- Tómbola / números aleatorios: cada elemento tiene probabilidad conocida e igual de ser elegido
- En Python/R: `sample()` implementa este principio en una línea

### Distribución Muestral de la Media
- **Una muestra** → un conjunto de datos (ej: 300 consultas de enero)
- **La media de esa muestra** → un número (ej: $53.000)
- **Distribución muestral** → si repitieras 1000 veces el muestreo, ¿cómo se distribuyen esas 1000 medias?

**Hallazgo clave:** la media de todas las medias muestrales = media poblacional real.  
Esto es lo que hace funcionar la inferencia estadística.

---

## 5. Código Python

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# ── 1. POISSON — Quejas diarias Movet ─────────────────────────
lam = 8

p_15 = stats.poisson.pmf(15, mu=lam)
p_15_o_mas = 1 - stats.poisson.cdf(14, mu=lam)
print(f"P(X=15)  = {p_15:.4f}")
print(f"P(X>=15) = {p_15_o_mas:.4f}")

# Visualizar
x = np.arange(0, 25)
colors = ['red' if v >= 15 else 'steelblue' for v in x]
plt.bar(x, stats.poisson.pmf(x, mu=lam), color=colors)
plt.title(f"Poisson(λ={lam}) - Quejas diarias Movet")
plt.xlabel("N° de quejas")
plt.show()

# ── 2. NORMAL — Peso perros Labrador ──────────────────────────
mu, sigma = 28, 3  # kg

p_rango = stats.norm.cdf(25.5, mu, sigma) - stats.norm.cdf(24.5, mu, sigma)
print(f"\nP(24.5 ≤ peso ≤ 25.5) = {p_rango:.4f}")

# ── 3. DISTRIBUCIÓN MUESTRAL — Simulación ─────────────────────
np.random.seed(42)
poblacion = np.random.normal(53, 8.34, 50000)
print(f"\nMedia poblacional real: {poblacion.mean():.2f}")

medias_muestrales = [
    np.random.choice(poblacion, size=30, replace=False).mean()
    for _ in range(1000)
]
print(f"Media de 1000 medias muestrales: {np.mean(medias_muestrales):.2f}")
print("→ Se acerca a la media poblacional real (TCL en acción)")
```

---

## 6. Código R

```r
# ── 1. POISSON ─────────────────────────────────────────────────
lambda_val <- 8
cat("P(X=15)  =", round(dpois(15, lambda_val), 4), "\n")
cat("P(X>=15) =", round(1 - ppois(14, lambda_val), 4), "\n")

x <- 0:25
barplot(dpois(x, lambda_val), names.arg=x,
        col=ifelse(x>=15,"red","steelblue"),
        main="Poisson(λ=8) - Quejas diarias",
        xlab="N° quejas", ylab="P")

# ── 2. NORMAL ──────────────────────────────────────────────────
p_rango <- pnorm(25.5, 28, 3) - pnorm(24.5, 28, 3)
cat("P(24.5 ≤ peso ≤ 25.5) =", round(p_rango, 4), "\n")

# ── 3. DISTRIBUCIÓN MUESTRAL ───────────────────────────────────
set.seed(42)
poblacion <- rnorm(50000, mean=53, sd=8.34)
medias <- replicate(1000, mean(sample(poblacion, 30, replace=FALSE)))
cat("Media poblacional:", round(mean(poblacion), 2), "\n")
cat("Media de medias muestrales:", round(mean(medias), 2), "\n")
```

---

## 🗺️ Mapa mental

```
DISTRIBUCIONES DE PROBABILIDAD
│
├── Variables
│     ├── Discreta  → se cuenta (quejas, emergencias)
│     └── Continua  → se mide (peso, tiempo)
│
├── Distribución Poisson (discreta)
│     └── Eventos raros en intervalo fijo → λ = promedio histórico
│
├── Distribución Normal (continua)
│     └── P(punto exacto) = 0 → siempre trabajar con rangos/áreas
│
└── Muestreo y Distribución Muestral
      ├── Muestreo aleatorio → cada elemento con igual probabilidad
      ├── Distribución muestral de la media → Normal (por TCL)
      └── Media de medias muestrales = Media poblacional (μ)
```

---

## 📚 Referencias

Gutiérrez González, E., & Panteleeva, O. V. (2016). *Estadística inferencial 1 para ingeniería y ciencias*. Grupo Editorial Patria.

Montgomery, D. C., & Runger, G. C. (2010). *Probabilidad y estadística aplicadas a la ingeniería* (2.ª ed.). Limusa Wiley.
