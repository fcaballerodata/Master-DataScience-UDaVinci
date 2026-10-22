# Actividad Práctica 1 — Minería de datos o data mining y el aprendizaje automático

**Asignatura:** Minería de Datos
**Trimestre:** T3 — 2026 | Semana 6
**Cubre:** UD1 (con apoyo de UD4–UD5 en la pregunta 3)
**Norma de citación:** APA 7.ª edición

---

**Objetivo general:** Comprender las bases esenciales sobre la minería de datos o data mining y el aprendizaje automático.

## 1. ¿Qué es la minería de datos y el aprendizaje automático?

### Respuesta

La **minería de datos** (*data mining*) es el proceso de descubrir patrones, tendencias y conocimiento significativo a partir de grandes conjuntos de datos. Se ubica en la intersección de la estadística, la inteligencia artificial y las bases de datos, y su objetivo es transformar datos brutos en información útil y comprensible para la toma de decisiones (Universidad DaVinci, s. f.). En esencia, es la búsqueda de patrones ocultos en los datos (Salazar & Girón, 2021).

Ese proceso se enmarca en el descubrimiento de conocimiento en bases de datos (KDD, *Knowledge Discovery in Databases*), que recorre siete etapas: selección, limpieza, integración, transformación y reducción de los datos; minería de datos propiamente dicha; y evaluación e interpretación de los resultados (Universidad DaVinci, s. f.).

El **aprendizaje automático** (*machine learning*) es una rama de la inteligencia artificial que agrupa técnicas capaces de mejorar su comportamiento mediante la experiencia: a partir de datos conocidos se extrae información y se obtiene un modelo, que se verifica y se reajusta según el error (Universidad DaVinci, s. f.).

Ambos conceptos **no son sinónimos**. La minería de datos es el proceso completo, desde elegir y limpiar los datos hasta interpretar y decidir. El aprendizaje automático es una herramienta que aporta los algoritmos para la etapa de modelado dentro de ese proceso. Por ejemplo, en una plataforma de domicilios, el modelo que agrupa clientes por su comportamiento de compra es aprendizaje automático, pero solo es un paso: antes hay que seleccionar y limpiar los pedidos, y después interpretar los grupos para decidir qué hacer con ellos.

## 2. Describe los modelos y técnicas de Data Mining.

### Respuesta

En minería de datos el enfoque depende del tipo de problema y del resultado que se necesite. Un **modelo** responde a qué tipo de análisis se hace; una **técnica** es la estrategia de tratamiento de los datos, representada por uno o varios algoritmos (Universidad DaVinci, s. f.). Salazar y Girón (2021), por ejemplo, distinguen algoritmos de clasificación (árboles de decisión, ID3, C4.5) y de predicción (regresión lineal, M5).

**Modelos (tipos de análisis)**

| Modelo | Qué hace | Ejemplo sencillo |
| --- | --- | --- |
| Predicción | Extrae patrones de datos actuales o históricos para estimar el futuro | Estimar si las compras de los clientes subirán o bajarán el próximo período |
| Clasificación | Encuentra la relación entre variables y asigna cada dato a una categoría | Clasificar un correo como spam o no spam |
| Asociación | Encuentra eventos que ocurren juntos o en secuencia | Quien compra pañales suele comprar polvos de talco |
| Agrupación | Detecta similitudes y diferencias entre grupos | Segmentar clientes según sus gustos de compra |

**Técnicas**

| Técnica | Descripción | Ejemplo sencillo | Interpretabilidad |
| --- | --- | --- | --- |
| Redes neuronales | Capas de neuronas (entrada, ocultas y salida) conectadas entre sí; aprenden de forma iterativa reajustando pesos según el error. Las redes de Kohonen agrupan datos sin etiquetas | Reconocer un rostro o una huella dactilar en el celular | Baja: muy potentes, pero una persona no puede seguir el recorrido exacto de la entrada a la predicción (Molnar, 2025; Universidad DaVinci, s. f.) |
| Árboles de decisión | Un nodo raíz se divide en ramas según los valores de cada variable hasta llegar a un nodo hoja que etiqueta el dato | Decidir si un paciente tiene gripe o no según sus síntomas | Alta mientras sean poco profundos: se interpretan como una serie de reglas compactadas (Molnar, 2025; Salazar & Girón, 2021) |
| Reglas de asociación e inducción | Reglas del tipo "si condición, entonces clase", con la probabilidad de que ocurra el segundo evento; pueden extraerse de un árbol | Si compra pañales, entonces probablemente compre talco (no necesariamente al revés) | Alta: las reglas de decisión están entre los modelos de predicción más interpretables (Molnar, 2025) |
| Redes bayesianas | Usan el teorema de Bayes para actualizar la probabilidad de un evento al llegar evidencia nueva | Calificar el riesgo de prestar dinero a un posible prestatario | Media: su marco probabilístico permite explicar el modelo, el razonamiento y la evidencia, aunque su uso suele ser ad hoc (Derks & de Waal, 2020) |
| Algoritmos genéticos | Técnica de optimización inspirada en la selección natural: genera soluciones, las muta, las recombina y conserva las mejores | Encontrar el menor número de variables que siguen explicando el problema | Media: depende de cómo se codifique la solución; los algoritmos estocásticos o basados en poblaciones son más difíciles de seguir que los deterministas (Zhou et al., 2024) |

La interpretabilidad y el potencial suelen ir en direcciones opuestas: los árboles de decisión son fáciles de interpretar, mientras que las técnicas de aprendizaje profundo modelan problemas mucho más complejos pero son difíciles de explicar (Universidad DaVinci, s. f.). Por eso la técnica se elige según el problema y según cuánto se necesite justificar la decisión; en decisiones de alto impacto se recomienda preferir modelos interpretables por diseño antes que explicar cajas negras (Rudin, 2019).

## 3. Haz un breve resumen sobre la minería de textos y Web Mining.

### Respuesta

La **minería de textos** es una rama de la minería de datos que aplica técnicas de procesamiento de lenguaje natural (PLN) y de minería de datos a texto no estructurado, como documentos, comentarios o noticias, para extraer patrones, tendencias y gustos. Sirve, por ejemplo, para detectar noticias falsas o comentarios ofensivos. Sus etapas generales son seleccionar los textos y documentos, extraer la información relevante y aplicar las técnicas de minería de datos (Universidad DaVinci, s. f.). Cabe aclarar que no "comprende" el texto como lo hace una persona: lo representa como un conjunto de palabras, normalmente en forma de vector numérico, y busca patrones sobre esa representación (Hotho et al., 2005).

El **Web Mining** es otra rama de la minería de datos y se usa para extraer información como las tendencias de uso de la web por parte de los usuarios (Universidad DaVinci, s. f.). Se organiza en tres enfoques (Kosala & Blockeel, 2000):

| Enfoque | Qué analiza | Ejemplo sencillo |
| --- | --- | --- |
| Minería de uso | Los datos generados por las sesiones y el comportamiento de los usuarios, como páginas visitadas, tiempo conectado, fecha y hora o país de origen (Universidad DaVinci, s. f.) | Agrupar a los usuarios según las páginas que visitan para recomendarles productos |
| Minería de estructura | El modelo que hay detrás de los enlaces entre páginas | Ver qué páginas reciben más enlaces para saber cuáles son las más referenciadas |
| Minería de contenido | La información contenida en las páginas y documentos de la web | Analizar las reseñas de un sitio para saber qué opinan los clientes |

Las dos ramas se tocan: la minería de textos puede verse como un caso particular de la minería de contenido web (Kosala & Blockeel, 2000).

## Referencias

Derks, I. P., & de Waal, A. (2020). A taxonomy of explainable Bayesian networks. En A. Gerber (Ed.), *Artificial intelligence research: SACAIR 2021* (Communications in Computer and Information Science, Vol. 1342). Springer. https://arxiv.org/abs/2101.11844

Hotho, A., Nürnberger, A., & Paaß, G. (2005). A brief survey of text mining. *Journal for Language Technology and Computational Linguistics, 20*(1), 19–62. https://doi.org/10.21248/jlcl.20.2005.68

Kosala, R., & Blockeel, H. (2000). Web mining research: A survey. *SIGKDD Explorations, 2*(1), 1–15. https://arxiv.org/abs/cs/0011033

Molnar, C. (2025). *Interpretable machine learning: A guide for making black box models explainable* (3.ª ed.). https://christophm.github.io/interpretable-ml-book/

Rudin, C. (2019). Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nature Machine Intelligence, 1*(5), 206–215. https://doi.org/10.1038/s42256-019-0048-x

Salazar, J. I., & Girón, E. (2021). Análisis y aplicación de algoritmos de minería de datos. *Perspectivas, 6*(21), 71–88. https://doi.org/10.26620/uniminuto.perspectivas.6.21.2021.71-88

Universidad DaVinci. (s. f.). *Minería de datos o data mining y el aprendizaje automático* [Material de la Unidad 1]. Minería de Datos. LMS Universidad DaVinci. https://lms.udavinci.edu.mx

Zhou, R., Bacardit, J., Brownlee, A., Cagnoni, S., Fyvie, M., Iacca, G., McCall, J., van Stein, N., Walker, D. J., & Hu, T. (2024). *Evolutionary computation and explainable AI: A roadmap to understandable intelligent systems* [Preprint]. arXiv. https://arxiv.org/abs/2406.07811

---

### Notas de verificación de fuentes
- Las ocho fuentes se consultaron y se verificaron sus datos bibliográficos antes de citarlas (Salazar y Girón, Hotho et al., Kosala y Blockeel, Molnar, Rudin, Derks y de Waal, Zhou et al. y la Unidad 1).
- Los niveles de interpretabilidad de la tabla de técnicas se respaldan con las citas indicadas en cada celda; Zhou et al. (2024) es un preprint (sin revisión por pares).
- Los ejemplos sencillos de las tablas son propios, salvo los tomados de la Unidad 1 (gripe, spam, pañales y talco, préstamo, huella dactilar).
