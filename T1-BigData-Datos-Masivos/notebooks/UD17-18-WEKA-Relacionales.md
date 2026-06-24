# 📊 UD17-18 — WEKA y Bases de Datos Relacionales

**Trimestre 1 · S10 (May 2026)**

---

## 1. WEKA — Waikato Environment for Knowledge Analysis

WEKA es una herramienta de código abierto de la Universidad de Waikato (Nueva Zelanda) para Machine Learning y Data Mining con interfaz gráfica.

### Módulos principales

| Módulo | Función |
|---|---|
| **Explorer** | Cargar dataset, explorar atributos, aplicar algoritmos |
| **Experimenter** | Comparar múltiples algoritmos sobre múltiples datasets |
| **KnowledgeFlow** | Pipelines de ML con interfaz visual drag-and-drop |
| **Workbench** | Interfaz unificada (versiones modernas) |

### Formato ARFF

WEKA usa el formato `.arff` (Attribute-Relation File Format):

```
@relation mascotas_movet

@attribute nombre string
@attribute especie {Perro, Gato, Conejo}
@attribute peso numeric
@attribute enfermedad_cronica {Si, No}

@data
Firulais, Perro, 22.5, No
Michi, Gato, 4.2, Si
Rex, Perro, 35.0, No
```

---

## 2. Bases de Datos Relacionales — Revisión

### Niveles de abstracción

| Nivel | Descripción | Herramienta |
|---|---|---|
| **Modelo conceptual** | Entidades y relaciones (independiente de tecnología) | Diagrama E-R |
| **Modelo lógico** | Tablas, columnas, claves (independiente de motor) | Esquema relacional |
| **Modelo físico** | Implementación en un motor específico | DDL en SQL Server / Oracle |

### DDL esencial

```sql
CREATE TABLE pacientes (
    id_paciente  INT PRIMARY KEY,
    nombre       VARCHAR(100) NOT NULL,
    especie      VARCHAR(20),
    id_dueño     INT,
    FOREIGN KEY (id_dueño) REFERENCES dueños(id_dueño)
);

ALTER TABLE pacientes ADD peso DECIMAL(5,2);
DROP TABLE pacientes;
```

---

## 📚 Referencias

Witten, I. H., Frank, E., Hall, M. A., & Pal, C. J. (2016). *Data Mining: Practical Machine Learning Tools and Techniques* (4a ed.). Morgan Kaufmann.
