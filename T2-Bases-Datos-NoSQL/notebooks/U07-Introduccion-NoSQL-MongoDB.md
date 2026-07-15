# 🍃 U7 — Introducción a Bases de Datos NoSQL y MongoDB

**Asignatura:** Bases de Datos y Bases de Datos NoSQL
**Semana:** S6

---

## 1. SQL vs. NoSQL

| | SQL (Relacional) | NoSQL |
|---|---|---|
| Estructura | Tablas con esquema fijo | Documentos flexibles, sin esquema fijo |
| Relaciones | Explícitas (claves foráneas) | Normalmente no relacionadas entre sí |
| Cuándo usar | Datos estructurados con jerarquía clara | Datos variables, gran volumen, cambios frecuentes |
| Ejemplo | Oracle, SQL Server, MySQL | MongoDB |

El nombre "NoSQL" ("not only SQL") nació como respuesta a las limitaciones de las bases relacionales ante datos no estructurados y necesidad de escalado masivo.

---

## 2. Escalabilidad — vertical vs. horizontal

| Tipo | Qué hace | Costo/complejidad |
|---|---|---|
| **Vertical** | Mejorar el hardware de UN servidor | Más simple, tiene un techo físico |
| **Horizontal** | Repartir la carga entre VARIOS servidores/nodos | Más compleja, más potente — fortaleza típica de NoSQL |

---

## 3. MongoDB — lo esencial

- Guarda datos en **documentos BSON** (similar a JSON), no en tablas.
- Nació en 2007 (10gen Inc. → MongoDB Inc.), lanzado en 2009, licencia AGPL.
- **No requiere esquema fijo**: dos documentos en la misma colección pueden tener campos distintos.

**Ejemplo:** en SQL, si la tabla MASCOTAS tiene columna `alergias`, todas las filas la comparten. En MongoDB, un documento puede simplemente no tener el campo `alergias` si no aplica.

---

## 4. Sintaxis básica — equivalencia SQL vs. MongoDB

| Operación | SQL | MongoDB |
|---|---|---|
| Crear/usar BD | `CREATE DATABASE veterinaria;` | `use veterinaria` |
| Insertar | `INSERT INTO ...` | `db.mascotas.insert({...})` |
| Consultar todo | `SELECT * FROM mascotas;` | `db.mascotas.find()` |
| Consultar con filtro | `SELECT * FROM mascotas WHERE nombre='Firulais';` | `db.mascotas.find({nombre: "Firulais"})` |
| Ordenar | `ORDER BY edad DESC` | `.sort({edad: -1})` |
| Modificar | `UPDATE mascotas SET nombre='Rocky' WHERE nombre='Firulais';` | `db.mascotas.update({nombre:"Firulais"}, {$set:{nombre:"Rocky"}})` |
| Eliminar | `DELETE FROM mascotas WHERE nombre='Firulais';` | `db.mascotas.remove({nombre:"Firulais"})` |

```javascript
// Ejemplo: insertar una mascota con un array anidado (natural en NoSQL)
db.mascotas.insert({
  nombre: "Luna",
  especie: "Gato",
  edad: 3,
  vacunas: ["rabia", "triple felina"]
})
```

En SQL, `vacunas` normalmente requeriría una tabla aparte relacionada por clave foránea. MongoDB anida la información relacionada dentro del mismo documento en lugar de separarla en tablas y unirla con JOIN.

---

## 5. ¿Cuándo usar cada una?

| Usa SQL cuando... | Usa NoSQL (MongoDB) cuando... |
|---|---|
| Estructura de datos clara y estable | Estructura cambia frecuentemente / es impredecible |
| Necesitas integridad referencial estricta | Redes sociales, Big Data, apps móviles |
| Negocio maduro, esquema estable | Desarrollo ágil, esquema aún evolucionando |

---

## 📚 Referencias

Guía de la Unidad 7 — Universidad DaVinci (2026). Introducción de bases de datos NoSQL.
