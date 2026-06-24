# 💬 Foro II — Stack Tecnológico y Cloud

**Asignatura:** Big Data y Datos Masivos · T1 S6

---

## 📋 Preguntas

1. ¿Qué es el stack tecnológico de Big Data y cuáles son sus capas?
2. ¿Cómo el cloud computing ha transformado el almacenamiento y procesamiento de Big Data?
3. ¿Cuál es la diferencia entre IaaS, PaaS y SaaS?
4. Describe cómo aplicarías un stack de Big Data en un escenario real.

---

## ✍️ Respuesta publicada

El stack tecnológico de Big Data es el conjunto de herramientas que, organizadas en capas, permiten ingestar, almacenar, procesar y visualizar grandes volúmenes de datos. El cloud computing transformó este stack de una infraestructura de alto costo y mantenimiento propio, a un modelo de servicio accesible y elástico.

**El stack tecnológico de Big Data**

El stack se organiza en cinco capas funcionales: ingesta (Kafka, Flume, Sqoop), almacenamiento (HDFS, S3, Azure Data Lake), procesamiento (MapReduce, Spark), análisis y consultas (Hive, Presto, dbt, Snowflake) y visualización (Power BI, Tableau, Superset). Cada capa resuelve un problema específico, y la elección de herramientas en cada una depende del volumen de datos, los requisitos de latencia y el presupuesto disponible. Según White (2015), la clave del ecosistema Hadoop es precisamente esta modularidad: cada componente puede ser reemplazado o actualizado sin necesidad de rediseñar toda la arquitectura.

**El cloud y la democratización del Big Data**

Antes del cloud, implementar un clúster Hadoop requería inversión en hardware físico, personal especializado y meses de configuración. AWS, Azure y GCP convirtieron esa infraestructura en servicios de pago por uso: EMR (AWS), HDInsight (Azure) o Dataproc (GCP) permiten levantar un clúster de 100 nodos en minutos y pagarlo solo mientras se usa. Armbrust et al. (2010) identificaron como transformación clave la ilusión de recursos infinitos bajo demanda, que elimina la necesidad de planificar capacidad a largo plazo.

**Diferencia entre IaaS, PaaS y SaaS**

IaaS (Infrastructure as a Service) provee recursos de hardware virtualizados — el usuario gestiona SO, runtime y aplicaciones (AWS EC2, Azure VMs). PaaS (Platform as a Service) añade el SO y el runtime — el usuario solo gestiona las aplicaciones y datos (Azure App Service, Heroku). SaaS (Software as a Service) provee la aplicación completa — el usuario solo configura y usa (Salesforce, Snowflake, Office 365). En el contexto de datos, Snowflake es SaaS: no gestionas servidores ni runtime, solo tu SQL y tus datos.

**Aplicación real: stack de analítica para Movet**

Un stack de Big Data aplicado a Movet en Azure seguiría este flujo: Odoo ERP y API de citas generan eventos que Kafka captura en tiempo real; Azure Data Lake almacena los datos crudos (capa raw); Spark en Azure Databricks realiza la transformación y limpieza (capa procesada); Snowflake actúa como Data Warehouse para consultas analíticas; y Power BI presenta los dashboards a la dirección. Este stack responde a las 3 Vs: maneja el volumen creciente de consultas, la velocidad de eventos en tiempo real y la variedad de fuentes (ERP, web, sensores).

---

## 📚 Referencias

Armbrust, M., et al. (2010). A view of cloud computing. *Communications of the ACM*, 53(4), 50-58.

White, T. (2015). *Hadoop: The Definitive Guide* (4a ed.). O'Reilly Media.
