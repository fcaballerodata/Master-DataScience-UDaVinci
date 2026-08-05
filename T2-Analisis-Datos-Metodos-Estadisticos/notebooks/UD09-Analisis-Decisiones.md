# 🎯 UD9 — Análisis de Decisiones

**Asignatura:** Análisis de Datos y Métodos Estadísticos
**Semana:** S9

---

## 1. Elementos del análisis de decisiones (7 pasos)

1. **Investigación** — recopilar información relevante
2. **Análisis de riesgos** — evaluar probabilidad e impacto de cada riesgo
3. **Modelado de decisiones** — estructurar el problema (árboles, tablas de recompensa)
4. **Programas y software** — procesar datos y calcular resultados
5. **Diseño de soluciones** — generar y evaluar alternativas
6. **Toma de decisiones** — elegir según metas y tolerancia al riesgo
7. **Optimización de elecciones** — evaluar resultados y ajustar decisiones futuras

---

## 2. Tabla de recompensa y Método del Valor Esperado (EMV)

$$EMV_i = \sum_j (\text{recompensa}_{ij}) \times (\text{probabilidad}_j)$$

**Ejemplo:** ampliación de consultorio veterinario.

| Alternativa | Demanda alta (0.6) | Demanda baja (0.4) |
|---|---|---|
| Ampliación grande | 200 | -50 |
| Ampliación pequeña | 100 | 20 |
| No ampliar | 0 | 0 |

```
EMV(Ampliación grande)  = 200(0.6) + (-50)(0.4) = 100
EMV(Ampliación pequeña) = 100(0.6) + 20(0.4)    = 68
EMV(No ampliar)         = 0
```

Decisión óptima: **Ampliación grande** (EMV = 100).

### Python
```python
import numpy as np
recompensas = np.array([[200, -50], [100, 20], [0, 0]])
probabilidades = np.array([0.6, 0.4])
emv = recompensas @ probabilidades
mejor = np.argmax(emv)
```
### R
```r
recompensas <- matrix(c(200, -50, 100, 20, 0, 0), nrow = 3, byrow = TRUE)
probabilidades <- c(0.6, 0.4)
emv <- recompensas %*% probabilidades
```

---

## 3. Valor Esperado de la Información Perfecta (EVPI)

$$EVPI = VEIP - \text{mejor } EMV$$

```
VEIP = 200(0.6) + 0(0.4) = 120
EVPI = 120 - 100 = 20
```

No pagar más de $20,000 por información perfecta sobre la demanda.

```python
mejores_por_escenario = recompensas.max(axis=0)
veip = mejores_por_escenario @ probabilidades
evpi = veip - emv.max()
```
```r
mejores_por_escenario <- apply(recompensas, 2, max)
veip <- mejores_por_escenario %*% probabilidades
evpi <- veip - max(emv)
```

---

## 4. Árbol de decisión

Cuadrados = puntos de decisión; círculos = puntos de azar. Se resuelve de derecha a izquierda ("rollback"): EMV en cada nodo de azar, mejor rama en cada nodo de decisión.

---

## 5. Revisión de probabilidades — Teorema de Bayes

```python
p_alta, p_baja = 0.6, 0.4
p_predice_alta_dado_alta = 0.80
p_predice_alta_dado_baja = 0.30

numerador = p_predice_alta_dado_alta * p_alta
denominador = numerador + (p_predice_alta_dado_baja * p_baja)
p_alta_revisada = numerador / denominador
```
```r
numerador <- p_predice_alta_dado_alta * p_alta
denominador <- numerador + (p_predice_alta_dado_baja * p_baja)
p_alta_revisada <- numerador / denominador
```

---

## 6. Técnicas de clasificación y predicción

- Partición train/test, matriz de confusión, curva ROC (sensibilidad vs. 1-especificidad), AUC.

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, auc
```
```r
set.seed(42)
library(pROC)
```

---

## 📚 Referencias

Anderson, D. R., Sweeney, D. J., & Williams, T. A. (2008). *Estadística para administración y economía* (10.ª ed., Cap. 21). Cengage Learning.

Guía de la Unidad 9 — Universidad DaVinci (2026). Análisis de decisiones.

---

## 🗺️ Way of Work — EMV y EVPI

```
PASO 1 — Identificar los 3 componentes del problema     (5 min)
PASO 2 — Construir la tabla de recompensa                (10 min)
PASO 3 — Asignar probabilidades a los estados            (10 min)
PASO 4 — Calcular el EMV de cada alternativa             (5-10 min)
PASO 5 — Elegir la alternativa óptima                    (2 min)
PASO 6 — Calcular el EVPI                                (10 min)
PASO 7 — Análisis de sensibilidad                        (10-15 min)
```

### PASO 1 — Identificar los 3 componentes

1. Alternativas de decisión (lo que TÚ controlas)
2. Estados de la naturaleza (lo que NO controlas)
3. Recompensas (misma unidad para todos)

**Error común:** confundir una alternativa con un estado de la naturaleza.

### PASO 2 — Construir la tabla de recompensa

Verificar que la tabla refleje realistamente cada escenario (ej. no poner costo de oportunidad en 0 "por comodidad").

### PASO 3 — Asignar probabilidades

Orden de preferencia: (1) frecuencias históricas, (2) estudios de mercado/benchmarks, (3) estimación subjetiva experta (declarada explícitamente como tal — Anderson et al., 2008).

```python
probabilidades = [0.55, 0.45]
assert abs(sum(probabilidades) - 1.0) < 1e-9
```

### PASO 4 — Calcular el EMV

```python
emv = recompensas @ probabilidades
```

### PASO 5 — Elegir la alternativa óptima

Mayor EMV si son ganancias, menor si son costos. Si dos alternativas están muy cerca, mencionarlo en el reporte.

### PASO 6 — Calcular el EVPI

```python
veip = recompensas.max(axis=0) @ probabilidades
evpi = veip - emv.max()
```

Regla práctica: si el costo real de la información es menor al EVPI, vale la pena obtenerla.

### PASO 7 — Análisis de sensibilidad

Variar la probabilidad estimada y observar si la decisión óptima cambia — el punto de cruce entre alternativas es el umbral de sensibilidad.

```python
p_aumento = np.linspace(0, 1, 100)
# recalcular EMV de cada alternativa a través de p_aumento y graficar
```

**Checklist final:**
- ¿La decisión se mantiene dentro de un rango razonable de probabilidades?
- ¿El EVPI justifica buscar más información?
- ¿Se documentó el origen de las probabilidades usadas?
