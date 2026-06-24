# 💬 Foro I — Fundamentos del Big Data y Computación Distribuida

**Asignatura:** Big Data y Datos Masivos · T1 S2

---

## 📋 Preguntas

1. ¿Qué es el Big Data y cuáles son sus características principales?
2. ¿Cómo la computación distribuida resuelve los retos del Big Data?
3. ¿Cuál es el impacto del Big Data en las organizaciones modernas?
4. Describe un caso de uso de Big Data en tu área de trabajo.

---

## ✍️ Respuesta publicada

El Big Data no es simplemente una cuestión de volumen — es la convergencia de tres desafíos simultáneos que los sistemas de información tradicionales no estaban diseñados para enfrentar. Entender esto es el punto de partida para cualquier arquitectura de datos moderna.

**¿Qué es el Big Data y cuáles son sus características?**

El Big Data se define por las 3 Vs identificadas por Gartner: Volumen (datos en escala de terabytes o petabytes), Velocidad (generación y procesamiento en tiempo real o casi real) y Variedad (datos estructurados, semiestructurados y no estructurados de múltiples fuentes). A estas se han añadido Veracidad (calidad y confiabilidad de los datos) y Valor (capacidad de extraer insights útiles). El Big Data no es un problema tecnológico exclusivamente — es un problema de negocio: los datos solo generan valor cuando se transforman en decisiones accionables (IBM, 2024).

**¿Cómo la computación distribuida resuelve los retos del Big Data?**

La computación distribuida divide el problema en partes y las procesa en paralelo sobre múltiples nodos de hardware commodity. El principio clave es "mover el código a los datos, no los datos al código": en lugar de centralizar terabytes de datos en un único servidor, el proceso se envía a los nodos donde ya están almacenados los datos. Hadoop implementó este principio con HDFS (almacenamiento distribuido con replicación automática) y MapReduce (procesamiento paralelo en dos fases). Apache Spark lo evolucionó procesando en memoria RAM en lugar de disco, logrando hasta 100 veces mayor velocidad (White, 2015).

**Impacto en las organizaciones**

El Big Data transformó la capacidad de las organizaciones para tomar decisiones basadas en evidencia a escala. Empresas como Netflix, Amazon y Spotify construyeron ventajas competitivas directamente sobre su capacidad de procesar y aprender de datos masivos en tiempo real. Para organizaciones más pequeñas, la democratización del cloud computing (AWS, Azure, GCP) puso esas capacidades al alcance de cualquier empresa sin inversión en infraestructura propia.

**Caso de uso real: pipeline de datos en Movet**

En Movet, los datos de operación estaban distribuidos en múltiples fuentes: Odoo ERP (consultas y facturación), sistemas de citas en línea y registros manuales de las sedes. El reto era consolidar y analizar ese volumen heterogéneo para tomar decisiones operativas. La solución fue un pipeline que extraía datos de Odoo vía API, los consolidaba en Snowflake (Data Warehouse cloud) y los presentaba en dashboards de Power BI actualizados diariamente. Este es un caso de Big Data a escala empresarial mediana: no estamos hablando de petabytes, pero sí de las mismas 3 Vs — volumen creciente, variedad de fuentes y necesidad de velocidad en la toma de decisiones.

---

## 📚 Referencias

IBM. (2024). *What is big data?* https://www.ibm.com/topics/big-data

White, T. (2015). *Hadoop: The Definitive Guide* (4a ed.). O'Reilly Media.
