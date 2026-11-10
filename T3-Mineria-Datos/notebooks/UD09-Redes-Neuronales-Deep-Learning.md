# UD09 · Redes neuronales y Deep Learning — Minería de Datos (T3)

> **Fuentes:** guía académica de la unidad (14 pp.), Recursos y Bibliografía de la asignatura (solo como listado) y fuentes verificadas (sección Referencias).
> **Convención:** **[guía]** · **[complemento]** (fuente externa) · **[propio]** (lo ejecuté yo).
> **Código:** [`redes_neuronales_optimizadores_hopfield.py`](../codigo/redes_neuronales_optimizadores_hopfield.py)
> ⚠️ **El título dice Deep Learning, pero la guía casi no lo trata.** No hay redes convolucionales, recurrentes ni LSTM; cubre perceptrón, feed-forward, backpropagation, paradigmas de aprendizaje y la red de Hopfield. Lo de Deep Learning se complementa con Goodfellow et al. (2016, caps. 6, 8, 9 y 10) y LeCun et al. (2015). Varios párrafos del PDF salen mezclados: **[verificar]**.

---

## 1. Explicación sencilla
- Una **red neuronal** son muchas neuronas simples conectadas; cada una suma lo que recibe y decide cuánto pasar a la siguiente.
- **Aprende ajustando los pesos** de las conexiones hasta que sus predicciones se parecen a la realidad.
- Sirve para **clasificar** (con etiquetas) y **agrupar** (sin etiquetas); también extrae características para otros algoritmos **[guía]**.

## 2. Fundamentos técnicos

### 2.1 Componentes **[guía]**
- **Neurona:** recibe entradas, las combina y se activa o no.
- **Perceptrón** (Rosenblatt): discriminador lineal, la unidad básica (ver ML UD8).
- **Red feed-forward** (perceptrón multicapa): las salidas de una capa alimentan a la siguiente, **sin bucles**.

### 2.2 Backpropagation **[guía + complemento]**
Ciclo de entrenamiento: (1) predicción, (2) medir el error, (3) **retropropagar** el error para saber cuánto aportó cada peso, (4) ajustar los parámetros y repetir.

La guía clasifica los algoritmos de backpropagation en tres categorías: **descenso más agudo**, **cuasi-Newton** y **Levenberg-Marquardt / gradiente conjugado**.
⚠️ **[complemento]** Eso mezcla dos cosas: **backpropagation calcula los gradientes**; esas tres categorías son **métodos de optimización** que los usan para mover los pesos (Goodfellow et al., 2016, cap. 8).

### 2.3 Paradigmas de aprendizaje **[guía]**

| Paradigma | Qué recibe la red | Algoritmos que menciona la guía | Ejemplo de negocio |
|---|---|---|---|
| **Supervisado** | Ejemplos con la respuesta | Corrección de error; estocástico | Predecir qué clientes cancelan |
| **No supervisado** | Solo entradas | Asociativo, competitivo, cooperativo | Agrupar clientes por comportamiento |
| **Por refuerzo** | Recompensas y castigos | Lineal con recompensa/penalización, asociativo con recompensa/penalización, *Adaptive Heuristic Critic* | Aprender qué oferta mostrar según si el cliente compra |

### 2.4 Red de Hopfield **[guía]**
- **Memoria asociativa:** guarda patrones y recupera el completo desde una versión incompleta o con ruido.
- Neuronas **binarias**, **una capa**, **no lineal**; está diseñada para **converger a un mínimo local**.
- Fuente original: Hopfield (1982). Su resumen dice que el modelo produce una memoria direccionable por contenido que "correctly yields an entire memory from any subpart of sufficient size".

## 3. Ejemplos sencillos
- **Feed-forward:** una tabla de clientes entra y sale la probabilidad de cancelar.
- **Backpropagation:** un pronóstico falla; se repasa hacia atrás cuánto aportó cada eslabón.
- **Hopfield:** completar "CLI_NT_" → "CLIENTE" a partir de lo que sí se ve.
- **No supervisado:** agrupar clientes sin etiquetas (segmentación RFM de la UD7).

## 4. Python (ejecutado) **[propio]**

### 4.1 El mismo MLP con distintos optimizadores
Cáncer de mama (569 casos, 143 en prueba, estandarizado, una capa oculta de 16 neuronas):

| Optimizador (sklearn) | Familia | Iter. | Pérdida final | Train | Prueba | Recall maligno |
|---|---|---|---|---|---|---|
| `sgd` | Descenso del gradiente (estocástico) | 400 | 0.0838 | 0.977 | 0.986 | 0.962 |
| `adam` | Descenso adaptativo | 388 | 0.0387 | 0.993 | 0.979 | 0.943 |
| `lbfgs` | Cuasi-Newton | **23** | 0.0001 | **1.000** | 0.958 | 0.906 |
| Logística (base) | — | — | — | 0.988 | 0.965 | 0.925 |

- `lbfgs` (cuasi-Newton) convergió en 23 iteraciones contra ~400, pero llegó a train = 1.000 y tuvo la prueba más baja: **converger rápido no es generalizar mejor**.
- Las diferencias de prueba son de pocos casos de 143. Con 5 semillas de `adam` la prueba varió entre 0.965 y 0.979: **no hay un optimizador claramente mejor**.
- Pérdida de `adam`: 1.43 (iter. 1) → 0.93 (10) → 0.19 (50) → 0.04 (final).
- Sin estandarizar, `adam` baja de 0.979 a 0.923.
- Levenberg-Marquardt (mencionado en la guía) no está en scikit-learn; no lo probé.

### 4.2 Red de Hopfield desde cero (100 neuronas ±1, ruido del 10 %)
```python
W = P.T @ P / N; np.fill_diagonal(W, 0)           # guardar patrones (regla de Hebb)
# recuperar: actualizar neurona por neurona  s[i] = 1 si W[i] @ s >= 0 sino -1
# energía:   E = -0.5 * s @ W @ s    (nunca sube: llega a un mínimo local)
```

| Patrones guardados | Recupera exacto | ¿La energía nunca sube? |
|---|---|---|
| 3 | 20/20 | Sí |
| 10 | 20/20 | Sí |
| 20 | **6/20** | Sí |

Con pocos patrones reconstruye el original desde una versión con 10 % de errores; al guardar demasiados se confunden y a veces cae en un mínimo local que no es ningún patrón guardado. Confirma lo que dice la guía y muestra su límite: **capacidad de memoria pequeña**.

## 5. R (no probado: R no está disponible en mi entorno)
```r
library(nnet)
set.seed(42)
idx <- sample(nrow(iris), 100)
tr <- iris[idx, ]; te <- iris[-idx, ]
m <- nnet(Species ~ ., data = tr, size = 8, decay = 0.01, maxit = 300)
mean(predict(m, te, type = "class") == te$Species)
```

## 6. Aplicación real (BI)
- **Churn:** feed-forward con frecuencia, monto y recencia → probabilidad de cancelar; siempre contra una línea base y evaluada como en la UD8 (recall, PR-AUC).
- **Extractor de características:** la red genera variables que luego usa otro algoritmo.
- **Agrupar sin etiquetas:** segmentar clientes (UD7).
- **Refuerzo:** personalizar una oferta aprendiendo de cada interacción.
- **Hopfield:** hoy sirve sobre todo como ejemplo didáctico de memoria asociativa.

## 7. Puntos de la guía que conviene manejar con cuidado
1. **Backpropagation no es el optimizador.**
2. **Poco Deep Learning:** faltan las arquitecturas convolucionales y recurrentes.
3. Los paradigmas no supervisado y por refuerzo solo aparecen **listados**.
4. Texto mezclado en el PDF: **[verificar]**.
5. La actividad de arrastrar palabras (supervisado / no supervisado / refuerzo) coincide con la tabla de 2.3.

## 8. Preguntas de comprensión y respuestas

**1. Ciclo con backpropagation y diferencia con el optimizador.**
Predicción → error → retropropagación (gradiente) → ajuste. Backpropagation **calcula los gradientes**; el optimizador (descenso del gradiente, cuasi-Newton, etc.) **los usa para actualizar los pesos**. En la prueba, el cuasi-Newton convergió en 23 iteraciones contra ~400, pero memorizó el entrenamiento (1.000).

**2. Tres paradigmas con ejemplo.**
Supervisado: predecir cancelación con historial etiquetado. No supervisado: agrupar clientes por comportamiento (RFM). Por refuerzo: elegir qué oferta mostrar según si el cliente compra o ignora.

**3. Red de Hopfield.**
Memoria asociativa de una capa, binaria y no lineal; recupera un patrón completo desde uno incompleto. Limitaciones: converge a un mínimo local (a veces no es ninguno de los patrones guardados), capacidad pequeña (con 100 neuronas y 20 patrones recuperó solo 6 de 20) y solo valores binarios.

## 🧠 Lo que debes recordar
1. **Neurona:** suma lo que recibe y decide cuánto pasar. **Feed-forward:** capas hacia adelante, sin bucles.
2. **Ciclo de entrenamiento:** predecir → medir el error → retropropagar → ajustar pesos → repetir.
3. **Backpropagation calcula los gradientes; el optimizador actualiza los pesos.**
4. **Converger rápido no es generalizar bien** (cuasi-Newton: 23 iteraciones, pero memorizó).
5. **Paradigmas:** supervisado (con respuesta), no supervisado (sin respuesta), por refuerzo (recompensa y castigo).
6. **Hopfield:** memoria asociativa, binaria, una capa; converge a un mínimo local y tiene poca capacidad.
7. **Estandariza antes de entrenar:** sin eso, el MLP bajó de 0.979 a 0.923.
8. **Las diferencias pequeñas no son concluyentes** con 143 casos de prueba.
9. **La guía casi no trata Deep Learning:** se complementa con Goodfellow et al. (2016, caps. 9 y 10) y LeCun et al. (2015).

## Referencias (APA 7)
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT Press. *(Autores, editorial y capítulos 6 a 12 verificados en su tabla de contenidos; no leí los capítulos.)*
- Hopfield, J. J. (1982). Neural networks and physical systems with emergent collective computational abilities. *Proceedings of the National Academy of Sciences, 79*(8), 2554–2558. *(Datos y resumen verificados en el registro de Caltech.)*
- LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. *Nature, 521*(7553), 436–444. https://doi.org/10.1038/nature14539 *(Datos verificados en listados; no leí el artículo completo.)*
- Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830.
- Universidad DaVinci. (s. f.). *Redes neuronales y Deep Learning* [Guía académica, Unidad 9]. Minería de Datos. LMS UDaVinci.

*La bibliografía de la asignatura (Alpaydin, 2021; Bobadilla, 2021 y otros) se leyó solo como listado; no se cita contenido de esos libros.*
