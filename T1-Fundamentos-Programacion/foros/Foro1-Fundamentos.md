# 💬 Foro I — Fundamentos de Programación

**Asignatura:** Fundamentos de Programación (JavaScript) · T1 S2

---

## 📋 Preguntas

1. ¿Qué es un lenguaje de programación y para qué sirve?
2. ¿Cuál es la diferencia entre lenguaje compilado e interpretado?
3. ¿Por qué JavaScript es relevante en el desarrollo web actual?
4. Describe una situación real donde la programación resolvería un problema en tu área de trabajo.

---

## ✍️ Respuesta publicada

La programación es, en esencia, la capacidad de comunicarle instrucciones precisas a una máquina para que realice tareas que de otro modo requerirían intervención humana repetitiva. Para quienes trabajamos con datos, comprender sus fundamentos no es opcional — es la base sobre la que se construyen las automatizaciones, los pipelines y los modelos que generan valor real.

**¿Qué es un lenguaje de programación y para qué sirve?**

Un lenguaje de programación es un sistema formal de notación que permite expresar algoritmos y procesos computacionales de manera que una máquina pueda interpretarlos y ejecutarlos. Sirve como puente entre el pensamiento humano y la lógica binaria de los procesadores. Según Haverbeke (2018), la programación es fundamentalmente el arte de construir y controlar la complejidad, dotando a las máquinas de instrucciones que transforman entradas en salidas de manera predecible y reproducible.

**¿Cuál es la diferencia entre lenguaje compilado e interpretado?**

Un lenguaje compilado (como C o C++) traduce el código fuente completo a código máquina antes de ejecutarlo, generando un ejecutable optimizado. Un lenguaje interpretado (como JavaScript o Python) traduce y ejecuta el código línea por línea en tiempo real, sin generar un ejecutable previo. La diferencia práctica es que los compilados suelen ser más rápidos en ejecución, mientras que los interpretados ofrecen mayor flexibilidad y rapidez de desarrollo. JavaScript es interpretado por los motores de los navegadores (V8 en Chrome, SpiderMonkey en Firefox), lo que permite su ejecución directa sin pasos previos de compilación.

**¿Por qué JavaScript es relevante en el desarrollo web actual?**

JavaScript es el único lenguaje que los navegadores ejecutan de forma nativa en el cliente, lo que lo convierte en el estándar indiscutible para la interactividad web. Su relevancia se ha multiplicado con Node.js, que lleva JS al servidor, y con ecosistemas como React y Vue para interfaces, convirtiéndolo en un lenguaje full-stack. MDN Web Docs (2024) lo describe como el lenguaje de scripting de la web, fundamental para crear páginas web interactivas y que hoy es parte esencial de la mayoría de sitios y aplicaciones.

**Escenario real: automatización de reportes en Movet**

En mi rol como BI Analyst en Movet, una de las tareas más repetitivas era la generación semanal de reportes de consultas por sede. El proceso manual implicaba exportar datos de Snowflake, transformarlos en Excel y enviarlos por correo. Con programación, ese flujo completo se automatizó: un script Python extraía los datos vía API, los transformaba con pandas y enviaba el reporte automáticamente cada lunes. Lo que tomaba 2 horas se redujo a 0 intervención humana. Este es exactamente el tipo de problema que la programación resuelve: tareas repetitivas, predecibles y basadas en reglas.

---

## 📚 Referencias

Haverbeke, M. (2018). *Eloquent JavaScript* (3a ed.). https://eloquentjavascript.net/

MDN Web Docs. (2024). *JavaScript — MDN*. https://developer.mozilla.org/es/docs/Web/JavaScript
