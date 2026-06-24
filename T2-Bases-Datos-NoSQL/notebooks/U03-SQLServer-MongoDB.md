# 🗄️ U3 — DBMS SQL Server y MongoDB

**Asignatura:** Bases de Datos y Bases de Datos NoSQL  
**Semana:** S3 (22–27 Jun 2026)

---

## 🎯 Conceptos clave

SQL Server y MongoDB representan dos paradigmas: el relacional maduro (SQL Server) y el orientado a documentos (MongoDB). Conocer ambos es esencial para elegir el motor correcto según el problema.

---

## 1. SQL Server — Historia

Microsoft entró al mundo de las BD en **1989** (colaboración con Sybase para OS/2).

| Versión | Año | Hito |
|---|---|---|
| 1.0 (OS/2) | 1989 | Primer SQL Server — con Sybase |
| 4.21 (WinNT) | 1993 | Primera versión para Windows |
| 7.0 | 1998 | Código completamente reescrito por Microsoft |
| 2005 | 2005 | Reescritura total + SSMS (interfaz gráfica moderna) |
| SQL Azure DB | 2010 | **Primera versión cloud** — antecedente directo de Snowflake |
| 2017 | 2017 | Soporte Linux + contenedores Docker |
| 2019 | 2019 | Big Data Clusters (Spark + HDFS en Kubernetes) |

> **Conexión con tu stack:** Snowflake es la evolución cloud de lo que SQL Server comenzó con SQL Azure en 2010 — separar almacenamiento y cómputo tiene sus raíces en esa transición.

---

## 2. Interfaces de SQL Server

| Interfaz | Tipo | Descripción |
|---|---|---|
| **SSMS** (SQL Server Management Studio) | Gráfica | Interfaz estándar desde 2005. Equivalente al UI de Snowflake |
| **T-SQL** (Transact-SQL) | Lenguaje | Dialecto SQL propietario de Microsoft |
| **SQLCmd** | Línea de comandos | Ejecutar scripts desde terminal |

### T-SQL vs SQL estándar

Las diferencias en queries básicas son mínimas. Las diferencias aparecen en variables, control de flujo y procedimientos almacenados:

```sql
-- SQL estándar (funciona en Snowflake, MySQL, Oracle, SQL Server)
SELECT id_mascota, nombre FROM mascotas WHERE especie = 'Perro';

-- T-SQL con características propias: variable + condicional
DECLARE @especie VARCHAR(20) = 'Perro';

IF @especie = 'Perro'
    SELECT COUNT(*) AS total_perros
    FROM mascotas WHERE especie = @especie;
ELSE
    SELECT COUNT(*) AS otras_especies
    FROM mascotas WHERE especie != 'Perro';
```

> Con tu nivel de SQL en Snowflake, adaptarte a T-SQL toma días, no semanas.

---

## 3. Requisitos de instalación SQL Server 2019

Según Microsoft Learn (2022):

| Componente | Mínimo | Recomendado |
|---|---|---|
| **Procesador** | x64, 1.4 GHz | 2.0 GHz o superior |
| **RAM** | 1 GB (Express) / 4 GB (otras ediciones) | 4 GB+ (aumentar con la BD) |
| **Disco duro** | 6 GB disponibles | Variable según features |
| **Pantalla** | 800×600 px | — |
| **SO** | Windows Server 2016 / Linux | — |
| **Software** | .NET Framework 4.6+ | Se instala automáticamente |

---

## 4. MongoDB — El cambio de paradigma

### Del modelo relacional al modelo de documentos

| Concepto | SQL (Relacional) | MongoDB (Documentos) |
|---|---|---|
| Contenedor | Base de datos | Base de datos |
| Agrupador | **Tabla** | **Colección** |
| Registro | **Fila / Tupla** | **Documento** (JSON) |
| Campo | **Columna** | **Campo** (clave:valor) |
| Relación | JOIN entre tablas | Documentos embebidos |
| Esquema | Rígido (predefinido) | **Flexible** (dinámico) |

> **Origen del nombre:** MongoDB viene de *humongous* (enorme en inglés). Fue creado por **10gen** (hoy MongoDB Inc.), escrito en C++, open source.

### SQL vs MongoDB — Mismo dato, diferente estructura

**En SQL Server** (3 tablas + JOINs para una consulta):
```sql
SELECT c.fecha, c.diagnostico,
       m.nombre AS mascota,
       d.nombre AS dueno
FROM consultas c
JOIN mascotas m ON c.id_mascota = m.id_mascota
JOIN duenos d ON m.id_dueno = d.id_dueno
WHERE c.id_consulta = 1;
```

**En MongoDB** (un solo documento, sin JOINs):
```json
{
  "_id": "507f1f77bcf86cd799439011",
  "id_consulta": 1,
  "fecha": "2025-01-10",
  "diagnostico": "Otitis",
  "mascota": {
    "nombre": "Firulais",
    "especie": "Perro"
  },
  "dueno": {
    "nombre": "Juan Pérez",
    "telefono": "3001234567"
  }
}
```

---

## 5. ¿Cuándo usar MongoDB?

### ✅ Casos de uso ideales

- Datos semi-estructurados o con estructura variable entre registros
- Escalabilidad horizontal mediante **sharding** (distribuir datos en múltiples servidores)
- Alto rendimiento en lectura/escritura de documentos completos
- Aplicaciones web donde los datos ya vienen en JSON desde el frontend
- IoT: dispositivos que generan datos con campos variables (caso Bosch del material)

### ❌ Cuándo NO usar MongoDB

1. **Transacciones complejas:** MongoDB garantiza atomicidad solo a nivel de documento — no tiene transacciones multi-documento nativas robustas
2. **JOINs complejos:** el Aggregation Framework no llega a la potencia de JOINs relacionales
3. **Datos altamente relacionados:** si el modelo es naturalmente relacional, forzarlo a documentos complica más de lo que simplifica

> **Regla práctica:** el esquema en MongoDB lo definen las **consultas que harás con más frecuencia**. Diseñas en función de cómo leerás los datos, no de cómo están relacionados.

---

## 6. Esquema flexible en MongoDB

Documentos en la misma colección pueden tener campos distintos:

```json
// Documento 1 — colección "mascotas_movet"
{ "_id": 1, "nombre": "Firulais", "especie": "Perro", "chip_id": "985112003456789" }

// Documento 2 — MISMA colección, campos distintos
{ "_id": 2, "nombre": "Michi", "especie": "Gato", "vacunas": ["triple felina", "rabia"] }
```

Esto sería imposible en SQL sin agregar columnas NULL o crear tablas separadas.

---

## 7. Cuadro comparativo: Oracle vs SQL Server 2019

| Criterio | Oracle Database | SQL Server 2019 |
|---|---|---|
| Fabricante | Oracle Corporation | Microsoft |
| Lenguaje propietario | PL/SQL | T-SQL |
| Plataformas | Windows, Linux, Unix | Windows, Linux, Docker |
| Escalabilidad | Oracle RAC (clustering) | Big Data Clusters (Spark/HDFS) |
| Seguridad | Auditoría avanzada, cifrado | Siempre cifrado, enmascaramiento |
| Cloud nativo | Oracle Cloud | Azure SQL |
| Licenciamiento | Propietario, costo elevado | Edición Developer gratuita |
| Ecosistema BI | Oracle Analytics Cloud | Power BI + SSRS |

---

## 🗺️ Mapa mental

```
U3: SQL SERVER Y MONGODB
│
├── SQL Server
│     ├── Historia: 1989 (Sybase) → 1993 (Windows) → 2019 (cloud+Linux)
│     ├── Interfaz: SSMS + T-SQL + SQLCmd
│     └── T-SQL: SQL estándar + variables, IF/ELSE, procedimientos
│
└── MongoDB
      ├── "Humongous" — 10gen → MongoDB Inc. — C++ open source
      ├── Paradigma: Documentos JSON → Colecciones (sin esquema fijo)
      ├── Ventajas: flexible, escalable horizontalmente (sharding)
      ├── ✅ Usar cuando: datos semiestructurados, JSON nativo, escala masiva
      └── ❌ No usar cuando: transacciones críticas, JOINs complejos
```

---

## 📚 Referencias

Microsoft. (2022). *Requisitos de hardware y software para instalar SQL Server 2019*. Microsoft Learn. https://learn.microsoft.com/es-es/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server-2019

MongoDB Inc. (2024). *MongoDB documentation*. https://www.mongodb.com/docs/

Softtrader. (2025). *Microsoft SQL Server 2019: requerimientos y características*. https://softtrader.es/todo-lo-que-necesitan-saber-sobre-microsoft-sql-server-2019/
