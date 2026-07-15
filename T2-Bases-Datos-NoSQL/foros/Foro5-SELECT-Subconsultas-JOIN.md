# 💬 Foro 5 — SELECT, Subconsultas, Multitabla, Agrupación y JOIN

**Asignatura:** Bases de Datos y Bases de Datos No SQL
**Semana:** S6

---

## 📋 Preguntas

A partir de los materiales revisados durante la Unidad VII, responde:

1. Ejemplifica la sentencia SELECT en: consultas, subconsultas y con múltiples tablas.
2. ¿Cuáles son las funciones de agrupación en SQL?
3. Mencione los operadores para múltiples tablas.
4. Mencione la función de la sentencia JOIN.

---

## ✍️ Respuesta publicada

### 1. Sentencia SELECT: consultas, subconsultas y múltiples tablas

**Consulta simple** — trae datos de una sola tabla:

```sql
SELECT nombre, especie FROM Mascotas;
```

**Subconsulta** — un SELECT dentro de otro SELECT, entre paréntesis:

```sql
SELECT nombre FROM Mascotas
WHERE id_mascota IN (SELECT id_mascota FROM Consultas WHERE costo > 500);
```

*(Trae las mascotas que han tenido al menos una consulta de más de $500.)*

**Múltiples tablas (JOIN)** — combina columnas de dos o más tablas relacionadas:

```sql
SELECT m.nombre, c.fecha, c.costo
FROM Mascotas m
INNER JOIN Consultas c ON m.id_mascota = c.id_mascota;
```

### 2. Funciones de agrupación en SQL

Se usan junto con `GROUP BY` para resumir datos de varias filas en un solo valor:

| Función | Qué hace |
|---|---|
| `COUNT()` | Cuenta filas/registros |
| `SUM()` | Suma valores |
| `AVG()` | Calcula el promedio |
| `MAX()` | Devuelve el valor máximo |
| `MIN()` | Devuelve el valor mínimo |

```sql
SELECT especie, COUNT(*) AS total
FROM Mascotas
GROUP BY especie;
```

### 3. Operadores para múltiples tablas

| Operador | Función |
|---|---|
| `INNER JOIN` | Solo filas con coincidencia en ambas tablas |
| `LEFT JOIN` | Todas las de la izquierda + coincidencias de la derecha |
| `RIGHT JOIN` | Todas las de la derecha + coincidencias de la izquierda |
| `FULL OUTER JOIN` | Todo de ambas tablas, coincida o no |
| `UNION` | Combina resultados de dos SELECT (simula FULL OUTER JOIN en MySQL) |

### 4. Función de la sentencia JOIN

`JOIN` combina filas de dos o más tablas relacionadas usando una clave en común (normalmente clave primaria ↔ clave foránea), para poder consultar información distribuida en varias tablas como si fuera una sola. Es la base de cualquier reporte que necesite cruzar datos — por ejemplo, saber qué mascota corresponde a qué consulta sin tener toda la información duplicada en una sola tabla gigante.

---

## 📚 Referencias

ISO/IEC. (2016). *Information technology — Database languages — SQL*. https://www.iso.org/standard/63555.html
