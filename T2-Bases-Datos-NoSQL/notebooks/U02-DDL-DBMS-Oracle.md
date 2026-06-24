# 🗄️ U2 — DDL y DBMS Oracle

**Asignatura:** Bases de Datos y Bases de Datos NoSQL  
**Semana:** S2 (15–20 Jun 2026)

---

## 🎯 Conceptos clave

DDL define la estructura de una base de datos. Oracle es el DBMS relacional de referencia empresarial con más historia en el mercado.

---

## 1. DDL vs DML — La distinción fundamental

| | **DDL** (Data Definition Language) | **DML** (Data Manipulation Language) |
|---|---|---|
| **Define** | La estructura | Los datos dentro |
| **Verbos** | CREATE, ALTER, DROP | SELECT, INSERT, UPDATE, DELETE |
| **Analogía** | Construir el armario | Meter/sacar la ropa |
| **Naturaleza** | Siempre declarativo | Declarativo o procedural |

```sql
-- DDL: defino la estructura
CREATE TABLE mascotas (
    id_mascota INT,
    nombre     VARCHAR(50),
    especie    VARCHAR(20)
);

-- DML: manipulo los datos
INSERT INTO mascotas VALUES (1, 'Firulais', 'Perro');
SELECT * FROM mascotas WHERE especie = 'Perro';
```

> Con tu experiencia en Snowflake ya diferenciabas esto intuitivamente: crear una tabla nueva (DDL) vs. correr un SELECT para extraer datos (DML/DQL).

---

## 2. Estándares SQL

SQL no nació como un estándar único — cada motor lo fue adaptando, hasta que ANSI e ISO lo estandarizaron:

| Año | Versión | Aporte |
|---|---|---|
| 1986 | SQL1 | Primera especificación |
| 1992 | SQL2 | Revisión mayor — base del SQL moderno |
| 1999 | SQL3 | Incorpora orientación a objetos |

> Por eso la sintaxis base de `CREATE TABLE` es casi idéntica entre Oracle, SQL Server y MySQL, pero cada uno tiene dialectos propios (PL/SQL en Oracle, T-SQL en SQL Server).

---

## 3. Tipos de Datos en DDL

| Tipo | Descripción | Ejemplo Movet |
|---|---|---|
| `CHARACTER(n)` / `CHAR(n)` | Cadena longitud fija | `genero CHAR(1)` → 'M'/'H' |
| `CHARACTER VARYING(n)` / `VARCHAR(n)` | Cadena longitud variable | `nombre VARCHAR(100)` |
| `INTEGER` / `SMALLINT` | Enteros | `id_mascota INT` |
| `DECIMAL(p,s)` / `NUMERIC(p,s)` | Decimales exactos | `costo DECIMAL(10,2)` |
| `REAL` / `FLOAT` | Decimales de punto flotante | Mediciones científicas |
| `DATE` | Fecha (año-mes-día) | `fecha_consulta DATE` |
| `TIME` | Hora (hora-min-seg) | `hora_inicio TIME` |
| `TIMESTAMP` | Fecha + hora | `fecha_registro TIMESTAMP` |

> ⚠️ **Regla de oro:** nunca uses `FLOAT` para valores monetarios — usa `DECIMAL(10,2)`. El punto flotante puede introducir errores de redondeo en operaciones financieras.

### Ejemplo completo — Tabla consultas Movet

```sql
CREATE TABLE consultas (
    id_consulta    INTEGER,
    id_mascota     INTEGER,
    fecha          DATE,
    hora_inicio    TIME,
    costo          DECIMAL(10,2),
    diagnostico    VARCHAR(200),
    fecha_registro TIMESTAMP
);
```

---

## 4. Sentencias DDL para Esquemas

Un **esquema** agrupa tablas, vistas e índices bajo un mismo propietario — como una carpeta contenedora.

```sql
-- Crear esquema
CREATE SCHEMA movet_clinico AUTHORIZATION fredys_admin;

-- Borrar esquema vacío (falla si tiene objetos)
DROP SCHEMA movet_clinico RESTRICT;

-- Borrar esquema y TODO su contenido
DROP SCHEMA movet_clinico CASCADE;
```

> ⚠️ `CASCADE` es peligroso — borra todo sin confirmación adicional. En producción, siempre verificar antes de usar.

---

## 5. Oracle Database — Historia y arquitectura

### Línea de tiempo clave

| Año | Versión | Hito |
|---|---|---|
| 1977 | — | Larry Ellison, Bob Miner y Ed Oates fundan Oracle Corp. |
| 1979 | Oracle V2 | Primer RDBMS comercial disponible |
| 1983 | V3 | Primera BD relacional multiplataforma (en C) |
| 1992 | Oracle7 | Triggers y PL/SQL maduros |
| 1997 | Oracle8 | Soporte de objetos + particionamiento |
| 1999 | Oracle8i | Soporte nativo Internet y Java |
| 2013 | Oracle12c | Arquitectura multiinquilino + soporte JSON |
| Hoy | Oracle21c | Cloud-first, Autonomous Database |

> El salto de 2013 (Oracle12c) es clave: ahí Oracle empieza a **converger con NoSQL**, permitiendo documentos JSON dentro de un motor relacional — el mismo fenómeno que verás en U7-U8.

### Los 3 pilares del modelo relacional Oracle

1. **Estructuras** — objetos que almacenan datos (tablas)
2. **Operaciones** — acciones que manipulan datos (SELECT, INSERT...)
3. **Reglas de integridad** — qué valores son válidos (id no puede repetirse)

### RDBMS vs ORDBMS

Oracle es técnicamente un **ORDBMS** (Object-Relational DBMS): relacional en su núcleo, con soporte de tipos de objetos definidos por el usuario, herencia y polimorfismo.

> **Nota importante:** en Oracle, **un esquema = un usuario**. Si creas el usuario `fredys`, automáticamente tienes el esquema `fredys` donde van todos tus objetos. Esto es diferente a otros motores.

---

## 🗺️ Mapa mental

```
U2: DDL Y DBMS ORACLE
│
├── DDL vs DML
│     ├── DDL → estructura (CREATE, ALTER, DROP)
│     └── DML → datos (SELECT, INSERT, UPDATE, DELETE)
│
├── Tipos de Datos
│     ├── Texto: CHAR, VARCHAR
│     ├── Numérico: INTEGER, DECIMAL (nunca FLOAT para dinero)
│     └── Temporal: DATE, TIME, TIMESTAMP
│
├── CREATE/DROP SCHEMA
│     ├── RESTRICT → solo si vacío
│     └── CASCADE → borra todo (⚠️ peligroso en producción)
│
└── Oracle Database
      ├── Historia: 1977 fundación → 1979 V2 → 2013 JSON → hoy cloud
      ├── Modelo: Estructuras + Operaciones + Integridad
      ├── ORDBMS: relacional + soporte de objetos
      └── Esquema = Usuario (específico de Oracle)
```

---

## 📚 Referencias

Beynon-Davies, P. (2018). *Sistemas de bases de datos*. Reverté.

Oracle Corporation. (2023). *Oracle Database documentation*. https://docs.oracle.com/en/database/
