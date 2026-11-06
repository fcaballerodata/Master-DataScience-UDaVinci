# Actividad Práctica 2 — Weka y Data Mining

**Asignatura:** Minería de Datos
**Trimestre:** T3 — 2026 | Semana 9
**Cubre:** UD2 (Weka y Data Mining), según el enunciado del campus
**Norma de citación:** APA 7.ª edición
**Entrega:** archivo de Word ([`Actividad-Practica-Weka-y-Data-Mining.docx`](./Actividad-Practica-Weka-y-Data-Mining.docx))

---

**Objetivo general:** Conocer los aspectos básicos de Weka y Data Mining.

## 1. ¿Qué es Weka?

### Respuesta

**Weka** (*Waikato Environment for Knowledge Analysis*) es un conjunto de librerías Java para extraer conocimiento de bases de datos, desarrollado en la Universidad de Waikato, en Nueva Zelanda (Universidad DaVinci, s. f.). Es una colección de algoritmos de aprendizaje automático y de herramientas de preparación de datos, escrita en Java, distribuida con licencia pública general de GNU (GPL) y probada en Linux, Windows y macOS (Frank et al., 2016). Cubre las tareas propias de la minería de datos: preprocesamiento, clasificación, regresión, agrupamiento (*clustering*), selección de atributos y visualización (Universidad DaVinci, s. f.).

| **Característica**        | **Qué significa**                                                                                                                                                                |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Software libre y portable | Funciona en cualquier plataforma con máquina virtual de Java; es su único requisito (Universidad DaVinci, s. f.).                                                                |
| Entorno visual            | Permite probar algoritmos sin programar, así que el analista se concentra en estudiar los resultados y no en el código (Universidad DaVinci, s. f.).                             |
| Formato ARFF              | Lee archivos planos con tres partes: nombre de la relación (`@RELATION`), atributos con su tipo (`@ATTRIBUTE`) y los datos (`@DATA`) (Universidad DaVinci, s. f.).                     |
| Conexión a bases de datos | Puede procesar los datos que devuelve una consulta SQL mediante JDBC, y ofrece una API para uso de terceros (Universidad DaVinci, s. f.).                                        |
| Trayectoria               | Según Hall et al. (2009), lleva más de doce años de evolución desde su primera versión, fue reescrito por completo y se usa tanto en el ámbito académico como en el empresarial. |

## 2. Describe las técnicas de Data Mining en Weka.

### Respuesta

Weka aplica algoritmos de minería de datos de cuatro tipos principales (Universidad DaVinci, s. f.). Todos están disponibles en la interfaz **Explorer**, cada uno en su pestaña:

| **Técnica**                 | **Qué hace**                                                                 | **Pestaña en Explorer** |
|-----------------------------|------------------------------------------------------------------------------|-------------------------|
| Clasificación               | A partir de elementos con etiqueta, predice la etiqueta de elementos nuevos. | Classify                |
| Regresión                   | Predice variables continuas a partir de otras características de los datos.  | Classify                |
| Agrupamiento (*clustering*) | Identifica grupos con características similares.                             | Cluster                 |
| Selección de atributos      | Busca automáticamente los atributos más relevantes para clasificar.          | Select attributes       |

Además, Weka ofrece **asociación** (pestaña Associate, con el algoritmo Apriori, que busca relaciones entre los datos), **preprocesamiento** mediante filtros (pestaña Preprocess) y **visualización** de los resultados (pestaña Visualize) (Universidad DaVinci, s. f.).

**Cómo se evalúa un modelo.** El cuadro *Test options* ofrece cuatro formas (Universidad DaVinci, s. f.):

- **Use training set:** evalúa con los mismos datos del entrenamiento. La guía advierte que da una estimación demasiado optimista.

- **Supplied test set:** usa un conjunto independiente.

- **Cross-validation:** validación cruzada, la más elaborada y costosa.

- **Percentage split:** divide los datos según un porcentaje (una parte para entrenar y el resto para evaluar).

**Selección de atributos.** Tiene dos componentes: un *método de evaluación*, que mide la calidad de un conjunto de atributos, y un *método de búsqueda*, que decide cómo recorrer los subconjuntos. Evaluar todos es un problema combinatorio inabordable cuando crecen los atributos, por eso se usan estrategias de búsqueda eficientes. Los métodos de evaluación *wrapper* miden la calidad con la tasa de error de un clasificador (Universidad DaVinci, s. f.).

## 3. Haz un breve resumen sobre las interfaces de Weka.

### Respuesta

Al abrir Weka aparece el **selector de interfaces**, desde el cual se elige cómo trabajar según la experiencia del usuario y el tipo de análisis (Universidad DaVinci, s. f.):

| **Interfaz**      | **Para qué sirve**                                                                                                                                                                                                                            |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Explorer**      | Ejecuta los algoritmos sobre un conjunto de datos, con pestañas para preprocesar, clasificar, agrupar, asociar, seleccionar atributos y visualizar. Es la más usada y la más accesible para empezar.                                          |
| **Experimenter**  | Configura experimentos avanzados con varios conjuntos de datos y varios algoritmos, de forma secuencial o paralela. Permite repetir ensayos y aplicar pruebas estadísticas para saber si las diferencias entre algoritmos son significativas. |
| **KnowledgeFlow** | Construye el análisis como un diagrama de flujo: fuentes de datos, filtros, clasificadores y evaluadores conectados visualmente. Facilita ver cómo se transforman los datos en cada paso y reutilizar los esquemas.                           |
| **Workbench**     | Reúne en un solo espacio de trabajo el Explorer, el SimpleCLI, el Experimenter y el flujo de minería de datos, para no cambiar de interfaz. Se introdujo en la versión 3.8.                                                                   |
| **Simple CLI**    | Ventana de comandos para ejecutar clases Java de Weka manualmente. Se mantiene porque las primeras versiones no tenían interfaz gráfica.                                                                                                      |

Aparte, el menú *Tools* ofrece utilidades como el Arff Viewer (ver y editar archivos en forma de tabla), el SQL Viewer, el editor de redes bayesianas y el administrador de paquetes (Universidad DaVinci, s. f.).

## Referencias

Frank, E., Hall, M. A., & Witten, I. H. (2016). *The WEKA workbench. Online appendix for "Data mining: Practical machine learning tools and techniques"* (4.ª ed.). University of Waikato. https://researchcommons.waikato.ac.nz/entities/publication/d1c32263-dd7f-48fc-899d-2893b45205c7

Hall, M., Frank, E., Holmes, G., Pfahringer, B., Reutemann, P., & Witten, I. H. (2009). The WEKA data mining software: An update. *SIGKDD Explorations, 11*(1), 10–18. https://doi.org/10.1145/1656274.1656278

Universidad DaVinci. (s. f.). *WEKA y Data Mining* \[Material de la Unidad 2\]. Minería de Datos. LMS Universidad DaVinci. https://lms.udavinci.edu.mx

---

### Notas de verificación de fuentes
- Frank et al. (2016) y Hall et al. (2009): se verificaron autores, título, año y, en Hall et al., revista, volumen, número, páginas y DOI; la descripción de Frank et al. sale del resumen del registro de Waikato (no se leyó el apéndice completo ni el artículo de Hall).
- El resto del contenido sale de la Unidad 2. La guía dice que la selección de atributos "encuentra atributos nuevos", pero su sección 4 explica que busca los subconjuntos **más relevantes**; se usó esta segunda versión.
- No se incluyen ejemplos con datos (iris, weather) por decisión del autor, ni experiencia personal con Weka.
