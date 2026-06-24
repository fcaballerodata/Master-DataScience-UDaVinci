# 📊 UD9-10 — Ecosistema Hadoop y Administración

**Trimestre 1 · S7-S8 (Abr-May 2026)**

---

## 1. Hadoop — Arquitectura

Hadoop es un framework open source para procesamiento distribuido de grandes volúmenes de datos.

### Componentes core

| Componente | Función |
|---|---|
| **HDFS** (Hadoop Distributed File System) | Almacenamiento distribuido con replicación |
| **YARN** (Yet Another Resource Negotiator) | Gestión de recursos del clúster |
| **MapReduce** | Modelo de programación para procesamiento paralelo |

### HDFS — Cómo funciona

```
NameNode (maestro)
    ├── Guarda el mapa de dónde está cada bloque
    └── Coordina acceso de clientes

DataNode x3 (esclavos)
    ├── DataNode 1: Bloque A, Bloque C
    ├── DataNode 2: Bloque A (réplica), Bloque B
    └── DataNode 3: Bloque B (réplica), Bloque C (réplica)
```

> **Factor de replicación = 3 por defecto:** cada bloque se replica en 3 nodos. Si un DataNode falla, los datos siguen disponibles.

---

## 2. MapReduce — El paradigma

```
INPUT: 1TB de logs de consultas Movet

MAP (paralelo en cada nodo):
    ("sede_norte", 1), ("sede_sur", 1), ("sede_norte", 1)...

SHUFFLE (agrupa por clave):
    "sede_norte": [1, 1, 1, 1...]
    "sede_sur": [1, 1...]

REDUCE (suma por clave):
    "sede_norte": 1547
    "sede_sur": 892

OUTPUT: conteo de consultas por sede
```

---

## 3. Apache Spark — La evolución

| | MapReduce | Apache Spark |
|---|---|---|
| **Velocidad** | Lento (disco I/O entre etapas) | 100x más rápido (memoria RAM) |
| **Modelo** | Solo batch | Batch + Streaming + ML + SQL |
| **API** | Java nativo | Python (PySpark), Scala, R, SQL |
| **Facilidad** | Complejo | API de alto nivel |

---

## 📚 Referencias

White, T. (2015). *Hadoop: The Definitive Guide* (4a ed.). O'Reilly Media.

Karau, H., & Warren, R. (2017). *High Performance Spark*. O'Reilly Media.
