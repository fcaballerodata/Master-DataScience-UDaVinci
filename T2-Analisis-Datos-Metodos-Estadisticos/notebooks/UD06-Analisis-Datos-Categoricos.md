# 📊 UD6 — Análisis de Datos Categóricos

**Asignatura:** Análisis de Datos y Métodos Estadísticos
**Semana:** S6

---

## 📌 Aplicación profesional

**¿Para qué sirve?** Analizar variables que son categorías (no números continuos): verificar si una distribución observada coincide con lo esperado, y verificar si dos variables categóricas están asociadas entre sí.

**¿Cómo se usa?** La prueba **Chi-cuadrado de bondad de ajuste** compara una distribución observada contra una teórica (una sola variable); la prueba **Chi-cuadrado de independencia** usa una tabla de contingencia para ver si dos variables categóricas se mueven juntas.

**¿En qué casos lo vas a usar como Data Analyst / Data Scientist?**
- **Análisis de churn:** ¿la tasa de cancelación está asociada con el plan de suscripción (básico/premium)?
- **Marketing y adquisición:** ¿el canal de adquisición (orgánico, pago, referido) está asociado con la tasa de conversión?
- **Control de calidad:** ¿la distribución de defectos por turno de producción coincide con lo esperado, o hay un turno problemático?
- **Segmentación:** validar si dos variables categóricas de un dataset (ej. región y preferencia de producto) están realmente relacionadas antes de construir un modelo o una estrategia sobre ese supuesto.

---

## 1. Variables categóricas — escalas de medida

| Escala | Característica | Ejemplo |
|---|---|---|
| **Nominal** | Categorías sin orden inherente | Canal de adquisición (orgánico, pago, referido) |
| **Ordinal** | Categorías con orden lógico | Nivel de satisfacción (bajo, medio, alto) |
| **Dicotómica** | Solo dos categorías posibles | ¿El cliente canceló? (sí/no) |

---

## 2. Prueba de bondad de ajuste (Chi-cuadrado)

**Pregunta que responde:** ¿la distribución observada coincide con una distribución teórica esperada?

- H₀: los datos siguen la distribución esperada
- H₁: los datos NO siguen la distribución esperada

$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$

### Ejemplo — distribución de canal de adquisición (esperado: 20% cada uno de 5 canales, sobre 1000 nuevos clientes)

| Canal | Observado (O) | Esperado (E) | (O-E)² | (O-E)²/E |
|---|---|---|---|---|
| Orgánico | 180 | 200 | 400 | 2.000 |
| Pago (ads) | 250 | 200 | 2500 | 12.500 |
| Referido | 120 | 200 | 6400 | 32.000 |
| Email | 225 | 200 | 625 | 3.125 |
| Redes sociales | 225 | 200 | 625 | 3.125 |
| **Total** | | | | **χ² = 52.75** |

Con gl = k-1 = 4 y α=0.05, valor crítico = 9.488. Como 52.75 > 9.488 → **se rechaza H₀**: la distribución de canales no es uniforme.

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

### Ejemplo — canal de adquisición vs. conversión

| | Convirtió | No convirtió | Total |
|---|---|---|---|
| Pago (ads) | 30 | 70 | 100 |
| Orgánico | 15 | 85 | 100 |
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
                dimnames = list(c("Pago", "Organico"), c("Convirtio", "NoConvirtio")))
resultado <- chisq.test(tabla)
print(resultado)
```

**Resultado:** χ² ≈ 5.16, p ≈ 0.023 → se rechaza H₀: sí hay asociación entre canal de adquisición y conversión en esta muestra (el canal de pago convierte proporcionalmente mejor).

---

## 4. Resumen — ¿cuál prueba usar?

| Situación | Prueba |
|---|---|
| Una variable categórica vs. distribución teórica esperada | Bondad de ajuste (`chisquare` / `chisq.test(x, p=...)`) |
| Dos variables categóricas entre sí | Independencia con tabla de contingencia (`chi2_contingency` / `chisq.test(tabla)`) |

---

## 🗺️ Way of Work — Análisis de Datos Categóricos

```
PASO 1 — Identificar si la pregunta es sobre 1 variable (bondad de ajuste) o 2 (independencia)
PASO 2 — Construir la tabla de frecuencias observadas (y esperadas, si aplica)
PASO 3 — Verificar que las frecuencias esperadas sean suficientes (regla práctica: ≥5 por celda)
PASO 4 — Ejecutar la prueba Chi-cuadrado correspondiente
PASO 5 — Comparar contra el valor crítico o el p-valor
PASO 6 — Interpretar la asociación/diferencia en términos de negocio, no solo "se rechaza H0"
```

1. **Definir el tipo de pregunta primero:** "¿esta distribución es la esperada?" (bondad de ajuste) es distinto de "¿estas dos variables están relacionadas?" (independencia) — cada una usa una prueba distinta.
2. **Construir la tabla:** para bondad de ajuste, necesitas O y E por categoría; para independencia, una tabla de contingencia completa.
3. **Revisar el tamaño de muestra:** si alguna celda esperada tiene menos de 5 observaciones, la aproximación Chi-cuadrado pierde precisión — considera agrupar categorías o usar el test exacto de Fisher (para tablas 2x2 pequeñas).
4. **Ejecutar la prueba:** usa `scipy.stats` o `chisq.test` de R directamente — no calcules a mano salvo que necesites mostrar el detalle en un reporte académico.
5. **Comparar contra α=0.05** (u otro nivel definido de antemano).
6. **Interpretar con cuidado:** Chi-cuadrado te dice que hay asociación, pero no la dirección ni la fuerza — revisa las proporciones dentro de la tabla de contingencia para explicar el hallazgo en términos de negocio (ej. "el canal pago convierte el doble que el orgánico").

---

## 📚 Referencias

Guía de la Unidad 6 — Universidad DaVinci (2026). Análisis de datos categóricos.
