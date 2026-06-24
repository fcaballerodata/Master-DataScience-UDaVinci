# 📊 UD15-16 — Ecosistema Hadoop completo y Data Mining

**Trimestre 1 · S9 (May 2026)**

---

## 1. Ecosistema Hadoop completo

| Herramienta | Función | Analogía |
|---|---|---|
| **HDFS** | Sistema de archivos distribuido | El disco duro del clúster |
| **YARN** | Gestor de recursos | El sistema operativo del clúster |
| **MapReduce** | Procesamiento batch clásico | El motor antiguo |
| **Spark** | Procesamiento en memoria | El motor moderno (100x más rápido) |
| **Hive** | SQL sobre Hadoop (HiveQL) | Snowflake para Hadoop |
| **Pig** | Scripting de datos (Pig Latin) | ETL simplificado |
| **HBase** | BD NoSQL sobre HDFS | MongoDB para Hadoop |
| **Sqoop** | Transferencia RDBMS ↔ HDFS | ETL entre mundos SQL y Hadoop |
| **Flume** | Ingesta de logs en tiempo real | Colector de eventos |
| **Oozie** | Orquestador de workflows | Airflow de Hadoop |
| **Zookeeper** | Coordinación de servicios distribuidos | El árbitro del clúster |

---

## 2. Data Mining — Extracción de conocimiento

### Proceso KDD (Knowledge Discovery in Databases)

```
DATOS CRUDOS
    ↓ Selección
DATOS RELEVANTES
    ↓ Preprocesamiento (limpieza)
DATOS LIMPIOS
    ↓ Transformación (normalización, encoding)
DATOS TRANSFORMADOS
    ↓ Data Mining (algoritmos)
PATRONES
    ↓ Interpretación / Evaluación
CONOCIMIENTO
```

### Técnicas principales

| Técnica | Tipo | Ejemplo Movet |
|---|---|---|
| **Clasificación** | Supervisado | Predecir si una mascota desarrollará una enfermedad |
| **Clustering** | No supervisado | Agrupar mascotas por perfil de salud similar |
| **Regresión** | Supervisado | Predecir el costo de próximas consultas |
| **Asociación** | No supervisado | "Los perros que toman vacuna X también necesitan Y" |
| **Text Mining** | Semisupervisado | Extraer diagnósticos de notas clínicas en texto libre |

---

## 📚 Referencias

Han, J., Kamber, M., & Pei, J. (2011). *Data Mining: Concepts and Techniques* (3a ed.). Morgan Kaufmann.
