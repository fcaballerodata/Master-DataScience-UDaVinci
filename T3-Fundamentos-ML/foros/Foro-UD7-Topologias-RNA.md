# Foro 2 — Topologías en redes neuronales artificiales

> Respuesta publicada en el campus (Fundamentos de Machine Learning, Semana 7).
> **Rúbrica:** formato estructurado 30 % · APA 7 20 % · gramática y ortografía 20 % · redacción 20 % · cita de al menos 4 elementos de contenidos o recursos 10 %.

**Enunciado:** Las Redes Neuronales Artificiales (RNA) pueden adoptar diferentes topologías, como redes monocapa y multicapa, así como redes heteroasociativas y autoasociativas, e incluso redes estocásticas.

---

## Introducción

La topología de una red neuronal artificial (RNA) es la forma en que se organizan y conectan sus neuronas, y de ella depende qué tipo de problema puede resolver (Universidad DaVinci, s. f., introducción). A continuación respondo las dos preguntas del foro.

## ¿Cómo influye cada una de estas topologías en el rendimiento y la aplicabilidad de las RNA?

**Redes monocapa.** Tienen una sola capa de neuronas que conecta la entrada con la salida, sin capas ocultas. Son simples y adecuadas para problemas lineales, pero tienen limitaciones cuando el problema es más complejo (Universidad DaVinci, s. f., sección 1.1).

**Redes multicapa.** Incluyen una o más capas ocultas entre la entrada y la salida. Cada capa procesa la información antes de pasarla a la siguiente, lo que permite modelar relaciones no lineales y tareas como el reconocimiento de patrones, la clasificación y la predicción (Universidad DaVinci, s. f., sección 1.1).

**Redes heteroasociativas.** Relacionan patrones de entrada con patrones de salida distintos. Se entrenan ajustando los pesos para reducir la diferencia entre la salida deseada y la obtenida. Se aplican en sistemas de recomendación y en traducción automática (Universidad DaVinci, s. f., sección 1.2).

**Redes autoasociativas.** Reconstruyen su propia entrada, por lo que su capa de salida tiene el mismo tamaño que la de entrada. Al hacerlo aprenden una representación interna de los datos, útil en compresión, reducción de dimensionalidad y detección de anomalías (Universidad DaVinci, s. f., sección 1.2).

**Redes estocásticas.** Incorporan aleatoriedad y modelos probabilísticos, lo que les permite manejar datos con ruido o incertidumbre y generar muestras nuevas (Universidad DaVinci, s. f., sección 1.3).

En resumen, la topología marca el alcance de la red. Una muy simple no aprende problemas complejos, y una muy compleja agrega costo de diseño y entrenamiento cuando no hace falta. Por eso elegir bien la arquitectura ayuda a evitar errores de diseño y a optimizar el rendimiento (Universidad DaVinci, s. f., sección 1).

## ¿Podrían compartir ejemplos específicos donde una topología sea más ventajosa que otra y explicar por qué?

**1. Monocapa: costo de envío según el peso del paquete.** A más kilos, más costo, y el aumento es casi constante. Una sola recta describe bien esa relación, así que una red monocapa es suficiente. Usar algo más complejo no mejoraría el resultado y sería más difícil de explicar y entrenar.
*Para recordar:* si el problema se resuelve con una línea recta, usa monocapa.

**2. Multicapa: saber si una temperatura es agradable.** Con 5 °C el clima no es agradable (muy frío), con 22 °C sí, y con 40 °C no (muy caluroso). La respuesta sube y luego baja, y una sola línea recta no puede representarlo: si dice "sí" para los valores altos, también lo diría para los 40 °C. Con una capa oculta, una neurona aprende "demasiado frío", otra aprende "demasiado calor", y la salida las combina: es agradable si no es ninguna de las dos.
*Para recordar:* cuando una sola variable o una combinación de variables no se explica con una recta, usa multicapa.

**3. Heteroasociativa: sugerir un producto en una tienda.** Si el cliente compró pan y leche, la red sugiere huevos. La entrada (lo comprado) y la salida (lo sugerido) son cosas distintas.
*Para recordar:* si quieres pasar de "A" a un "B" diferente, usa heteroasociativa.

**4. Autoasociativa: detectar un gasto raro en una tarjeta.** Se entrena la red con gastos normales de un cliente para que aprenda a "copiarlos". Es como aprender a copiar una firma de memoria. Cuando llega una compra muy distinta a las habituales, la red la copia mal, es decir, el error de reconstrucción es alto, y eso genera una alerta. No hay una "respuesta correcta" que predecir; solo se necesita saber qué es lo normal.
*Para recordar:* si quieres encontrar lo que se sale de lo normal, usa autoasociativa.

**5. Estocástica: pronosticar las ventas de mañana.** Las ventas diarias cambian por muchos factores impredecibles, como el clima o un festivo. En lugar de decir "se venderán 100 unidades", una red estocástica puede dar un rango probable, por ejemplo entre 80 y 120, porque su salida incluye variación. Eso ayuda a planear inventario con más seguridad.
*Para recordar:* si los datos tienen ruido o necesitas medir la incertidumbre, usa estocástica.

## Cierre

No existe una topología mejor que las demás: la adecuada depende del problema. Para relaciones rectas, la monocapa; para relaciones complejas, la multicapa; para relacionar entradas con salidas distintas, la heteroasociativa; para reconstruir y detectar lo atípico, la autoasociativa; y para ruido e incertidumbre, la estocástica.

## Referencias

Universidad DaVinci. (s. f.). *Topologías de las RNA* [Guía académica, Unidad 7]. Fundamentos de Machine Learning. LMS UDaVinci. https://lms.udavinci.edu.mx
