# 🔬 UD3 — Diseño de Experimentos (Inferencia Estadística)

**Asignatura:** Análisis de Datos y Métodos Estadísticos  
**Semana:** S3 (22–27 Jun 2026)

---

## 🎯 Conceptos clave

Tres conceptos que se encadenan:

```
Teorema del Límite Central → Intervalos de Confianza → Pruebas de Hipótesis
     (el "por qué funciona")       (estimación)             (decisión)
```

---

## 1. Teorema del Límite Central (TCL)

> Si tomas muchas muestras de cualquier población, las medias de esas muestras siempre formarán una distribución **Normal** — sin importar cómo se distribuya la población original.

### Las 3 propiedades clave

| Propiedad | Descripción |
|---|---|
| Distribución de medias muestrales → **Normal** | Siempre válido si n ≥ 30 |
| Media de esas medias = **μ poblacional** | El promedio de promedios = el real |
| Varianza de esas medias = **σ²/n** | A mayor muestra, más concentradas las medias |

**Regla práctica:** con n ≥ 30 puedes asumir normalidad.

**Ejemplo Movet:** tiempos de espera con μ=35 min, σ=8 min (distribución desconocida). Con n=50:
```
X̄ ~ Normal(μ=35, σ_x̄ = 8/√50 = 1.13)
→ Ya puedes calcular probabilidades con la Normal estándar
```

---

## 2. Intervalos de Confianza

> En vez de decir "la media es 53", dices: **"estoy 95% seguro de que la media está entre 50.3 y 55.7"**.

### Fórmula

```
IC = X̄  ±  Z × (σ / √n)

Donde:
  X̄    = media muestral
  Z     = valor crítico (95% → Z=1.96 | 99% → Z=2.576)
  σ/√n  = error estándar
```

### Factores que afectan el intervalo

| Factor | Efecto sobre el IC |
|---|---|
| ↑ Tamaño de muestra (n) | Intervalo más **estrecho** (más preciso) |
| ↑ Nivel de confianza (95%→99%) | Intervalo más **ancho** |
| ↑ Variabilidad (σ) | Intervalo más **ancho** |

### Ejemplo Movet — Costo promedio de consulta

```
X̄ = 53.000 COP | σ = 8.340 | n = 50 | Confianza = 95%

Error estándar = 8.340 / √50 = 1.179
Margen de error = 1.96 × 1.179 = 2.310

IC 95% = [50.690 , 55.310] miles COP
```

**Interpretación:** Con 95% de confianza, el costo promedio real de todas las consultas Movet está entre $50.690 y $55.310 COP.

---

## 3. Pruebas de Hipótesis

> Regla formal para decidir si los datos dan suficiente evidencia para rechazar una afirmación sobre la población.

### Los dos actores

| | H₀ (Nula) | H₁ (Alternativa) |
|---|---|---|
| **Representa** | El estado actual / "nada cambió" | Lo que quieres demostrar |
| **Actitud** | Se asume verdadera hasta que se pruebe lo contrario | Requiere evidencia |
| **Ejemplo Movet** | "El tiempo promedio es 35 min" | "El tiempo cambió" |

### El p-valor

```
p-valor < α (0.05)  →  Rechazar H₀  →  "Hay evidencia suficiente"
p-valor ≥ α (0.05)  →  No rechazar H₀  →  "No hay evidencia suficiente"
```

> ⚠️ "No rechazar H₀" ≠ probar que H₀ es verdadera.

### Ejemplo Movet — ¿Mejoró el tiempo de espera tras contratar una veterinaria nueva?

```
H₀: μ = 35 min  |  H₁: μ ≠ 35 min  (dos colas)
Muestra: n=40, X̄=31 min, σ=8 min, α=0.05

Z = (31 − 35) / (8 / √40) = −4 / 1.265 = −3.16
p-valor = 0.0016  <  0.05  → Se rechaza H₀ ✅

Conclusión: hay evidencia estadística de que el tiempo de espera mejoró.
```

---

## 4. Conexión entre los tres conceptos

```
CASO: ¿El nuevo veterinario mejoró el tiempo de atención?

PASO 1 — TCL:
  Aunque los tiempos no sean normales, con n=40 la media SÍ es normal → podemos continuar.

PASO 2 — Intervalo de Confianza:
  IC 95% = [28.5, 33.5] min → el valor histórico (35) NO está dentro → señal de cambio.

PASO 3 — Prueba de Hipótesis:
  p-valor = 0.0016 < 0.05 → Rechazamos H₀
  Conclusión: el tiempo de atención mejoró significativamente.
```

---

## 5. Código Python

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# ── 1. TCL — Simulación visual ────────────────────────────────
np.random.seed(42)
poblacion = np.random.exponential(scale=35, size=100_000)  # NO normal
medias = [np.random.choice(poblacion, 50).mean() for _ in range(2000)]

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(poblacion[:500], bins=30, color='tomato', edgecolor='white')
axes[0].set_title("Población original (exponencial — NO normal)")
axes[1].hist(medias, bins=30, color='steelblue', edgecolor='white')
axes[1].set_title("Medias muestrales (n=50) → ¡Normal por TCL!")
plt.tight_layout()
plt.show()

# ── 2. INTERVALO DE CONFIANZA ──────────────────────────────────
x_bar, sigma, n = 53.0, 8.34, 50
z = stats.norm.ppf(0.975)  # 1.96 para 95%
margen = z * (sigma / np.sqrt(n))
print(f"IC 95%: [{x_bar - margen:.2f}, {x_bar + margen:.2f}]")

# ── 3. PRUEBA DE HIPÓTESIS ────────────────────────────────────
mu_0 = 35.0
x_bar_new, sigma_new, n_new = 31.0, 8.0, 40

z_stat = (x_bar_new - mu_0) / (sigma_new / np.sqrt(n_new))
p_valor = 2 * (1 - stats.norm.cdf(abs(z_stat)))

print(f"\nH₀: μ = {mu_0} | H₁: μ ≠ {mu_0}")
print(f"Z = {z_stat:.3f}  |  p-valor = {p_valor:.4f}")
print("→ Se RECHAZA H₀" if p_valor < 0.05 else "→ No se rechaza H₀")
```

---

## 6. Código R

```r
# ── 1. TCL ─────────────────────────────────────────────────────
set.seed(42)
poblacion <- rexp(100000, rate=1/35)
medias <- replicate(2000, mean(sample(poblacion, 50)))
par(mfrow=c(1,2))
hist(poblacion[1:500], col="tomato", main="Población (exponencial)")
hist(medias, col="steelblue", main="Medias muestrales → Normal")

# ── 2. INTERVALO DE CONFIANZA ──────────────────────────────────
x_bar <- 53.0; sigma <- 8.34; n <- 50
z <- qnorm(0.975)
margen <- z * (sigma / sqrt(n))
cat("IC 95%: [", round(x_bar - margen, 2), ",", round(x_bar + margen, 2), "]\n")

# ── 3. PRUEBA DE HIPÓTESIS ─────────────────────────────────────
mu_0 <- 35.0; x_bar_new <- 31.0; sigma_new <- 8.0; n_new <- 40
z_stat <- (x_bar_new - mu_0) / (sigma_new / sqrt(n_new))
p_valor <- 2 * (1 - pnorm(abs(z_stat)))
cat("Z =", round(z_stat, 3), "| p-valor =", round(p_valor, 4), "\n")
if (p_valor < 0.05) cat("→ Se RECHAZA H₀\n") else cat("→ No se rechaza H₀\n")
```

---

## 🗺️ Mapa mental

```
UD3: INFERENCIA ESTADÍSTICA
│
├── Teorema del Límite Central (TCL)
│     ├── n ≥ 30: medias muestrales ~ Normal (siempre)
│     ├── Media de medias = μ poblacional
│     └── Varianza de medias = σ²/n
│
├── Intervalos de Confianza
│     ├── IC = X̄ ± Z × (σ/√n)
│     ├── 95% → Z=1.96  |  99% → Z=2.576
│     └── Mayor n → IC más estrecho (más preciso)
│
└── Pruebas de Hipótesis
      ├── H₀: "nada cambió" — se asume verdadera
      ├── H₁: lo que quieres demostrar
      ├── p-valor < α (0.05) → Rechazar H₀
      └── No rechazar H₀ ≠ probar que H₀ es verdadera
```

---

## 📚 Referencias

Gutiérrez González, E., & Panteleeva, O. V. (2016). *Estadística inferencial 1 para ingeniería y ciencias*. Grupo Editorial Patria.

Montgomery, D. C., & Runger, G. C. (2010). *Probabilidad y estadística aplicadas a la ingeniería* (2.ª ed.). Limusa Wiley.
