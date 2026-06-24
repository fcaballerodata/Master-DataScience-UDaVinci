# 📊 UD1-2 — Fundamentos del Big Data y Computación Distribuida

**Trimestre 1 · S1-S2 (Mar 2026)**

---

## 1. ¿Qué es el Big Data?

Big Data no es solo "mucho dato" — es la incapacidad de los sistemas tradicionales para gestionar datos por su **volumen, velocidad o variedad**. El término fue popularizado por Gartner en 2011.

### Las 3 Vs originales (Gartner, 2001)

| V | Definición | Ejemplo Movet |
|---|---|---|
| **Volumen** | Cantidad masiva de datos | Millones de registros de consultas históricas |
| **Velocidad** | Rapidez de generación y procesamiento | Sensores IoT en tiempo real, alerts automáticos |
| **Variedad** | Diversidad de formatos y fuentes | Texto (diagnósticos), imágenes (radiografías), estructurado (BD) |

> Con el tiempo se añadieron más Vs: Veracidad (calidad), Valor (utilidad), Variabilidad, Visualización.

---

## 2. Evolución histórica

| Era | Característica | Ejemplo |
|---|---|---|
| **Pre-digital** | Datos en papel, acceso manual | Fichas veterinarias en carpetas |
| **Bases de datos** (1970s) | SQL, modelos relacionales | MySQL, Oracle |
| **Data Warehouse** (1990s) | Análisis histórico centralizado | Snowflake, Redshift |
| **Big Data** (2000s) | Procesamiento distribuido masivo | Hadoop, Spark |
| **Cloud Data** (2010s) | Escalabilidad elástica | AWS S3, Azure Data Lake |

---

## 2. Computación Distribuida

La computación distribuida divide el procesamiento entre múltiples nodos que trabajan en paralelo.

### Comparación: Centralizado vs Distribuido

| | Centralizado | Distribuido |
|---|---|---|
| **Escalabilidad** | Vertical (más RAM/CPU al mismo servidor) | Horizontal (más servidores) |
| **Tolerancia a fallos** | Baja (un fallo = caída total) | Alta (nodos independientes) |
| **Costo de escala** | Alto (hardware premium) | Bajo (commodity hardware) |
| **Ejemplos** | SQL Server on-premise | Hadoop, Spark, Snowflake |

### Principio clave: llevar el código a los datos

En Big Data, mover terabytes de datos es costoso. La solución es el principio **"move the code, not the data"**: el proceso se envía a los nodos donde ya están los datos.

---

## 🗺️ Mapa mental

```
BIG DATA FUNDAMENTOS
│
├── Las 3 Vs → Volumen, Velocidad, Variedad
├── Limitación → sistemas tradicionales no pueden con las 3Vs
├── Solución → computación distribuida
│     ├── Divide el problema en partes
│     ├── Procesa en paralelo en múltiples nodos
│     └── Combina los resultados
└── Paradigma → mover el código a los datos (no al revés)
```

## 📚 Referencias

Schmarzo, B. (2013). *Big Data: Understanding How Data Powers Big Business*. Wiley.
