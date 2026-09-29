# UD3 — Introducción a la Inteligencia Artificial

**Asignatura:** Minería de Datos
**Trimestre:** T3 — 2026 | Semana 3

---

## 📌 Resumen ejecutivo (repaso rápido de 30 segundos)

- IA = rama de la informática dedicada a crear máquinas inteligentes. Término acuñado por **John McCarthy en 1956** (Conferencia de Dartmouth).
- 5-7 capacidades que definen un sistema de IA: **percepción, razonamiento, aprendizaje, resolución de problemas, comprensión del lenguaje**, conocimiento, planificación/manipulación física.
- El **Machine Learning es solo una de esas capacidades** (aprendizaje) — hay IA sin ML (sistemas de reglas fijas, Deep Blue).
- Historia: 1956 (Dartmouth) → "invierno de la IA" (1975-1995, por falta de datos y hardware) → Deep Blue vence a Kasparov (1997) → explosión actual (datos masivos + poder de cómputo).
- La IA impulsa la transformación digital: automatizar, analizar patrones, generar contenido, apoyar decisiones.
- Limitación central: **falta de comprensión real** — puede dar respuestas coherentes sin "entender" el significado; requiere siempre supervisión humana.

---

## 1. ¿Qué es la Inteligencia Artificial?

### 1.1 Definición

La Inteligencia Artificial es una rama de la informática que tiene como objetivo **crear máquinas inteligentes**: hace posible que las máquinas aprendan de la experiencia, se ajusten a nuevas entradas y realicen tareas similares a las de los humanos. Se ha convertido en una parte esencial de la industria tecnológica.

**Origen del término:** acuñado por **John McCarthy en 1956**, en el contexto de la Conferencia de Dartmouth. Definición operativa de McCarthy: *"la ciencia y la ingeniería de hacer máquinas inteligentes, especialmente programas de cómputo inteligentes"*.

### 1.2 Conexión con el Test de Turing

Una aproximación de la IA, según Alan Turing, es un sistema capaz de realizar tareas que, si las realizara un humano, requerirían inteligencia — sin que la máquina necesite razonar exactamente igual que un humano, solo producir resultados equivalentes ("el juego de la imitación").

### 1.3 Las 5 capacidades fundamentales

| Capacidad | Qué implica | Ejemplo |
|---|---|---|
| **Percepción** | Entender e interpretar datos sensoriales | Visión artificial, reconocimiento de voz |
| **Razonamiento** | Sacar conclusiones lógicas nuevas a partir de información almacenada | Sistemas expertos, diagnóstico |
| **Aprendizaje** | Mejorar el rendimiento de forma autónoma basándose en datos históricos | Machine Learning (clasificación, regresión, clustering, RNA) |
| **Resolución de problemas** | Encontrar caminos óptimos hacia una solución en entornos complejos | Algoritmos genéticos (Minería de Datos UD1), planificación de rutas |
| **Comprensión del lenguaje** | Interpretar, traducir y generar comunicación humana | PLN (unidades 5-6 de esta materia) |

Ampliando el listado, el material también asocia al campo de la IA: **Conocimiento** (la "ingeniería del conocimiento": acceso a objetos, categorías, propiedades y relaciones para actuar de forma inteligente) y **Planificación/manipulación física** (robótica — localización, trayectorias, mapas).

> 🔎 **Idea clave:** el Machine Learning ya trabajado (clasificación, regresión, clustering, RNA) corresponde **exclusivamente a la capacidad de Aprendizaje**. La IA es un campo mucho más amplio que incluye percepción, razonamiento, resolución de problemas y lenguaje — el ML es una vía para lograr una de las 5-7 capacidades, no la única.

### ⚠️ Error común
Pensar que "hacer Machine Learning" es sinónimo de "hacer Inteligencia Artificial completa", o que **todo** sistema de IA necesariamente aprende de datos. Un sistema de reglas fijas (IA simbólica) ejerce razonamiento y resolución de problemas sin tener la capacidad de aprendizaje — sigue siendo IA, pero no es ML.

---

## 2. Historia de la Inteligencia Artificial

### 2.1 Línea de tiempo completa

| Período | Hito |
|---|---|
| **Segunda Guerra Mundial** | Alan Turing y su equipo desarrollan la máquina **Bombe** para descifrar el código Enigma alemán |
| **1950** | Turing explora el concepto de máquina inteligente — origen del **Test de Turing** |
| **1951** | La máquina **Ferranti Mark 1** domina el juego de las damas mediante un algoritmo |
| **1956** | **Conferencia de Dartmouth**: John McCarthy acuña "Inteligencia Artificial"; con Allen Newell y Herbert Simon se sientan las bases de la IA simbólica; se desarrolla **LISP** y el **General Problem Solver** |
| **Década de 1960** | Se investiga cómo enseñar a las computadoras a razonar lógicamente; el Departamento de Defensa de EE.UU. invierte en IA |
| **1970-1972** | Se construye **WABOT-1**, el primer robot humanoide (Japón) |
| **Fines 1960-1970** | La **DARPA** financia proyectos de mapeo de calles con IA — la visión artificial y el razonamiento básico resultan mucho más difíciles de lo esperado |
| **Mediados 1970 – mediados 1990** | **"Invierno de la IA"**: grave escasez de fondos por expectativas no cumplidas |
| **Fines de 1990** | Resurge el interés corporativo; Japón anuncia planes de una "computadora de quinta generación" |
| **1997** | **Deep Blue (IBM)** derrota al campeón mundial de ajedrez Garry Kasparov — mediante fuerza bruta computacional (razonamiento + resolución de problemas), **no mediante aprendizaje de datos históricos** |
| **Principios de 2000** | Estalla la burbuja de las puntocom; algunos fondos de IA se agotan, pero el ML continúa avanzando gracias a mejoras de hardware |
| **Últimos años** | Explosión del ML/IA en productos de consumo masivo: asistentes virtuales, sistemas de recomendación, generación de contenido |

### 2.2 Por qué ocurrió el "invierno de la IA" (y por qué importa hoy)

No fue por ideas equivocadas, sino porque **la tecnología de la época no tenía suficiente poder de cómputo ni suficientes datos digitales masivos** para cumplir las promesas hechas. El ML explotó específicamente en la última década porque **convergieron datos masivos + poder de cómputo al mismo tiempo** — los fundamentos matemáticos y conceptuales llevan 70 años de desarrollo.

### 2.3 Caso de estudio — Deep Blue vs. Kasparov (1997)

Deep Blue ganó evaluando millones de jugadas posibles mediante lógica y fuerza bruta computacional — **no** aprendió de partidas históricas como lo haría un modelo de ML moderno. Es la prueba histórica de que se puede lograr un desempeño sobrehumano en una tarea compleja sin aprendizaje de datos: puro razonamiento y búsqueda exhaustiva. Contraejemplo perfecto a la idea de que "toda IA impresionante usa Machine Learning".

### ⚠️ Error común
Pensar que el Machine Learning es una disciplina "nueva" (últimos 10-15 años). Sus fundamentos llevan 70 años de desarrollo — lo que cambió fue la disponibilidad de datos y hardware para aplicarlos a gran escala.

---

## 3. La Importancia de la IA

### 3.1 La IA como motor de transformación digital

La incorporación progresiva de la IA impulsa la **transformación digital**: uso de tecnologías avanzadas para mejorar la gestión de información, optimizar procesos y generar nuevas oportunidades de desarrollo.

**4 tareas principales para las que las organizaciones usan IA:**

| Tarea | Ejemplo |
|---|---|
| **Automatizar tareas repetitivas** | Clasificación automática de documentos |
| **Analizar patrones y tendencias** | Detectar comportamientos en grandes volúmenes de datos |
| **Generar contenidos y propuestas** | Redacción asistida, resúmenes |
| **Apoyar la toma de decisiones** | Recomendaciones basadas en datos |

### 3.2 Aplicaciones por sector

| Sector | Aplicación |
|---|---|
| **Salud** | Apoyo al diagnóstico, análisis de imágenes médicas, gestión de información clínica |
| **Industria** | Automatización de procesos, mantenimiento predictivo, control de calidad |
| **Finanzas** | Detección de fraudes, análisis de riesgos, procesamiento de operaciones |
| **Educación** | Generación de recursos, apoyo al aprendizaje, personalización de contenidos |
| **Comercio y marketing** | Recomendaciones personalizadas, análisis del comportamiento del consumidor |
| **Administración y servicios** | Automatización de trámites, gestión documental |

> 💡 Muchas aplicaciones de IA funcionan de forma **invisible** para el usuario: motores de búsqueda, sistemas de recomendación, filtros de spam — sin interacción consciente con "una IA".

### 3.3 Beneficios

- **Mayor eficiencia** — tareas en menos tiempo
- **Escalabilidad** — gestión de un volumen elevado de tareas/consultas simultáneas
- **Disponibilidad continua**
- **Personalización** de contenidos, productos o servicios
- **Apoyo en la toma de decisiones** — identificación de patrones relevantes
- **Procesamiento de información** — análisis eficaz de grandes volúmenes de datos

### 3.4 Limitaciones

- **Posibles errores** — puede generar información incorrecta o imprecisa
- **Dependencia de los datos** — la calidad del resultado depende de la calidad de los datos de entrenamiento
- **Falta de comprensión real** — puede producir respuestas coherentes **sin comprender realmente** el significado de la información
- **Necesidad de supervisión** — los resultados deben revisarse antes de usarse
- **Consideraciones éticas y legales** — privacidad, transparencia, uso responsable de los datos

> ⚠️ **Distinción importante:** "falta de comprensión real" no es lo mismo que "falta de contexto/información". Darle más datos o contexto a un sistema (por ejemplo, conectar un modelo a las tablas y relaciones de un proyecto vía MCP) resuelve problemas de información faltante — pero no elimina el riesgo de que, incluso con toda la información disponible, una respuesta "suene coherente" sin ser realmente correcta. Por eso la supervisión humana sigue siendo necesaria independientemente de cuánto contexto se le dé al sistema.

### 3.5 Caso guiado del material — conclusión central de la unidad

El material plantea un escenario: una empresa automatiza la gestión de consultas de clientes con IA, logrando respuestas más rápidas, pero recibe consultas complejas que la IA no resuelve bien, generando respuestas homogéneas y retrasos cuando se requiere intervención humana.

> *"La inteligencia artificial actúa como una herramienta de apoyo que complementa las capacidades humanas, pero no sustituye la responsabilidad asociada a su utilización."*

---

## 4. Glosario de la unidad

| Término | Definición breve |
|---|---|
| **Inteligencia Artificial (IA)** | Rama de la informática dedicada a crear máquinas que ejecutan tareas que normalmente requerirían inteligencia humana |
| **Test de Turing** | Criterio propuesto por Alan Turing: una máquina es "inteligente" si sus respuestas son indistinguibles de las de un humano |
| **IA simbólica** | Paradigma de IA basado en reglas y lógica programada explícitamente, sin aprendizaje de datos |
| **Ingeniería del conocimiento** | Disciplina de dar acceso a un sistema a objetos, categorías, propiedades y relaciones del mundo para que actúe de forma inteligente |
| **Invierno de la IA** | Período (mediados 1970 – mediados 1990) de escasez de fondos para investigación en IA |
| **LISP** | Lenguaje de programación desarrollado en el contexto de los primeros trabajos de IA simbólica |
| **General Problem Solver** | Programa pionero (Newell y Simon) para resolución general de problemas mediante razonamiento |
| **Transformación digital** | Uso de tecnologías avanzadas (incluida la IA) para mejorar gestión de información, optimizar procesos y generar nuevas oportunidades |

---

## 5. Preguntas de repaso

1. ¿Cuál es la relación entre IA y Machine Learning según las 5-7 capacidades vistas en esta unidad? Da un ejemplo de IA que no use ML.
2. Ordena cronológicamente: Conferencia de Dartmouth, Deep Blue vs. Kasparov, invierno de la IA, máquina Bombe.
3. ¿Por qué el "invierno de la IA" es relevante para entender por qué el ML se popularizó específicamente en la última década?
4. Nombra las 4 tareas principales para las que las organizaciones usan IA en transformación digital, con un ejemplo de tu propio entorno profesional.
5. ¿Cuál es la diferencia entre "falta de contexto/información" y "falta de comprensión real" como limitación de la IA?
6. ¿Por qué Deep Blue es un buen contraejemplo de la idea "toda IA impresionante usa Machine Learning"?

---

## 6. Referencias

- Material oficial de la Unidad 3 — Universidad DaVinci, asignatura Minería de Datos.
- Alpaydin, E. (2021). *Aprendizaje automático*. MIT Press.
- Bobadilla, J. (2021). *Aprendizaje automático y aprendizaje profundo: usando Python, Scikit y Keras*. Ediciones Zhou.
