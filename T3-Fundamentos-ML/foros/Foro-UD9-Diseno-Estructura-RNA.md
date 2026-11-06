# Foro 3 — Diseño y estructura en redes neuronales artificiales

> **Estado:** borrador preparado para el campus (Fundamentos de Machine Learning, Semana 9). Ajustar este archivo al texto final publicado.
> **Rúbrica:** formato estructurado 30 % · APA 7 20 % · gramática y ortografía 20 % · redacción 20 % · cita de al menos 4 elementos de contenidos o recursos 10 %.

**Enunciado:** La construcción efectiva de una Red Neuronal Artificial implica una cuidadosa consideración de los tipos de datos, la topología y el diseño de la estructura.

---

Construir una Red Neuronal Artificial (RNA) no consiste en elegir la red más grande. Consiste en decidir sobre los datos, la topología y la estructura, y comprobar esas decisiones con validación (Universidad DaVinci, s. f.). Para explicarlo uso un ejemplo sencillo: predecir qué clientes van a cancelar un servicio (*churn*).

## ¿Cómo se puede determinar la topología óptima de una RNA en función de diferentes tipos de datos y objetivos de aprendizaje?

No existe una topología óptima universal. Se elige según el tipo de dato y el objetivo, y luego se confirma probando. La guía de la unidad propone considerar la naturaleza del problema, la cantidad de datos, los recursos computacionales, la interpretabilidad y la validación cruzada (Universidad DaVinci, s. f.).

- **Datos tabulares** (clientes con monto, frecuencia y canal): una red *feedforward* (Goodfellow et al., 2016, cap. 6).
- **Series de tiempo** (ventas por día): una red recurrente, porque el orden importa (Goodfellow et al., 2016, cap. 10; LeCun et al., 2015).
- **Imágenes:** una red convolucional (Goodfellow et al., 2016, cap. 9; LeCun et al., 2015).
- **Texto:** primero se convierte en números, por ejemplo con *embeddings* (Universidad DaVinci, s. f.).

El objetivo también define la salida. Interactive Chaos (s. f.) indica que la capa de salida tiene una o más neuronas según sea clasificación o regresión. En el churn, una sola neurona de salida entrega la probabilidad de que el cliente cancele.

Antes de entrenar, los datos deben ser numéricos: se estandarizan las variables numéricas, se codifican las categóricas y se conserva el orden en las ordinales (Universidad DaVinci, s. f.).

## Además, discutan cómo el diseño de la estructura, incluyendo la configuración de las capas y el número de neuronas, impacta en la capacidad de la red para aprender y generalizar.

Las capas y las neuronas determinan la **capacidad** de la red. Interactive Chaos (s. f.) señala que el número de capas ocultas varía según el objetivo. En teoría, una red con una capa oculta y suficientes neuronas puede aproximar funciones muy generales (Hornik et al., 1989), pero eso no garantiza que generalice bien con datos nuevos.

Con poca capacidad, la red no capta patrones complejos. Con demasiada, memoriza el entrenamiento y falla con datos que no vio; es el sobreajuste, un problema serio en redes grandes (Srivastava et al., 2014). Por eso la guía incluye la regularización como parte del diseño (Universidad DaVinci, s. f.).

**Ejemplo de churn.** Probé este caso con 4.000 clientes simulados (21 % cancelaban):
- Una red muy grande (3 capas de 128 neuronas) acertó 89,5 % en entrenamiento, pero solo 82,8 % en prueba: memorizaba.
- Una red intermedia (capas de 32 y 16 neuronas) tuvo la mejor validación (0,651 frente a 0,575 de la red grande y de la línea base logística).
- Al regularizar la red grande, su validación subió de 0,575 a 0,672.
- Sin estandarizar los datos, el desempeño cayó de 0,626 a 0,302.

*(Datos simulados y resultados de mi prueba; no son un estudio publicado. Código: [`construccion_rna.py`](../codigo/construccion_rna.py).)*

## Conclusión

La topología se elige según los datos y el objetivo, y la estructura se ajusta buscando equilibrio. Conviene empezar con un modelo simple, crecer solo si la validación mejora y vigilar la diferencia entre entrenamiento y prueba.

## Referencias

Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT Press.

Hornik, K., Stinchcombe, M. B., & White, H. (1989). Multilayer feedforward networks are universal approximators. *Neural Networks, 2*(5), 359–366.

Interactive Chaos. (s. f.). *Estructura de una red neuronal*. https://interactivechaos.com/es/manual/tutorial-de-machine-learning/estructura-de-una-red-neuronal

LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. *Nature, 521*(7553), 436–444. https://doi.org/10.1038/nature14539

Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R. (2014). Dropout: A simple way to prevent neural networks from overfitting. *Journal of Machine Learning Research, 15*(56), 1929–1958. https://jmlr.org/papers/v15/srivastava14a.html

Universidad DaVinci. (s. f.). *Construcción de una RNA* [Guía académica, Unidad 9]. Fundamentos de Machine Learning. LMS UDaVinci.
