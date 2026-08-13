# 📊 UD5 — ANOVA: Análisis de Varianzas

**Asignatura:** Análisis de Datos y Métodos Estadísticos
**Semana:** S5 (6-11 Jul 2026)

---

## 📌 Aplicación profesional

**¿Para qué sirve?** Comparar las medias de **3 o más grupos a la vez** de forma estadísticamente correcta, sin inflar el riesgo de encontrar una diferencia falsa (lo que pasaría si hicieras muchas pruebas t por pares).

**¿Cómo se usa?** Se calcula qué proporción de la variabilidad total se explica por las diferencias *entre* los grupos, frente a la variabilidad *dentro* de cada grupo. Si esa proporción (el estadístico F) es lo suficientemente grande, se concluye que al menos un grupo es distinto.

**¿En qué casos lo vas a usar como Data Analyst / Data Scientist?**
- **Tests A/B/C:** comparar 3+ variantes de una campaña, landing page o experiencia de producto al mismo tiempo.
- **Comparar desempeño entre grupos operativos:** sucursales, turnos, proveedores, regiones — ¿alguno realmente rinde distinto o las diferencias son ruido muestral?
- **Validación de segmentos:** confirmar si distintos segmentos de clientes (ej. por plan de suscripción) tienen gasto promedio realmente diferente.
- Es el paso natural después de que un análisis descriptivo muestra "diferencias" entre grupos — ANOVA responde si esas diferencias son estadísticamente sólidas.

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

**Ejemplo:** evaluar las ventas según *tipo de campaña* (Factor A: descuento vs. envío gratis) y *canal* (Factor B: email vs. redes sociales). Si el descuento funciona mejor en redes pero el envío gratis funciona mejor en email, hay interacción.

---

## 5. Ejemplo ilustrativo — Comparación de proveedores logísticos

**Contexto (negocio general):** una empresa evalúa 3 proveedores logísticos distintos, midiendo el tiempo de entrega (en días) de 5 envíos por proveedor. ¿Existe diferencia real en el tiempo de entrega entre los 3 proveedores?

| Proveedor A | Proveedor B | Proveedor C |
|---|---|---|
| 3, 4, 3, 5, 4 | 5, 6, 5, 7, 6 | 4, 4, 5, 3, 4 |

```python
import scipy.stats as stats

proveedor_a = [3, 4, 3, 5, 4]
proveedor_b = [5, 6, 5, 7, 6]
proveedor_c = [4, 4, 5, 3, 4]

f_stat, p_valor = stats.f_oneway(proveedor_a, proveedor_b, proveedor_c)
print(f"F = {f_stat:.3f} | p-valor = {p_valor:.4f}")
# F ≈ 10.29, p ≈ 0.003 -> se rechaza H0: sí hay diferencia real entre proveedores
```

**Interpretación:** con p≈0.003 (<0.05), se rechaza H₀ — al menos un proveedor tiene un tiempo de entrega promedio distinto. El siguiente paso sería un post hoc de Tukey para identificar cuál proveedor específicamente difiere (en este caso, el Proveedor B es visiblemente más lento).

---

## 6. Python — implementación completa

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

## 🗺️ Way of Work — ANOVA

```
PASO 1 — Confirmar que son 3+ grupos (con 2 grupos, usar t-test en su lugar)
PASO 2 — Verificar el supuesto de homocedasticidad (Levene)
PASO 3 — Ejecutar ANOVA y obtener F y p-valor
PASO 4 — Si p < 0.05, ejecutar un post hoc para identificar QUÉ grupo difiere
PASO 5 — Si hay 2 factores, revisar primero la interacción antes que los efectos principales
PASO 6 — Interpretar en magnitud real, no solo en significancia estadística
```

1. **Confirmar el número de grupos:** ANOVA es para 3+; con solo 2 grupos, usa t-test (más simple y directo).
2. **Levene primero:** si las varianzas son muy distintas entre grupos, considera un post hoc robusto (T3 de Dunnett) o una alternativa no paramétrica (Kruskal-Wallis).
3. **Ejecutar ANOVA:** revisa tanto el p-valor como el tamaño de F — un F apenas por encima del crítico es una señal más débil que uno muy por encima.
4. **Post hoc solo si el ANOVA fue significativo:** no tiene sentido comparar pares si el ANOVA global no encontró diferencia.
5. **Con 2 factores, mira la interacción primero:** una interacción significativa cambia por completo cómo interpretas los efectos principales.
6. **Conecta con el negocio:** una diferencia "significativa" de 0.2 días de entrega puede no justificar cambiar de proveedor si el costo es mayor — la decisión final combina estadística + contexto de negocio.

---

## 📚 Referencias

Montgomery, D. C., & Runger, G. C. (2010). *Probabilidad y estadística aplicadas a la ingeniería*. Limusa Wiley.
