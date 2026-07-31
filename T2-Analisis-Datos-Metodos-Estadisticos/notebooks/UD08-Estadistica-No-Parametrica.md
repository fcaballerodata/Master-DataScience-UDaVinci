# 📊 UD8 — Estadística No Paramétrica

**Asignatura:** Análisis de Datos y Métodos Estadísticos
**Semana:** S8

---

## 1. ¿Cuándo usar pruebas no paramétricas?

| Estadística paramétrica | Estadística no paramétrica |
|---|---|
| Asume una distribución específica (normalmente normal) | No requiere ese supuesto |
| Trabaja con medias | Trabaja con medianas / rangos / signos |
| Ejemplo: t-test, ANOVA | Ejemplo: prueba del signo, Wilcoxon, Mann-Whitney |

**Ventajas de las pruebas no paramétricas:** más rápidas y simples de calcular, más fáciles de entender, menos sensibles a outliers, supuestos más simples, funcionan con muestras pequeñas y con variables ordinales/nominales.

---

## 2. Prueba del signo

Compara dos medianas relacionadas (datos pareados) usando solo la **dirección** (+/-) de la diferencia — ignora la magnitud. Bajo H0, se espera una distribución binomial con p=0.5.

```
H0: no hay diferencia (P(+) = 0.5, como al azar)
H1: sí hay diferencia
```

### Python
```python
from scipy.stats import binomtest
resultado = binomtest(k=15, n=20, p=0.5, alternative="greater")
print(f"p-valor = {resultado.pvalue:.4f}")
```
### R
```r
binom.test(x = 15, n = 20, p = 0.5, alternative = "greater")
```

---

## 3. Prueba de rangos con signo de Wilcoxon (Wilcoxon signed-rank)

Alternativa no paramétrica al t-test pareado. Compara muestras pareadas considerando dirección Y magnitud (mediante rangos).

```
H0: la mediana de las diferencias es 0
H1: la mediana de las diferencias es distinta de 0
```

### Python
```python
from scipy.stats import wilcoxon
resultado = wilcoxon(antes, despues, alternative="greater")
```
### R
```r
wilcox.test(antes, despues, paired = TRUE, alternative = "greater")
```

**Nota:** más potente que la prueba del signo, pero menos potente que el t-test pareado cuando sí se cumple normalidad.

---

## 4. Prueba U de Mann-Whitney

Alternativa no paramétrica al t-test de muestras independientes.

```
H0: no hay diferencia entre las medianas de ambos grupos
H1: las medianas son diferentes
```

### Python
```python
from scipy.stats import mannwhitneyu
resultado = mannwhitneyu(grupo_A, grupo_B, alternative="two-sided")
```
### R
```r
wilcox.test(grupo_A, grupo_B, alternative = "two.sided")
```

---

## 5. Resumen — ¿cuál prueba usar?

| Situación | Paramétrica equivalente | No paramétrica |
|---|---|---|
| Pareadas, solo dirección | — | Prueba del signo |
| Pareadas, magnitud | t-test pareado | Wilcoxon signed-rank |
| Independientes | t-test independiente | U de Mann-Whitney |

---

## 📚 Referencias

Guía de la Unidad 8 — Universidad DaVinci (2026). Estadística no paramétrica.

Wilcoxon, F. (1945). Individual comparisons by ranking methods. *Biometrics Bulletin*, 1(6), 80-83.

---

## 🗺️ Way of Work — Pruebas No Paramétricas

Checklist paso a paso, apoyado también en literatura especializada (Siegel & Castellan, Conover, Laerd Statistics).

```
PASO 1 — Formular la pregunta y el tipo de comparación   (5 min)
PASO 2 — Verificar los supuestos                          (10-15 min)
PASO 3 — Decidir: ¿paramétrica o no paramétrica?          (5 min)
PASO 4 — Elegir la prueba no paramétrica específica       (5 min)
PASO 5 — Plantear H0 y H1 correctamente                   (5 min)
PASO 6 — Ejecutar la prueba                                (10 min)
PASO 7 — Interpretar y reportar                            (10 min)
```

### PASO 1 — Formular la pregunta y el tipo de comparación

1. ¿Cuántos grupos/condiciones se comparan? (2, o más de 2)
2. ¿Los datos están relacionados o son independientes?
   - **Relacionados/pareados:** mismo sujeto medido dos veces, o sujetos emparejados deliberadamente.
   - **Independientes:** sujetos distintos en cada grupo.

Esta distinción determina la elección entre Wilcoxon signed-rank y Mann-Whitney (Statistics Solutions, 2025).

### PASO 2 — Verificar los supuestos

| Supuesto | Cómo evaluarlo |
|---|---|
| Normalidad | Shapiro-Wilk + histograma/Q-Q plot |
| Tamaño de muestra | n<30 dificulta confiar en el Teorema del Límite Central |
| Tipo de variable | ¿Ordinal, o continua con outliers/asimetría fuerte? |
| Independencia | ¿El diseño garantiza que una observación no influye en otra? |

```python
from scipy.stats import shapiro
estadistico, p_valor = shapiro(datos)
```
```r
shapiro.test(datos)
```

Según Laerd Statistics (s.f.), antes de Mann-Whitney o Wilcoxon también conviene verificar independencia/aleatoriedad y que la variable dependiente sea al menos ordinal.

### PASO 3 — Decidir: ¿paramétrica o no paramétrica?

```
¿Se cumple normalidad (Shapiro-Wilk p>0.05)?
   SÍ → ¿Muestra grande (n≥30)? → SÍ → Paramétrica
                                → NO → ¿Se puede verificar normalidad con confianza? → SÍ: Paramétrica / NO: No paramétrica
   NO → No paramétrica
```

Regla de Conover (1999): si ambos tipos de prueba aplican, la paramétrica suele tener mayor potencia — pero si normalidad realmente falla, la no paramétrica es la opción más honesta.

### PASO 4 — Elegir la prueba específica

| ¿Cuántos grupos? | ¿Relación? | Prueba |
|---|---|---|
| 2 | Pareados, solo dirección | Prueba del signo |
| 2 | Pareados, magnitud | Wilcoxon signed-rank |
| 2 | Independientes | U de Mann-Whitney |
| 3+ | Independientes | Kruskal-Wallis |

Aclaración (Wiley, 2017): Mann-Whitney es para dos muestras **independientes**, Wilcoxon signed-rank para dos muestras **dependientes** — error de elección más común.

### PASO 5 — Plantear H0 y H1 correctamente

Las pruebas no paramétricas comparan **medianas/distribuciones**, no medias (Siegel & Castellan, 1988).

| Prueba | H0 |
|---|---|
| Prueba del signo | P(aumento) = P(disminución) = 0.5 |
| Wilcoxon signed-rank | La mediana de las diferencias pareadas es 0 |
| Mann-Whitney U | Las dos poblaciones tienen la misma distribución |

### PASO 6 — Ejecutar la prueba

Verificar el supuesto propio de cada prueba antes de correrla:

| Prueba | Supuesto adicional |
|---|---|
| Wilcoxon signed-rank | Diferencias aproximadamente simétricas alrededor de su mediana (Laerd Statistics, s.f.) |
| Mann-Whitney U | Idealmente, distribuciones de forma similar |

```python
from scipy.stats import wilcoxon, mannwhitneyu, binomtest
wilcoxon(antes, despues, alternative="greater")
mannwhitneyu(grupo_A, grupo_B, alternative="two-sided")
binomtest(k=positivos, n=total, p=0.5, alternative="greater")
```
```r
wilcox.test(antes, despues, paired = TRUE, alternative = "greater")
wilcox.test(grupo_A, grupo_B, alternative = "two.sided")
binom.test(x = positivos, n = total, p = 0.5, alternative = "greater")
```

### PASO 7 — Interpretar y reportar

No basta el p-valor — reportar también el **tamaño del efecto** (r de rango-biserial):

```python
n = len(antes)
r = resultado.statistic / (n * (n + 1) / 2)  # aproximación simple
```

**Checklist final:**
- ¿Se reportó el estadístico (W, U) y el p-valor exacto?
- ¿Se interpretó en términos de mediana, no de media?
- ¿Se contextualizó el hallazgo en el problema real?
- ¿El tamaño del efecto es relevante en la práctica, o solo estadísticamente significativo?

**Ejemplo de reporte:**
> "La prueba de Wilcoxon signed-rank mostró una reducción significativa en el peso de las mascotas tras el plan nutricional (W=3, p=0.014), con una mediana de reducción de 0.6 kg — un cambio clínicamente relevante."

### Referencias adicionales del Way of Work

Conover, W. J. (1999). *Practical Nonparametric Statistics* (3.ª ed.). Wiley.

Siegel, S., & Castellan, N. J. (1988). *Nonparametric Statistics for the Behavioral Sciences* (2.ª ed.). McGraw-Hill.

Statistics Solutions. (2025). *When to use the Wilcoxon sign test: A guide for data analysis*. https://www.statisticssolutions.com/free-resources/directory-of-statistical-analyses/wilcoxon-sign-test/

Laerd Statistics. (s.f.). *Wilcoxon signed-rank test using SPSS Statistics*. https://statistics.laerd.com/spss-tutorials/wilcoxon-signed-rank-test-using-spss-statistics.php
