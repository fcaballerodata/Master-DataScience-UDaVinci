# UD2 — Introducción a las Redes Neuronales Artificiales (RNA)

**Asignatura:** Fundamentos de Machine Learning
**Trimestre:** T3 — 2026 | Semana 2

---

## 📌 Resumen ejecutivo (repaso rápido de 30 segundos)

- Jerarquía: **IA ⊃ Machine Learning ⊃ RNA** (relación de contención, no sinónimos).
- Una RNA está inspirada en la neurona biológica: **entrada → suma ponderada → ¿supera umbral? → salida**.
- Componentes biológicos y su función: Dendritas (reciben) → Soma (suma) → Axón (transmite salida) → Sinapsis (conexión con "fuerza"/peso).
- Aplicaciones principales: visión por computadora (CNN), PLN (asistentes virtuales), autos autónomos.
- Las RNA son técnica de "caja negra": alta precisión, baja interpretabilidad (trade-off ya visto en Minería de Datos UD1).

---

## 1. Concepto clave

### 1.1 Jerarquía de conceptos

```
Inteligencia Artificial (IA)
   └── Machine Learning (ML) — subdisciplina de la IA
          └── Redes Neuronales Artificiales (RNA) — una técnica del ML
```

La **Inteligencia Artificial** es el campo de la informática dedicado al diseño de sistemas y algoritmos capaces de ejecutar tareas que, en condiciones normales, requerirían inteligencia humana. Dentro de la IA, el **aprendizaje automático (Machine Learning)** es la subdisciplina que desarrolla algoritmos que permiten a las máquinas aprender y mejorar su rendimiento a partir de la experiencia, sin ser explícitamente programadas para cada tarea específica.

Las **Redes Neuronales Artificiales** son sistemas computacionales inspirados en la estructura y funcionamiento del cerebro humano, diseñados para reconocer patrones y aprender de los datos. Son una de las técnicas más representativas del Machine Learning para el modelado y análisis de datos complejos.

> ⚠️ **Error común:** pensar que IA, ML y RNA son sinónimos intercambiables. No lo son — toda RNA es ML, todo ML es IA, pero **no al revés**. Hay ML sin RNA (regresión logística, K-Means, árboles de decisión — todos ya trabajados) y hay IA sin ML (sistemas expertos basados en reglas fijas escritas a mano, por ejemplo).

### 1.2 A diferencia de los sistemas tradicionales

Las RNA se adaptan y mejoran mediante entrenamiento con datos que se alimentan constantemente, ajustando su comportamiento para arrojar resultados más precisos en el contexto en el que operan — en contraste con sistemas tradicionales de reglas fijas, que no cambian su comportamiento sin intervención manual del programador.

---

## 2. El modelo biológico

### 2.1 Por qué se estudia primero la neurona real

El diseño de la RNA copia (de forma simplificada) la estructura y el mecanismo de la neurona biológica. Entender el modelo biológico es la base para comprender, en unidades posteriores (UD5, UD6, UD8), la estructura matemática de la RNA.

### 2.2 Los 4 componentes de la neurona biológica

| Componente | Función biológica | Equivalente conceptual en RNA |
|---|---|---|
| **Dendritas** | Árbol receptor: fibras nerviosas que cargan de señales eléctricas el cuerpo de la célula | Las entradas (*inputs*) del nodo |
| **Soma (cuerpo de la célula)** | Realiza la suma de las señales de entrada | La función de agregación (suma ponderada) del nodo |
| **Axón** | Fibra larga que lleva la señal desde el cuerpo de la célula hacia otras neuronas | La salida (*output*) hacia la siguiente capa |
| **Sinapsis** | Punto de contacto entre el axón de una célula y la dendrita de otra; su longitud/fuerza depende de la complejidad del proceso químico | La conexión entre nodos, con su **peso** asociado (valor numérico que se ajusta durante el entrenamiento) |

### 2.3 Cómo se transmite la información

- La información viaja a lo largo de los axones en breves impulsos eléctricos llamados **potenciales de acción** (hasta ~100 mV, duran un par de ms).
- Se producen por el desplazamiento de iones de sodio (carga positiva) hacia el interior de la célula, seguido de un desplazamiento de iones de potasio (carga negativa) hacia el exterior.
- Los potenciales de acción **no saltan de una célula a otra** — la comunicación entre neuronas siempre está mediada por **neurotransmisores** químicos liberados en las sinapsis.

### 2.4 Dos tipos de sinapsis

| Tipo | Efecto |
|---|---|
| **Sinapsis excitadoras** | Sus neurotransmisores provocan disminuciones de potencial en la membrana de la célula postsináptica, **facilitando** la generación de impulsos |
| **Sinapsis inhibidoras** | Sus neurotransmisores **estabilizan** el potencial de membrana, **dificultando** la emisión de impulsos |

### 2.5 El mecanismo de activación (la pieza clave)

La neurona recibe impulsos amplificados (excitadores) o atenuados (inhibidores). **La suma de estos impulsos en el cuerpo de la célula determina si la neurona se activa o no**, dependiendo de si esa suma supera el **valor de umbral** de generación del potencial de acción.

> 💡 **Idea clave — el patrón que hereda toda RNA:**
> **entrada(s) → suma ponderada (excitación − inhibición) → ¿supera el umbral? → se activa / no se activa → salida**
>
> No es necesario memorizar los nombres biológicos en sí — lo que hay que interiorizar es este patrón matemático, porque es exactamente el mecanismo que usará cada neurona artificial (con función de activación) en las unidades 5, 7 y 8.

---

## 3. Aplicaciones de las RNA

Impulsadas por mejoras en capacidad de cómputo, disponibilidad de grandes volúmenes de datos, y arquitecturas más sofisticadas (redes convolucionales, recurrentes), las RNA se aplican en:

| Aplicación | Ejemplo concreto | Variante de RNA mencionada |
|---|---|---|
| **Visión por computadora** | Sistemas de seguridad: detección de objetos, reconocimiento facial | Redes Neuronales Convolucionales (CNN) |
| **Procesamiento del Lenguaje Natural (PLN)** | Asistentes virtuales (Siri, Alexa) — entender y responder consultas | — |
| **Automóviles autónomos** | Tesla, Waymo — procesan datos de sensores/cámaras para decisiones de conducción en tiempo real | — |

Estas mismas aplicaciones se mencionaron en Minería de Datos UD1 (Bloque 4: Áreas de aplicación) — la diferencia es que ahora se conoce específicamente **qué técnica** hay detrás de muchas de ellas.

---

## 4. Conexión con el trade-off precisión/interpretabilidad (Minería de Datos UD1)

| Técnica | Interpretabilidad |
|---|---|
| Redes Neuronales | Baja ("caja negra") |
| Árboles de Decisión | Alta |

Las RNA son la técnica "caja negra" por excelencia: alta capacidad de resolver problemas complejos, pero baja capacidad de explicar *por qué* llegó a una decisión concreta. Esto es relevante en contextos regulados o de alto riesgo (médico, financiero, legal) donde la trazabilidad de la decisión puede pesar más que unos puntos extra de precisión.

---

## 5. Ejemplos de código ejecutable

**Nota:** el detalle matemático de cómo se construye y entrena una RNA se profundiza en las unidades 5 (Fundamentos), 6 (Mecanismo de aprendizaje) y 8 (El perceptrón). El ejemplo de esta unidad es intencionalmente introductorio: mostrar el patrón "entrada → pesos → suma → activación" funcionando en código real, con un problema de negocio conocido (clasificación de clientes VIP, ya trabajado en UD1 vía RFM).

### Python

```python
import numpy as np
from sklearn.neural_network import MLPClassifier

# Datos: gasto_mensual (miles), frecuencia_compras
X = np.array([
    [5, 2], [1, 1], [8, 6], [2, 1], [9, 7], [1, 2], [7, 5], [3, 1]
])
y = np.array([0, 0, 1, 0, 1, 0, 1, 0])  # 1 = candidato VIP

# hidden_layer_sizes=(4,) -> una capa oculta con 4 neuronas artificiales
modelo = MLPClassifier(hidden_layer_sizes=(4,), max_iter=2000, random_state=42)
modelo.fit(X, y)

nuevo_cliente = [[6, 4]]
print("¿Candidato VIP?", modelo.predict(nuevo_cliente))
print("Pesos entrada -> capa oculta:\n", modelo.coefs_[0])
```

`modelo.coefs_[0]` expone explícitamente los **pesos** aprendidos entre la capa de entrada y la capa oculta — es la traducción numérica directa de la "fuerza de la sinapsis" que vimos en el modelo biológico.

### R

```r
library(nnet)

datos <- data.frame(
  gasto_mensual = c(5, 1, 8, 2, 9, 1, 7, 3),
  frecuencia    = c(2, 1, 6, 1, 7, 2, 5, 1),
  vip           = as.factor(c(0, 0, 1, 0, 1, 0, 1, 0))
)

# size = 4 -> 4 neuronas en la capa oculta (equivalente a hidden_layer_sizes)
modelo <- nnet(vip ~ gasto_mensual + frecuencia, data = datos, size = 4, maxit = 2000)

nuevo_cliente <- data.frame(gasto_mensual = 6, frecuencia = 4)
predict(modelo, nuevo_cliente, type = "class")

# Ver los pesos aprendidos
summary(modelo)
```

---

## 6. Glosario de la unidad

| Término | Definición breve |
|---|---|
| **Inteligencia Artificial (IA)** | Campo de la informática dedicado a sistemas que ejecutan tareas que normalmente requieren inteligencia humana |
| **Machine Learning (ML)** | Subdisciplina de la IA: algoritmos que aprenden de la experiencia sin ser programados explícitamente para cada tarea |
| **Red Neuronal Artificial (RNA)** | Técnica de ML inspirada en el cerebro humano, compuesta por nodos interconectados en capas |
| **Dendritas** | Estructura receptora de la neurona — equivalente a las entradas de un nodo artificial |
| **Soma** | Cuerpo celular que suma las señales de entrada |
| **Axón** | Fibra que transmite la señal de salida hacia otras neuronas |
| **Sinapsis** | Punto de conexión entre neuronas — equivalente al peso en una RNA |
| **Potencial de acción** | Impulso eléctrico que viaja por el axón cuando se supera el umbral de activación |
| **Neurotransmisores** | Sustancias químicas que median la comunicación entre neuronas en la sinapsis |
| **Sinapsis excitadora / inhibidora** | Facilita / dificulta la generación de impulsos |
| **CNN (Red Neuronal Convolucional)** | Variante de RNA especializada en visión por computadora |

---

## 7. Preguntas de repaso

1. ¿Cuál es la relación jerárquica entre IA, ML y RNA? Da un ejemplo de ML que **no** use RNA.
2. Describe, en tus propias palabras, el mecanismo completo por el cual una neurona biológica decide "activarse" o no.
3. ¿Qué componente biológico es el equivalente conceptual del "peso" en una RNA, y por qué?
4. Nombra 3 aplicaciones reales de las RNA y la variante de red mencionada para cada una.
5. ¿Por qué las RNA se consideran técnicas de "caja negra", y en qué tipo de contexto de negocio esto puede ser una desventaja crítica?

---

## 8. Referencias

- Material oficial de la Unidad 2 — Universidad DaVinci, asignatura Fundamentos de Machine Learning.
- Bibliografía oficial de la asignatura (Universidad DaVinci): Burkov, A.; Géron, A.; Müller, A. C. & Guido, S.; Kelleher, J. D. et al.
- **Complemento externo:** documentación oficial de [scikit-learn — `MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html) y del paquete [`nnet` de R](https://cran.r-project.org/web/packages/nnet/nnet.pdf), para quien quiera profundizar en los parámetros usados en los ejemplos de código.
