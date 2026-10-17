# UD5 — PLN en Python (NLTK)

**Asignatura:** Minería de Datos
**Trimestre:** T3 — 2026 | Semana 5

---

## 📌 Resumen ejecutivo (repaso rápido de 30 segundos)

- El PLN en Python es un flujo tipo ETL: texto crudo → limpieza → tokens → *stop words* → *stemming* o lematización → vectores → modelo.
- **Bolsa de palabras (BoW):** cuenta palabras por documento e ignora el orden.
- **TF-IDF:** frecuencia en el documento × rareza en el corpus. Una palabra que está en todos los documentos pesa casi cero.
- **Stemming** corta terminaciones (rápido, puede dar raíces que no existen). **Lematización** devuelve el lema del diccionario (más precisa).
- Quitar *stop words* sin cuidado puede cambiar el sentido: las negaciones ("no", "nunca", "sin") deben protegerse.

---

## 🗺️ Ruta de estudio

1. De texto a números: el flujo completo
2. Limpieza y normalización: tokenización, *stop words*, regex, *stemming*/lematización
3. Bolsa de palabras
4. TF-IDF
5. Otras herramientas (Stanford CoreNLP, CSLU Toolkit, Visualtext)
6. Python, R y aplicación real

Continuación de UD4: allá se vio qué es el PLN (tareas y niveles); aquí se ve cómo se prepara el texto en código para que un modelo lo consuma.

---

## 1. El flujo completo

**En simple:** un modelo solo entiende números. Todo el PLN de esta unidad es una cadena de pasos que convierte "texto sucio" en una tabla numérica.

```
texto crudo → limpieza (regex) → tokenización → stop words → stemming/lematización → vectores (BoW / TF-IDF) → modelo
```

**Analogía de BI:** es un ETL. El texto es la fuente sucia, los pasos de limpieza son las transformaciones y la matriz documento-término es la tabla final lista para el modelo.

---

## 2. Limpieza y normalización

| Paso | Qué hace | Ejemplo |
|---|---|---|
| **Tokenización de oraciones** | Divide el texto en frases. Cuidado con puntos que no cierran frase (abreviaturas). | `sent_tokenize` |
| **Tokenización de palabras** | Divide en palabras. Separar por espacios no basta (puntuación pegada). | `word_tokenize` |
| **Stop words** | Quita palabras muy frecuentes y poco informativas ("el", "y", "la"). | `stopwords.words("spanish")` |
| **Regex** | Limpia o extrae patrones (quitar signos, extraer números, correos). | `re.sub(r"\W+", " ", t)` |
| **Stemming** | Corta sufijos con reglas: rápido, pero puede dar raíces que no son palabras. | *jugando → jug* |
| **Lematización** | Lleva la palabra a su forma del diccionario (lema), usando contexto. Más precisa, más lenta. | *mejor → bueno* |

**Técnico y rigor:**
- *Stemming* es heurístico (cortar terminaciones). Lematización es morfológico (diccionario + categoría gramatical).
- Con el conjunto (`set`) de stop words, la búsqueda cuesta O(1) frente a O(n) en una lista. Por eso el PDF convierte la lista a `set`.
- Resultados reales con NLTK (español): *jugando → jug*, *perros/perro → perr*, *nacional/nacionalidad → nacional*, *reunión → reunion*. En inglés (Porter): *studies → studi*, *happily → happili*, *university/universe → univers* (junta dos significados distintos).

⚠️ **Observaciones sobre el material (simplificaciones o erratas):**
- El PDF dice que las variables no pueden llevar acentos. En Python 3 sí pueden (los identificadores admiten Unicode); evitar acentos en nombres de variables es solo una buena práctica de portabilidad.
- El PDF define "Frecuencia de término inverso (ITF)". El nombre correcto es **IDF** (*inverse document frequency*).

⚠️ **[Complemento]** NLTK no trae lematizador en español (`WordNetLemmatizer` es solo para inglés). En proyectos en español se usa spaCy (`es_core_news_sm`).

---

## 3. Bolsa de palabras (Bag of Words)

**En simple:** cuentas cuántas veces aparece cada palabra del vocabulario en cada documento e ignoras el orden.

**Técnico:** se diseña un vocabulario de *k* palabras y cada documento se vuelve un vector de largo *k*. La matriz resultante (documentos × términos) suele ser muy dispersa (muchos ceros).

| | dañado | el | es | excelente | llegó | pedido | producto | rápido | tarde |
|---|---|---|---|---|---|---|---|---|---|
| "el pedido llegó tarde" | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| "el pedido llegó rápido" | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| "el producto es excelente" | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 |
| "el producto llegó dañado" | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |

⚠️ **Error común:** pensar que BoW entiende el significado. "El perro mordió al niño" y "el niño mordió al perro" dan el mismo vector: se pierde el orden. Los **bigramas** (`ngram_range=(1,2)`) recuperan algo de contexto.

---

## 4. TF-IDF

**En simple:** el conteo trata igual a "el" que a "dañado". TF-IDF premia las palabras frecuentes **en este documento** pero **raras en el resto**.

**Intuición → fórmula:**

```
TF-IDF(t, d) = TF(t, d) × IDF(t)        IDF(t) = ln( N / df(t) )
```

- **TF:** qué tan frecuente es el término *t* en el documento *d*.
- **IDF:** qué tan rara es la palabra en el corpus (*N* = número de documentos, df = en cuántos aparece).

**Ejemplo numérico:** con N = 4, "el" aparece en los 4 documentos → IDF = ln(4/4) = 0, aporta cero. "dañado" aparece en 1 → IDF = ln(4/1) ≈ 1,39, pesa mucho. Con `TfidfVectorizer`, "dañado" y "tarde" salen con ≈ 0,66 y "el" con ≈ 0,34.

⚠️ **Variante de librería:** `TfidfVectorizer` (scikit-learn) usa IDF suavizado, ln((1+N)/(1+df))+1, y normaliza cada fila a norma 1; por eso "el" no queda en cero. `bind_tf_idf` (tidytext, R) usa ln(N/df) sin suavizado ni normalización. Los números cambian entre librerías, la idea es la misma.

---

## 5. Otras herramientas (sección 2 del material)

- **Stanford CoreNLP:** suite en Java con tokenización, etiquetado gramatical (POS) y análisis sintáctico en varios idiomas, incluido español.
- **CSLU Toolkit:** orientado a procesamiento de voz y animación facial (educación e investigación).
- **Visualtext:** herramientas escritas en NLP++ para análisis profundo de texto y extracción de información; gratuito para uso no comercial.

---

## 6. Código en Python

> Las partes de scikit-learn, regex y *stemming* se ejecutaron y verificaron. Las llamadas que descargan datos de NLTK (`sent_tokenize`, `word_tokenize`, `stopwords`) no se pudieron ejecutar en el entorno de preparación (sin descarga de datos de NLTK): corre esa celda en Colab.

```python
import re, nltk
import pandas as pd
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Descargas únicas (en NLTK recientes 'punkt' se llama 'punkt_tab')
nltk.download("punkt"); nltk.download("punkt_tab")
nltk.download("stopwords"); nltk.download("wordnet")

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

texto = ("Mi pedido llegó tarde. El repartidor no contestó el teléfono. "
         "Pero la comida estaba excelente.")

# 1) Oraciones y palabras
oraciones = sent_tokenize(texto, language="spanish")
palabras  = word_tokenize(texto, language="spanish")

# 2) Limpieza con regex: minúsculas y quitar todo lo que no sea letra/número
limpio = re.sub(r"\W+", " ", texto.lower()).strip()

# 3) Stop words (set = búsqueda rápida)
vacias = set(stopwords.words("spanish"))
sin_vacias = [p for p in limpio.split() if p not in vacias]

# 4) Stemming en español
stem = SnowballStemmer("spanish")
raices = [stem.stem(p) for p in sin_vacias]
print(sin_vacias, raices, sep="\n")

# 5) BoW y TF-IDF con scikit-learn
docs = ["el pedido llegó tarde", "el pedido llegó rápido",
        "el producto es excelente", "el producto llegó dañado"]

bow = CountVectorizer()
M = bow.fit_transform(docs)
print(pd.DataFrame(M.toarray(), columns=bow.get_feature_names_out()))

tfidf = TfidfVectorizer()
T = tfidf.fit_transform(docs)
print(pd.DataFrame(T.toarray().round(2), columns=tfidf.get_feature_names_out()))
```

`CountVectorizer` ya pasa a minúsculas y descarta tokens de 1 carácter por defecto.

## 7. Código en R

> Sin probar (el entorno de preparación no tiene R). Revisar al ejecutar.

```r
library(tidyverse)
library(tidytext)
library(SnowballC)

docs <- tibble(
  id    = 1:4,
  texto = c("el pedido llegó tarde", "el pedido llegó rápido",
            "el producto es excelente", "el producto llegó dañado")
)

tokens <- docs |> unnest_tokens(palabra, texto)     # minúsculas + sin puntuación
bow    <- tokens |> count(id, palabra)              # bolsa de palabras
tfidf  <- bow |> bind_tf_idf(palabra, id, n)        # TF-IDF (ln(N/df), sin suavizado)

tokens |> mutate(raiz = wordStem(palabra, language = "spanish"))   # stemming
```

---

## 8. Aplicación real

**Caso:** reseñas de clientes de una app de domicilios.
- **Problema de negocio:** saber por qué baja la calificación y qué quejas se repiten.
- **Datos:** columna de comentarios en Snowflake.
- **Preparación:** regex, minúsculas, stop words (protegiendo negaciones), *stemming*; parte en SQL y parte en Python.
- **Modelo:** TF-IDF para hallar términos distintivos por categoría de queja; después un clasificador (Naive Bayes, UD4) para etiquetar reseñas nuevas.
- **Decisión:** los términos de mayor peso ("tarde", "frío", "incompleto") se muestran en Power BI y el negocio prioriza qué arreglar.
- **Error típico:** quitar "no" como stop word cambia por completo el sentido ("no llegó" → "llegó").

---

## 9. Preguntas de comprensión y correcciones

**1. "El servicio fue malo" vs "el servicio no fue malo": ¿qué problema aparece al quitar stop words y usar BoW?**
Respuesta del estudiante: queda "malo" en ambas; se evitaría con TF-IDF. → **Medio correcta.**
- Al quitar las stop words desaparece "no": las dos frases quedan como "servicio malo", aunque significan lo contrario.
- TF-IDF **no** lo arregla: solo cambia el peso de las palabras que quedan; si "no" ya se eliminó, ningún peso lo recupera.
- Solución: proteger las negaciones en la lista de stop words, o usar bigramas (`ngram_range=(1,2)`) para conservar "no fue" / "fue malo".

**2. Diferencia entre stemming y lematización.**
Respuesta: stemming es heurístico (corta terminaciones); lematización es la raíz de la palabra en diccionario. → **Correcta, con un matiz.**
- La lematización devuelve el **lema** (forma del diccionario, *mejor → bueno*), no una "raíz"; "raíz" es lo que produce el stemming.
- El ejemplo "drive → dri" **no es válido**: NLTK deja `drive` como `drive`. Ejemplos válidos: *studies → studi*, *happily → happili*, *university/universe → univers*, *jugando → jug*, *perros → perr*.

**3. Corpus de 1.000 reseñas: "pedido" en 980 y "reembolso" en 15. ¿Cuál tiene mayor IDF?**
Respuesta: reembolso. → **Correcta.**
- ln(1000/15) ≈ **4,2** frente a ln(1000/980) ≈ **0,02**.
- Matiz: lo que tiene puntuación alta es la **palabra** "reembolso" en las reseñas donde aparece (pista de una queja específica); "pedido" casi no pesa porque no distingue nada.
- ⚠️ Un IDF alto solo significa "rara": un error de tipeo que aparece una vez también tiene IDF máximo y no es información útil.

---

## 🧠 Lo que debes recordar

1. El PLN es un flujo tipo ETL: texto crudo → limpieza → tokens → stop words → stemming o lematización → vectores → modelo.
2. Quitar stop words sin pensar puede cambiar el sentido: protege las negaciones ("no", "nunca", "sin").
3. La bolsa de palabras cuenta palabras pero ignora el orden; los bigramas recuperan algo de contexto.
4. Stemming corta terminaciones y es rápido, pero puede dar raíces que no existen (*studi*, *jug*); la lematización devuelve el lema del diccionario y es más precisa.
5. NLTK no lematiza en español; para eso se usa spaCy.
6. TF-IDF = frecuencia en el documento × rareza en el corpus; una palabra presente en todos los documentos pesa casi cero.
7. Las librerías calculan TF-IDF con variantes distintas (scikit-learn suaviza y normaliza; tidytext no): los números cambian, la idea es la misma.

---

## 📚 Referencias

- Material oficial de la Unidad 5 — *PLN en Python*, Universidad DaVinci (LMS).
- Alpaydin, E. (2021). *Aprendizaje automático*. MIT Press. *(bibliografía de la asignatura; lectura complementaria)*
- Bobadilla, J. (2021). *Aprendizaje automático y aprendizaje profundo: usando Python, Scikit y Keras*. *(bibliografía de la asignatura; lectura complementaria)*
