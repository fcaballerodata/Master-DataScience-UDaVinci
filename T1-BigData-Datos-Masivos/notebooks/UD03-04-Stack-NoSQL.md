# 📊 UD3-4 — Stack Tecnológico y Almacenamiento

**Trimestre 1 · S3-S4 (Mar 2026)**

---

## 1. El Stack de Big Data (Pila tecnológica)

```
┌─────────────────────────────────────┐
│  Capa de Aplicación / Visualización │  Power BI, Tableau, Superset
├─────────────────────────────────────┤
│  Capa de Análisis                   │  Spark, Hive, Presto, dbt
├─────────────────────────────────────┤
│  Capa de Procesamiento              │  MapReduce, Spark Streaming
├─────────────────────────────────────┤
│  Capa de Almacenamiento             │  HDFS, S3, Azure Data Lake
├─────────────────────────────────────┤
│  Capa de Ingesta                    │  Kafka, Flume, Sqoop, NiFi
└─────────────────────────────────────┘
```

---

## 2. Herramientas clave por capa

| Herramienta | Capa | Función |
|---|---|---|
| **Kafka** | Ingesta | Streaming de eventos en tiempo real |
| **Sqoop** | Ingesta | Transferencia RDBMS ↔ Hadoop |
| **HDFS** | Almacenamiento | Sistema de archivos distribuido de Hadoop |
| **Spark** | Procesamiento | Motor de análisis en memoria (100x más rápido que MapReduce) |
| **Hive** | Análisis | SQL sobre Hadoop (HiveQL) |
| **Snowflake** | Análisis/DW | Data Warehouse cloud con separación cómputo/almacenamiento |

---

## 3. Almacenamiento analítico

| Tipo | Optimizado para | Ejemplo |
|---|---|---|
| OLTP | Transacciones (escritura frecuente) | MySQL, SQL Server |
| OLAP / DW | Consultas analíticas (lectura masiva) | Snowflake, Redshift, BigQuery |
| Data Lake | Datos crudos de cualquier formato | HDFS, S3, Azure Data Lake |
| NoSQL | Datos semiestructurados y escala horizontal | MongoDB, Cassandra, Redis |

> **Snowflake en contexto Movet:** al trabajar con Snowflake en Movet, usabas un Data Warehouse OLAP cloud que separaba cómputo (virtual warehouses) de almacenamiento (S3 interno), permitiendo escalar cada dimensión independientemente.

---

## 📚 Referencias

White, T. (2015). *Hadoop: The Definitive Guide* (4a ed.). O'Reilly Media.
