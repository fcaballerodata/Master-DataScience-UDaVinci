# UD1 — Minería de Datos o Data Mining y el Aprendizaje Automático

**Asignatura:** Minería de Datos
**Trimestre:** T3 — 2026

## 1. Concepto clave

La Minería de Datos (Data Mining) es el **proceso** de descubrir patrones, tendencias y conocimiento significativo a partir de grandes conjuntos de datos, ubicado en la intersección de estadística, inteligencia artificial y bases de datos. Su objetivo es transformar datos brutos en información útil para la toma de decisiones.

**Relación con Machine Learning:** el ML **es una herramienta dentro** del proceso de minería de datos — no son sinónimos. Minería de datos es el proceso completo (selección, limpieza, modelado, interpretación, decisión); ML es la técnica matemática usada en una de sus etapas.

## 2. Términos y definiciones

### Proceso KDD (Knowledge Discovery in Databases) — 8 etapas

1. Selección de datos
2. Limpieza de datos
3. Integración de datos
4. Transformación de datos
5. Reducción / generación de datos
6. **Minería de Datos** (aplicación de la técnica — aquí entra el ML)
7. Evaluación / interpretación de patrones
8. Evaluación de resultados

### Técnicas principales de Data Mining

| Técnica | Tipo de problema | Interpretabilidad |
|---|---|---|
| Redes Neuronales | Clasificación/predicción compleja | Baja ("caja negra") |
| Árboles de Decisión | Clasificación | Alta |
| Reglas (asociación/inducción) | Relaciones entre eventos | Alta |
| Redes Bayesianas | Probabilidad condicional | Media-alta |
| Algoritmos Genéticos | Optimización (no clasificación) | Baja |

- **Reglas de asociación:** "si ocurre A, probablemente ocurra B" (no simétrico) — ej. pañales → talco
- **Búsqueda de secuencias:** patrones de eventos ordenados en el tiempo (base de sistemas de recomendación)
- **Redes Bayesianas:** actualizan una probabilidad inicial (*prior*) con evidencia nueva → probabilidad final (*posterior*)
- **Algoritmos genéticos:** optimización por combinación, mutación y selección — útiles cuando el espacio de soluciones es demasiado grande para evaluarlo exhaustivamente (ej. problema del vendedor viajero)

### Minería de Textos y Web Mining

- **Minería de textos:** aplica PLN a texto no estructurado para extraer patrones (no "comprende" el texto como un humano)
- **Web Mining — tres enfoques:** uso (comportamiento de navegación), estructura (enlaces entre páginas), contenido (el contenido de las páginas)

### Data Mining y Marketing

- Tres fuentes de conocimiento del cliente: mercado, cliente propio, terceros
- Tres aplicaciones: elaboración de perfiles, análisis de desviaciones, análisis de tendencias

## 3. Ejemplos de código ejecutable

**Nota:** esta unidad es conceptual (introducción al proceso y las técnicas); el material no incluye ejercicios de código propios. El siguiente ejemplo ilustra la etapa 6 del proceso KDD (aplicación de la técnica), retomando clustering para segmentación — el mismo caso trabajado en Fundamentos de ML.

```python
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Etapas 1-5 de KDD (selección, limpieza, integración, transformación, reducción)
# ya resueltas: datos limpios de comportamiento de compra
data = pd.DataFrame({
    "recencia_dias":      [5, 200, 10, 150, 3, 180, 20, 220],
    "frecuencia_compras": [30, 2, 25, 3, 40, 1, 20, 2],
    "monto_total":        [4500, 300, 3800, 250, 6000, 150, 3200, 200]
})

# Etapa 6: Minería de Datos (aplicación de la técnica de clustering)
X_scaled = StandardScaler().fit_transform(data)
modelo = KMeans(n_clusters=3, random_state=42, n_init=10)
data["segmento"] = modelo.fit_predict(X_scaled)

# Etapas 7-8: interpretación y evaluación de resultados (fuera del código,
# corresponde al analista interpretar qué representa cada segmento)
print(data)
```

## 4. Conexión con experiencia real (Movet, Rappi)

- **Rappi:** reglas de asociación en "add-ons" — quien compra una hamburguesa probablemente compre bebida/postre (no bidireccional).
- **Movet:** aplicación completa del proceso KDD sobre historial de citas y compras para: (1) detectar clientes que se alejan del patrón esperado (análisis de desviaciones), (2) segmentar por comportamiento (clustering/RFM), y (3) construir perfiles de cliente para campañas dirigidas.
- **Random Forest en contexto veterinario:** para un caso donde se necesita trazabilidad de la decisión (ej. justificar un tratamiento), se prefiere un árbol de decisión sobre una red neuronal, a pesar de la menor precisión.

## 5. Preguntas de repaso

1. ¿Por qué "usar Machine Learning" no es automáticamente lo mismo que "hacer minería de datos" siguiendo el proceso KDD completo?
2. ¿Qué etapa del proceso KDD corresponde a "aplicar el algoritmo" y por qué representa solo una fracción del trabajo total?
3. ¿En qué se diferencia una regla de asociación de un árbol de decisión, en términos del tipo de resultado que entregan?
4. ¿Por qué las redes bayesianas son especialmente útiles para evaluación de riesgo (crediticio, fraude), a diferencia de un árbol de decisión?

## 6. Referencias

- Material oficial de la Unidad 1 — Universidad DaVinci, asignatura Minería de Datos.
- Alpaydin, E. (2021). *Aprendizaje automático*. MIT Press.
- Bobadilla, J. (2021). *Aprendizaje automático y aprendizaje profundo: usando Python, Scikit y Keras*. Ediciones Zhou.
