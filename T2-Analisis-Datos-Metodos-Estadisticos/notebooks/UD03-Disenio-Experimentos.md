# 📐 UD3 — Diseño de Experimentos (Inferencia Estadística)

**Asignatura:** Análisis de Datos y Métodos Estadísticos
**Semana:** S3

---

## 📌 Aplicación profesional

**¿Para qué sirve?** Es la base de toda la estadística inferencial: te permite tomar una **muestra** (no puedes medir a toda la población) y, a partir de ella, estimar parámetros poblacionales y tomar decisiones con un nivel de confianza cuantificado — en lugar de opinar "a ojo" sobre si algo cambió o no.

**¿Cómo se usa?** Tres piezas trabajan juntas: (1) el **Teorema del Límite Central**, que justifica usar la distribución normal aunque los datos originales no lo sean; (2) los **intervalos de confianza**, que estiman un rango plausible para un parámetro poblacional; (3) las **pruebas de hipótesis**, que formalizan la pregunta "¿este cambio es real o es ruido?".

**¿En qué casos lo vas a usar como Data Analyst / Data Scientist?**
- Validar si un cambio de proceso (ej. nuevo script de ventas, nuevo layout de tienda) tuvo un efecto real o fue casualidad.
- Estimar un promedio poblacional (tiempo de entrega, ticket promedio) con un margen de error controlado, sin censar a todos los clientes.
- Base conceptual de cualquier test A/B: sin esto, no puedes decir si la "Versión B" fue mejor con confianza estadística.

---

## 1. Teorema del Límite Central (TCL)

Sin importar la distribución original de la población, **la distribución de las medias muestrales se aproxima a una normal** cuando el tamaño de muestra es suficientemente grande (regla práctica: n ≥ 30).

```
Media muestral (x̄) ~ Normal(μ, σ/√n)   cuando n ≥ 30
```

Esto es lo que hace posible construir intervalos de confianza y pruebas de hipótesis usando la distribución normal, incluso cuando no sabes cómo se distribuyen los datos individuales.

---

## 2. Intervalos de Confianza

Un rango de valores donde, con cierto nivel de confianza, se espera que caiga el verdadero parámetro poblacional.

$$IC = \bar{x} \pm Z \times \frac{\sigma}{\sqrt{n}}$$

| Nivel de confianza | Valor de Z |
|---|---|
| 90% | 1.645 |
| 95% | 1.96 |
| 99% | 2.576 |

---

## 3. Pruebas de Hipótesis

| Elemento | Descripción |
|---|---|
| H₀ (nula) | Supuesto de "no hay cambio/diferencia" — lo que se intenta refutar |
| H₁ (alterna) | Lo que se sospecha que es cierto |
| Estadístico de prueba | Z o t, según se conozca o no la desviación estándar poblacional |
| p-valor | Probabilidad de observar un resultado así de extremo si H₀ fuera cierta |
| Regla de decisión | Si p-valor < α (usualmente 0.05) → se rechaza H₀ |

---

## 4. Ejemplo ilustrativo — Call Center

**Contexto (no veterinario, de negocio general):** un call center históricamente tarda en promedio **9.0 minutos** por llamada. Se implementa un nuevo script de atención y se mide una muestra de 40 llamadas, obteniendo una media de **8.2 minutos** con desviación estándar muestral de **2.1 minutos**. ¿El nuevo script realmente redujo el tiempo promedio, o la diferencia observada pudo deberse al azar?

**Hipótesis:**
```
H0: μ = 9.0 min (el script no cambió el tiempo promedio)
H1: μ < 9.0 min (el script redujo el tiempo promedio) -- prueba unilateral
```

**Cálculo del estadístico (Z, porque n≥30):**

```
Z = (x̄ - μ0) / (s/√n) = (8.2 - 9.0) / (2.1/√40) = -0.8 / 0.332 = -2.41
```

Con Z = -2.41, el p-valor asociado es aproximadamente **0.008**. Como 0.008 < 0.05, **se rechaza H₀**: hay evidencia estadística de que el nuevo script sí redujo el tiempo promedio de llamada.

### Python

```python
import numpy as np
from scipy import stats

media_muestral = 8.2
media_historica = 9.0
desv_muestral = 2.1
n = 40

# Estadístico Z (n>=30, se usa aproximación normal)
z = (media_muestral - media_historica) / (desv_muestral / np.sqrt(n))
p_valor = stats.norm.cdf(z)  # unilateral, cola izquierda

print(f"Z = {z:.3f}")
print(f"p-valor = {p_valor:.4f}")
print("Decisión:", "Rechazar H0" if p_valor < 0.05 else "No rechazar H0")

# Intervalo de confianza del 95% para la media muestral
ic_bajo = media_muestral - 1.96 * (desv_muestral/np.sqrt(n))
ic_alto = media_muestral + 1.96 * (desv_muestral/np.sqrt(n))
print(f"IC 95%: [{ic_bajo:.2f}, {ic_alto:.2f}] minutos")
```

### R

```r
media_muestral <- 8.2
media_historica <- 9.0
desv_muestral <- 2.1
n <- 40

z <- (media_muestral - media_historica) / (desv_muestral / sqrt(n))
p_valor <- pnorm(z)

cat("Z =", round(z,3), "| p-valor =", round(p_valor,4), "\n")

ic <- media_muestral + c(-1,1) * 1.96 * (desv_muestral/sqrt(n))
cat("IC 95%:", round(ic,2), "\n")
```

---

## 🗺️ Way of Work — Inferencia Estadística (IC y Pruebas de Hipótesis)

```
PASO 1 — Definir la pregunta y el parámetro de interés (media, proporción)
PASO 2 — Verificar condiciones para usar el TCL (n≥30, o normalidad conocida)
PASO 3 — Elegir el estadístico correcto (Z si σ conocida o n grande, t si no)
PASO 4 — Plantear H0 y H1 en función de la pregunta de negocio
PASO 5 — Calcular el estadístico de prueba y el p-valor
PASO 6 — Comparar contra α y decidir
PASO 7 — Interpretar el resultado en el contexto del negocio, no solo estadísticamente
```

1. **Definir la pregunta:** ¿quieres estimar un valor (IC) o comparar contra un valor de referencia (prueba de hipótesis)?
2. **Verificar TCL:** con n≥30, puedes usar la aproximación normal sin preocuparte por la forma de la distribución original.
3. **Elegir Z o t:** usa Z si conoces la desviación estándar poblacional o n es grande; usa t si trabajas con muestra pequeña y desviación estándar estimada.
4. **Plantear hipótesis con cuidado:** H0 siempre es la afirmación de "no hay cambio" — evita plantear H1 como lo que "quieres que sea cierto", plantea lo que la evidencia sugiere.
5. **Calcular:** usa las fórmulas o las funciones de `scipy.stats`/R directamente.
6. **Comparar contra α (usualmente 0.05):** documenta explícitamente qué α usaste, no lo des por sentado.
7. **Interpretar:** un resultado "estadísticamente significativo" no siempre es "relevante para el negocio" — conecta siempre el resultado con la magnitud real del cambio (ej. 0.8 minutos menos, ¿vale la pena el costo del nuevo script?).

---

## 📚 Referencias

Gutiérrez González, E., & Panteleeva, O. V. (2016). *Estadística inferencial 1 para ingeniería y ciencias*. Grupo Editorial Patria.

Montgomery, D. C., & Runger, G. C. (2010). *Probabilidad y estadística aplicadas a la ingeniería* (2.ª ed.). Limusa Wiley.
