# 💬 Foro 2 — Estadística Inferencial

**Asignatura:** Análisis de Datos y Métodos Estadísticos  
**Semana:** S3 (Jun 2026)

---

## 📋 Preguntas

1. ¿Qué es la estadística inferencial?
2. ¿Cuál es la diferencia entre la estadística inferencial y la estadística descriptiva?
3. ¿Cuál es la importancia de la estadística inferencial en la Ciencia de Datos?
4. Menciona tres escenarios donde la estadística inferencial ha jugado un gran papel en la Ciencia de Datos.

---

## ✍️ Respuesta publicada

La estadística inferencial representa el puente entre los datos que podemos observar y las conclusiones que podemos extraer sobre fenómenos más amplios. Su dominio es fundamental para cualquier profesional que trabaje con datos, especialmente en ciencia de datos, donde el objetivo no es solo describir lo que ocurrió, sino entender y predecir lo que ocurre en general.

**¿Qué es la estadística inferencial?**

La estadística inferencial es la rama de la estadística que, a partir del estudio de una muestra representativa, permite generalizar conclusiones válidas sobre una población completa. Como establecen Gutiérrez González y Panteleeva (2016), la estadística inferencial constituye el proceso inverso al de la probabilidad: mientras que en probabilidad se conocen los parámetros de la distribución y se calculan probabilidades de valores particulares, en estadística inferencial se parte de las observaciones de la muestra para conocer cómo es la población y cuáles son sus parámetros.

**¿Cuál es la diferencia entre la estadística inferencial y la estadística descriptiva?**

La estadística descriptiva analiza, estudia y describe la totalidad de los individuos de una población o muestra mediante medidas de tendencia central, dispersión y forma, con el fin de resumir y comunicar las características de los datos disponibles. La estadística inferencial va un paso más allá: usa esos resúmenes descriptivos como punto de partida para hacer inferencias sobre una población más amplia. En palabras de Gutiérrez González y Panteleeva (2016), la estadística descriptiva permite tener un conocimiento intuitivo sobre el comportamiento de la población de forma descriptiva, mientras que la estadística inferencial permite aplicar métodos formales para estimar parámetros, construir intervalos de confianza y realizar pruebas de hipótesis. En la práctica, una no reemplaza a la otra: siempre se describe primero, luego se infiere.

**¿Cuál es la importancia de la estadística inferencial en la Ciencia de Datos?**

En ciencia de datos, rara vez se trabaja con la totalidad de los datos de una población. Los modelos se entrenan sobre muestras, las conclusiones se generalizan a nuevos datos, y las decisiones de negocio se toman con base en evidencia estadística limitada. La estadística inferencial provee las herramientas formales para hacerlo con rigor: pruebas de hipótesis para validar si un resultado es estadísticamente significativo, intervalos de confianza para acotar la incertidumbre, y el Teorema del Límite Central para justificar el uso de distribuciones normales incluso cuando los datos originales no lo son. Sin inferencia estadística, los hallazgos de un análisis de datos serían simplemente descripciones de una muestra, sin capacidad de generalización ni de soporte a la toma de decisiones.

**Tres escenarios donde la estadística inferencial ha jugado un gran papel**

El primer escenario es el **A/B testing en plataformas digitales**. Cuando una empresa quiere saber si una nueva funcionalidad mejora el comportamiento del usuario, expone a un grupo de control y un grupo de tratamiento, y aplica una prueba de hipótesis para determinar si la diferencia observada es estadísticamente significativa. He vivido este proceso directamente: en mi experiencia en una empresa de tecnología, esta metodología fue determinante para decidir si una inversión en un equipo de contacto externo generaba un impacto real en la tasa de activación de restaurantes, evitando decisiones basadas en intuición.

El segundo escenario es la **validación de modelos de machine learning**. Cuando se evalúa el desempeño de un modelo predictivo, la inferencia estadística permite construir intervalos de confianza alrededor de las métricas de desempeño y comparar modelos de forma rigurosa, garantizando que las diferencias observadas no sean producto del azar.

El tercer escenario es la **estimación de métricas de negocio con muestreo**. En grandes plataformas con millones de registros, calcular ciertas métricas sobre toda la población es computacionalmente costoso. El muestreo estadístico representativo permite obtener estimaciones precisas con una fracción del costo computacional, un principio que apliqué frecuentemente al trabajar con grandes volúmenes de datos en Snowflake.

---

## 📚 Referencias

Gutiérrez González, E., & Panteleeva, O. V. (2016). *Estadística inferencial 1 para ingeniería y ciencias*. Grupo Editorial Patria.
