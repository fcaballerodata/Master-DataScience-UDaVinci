# UD4 — Introducción al PLN (Procesamiento del Lenguaje Natural)

**Asignatura:** Minería de Datos
**Trimestre:** T3 — 2026 | Semana 4

> Nota: en el temario general de la materia esta unidad aparece listada como "Machine Learning-Aprendizaje Automático", pero el material oficial de la unidad (archivo "Unidad 4 - Introducción al PLN") y su contenido corresponden a **Introducción al PLN**.

---

## 📌 Resumen ejecutivo (repaso rápido de 30 segundos)

- **PLN** = campo de la IA que permite a las máquinas leer, comprender y derivar significado del lenguaje humano. Trabaja con datos **no estructurados** (texto libre, voz).
- **8 tareas:** categorización, identificación del tema, extracción/abstracción, recuperación de información, análisis intencional, análisis de sentimientos, reconocimiento de voz, traducción automática.
- **4 niveles de análisis:** procesamiento del texto → sintáctico → semántico → pragmático. El conteo de palabras se queda en el primero.
- **Tokenización:** dividir la entrada en unidades procesables. **Ambigüedad** (léxica y estructural) = reto central.
- Aplicaciones: salud, correo (spam), asistentes de voz, medios, finanzas, RR.HH., legal, voz del cliente.
- Futuro: modelos entrenados con grandes volúmenes de datos, comprensión semántica profunda, integración multimodal, personalización y el desafío de los **sesgos heredados** de los datos.

---

## 1. ¿Qué es el PLN?

### 1.1 Definición

El **Procesamiento del Lenguaje Natural (PLN)** es un campo de la inteligencia artificial que brinda a las máquinas la capacidad de **leer, comprender y derivar el significado de los lenguajes humanos**. Integra lingüística, informática y aprendizaje automático. Su auge actual se explica por el mayor acceso a datos y el aumento del poder de cómputo (mismas causas del resurgimiento de la IA vistas en UD3).

### 1.2 Datos estructurados vs. no estructurados

| | Estructurados | No estructurados |
|---|---|---|
| **Forma** | Filas y columnas (bases relacionales) | Texto libre, voz, conversaciones, publicaciones en redes |
| **Ejemplo** | Tabla de ventas en Snowflake | Reseñas de clientes, tweets |
| **Análisis tradicional** | Directo (SQL, BI) | No se ajusta; requiere PLN para convertirlo en algo analizable |

### 1.3 Las 8 tareas del PLN

| Tarea | Qué hace |
|---|---|
| **Categorización** | Clasificar texto, crear resúmenes, indexar y buscar, detectar contenido duplicado |
| **Identificación del tema** | Detectar el significado y los temas tratados en grandes volúmenes de texto |
| **Extracción y abstracción** | Extraer los párrafos relevantes o crear una versión resumida de un documento |
| **Recuperación de información** | Buscar información específica dentro de texto digital |
| **Análisis intencional** | Discernir la intención en el lenguaje humano (base de los chatbots, que deben "aprender" respuestas apropiadas) |
| **Análisis de sentimientos** | Determinar el tono y las opiniones (positivas o negativas) detrás del texto |
| **Reconocimiento de voz** | Transformar lenguaje hablado en texto escrito, y viceversa |
| **Traducción automática** | Traducir texto o voz de un idioma a otro |

### 1.4 Ejemplo: de texto libre a tabla (bag of words)

Los algoritmos trabajan con **números**, no con texto. Hay que **representar el texto como números** antes de aplicar clasificación o clustering. La forma más simple es contar palabras.

```python
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

resenas = [
    "excelente servicio, entrega rapida",
    "pedido tarde, mala atencion",
    "entrega rapida y excelente atencion"
]

vectorizador = CountVectorizer()
matriz = vectorizador.fit_transform(resenas)

tabla = pd.DataFrame(matriz.toarray(), columns=vectorizador.get_feature_names_out())
print(tabla)
```

Salida de referencia (columnas = palabras; filas = reseñas):

```
   atencion  entrega  excelente  mala  pedido  rapida  servicio  tarde
0         0        1          1     0       0       1         1      0
1         1        0          0     1       1       0         0      1
2         1        1          1     0       0       1         0      0
```

Nota: por defecto `CountVectorizer` ignora palabras de una sola letra (como "y").

```r
resenas <- c("excelente servicio entrega rapida",
             "pedido tarde mala atencion",
             "entrega rapida y excelente atencion")

palabras <- strsplit(resenas, " ")
tabla <- table(unlist(palabras))
print(tabla)
```

> ⚠️ **Limitación del conteo de palabras:** trata cada palabra como una columna independiente. "rápida" y "veloz" serían dos columnas sin relación, aunque signifiquen casi lo mismo, y "genial, otra vez llegó frío mi pedido" (ironía) se leería como elogio. Captura **la forma** del texto, no **el significado**: se queda en el nivel de procesamiento del texto y nunca llega al semántico ni al pragmático.

---

## 2. ¿Qué incluye el PLN?

### 2.1 Los 4 subtemas

| Nivel | Qué hace | Ejemplo |
|---|---|---|
| **Procesamiento del texto** | Convierte la entrada (teclado, archivo) en unidades que la máquina pueda manejar | Separar una frase en palabras |
| **Análisis sintáctico** | Estudia la **estructura gramatical**: cómo se combinan palabras en frases y oraciones | Identificar sujeto, verbo y complemento |
| **Análisis semántico** | Estudia el **significado** de palabras y oraciones | Saber que "veloz" y "rápida" son equivalentes |
| **Análisis pragmático** | Estudia el significado **en contexto**: la función de la oración en la vida cotidiana y en la conversación | "¿Puedes pasarme la sal?" es una petición, no una pregunta sobre capacidad |

### 2.2 Tokenización

Conversión de una señal de entrada en partes (*tokens*) para que la computadora pueda procesarla. Aunque el texto entre por teclado, la máquina lo recibe como una secuencia de caracteres que hay que agrupar en unidades como palabras.

```python
import re

frase = "Pon el libro sobre la mesa"
tokens = re.findall(r"\w+", frase.lower())
print(tokens)   # ['pon', 'el', 'libro', 'sobre', 'la', 'mesa']
```

```r
frase <- "Pon el libro sobre la mesa"
tokens <- strsplit(tolower(frase), "\\s+")[[1]]
print(tokens)
```

(Herramientas más completas, como NLTK, se trabajan en la Unidad 5.)

### 2.3 Tipos de conocimiento lingüístico

1. **Fonético y fonológico:** cómo se relacionan las palabras con los sonidos.
2. **Morfológico:** cómo se construyen las palabras a partir de morfemas ("amigable" viene de "amigo"; singular/plural, tiempos verbales).
3. **Sintáctico:** cómo se combinan las palabras en oraciones correctas.
4. **Semántico:** el significado de palabras y oraciones.
5. **Pragmático:** cómo el contexto y las intenciones afectan la interpretación.
6. **De discurso:** cómo las oraciones anteriores influyen en la interpretación de las siguientes.
7. **Del mundo:** conocimiento general, como creencias y objetivos de otros en una conversación.

### 2.4 Ambigüedad

Las palabras tienen múltiples significados y las frases pueden estructurarse de más de una forma. Ejemplo del material (**ambigüedad estructural**):

- *"Pon el libro sobre la mesa"* → "sobre la mesa" indica *dónde* poner el libro.
- *"Pon el libro sobre la mesa en tu bolsillo"* → "el libro sobre la mesa" es el objeto: *cuál* libro, el que ya está sobre la mesa.

Las mismas palabras admiten **dos estructuras gramaticales válidas**; la gramática por sí sola no siempre puede decidir cuál es la correcta, y lo que desambigua es el contexto (lo que viene después).

### 2.5 Analizador sintáctico

Proceso de interpretación que asigna a cada oración su estructura sintáctica y su forma lógica, usando **reglas de gramática** y el **significado de las palabras (léxico)**.

---

## 3. Ejemplos de uso del PLN

| Sector | Aplicación mencionada |
|---|---|
| **Salud** | Amazon Comprehend Medical extrae información de registros electrónicos de salud e informes de ensayos clínicos; análisis del habla para detectar depresión, esquizofrenia o deterioro cognitivo (Winterlight Labs); Woebot (Stanford), chatbot de apoyo a personas con ansiedad |
| **Correo** | Yahoo y Google clasifican correos con PLN para filtrar spam |
| **Asistentes de voz** | Alexa, Cortana y Siri responden a indicaciones habladas |
| **Medios** | Sistema del MIT que evalúa si una fuente de noticias es precisa o está sesgada políticamente |
| **Finanzas** | Rastrear noticias e informes para alimentar algoritmos de trading |
| **Recursos humanos** | Búsqueda y selección de talento en reclutamiento |
| **Legal** | Automatización de tareas rutinarias en documentación jurídica |
| **Voz del cliente** | Analizar opiniones en reseñas, redes sociales y comentarios (p. ej., NPS) |

### 3.1 Ejemplo: filtro de spam con Naive Bayes

Combina conteo de palabras, probabilidad que se actualiza con evidencia (redes bayesianas, UD1) y clasificación supervisada.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

correos = [
    "gana dinero gratis ahora",
    "oferta gratis haz clic",
    "reunion de equipo manana",
    "adjunto el informe de ventas",
    "premio gratis reclama ya",
    "agenda de la reunion semanal"
]
etiquetas = [1, 1, 0, 0, 1, 0]  # 1 = spam, 0 = no spam

vec = CountVectorizer()
X = vec.fit_transform(correos)

modelo = MultinomialNB()
modelo.fit(X, etiquetas)

nuevo = vec.transform(["premio gratis"])
print("Probabilidad (no spam, spam):", modelo.predict_proba(nuevo))
```

Salida de referencia: aproximadamente `[0.10, 0.90]` (90 % de probabilidad de spam). En R, el equivalente es `naiveBayes()` del paquete `e1071`.

### 3.2 Errores en spam: falso positivo vs. falso negativo

En spam, la clase "positiva" es *spam*.

| Error | Qué ocurre | Costo típico | Métrica que lo cuida |
|---|---|---|---|
| **Falso positivo** | Un correo legítimo se marca como spam | Alto (se pierde un correo valioso) | **Precision** |
| **Falso negativo** | Un spam llega a la bandeja | Menor (molestia) | **Recall** |

### 3.3 Caso del material: falsos positivos en salud

El material relata que, analizando consultas en buscadores, se pudo identificar usuarios con cáncer de páncreas incluso antes del diagnóstico, y plantea cómo reaccionaría alguien ante ese aviso y qué pasaría si fuera un **falso positivo**. En aplicaciones sensibles el costo del error pesa tanto como la precisión; el PLN puede ser clave para el apoyo clínico, pero con desafíos pendientes.

---

## 4. Futuro del PLN

### 4.1 De reglas rígidas a modelos entrenados con datos

Antes dominaban los sistemas basados en reglas; hoy se imponen modelos entrenados con grandes volúmenes de datos, que ya no ven palabras aisladas sino que captan **intenciones, matices culturales, ironía y ambigüedad**, y mantienen coherencia en contextos extensos. Equivale al paso de la IA simbólica (UD3) al aprendizaje a partir de datos.

### 4.2 Líneas de desarrollo

1. **Comprensión semántica profunda**, centrada en el significado y no solo en la forma.
2. **Integración del lenguaje con otras modalidades:** imágenes, audio o datos estructurados.
3. **Adaptación a contextos culturales y lingüísticos específicos**, respetando variaciones regionales.

### 4.3 Personalización

Sistemas que se ajustan a distintos dominios, niveles de conocimiento y formas de expresión. Ejemplos del material: tutores virtuales que explican un concepto de distintas maneras según las dificultades detectadas, y sistemas que interpretan documentación técnica, contratos o informes con precisión creciente.

### 4.4 Desafíos: el lenguaje no es un recurso neutral

Los sistemas aprenden patrones de los datos con que se entrenan y pueden **repetir sesgos** presentes en ellos. El material subraya la necesidad de transparencia en el diseño y entrenamiento, evaluación cuidadosa, detección y reducción de sesgos, y atención a los riesgos de desinformación y exclusión. La conclusión es que la disciplina alcanzará avances significativos.

### 4.5 Demostración: un modelo hereda el sesgo de sus datos

Se entrena un clasificador de sentimiento con un dataset pequeño donde, por casualidad, "barato" solo aparece en reseñas negativas, y se comparan dos frases idénticas salvo por esa palabra.

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

resenas = [
    "excelente calidad muy bueno",
    "recomendado totalmente buen producto",
    "llego rapido excelente",
    "barato y malo se rompio",
    "barato mala calidad",
    "muy malo barato",
]
y = [1, 1, 1, 0, 0, 0]  # 1 = positivo, 0 = negativo

vec = CountVectorizer()
X = vec.fit_transform(resenas)
modelo = MultinomialNB().fit(X, y)

for texto in ["producto barato y funciona perfecto",
              "producto caro y funciona perfecto"]:
    p = modelo.predict_proba(vec.transform([texto]))[0]
    print(texto, "-> negativo=%.2f, positivo=%.2f" % (p[0], p[1]))
```

Resultado real al ejecutarlo:

| Frase | P(negativo) | P(positivo) |
|---|---|---|
| producto **barato** y funciona perfecto | 0.68 | 0.32 |
| producto **caro** y funciona perfecto | 0.34 | 0.66 |

La frase dice "funciona perfecto" en ambos casos, pero el modelo penaliza "barato" porque en sus datos esa palabra solo aparecía en reseñas negativas. No entiende qué significa "barato": repite la asociación que vio.

**Conexión con UD3 (dependencia de los datos):** el problema no es solo la cantidad de datos, sino su **calidad y representatividad**. Un millón de reseñas con el mismo sesgo daría el mismo error con más confianza. Mitigaciones: agregar ejemplos variados (incluyendo reseñas positivas con "barato"), revisar el dataset antes de entrenar (etapas de limpieza y transformación de KDD) y evaluar con datos no usados en el entrenamiento y con casos de prueba que cambien una sola palabra.

**Ejemplo aplicado (NPS):** quienes dejan comentarios suelen ser los muy satisfechos o los muy molestos, no una muestra de todos los clientes; aunque el modelo funcione bien, describiría solo a ese grupo. Conviene cruzar el texto con el puntaje numérico (estructurado) y revisar la representatividad.

---

## 5. Glosario de la unidad

| Término | Definición breve |
|---|---|
| **PLN** | Campo de la IA que permite a las máquinas leer, comprender y derivar significado del lenguaje humano |
| **Datos no estructurados** | Datos sin forma de filas y columnas (texto libre, voz) |
| **Bag of words** | Representación del texto como conteo de palabras |
| **Tokenización** | Dividir una entrada en unidades (tokens) procesables |
| **Análisis sintáctico / semántico / pragmático** | Niveles que estudian estructura gramatical / significado / significado en contexto |
| **Ambigüedad estructural** | Una misma secuencia de palabras admite varias estructuras gramaticales válidas |
| **Analizador sintáctico (parser)** | Proceso que asigna a una oración su estructura y su forma lógica |
| **Análisis intencional** | Tarea de reconocer la intención del usuario (base de los chatbots) |
| **Análisis de sentimientos** | Tarea de determinar el tono y la opinión en un texto |
| **Naive Bayes** | Clasificador probabilístico que asume independencia entre variables; usado en spam |
| **Falso positivo / falso negativo** | Error de marcar como positivo algo negativo / de no detectar un positivo real |
| **Sesgo heredado** | Prejuicio que un modelo aprende de los datos con los que se entrena |

---

## 6. Preguntas de repaso

1. ¿Por qué el texto libre se considera dato no estructurado y qué hay que hacer antes de aplicarle un algoritmo?
2. Nombra las 8 tareas del PLN y elige tres que aplicarías al análisis de comentarios de clientes.
3. ¿En qué nivel del PLN se queda el conteo de palabras y por qué falla con sinónimos e ironía?
4. ¿Por qué *"Pon el libro sobre la mesa en tu bolsillo"* ilustra la ambigüedad estructural?
5. En un filtro de spam, ¿qué error es más costoso, cómo se llama y qué métrica lo cuida?
6. ¿Cómo explica la dependencia de los datos que un modelo penalice la palabra "barato"? ¿Qué harías para corregirlo?
7. ¿Qué tres líneas de desarrollo marca el material para el futuro del PLN?

---

## 7. Referencias

- Material oficial de la Unidad 4 — Universidad DaVinci, asignatura Minería de Datos ("Introducción al PLN").
- Alpaydin, E. (2021). *Aprendizaje automático*. MIT Press.
- Bobadilla, J. (2021). *Aprendizaje automático y aprendizaje profundo: usando Python, Scikit y Keras*. Ediciones Zhou.
- **Complemento externo:** documentación de scikit-learn — [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) y [`MultinomialNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html).
