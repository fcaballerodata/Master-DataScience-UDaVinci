# 🗄️ U4 — SQL Introducción y SQL Consultas, Subconsultas y Funciones

**Asignatura:** Bases de Datos y Bases de Datos NoSQL  
**Semana:** S4 (29 Jun – 4 Jul 2026)

---

## 🎯 Conceptos clave

SQL es el lenguaje estándar para gestionar bases de datos relacionales, con raíces en los años 70 y una estructura formal que combina definición y manipulación de datos.

---

## 1. Historia de SQL

| Año | Hito |
|---|---|
| Principios 1970 | IBM desarrolla **Sequel** (proyecto System R) |
| — | Sequel evoluciona a **SQL** (Structured Query Language) |
| 1986 | ANSI publica la primera norma — SQL-86 |
| 1989 | Extensión — SQL-89 |
| 1992 | **SQL-92** (SQL2) — la versión más importante, base del SQL moderno |
| 1999 | SQL:1999 (SQL3) — incorpora objetos |
| 2019 | SQL:2019 — versión más reciente |

---

## 2. El Entorno SQL — 6 componentes

| Componente | Función |
|---|---|
| **Esquema** | Colección de tablas, vistas, dominios relacionados |
| **Catálogo** | Conjunto de esquemas — contenedor mayor |
| **Cliente SQL** | Aplicación que envía consultas |
| **Servidor SQL** | Motor que las procesa |
| **Módulo de aplicación** | Procedimientos SQL invocados |
| **Identificador de autorización** | Usuario/rol con sus privilegios |

> Jerarquía catálogo → esquema → tabla = exactamente `database.schema.table` en plataformas cloud modernas.

---

## 3. DDL vs DML — Repaso

```sql
-- DDL: estructura
CREATE TABLE clientes (...);
ALTER TABLE clientes ADD ...;
DROP TABLE clientes;

-- DML: datos
INSERT INTO clientes VALUES (...);
UPDATE clientes SET ... WHERE ...;
DELETE FROM clientes WHERE ...;
```

---

## 4. La sentencia SELECT

### Estructura básica

```sql
SELECT columnas
FROM tabla
WHERE condición;
```

### Orden de ejecución (clave y contraintuitivo)

| Cláusula | Álgebra relacional | Función |
|---|---|---|
| **FROM** | Producto cartesiano | Define las tablas a analizar |
| **WHERE** | Selección (predicado) | Filtra filas |
| **SELECT** | Proyección | Elige columnas a mostrar |

> Se escribe SELECT→FROM→WHERE pero se **ejecuta** FROM→WHERE→SELECT. Por eso un alias del SELECT no puede usarse en el WHERE.

```sql
SELECT nombre, especie
FROM mascotas
WHERE especie = 'Perro';
```

---

## 5. Operadores

| Comparación | Booleanos |
|---|---|
| `=` `<>` `<` `>` `<=` `>=` | `AND` `OR` `NOT` |

```sql
SELECT nombre, especie, peso
FROM mascotas
WHERE especie = 'Perro' AND peso > 20;

SELECT * FROM mascotas WHERE nombre LIKE 'Fi%';
```

---

## 6. Subconsultas

Una consulta SELECT completa dentro de otra, entre paréntesis.

### Reglas

- Hasta 16 subconsultas anidadas
- Se ejecutan de adentro hacia afuera (última a primera)
- No pueden contener `ORDER BY`, ni `BETWEEN`/`LIKE` directamente
- En `UPDATE`/`DELETE` no pueden leer de la misma tabla que modifican

### Ejemplo

```sql
-- Mascotas que pesan más que el peso promedio
SELECT nombre, especie, peso
FROM mascotas
WHERE peso >= (SELECT AVG(peso) FROM mascotas);

-- Consultas de un veterinario de una sede específica
SELECT id_consulta, fecha, diagnostico
FROM consultas
WHERE id_veterinario = (SELECT id_veterinario
                         FROM veterinarios
                         WHERE sede = 'Norte');
```

### ANY, ALL, IN

```sql
SELECT nombre FROM mascotas
WHERE especie IN ('Perro', 'Gato', 'Conejo');

SELECT nombre, peso FROM mascotas
WHERE peso > ANY (SELECT peso FROM mascotas WHERE especie = 'Gato');
```

---

## 7. ORDER BY

```sql
SELECT * FROM consultas
WHERE costo < 60000
ORDER BY costo;              -- ASC por defecto

SELECT * FROM consultas
ORDER BY fecha DESC, costo ASC;
```

> Siempre es la última cláusula en ejecutarse.

---

## 🗺️ Mapa mental

```
U4: SQL — INTRODUCCIÓN, CONSULTAS, SUBCONSULTAS Y FUNCIONES
│
├── Historia: IBM Sequel (1970) → ANSI SQL-86 → SQL-92 → SQL:2019
│
├── Entorno SQL: Catálogo → Esquema → Tabla
│
├── SELECT
│     ├── Escritura: SELECT → FROM → WHERE
│     └── Ejecución: FROM → WHERE → SELECT
│
├── Operadores: comparación, AND/OR/NOT, LIKE, IN
│
├── Subconsultas
│     ├── Entre paréntesis, máx 16 anidadas
│     └── Se ejecutan de adentro hacia afuera
│
└── ORDER BY → última cláusula, ASC/DESC
```

---

## 📚 Referencias

ISO/IEC. (2016). *ISO/IEC 9075-1:2016 — Information technology — Database languages — SQL*. https://www.iso.org/standard/63555.html
