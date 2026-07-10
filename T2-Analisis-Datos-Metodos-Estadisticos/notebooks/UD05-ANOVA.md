# 📊 UD5 — ANOVA: Análisis de Varianzas

**Asignatura:** Análisis de Datos y Métodos Estadísticos
**Semana:** S5 (6-11 Jul 2026)

---

## 🎯 Concepto clave

ANOVA (Analysis of Variance) compara las medias de **3 o más grupos** simultáneamente, evitando inflar el error tipo I que ocurriría al hacer múltiples pruebas t por pares.

**Hipótesis:**
- H₀: todas las medias de los grupos son iguales (μ₁ = μ₂ = ... = μₖ)
- H₁: al menos una media es diferente

---

## 1. Tabla ANOVA

| Fuente de variación | GL | Suma de Cuadrados (SC) | Media Cuadrados (MC) | Razón F | Prob > F |
|---|---|---|---|---|---|
| Entre grupos (Tratamiento) | k-1 | SCT | SCT/(k-1) | MCT/MCE | p-valor |
| Dentro de grupos (Error) | n-k | SCE | SCE/(n-k) | — | — |
| Total | n-1 | SCTotal | — | — | — |

Regla de decisión: si **p < 0.05** → se rechaza H₀ (al menos un grupo difiere).

---

## 2. Supuesto previo: prueba de Levene

Antes de interpretar el ANOVA, se debe verificar **homocedasticidad** (varianzas iguales entre grupos) con la prueba de Levene. Si no se cumple, los resultados del ANOVA pueden no ser confiables.

---

## 3. Pruebas Post Hoc

Cuando el ANOVA resulta significativo, no basta con saber que "algún grupo es diferente" — se necesita identificar **cuál**. Para eso existen las pruebas post hoc:

| Prueba | Cuándo usarla |
|---|---|
| **Tukey HSD** | La más usada; grupos de tamaño similar |
| **Bonferroni** | Más conservadora, controla mejor el error tipo I con pocas comparaciones |
| **Scheffé** | Flexible, útil para comparaciones complejas no planeadas |
| **T3 de Dunnett** | Cuando NO hay homocedasticidad (varianzas distintas) |

---

## 4. ANOVA de dos factores

Permite evaluar simultáneamente el efecto de **dos variables categóricas** (factores) sobre una variable continua, y su **interacción**.

- **Efecto principal:** el efecto promedio de un factor, ignorando el otro.
- **Interacción (αβ)ᵢⱼ:** ocurre cuando el efecto de un factor **depende del nivel** del otro factor.
- Si existe interacción significativa, **no se deben interpretar los efectos principales de forma aislada** ni usar post hoc simples — hay que analizar la interacción primero.
- Sí es posible tener un efecto principal significativo sin que exista interacción, y viceversa.

**Ejemplo veterinario:** evaluar el tiempo de recuperación de mascotas según *tipo de tratamiento* (Factor A) y *especie* (Factor B). Si el tratamiento funciona distinto en perros que en gatos, hay interacción.

---

## 5. Python — implementación

```python
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# ANOVA de un factor
modelo = ols('valor ~ C(grupo)', data=df).fit()
tabla_anova = sm.stats.anova_lm(modelo, typ=2)
print(tabla_anova)

# Prueba de Levene (homocedasticidad)
stats.levene(*[df[df.grupo == g]['valor'] for g in df.grupo.unique()])

# Post hoc de Tukey
tukey = pairwise_tukeyhsd(df['valor'], df['grupo'])
print(tukey)
```

**R:**
```r
modelo <- aov(valor ~ grupo, data = df)
summary(modelo)
TukeyHSD(modelo)
leveneTest(valor ~ grupo, data = df)
```

---

## 📚 Referencias

Montgomery, D. C., & Runger, G. C. (2010). *Probabilidad y estadística aplicadas a la ingeniería*. Limusa Wiley.
