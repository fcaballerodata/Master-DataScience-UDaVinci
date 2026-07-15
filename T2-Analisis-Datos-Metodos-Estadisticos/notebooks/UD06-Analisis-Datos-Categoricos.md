# 📊 UD6 — Análisis de Datos Categóricos

**Asignatura:** Análisis de Datos y Métodos Estadísticos
**Semana:** S6

---

## 1. Variables categóricas — escalas de medida

| Escala | Característica | Ejemplo |
|---|---|---|
| **Nominal** | Categorías sin orden inherente | Especie (perro, gato, ave) |
| **Ordinal** | Categorías con orden lógico | Gravedad del caso (leve, moderado, grave) |
| **Dicotómica** | Solo dos categorías posibles | ¿Está vacunado? (sí/no) |

---

## 2. Prueba de bondad de ajuste (Chi-cuadrado)

**Pregunta que responde:** ¿la distribución observada coincide con una distribución teórica esperada?

- H₀: los datos siguen la distribución esperada
- H₁: los datos NO siguen la distribución esperada

$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$

### Ejemplo — distribución de especies atendidas (esperado: 20% cada una de 5 especies, sobre 1000 casos)

| Especie | Observado (O) | Esperado (E) | (O-E)² | (O-E)²/E |
|---|---|---|---|---|
| Perro | 180 | 200 | 400 | 2.000 |
| Gato | 250 | 200 | 2500 | 12.500 |
| Conejo | 120 | 200 | 6400 | 32.000 |
| Ave | 225 | 200 | 625 | 3.125 |
| Reptil | 225 | 200 | 625 | 3.125 |
| **Total** | | | | **χ² = 52.75** |

Con gl = k-1 = 4 y α=0.05, valor crítico = 9.488. Como 52.75 > 9.488 → **se rechaza H₀**: la distribución de especies no es uniforme.

### Python

```python
from scipy.stats import chisquare

observado = [180, 250, 120, 225, 225]
esperado  = [200, 200, 200, 200, 200]

resultado = chisquare(f_obs=observado, f_exp=esperado)
print(f"Chi-cuadrado = {resultado.statistic:.2f}")
print(f"p-valor = {resultado.pvalue:.6f}")
```

### R

```r
observado <- c(180, 250, 120, 225, 225)
esperado_prop <- rep(1/5, 5)

resultado <- chisq.test(x = observado, p = esperado_prop)
print(resultado)
```

---

## 3. Tablas de contingencia y Chi-cuadrado de independencia

**Pregunta que responde:** ¿existe asociación real entre dos variables categóricas, o es variación aleatoria?

- H₀: las variables son independientes
- H₁: las variables están asociadas

### Ejemplo — especie vs. necesidad de cirugía

| | Requiere cirugía | No requiere | Total |
|---|---|---|---|
| Perro | 30 | 70 | 100 |
| Gato | 15 | 85 | 100 |
| **Total** | 45 | 155 | 200 |

### Python

```python
import numpy as np
from scipy.stats import chi2_contingency

tabla = np.array([[30, 70], [15, 85]])
chi2, p, gl, esperadas = chi2_contingency(tabla)

print(f"Chi-cuadrado = {chi2:.3f} | gl = {gl} | p-valor = {p:.4f}")
```

### R

```r
tabla <- matrix(c(30, 70, 15, 85), nrow = 2, byrow = TRUE,
                dimnames = list(c("Perro", "Gato"), c("Cirugia", "NoCirugia")))
resultado <- chisq.test(tabla)
print(resultado)
```

**Resultado:** χ² ≈ 5.16, p ≈ 0.023 → se rechaza H₀: sí hay asociación entre especie y necesidad de cirugía en esta muestra.

---

## 4. Resumen — ¿cuál prueba usar?

| Situación | Prueba |
|---|---|
| Una variable categórica vs. distribución teórica esperada | Bondad de ajuste (`chisquare` / `chisq.test(x, p=...)`) |
| Dos variables categóricas entre sí | Independencia con tabla de contingencia (`chi2_contingency` / `chisq.test(tabla)`) |

---

## 📚 Referencias

Guía de la Unidad 6 — Universidad DaVinci (2026). Análisis de datos categóricos.
