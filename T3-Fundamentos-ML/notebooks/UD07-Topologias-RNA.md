# UD07 · Topologías de las RNA — Fundamentos de Machine Learning (T3)

> **Fuentes:** guía académica de la unidad (10 pp.), listado de Recursos y Bibliografía de la asignatura, y fuentes académicas verificadas (sección Referencias).
> **Convención:** **[guía]** = sale de la guía · **[complemento]** = fuente externa o práctica habitual · **[propio]** = prueba que ejecuté yo.
> **Nota:** de los Recursos de la unidad solo revisé los resúmenes del listado, no su contenido completo.

---

## 1. Resumen ejecutivo

- **Topología** = cómo se organizan y conectan las neuronas: capas, neuronas por capa y conexiones. Determina para qué tareas sirve la red **[guía]**.
- **Monocapa:** solo problemas lineales. **Multicapa:** capas ocultas, relaciones no lineales.
- **Heteroasociativa:** entrada → salida distinta. **Autoasociativa:** reconstruye su propia entrada.
- **Estocástica:** aleatoriedad y modelos probabilísticos para ruido e incertidumbre.
- Elegir bien la topología evita errores de diseño y mejora el rendimiento **[guía]**.

## 2. Ruta de estudio
1. Qué es una topología → 2. Monocapa vs multicapa → 3. Hetero vs autoasociativa → 4. Estocásticas → 5. Código → 6. Aplicación a BI → 7. Preguntas → 8. Foro

## 3. Las topologías

### 3.1 Monocapa y multicapa **[guía]**
- **Monocapa:** una sola capa de neuronas conecta la entrada con la salida, sin capas ocultas; sirve para problemas lineales simples.
- **Multicapa:** una o más capas ocultas; cada una procesa la información antes de pasarla; modelan relaciones no lineales (reconocimiento de patrones, clasificación, predicción).

🟢 **Simple:** una monocapa traza **una recta**; las capas ocultas combinan varias rectas para dibujar curvas.
🔵 **Técnico:** el ejemplo clásico es **XOR**: los puntos (0,0) y (1,1) son de una clase y (0,1) y (1,0) de la otra, y ninguna recta los separa.
💡 **BI:** relación casi lineal (peso del paquete → costo de envío) = monocapa. Relación que sube y luego baja (temperatura "agradable": ni muy fría ni muy caliente) = multicapa.

### 3.2 Heteroasociativas y autoasociativas **[guía]**

| | Heteroasociativa | Autoasociativa |
|---|---|---|
| Idea | Asocia entradas con salidas **distintas** | Reconstruye **su propia entrada** |
| Estructura | Capa de entrada y de salida | Entrada, una o varias capas ocultas y salida **del mismo tamaño que la entrada** |
| Entrenamiento | Minimiza la diferencia entre salida deseada y obtenida | Minimiza la diferencia entre entrada y reconstrucción |
| Usos | Recomendación, traducción automática | Compresión, reducción de dimensionalidad, detección de anomalías |

- Hinton y Salakhutdinov (2006) entrenaron redes multicapa con una capa central pequeña para convertir datos de alta dimensión en códigos de baja dimensión, y mostraron que superaban al análisis de componentes principales en esa tarea **[complemento]**.
- **Detección de anomalías:** se entrena con datos normales; lo que se reconstruye mal (error alto) es sospechoso.

### 3.3 Estocásticas **[guía]**
Introducen aleatoriedad en el entrenamiento y en la salida, con modelos probabilísticos. Útiles con datos ruidosos, series temporales y generación de muestras.
- **[complemento]** El ejemplo clásico son las **máquinas de Boltzmann**, donde cada unidad adopta su estado como función probabilística de las unidades vecinas y de los pesos de sus conexiones (Ackley et al., 1985).
- **[complemento]** No confundir con *dropout* o con barajar los datos: son trucos de entrenamiento y no hacen estocástica a la red.

## 4. Python (ejecutado) **[propio]**

```python
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier, MLPRegressor, BernoulliRBM
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.datasets import load_digits

# Monocapa vs multicapa en XOR
X = np.array([[0,0],[0,1],[1,0],[1,1]]); y = np.array([0,1,1,0])
print(Perceptron(max_iter=1000, random_state=0).fit(X,y).score(X,y))          # 0.5
m = MLPClassifier(hidden_layer_sizes=(4,), activation="tanh",
                  solver="lbfgs", max_iter=2000, random_state=1).fit(X,y)
print(m.score(X,y))                                                           # 1.0

# Autoasociativa: reconstruye su entrada con un cuello de botella de 3 neuronas
rng = np.random.default_rng(42); n = 1000
a = rng.normal(size=(n,2))
Z = np.c_[a, a@[[1,.5],[.2,1]] + rng.normal(0,.1,(n,2)), a[:,0]-a[:,1] + rng.normal(0,.1,n)]
Zs = StandardScaler().fit_transform(Z)
ae = MLPRegressor(hidden_layer_sizes=(3,), max_iter=3000, random_state=0).fit(Zs, Zs)
err = lambda M: ((M - ae.predict(M))**2).mean(1)
umbral = np.quantile(err(Zs), .99)
an = Zs[:20].copy(); an[:,2] += 6                 # rompe la relación entre variables
print((err(an) > umbral).sum(), "/ 20")           # 20 / 20

# Estocástica: la RBM da salidas distintas con la misma entrada
Xd = MinMaxScaler().fit_transform(load_digits().data)
rbm = BernoulliRBM(n_components=16, learning_rate=.05, n_iter=10, random_state=0).fit(Xd)
print([rbm.gibbs(Xd[:1]).sum() for _ in range(3)])   # p. ej. [22, 17, 20]
```

| Prueba | Resultado |
|---|---|
| Monocapa en XOR | **0.5** (azar) |
| Multicapa (4 neuronas ocultas) en XOR | **1.0** |
| Error medio de reconstrucción (datos normales) | 0.0316 |
| Umbral (percentil 99) | 0.6874 |
| Anomalías detectadas | **20 de 20** |
| RBM, misma entrada, 3 muestreos | sumas 22, 17 y 20 (resultados distintos) |

**Lectura:** los datos son sintéticos (5 variables con solo 2 grados de libertad reales); es una demostración del mecanismo y no evidencia de rendimiento real. El autoencoder aprendió la estructura con 3 neuronas y una fila alterada se reconstruye mal.

## 5. R (no probado, R no está disponible en mi entorno)

```r
library(nnet)
d <- data.frame(x1=c(0,0,1,1), x2=c(0,1,0,1), y=factor(c(0,1,1,0)))
set.seed(1)
m <- nnet(y ~ x1 + x2, data=d, size=4, maxit=2000, trace=FALSE)
table(predict(m, d, type="class"), d$y)
```

## 6. Aplicación real (BI) y cuándo usar cada una

| Si el problema es… | Topología | Ejemplo sencillo |
|---|---|---|
| Relación recta | Monocapa | Costo de envío según el peso del paquete |
| Relación que se curva o combina variables | Multicapa | ¿Es agradable esta temperatura? |
| Pasar de "A" a un "B" distinto | Heteroasociativa | Pan y leche → sugerir huevos |
| Detectar lo que se sale de lo normal | Autoasociativa | Gasto raro en una tarjeta |
| Datos con ruido o necesidad de medir incertidumbre | Estocástica | Pronóstico de ventas como rango (80–120) |

## 7. Dos puntos a tener en cuenta de la guía
1. Presenta las redes estocásticas frente a "las tradicionales, generalmente deterministas": es una simplificación válida para el curso.
2. No incluye fórmulas ni entrena nada: las bases (pesos, activación, retropropagación) hay que buscarlas en los Recursos o en la bibliografía.

## 8. Preguntas de comprensión (respuestas modelo)
*A petición, las respuestas las redacté yo; reescríbelas con tus palabras antes de usarlas.*

**1. ¿Por qué una monocapa no resuelve XOR y una multicapa sí?** Una monocapa traza una sola recta; en XOR las clases están en diagonal y ninguna recta las separa (0.5). La capa oculta combina varias rectas y permite fronteras no lineales (1.0 con 4 neuronas ocultas).

**2. Hetero vs autoasociativa, y detección de anomalías.** La heteroasociativa relaciona entradas con salidas distintas (perfil del cliente → producto). La autoasociativa reconstruye su entrada (salida del mismo tamaño). Para anomalías se entrena solo con datos normales, se fija un umbral de error de reconstrucción (por ejemplo, el percentil 99) y lo que lo supera se marca como sospechoso (20 de 20 en la demo).

**3. Qué aporta una red estocástica.** Aleatoriedad y modelos probabilísticos: representa incertidumbre, genera muestras y soporta datos ruidosos. Se elige con ruido o cuando se necesitan escenarios; si se exige reproducibilidad exacta, se fijan semillas o se usa una determinista.

## 🧠 Lo que debes recordar
1. **Topología** = el plano de la red; define para qué sirve.
2. **Monocapa** = sin capas ocultas, solo problemas lineales. **Multicapa** = capas ocultas, no linealidad.
3. **XOR:** monocapa 0.5, multicapa 1.0.
4. **Heteroasociativa:** entrada → salida distinta. **Autoasociativa:** reconstruye su entrada; sirve para compresión, dimensionalidad y **anomalías**.
5. **Estocástica:** aleatoriedad y probabilidad; útil con ruido e incertidumbre.
6. Ejemplos clásicos de estocásticas (Boltzmann, RBM) no están en la guía: citar con fuente.
7. La mejor topología depende del problema, no hay una "mejor" en abstracto.

## Referencias (APA 7)

Ackley, D. H., Hinton, G. E., & Sejnowski, T. J. (1985). A learning algorithm for Boltzmann machines. *Cognitive Science, 9*(1), 147–169.

Hinton, G. E., & Salakhutdinov, R. R. (2006). Reducing the dimensionality of data with neural networks. *Science, 313*(5786), 504–507. https://doi.org/10.1126/science.1127647

Universidad DaVinci. (s. f.). *Topologías de las RNA* [Guía académica, Unidad 7]. Fundamentos de Machine Learning. LMS UDaVinci. https://lms.udavinci.edu.mx

*Bibliografía de la asignatura para ampliar (no leída en esta sesión):* Burkov (2019); Géron (2023); Guido & Müller (2016); Kelleher et al. (2015); Krizhevsky et al. (2012).

> **Verificación:** confirmé autores, año, revista, volumen y páginas de Ackley et al. y Hinton & Salakhutdinov. De la RBM de scikit-learn solo comprobé el comportamiento ejecutándola.
