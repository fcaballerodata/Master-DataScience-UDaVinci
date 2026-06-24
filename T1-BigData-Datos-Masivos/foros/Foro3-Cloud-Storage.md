# 💬 Foro III — Cloud y Sistemas de Almacenamiento Masivo

**Asignatura:** Big Data y Datos Masivos · T1 S9

---

## 📋 Preguntas

1. ¿Cuáles son los principales modelos de despliegue cloud y cuándo usar cada uno?
2. ¿Cuál es la diferencia entre Data Lake y Data Warehouse?
3. ¿Cómo HDFS garantiza la tolerancia a fallos?
4. Describe un caso donde elegirías NoSQL sobre SQL y viceversa.

---

## ✍️ Respuesta publicada

Las decisiones de arquitectura de almacenamiento en Big Data son decisiones de negocio tanto como técnicas: elegir entre Data Lake y Data Warehouse, o entre SQL y NoSQL, depende de los casos de uso, los usuarios finales y los requisitos de consistencia y escala.

**Modelos de despliegue cloud**

La nube pública (AWS, Azure, GCP) ofrece escalabilidad elástica y pago por uso, ideal cuando los requisitos de capacidad son variables o impredecibles. La nube privada mantiene la infraestructura on-premise bajo control total de la organización, apropiada para entornos con regulaciones estrictas de privacidad de datos (sector salud, financiero). La nube híbrida combina ambas, permitiendo mantener datos sensibles en privada y usar la pública para cargas de trabajo variables — una estrategia común en empresas que ya tienen infraestructura on-premise pero quieren escalar con cloud. El modelo multicloud usa múltiples proveedores públicos para evitar dependencia de un único vendor (Armbrust et al., 2010).

**Data Lake vs Data Warehouse**

El Data Lake almacena datos en su formato nativo (crudo), de cualquier tipo y estructura, pensado para exploración y análisis ad-hoc por científicos de datos y ingenieros. El Data Warehouse almacena datos transformados, estructurados y optimizados para consultas analíticas rápidas por analistas de negocio e informes. En mi experiencia con Snowflake en Movet, el DW era la capa que los equipos de negocio consultaban directamente para sus dashboards — limpia, estructurada y documentada. El Data Lake era la capa donde llegaban primero los datos crudos antes de ser transformados.

**HDFS y tolerancia a fallos**

HDFS garantiza la disponibilidad de los datos mediante replicación automática con un factor de 3 por defecto: cada bloque de datos se almacena en tres DataNodes distintos. El NameNode (nodo maestro) mantiene el mapa de qué bloque está en qué nodo. Si un DataNode falla, el NameNode detecta la pérdida de heartbeat y ordena la creación de nuevas réplicas en otros nodos, restaurando el factor de replicación automáticamente. El único punto único de fallo histórico era el NameNode mismo, lo que HDFS High Availability resolvió con un NameNode de respaldo en standby (White, 2015).

**SQL vs NoSQL — cuándo elegir cada uno**

Elegiría NoSQL (MongoDB) para almacenar perfiles de mascotas en una aplicación web donde cada mascota puede tener atributos diferentes — un perro tiene chip_id, un gato tiene tipo_pelaje, un conejo tiene jaula_id. El esquema flexible de MongoDB evita tener columnas NULL o múltiples tablas. Elegiría SQL (PostgreSQL o Snowflake) para el sistema de facturación y contabilidad de Movet, donde la integridad transaccional es crítica — una consulta médica genera un cargo, que genera una factura, que afecta la contabilidad — y las propiedades ACID garantizan que ninguna de esas operaciones quede incompleta o inconsistente.

---

## 📚 Referencias

Armbrust, M., et al. (2010). A view of cloud computing. *Communications of the ACM*, 53(4), 50-58.

White, T. (2015). *Hadoop: The Definitive Guide* (4a ed.). O'Reilly Media.
