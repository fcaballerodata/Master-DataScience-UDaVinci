# 🍃 U9 — MongoDB: Índices

**Asignatura:** Bases de Datos y Bases de Datos NoSQL
**Semana:** S7

---

## 1. Origen del nombre "Humongous"

MongoDB viene de "hu**mongo**us" (enorme) — refleja su capacidad de almacenar volúmenes masivos de datos.

---

## 2. ¿Qué es un índice en MongoDB?

Mismo concepto que en SQL (Unidad 6): estructura auxiliar que acelera búsquedas, a costa de más espacio y ligera ralentización en inserciones/actualizaciones.

```javascript
// Crear un índice
db.mascotas.createIndex({ "especie": 1 })

// Ver índices activos de una colección
db.mascotas.getIndexes()

// Eliminar un índice
db.mascotas.dropIndex({ "especie": 1 })
```

`1` = orden ascendente, `-1` = descendente.

---

## 3. Tipos de índices

| Tipo | Qué hace | Ejemplo |
|---|---|---|
| **Único (`_id`)** | Automático en cada documento, irrepetible, no se puede borrar | Identificador único de cada mascota |
| **Normal** | Índice simple sin condiciones | `db.mascotas.createIndex({"especie": 1})` |
| **Subdocumento** | Indexa todo el contenido de un documento/subdocumento anidado | Indexar objeto completo `{vacunas: {...}}` |
| **Embebido** | Indexa un campo específico dentro de un subdocumento | `db.mascotas.createIndex({"dueño.telefono": 1})` |
| **Compuesto** | Indexa varios campos combinados | `db.mascotas.createIndex({"especie": 1, "edad": -1})` |
| **Temporal (TTL)** | Expira y se autoelimina tras un tiempo definido | `db.sesiones.createIndex({"fecha": 1}, {expireAfterSeconds: 3600})` |

---

## 4. Opciones al crear un índice

```javascript
// unique: impide valores duplicados
db.mascotas.createIndex({ "microchip": 1 }, { unique: true })

// sparse: solo indexa documentos que SÍ tienen ese campo
db.mascotas.createIndex({ "alergia_conocida": 1 }, { sparse: true })

// background: crea el índice sin bloquear la base de datos
db.mascotas.createIndex({ "especie": 1 }, { background: true })
```

**Ejemplo veterinario:** `unique: true` en el campo de microchip evita registrar el mismo chip dos veces — equivalente NoSQL a una restricción de clave primaria en SQL.

---

## 5. Consultas cubiertas por índices ("covered queries")

Las consultas más eficientes posibles: cuando todos los campos pedidos y filtrados ya están dentro del índice, MongoDB responde directo desde el índice sin leer el documento completo.

```javascript
db.mascotas.createIndex({ "especie": 1, "nombre": 1 })

db.mascotas.find({ "especie": "Perro" }, { "nombre": 1, "especie": 1, "_id": 0 })
```

---

## 📚 Referencias

Guía de la Unidad 9 — Universidad DaVinci (2026). MongoDB, la base de datos.
