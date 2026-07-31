# 🍃 U11 — MongoDB en la Práctica

**Asignatura:** Bases de Datos y Bases de Datos NoSQL
**Semana:** S8

---

## 1. Instalación (resumen)

MongoDB se descarga desde `mongodb.com/try/download/community`. El servidor (`mongod.exe`) corre en segundo plano escuchando el puerto **27017**; la interfaz gráfica recomendada es Studio 3T, más amigable que la consola `mongosh`.

## 2. Documentos, colecciones y flexibilidad de esquema

```javascript
use veterinaria

db.mascotas.insertOne({
  nombre: "Firulais",
  especie: "Perro",
  edad: 4,
  vacunas: ["rabia", "parvovirus", "moquillo"],
  dueño: { nombre: "Ana Gómez", telefono: "555-1111" }
})

// Misma colección, estructura DISTINTA (imposible en SQL)
db.mascotas.insertOne({
  nombre: "Michi",
  especie: "Gato",
  observaciones: "Alérgico a ciertos antibióticos"
})
```

## 3. Insertar, actualizar y eliminar

```javascript
db.mascotas.insertOne({_id: 101, nombre: "Rocky", especie: "Perro"})

// insert falla si la clave ya existe; replaceOne actualiza o crea
db.mascotas.replaceOne({_id: 101}, {nombre: "Rocky", especie: "Perro", peso: 22})

db.mascotas.update(
  { _id: 101 },
  { $set: { peso: 23, estado: "en tratamiento" } }
)
```

**Operadores de actualización:**

| Operador | Qué hace |
|---|---|
| `$set` | Modifica o agrega campos |
| `$unset` | Elimina campos |
| `$inc` | Incrementa un valor numérico |
| `$rename` | Renombra un campo |
| `$push` | Agrega un elemento a un array |
| `$pull` | Elimina elementos de un array que cumplan una condición |
| `$addToSet` | Agrega a un array solo si no existe ya |

```javascript
db.mascotas.update(
  { _id: 101 },
  { $addToSet: { vacunas: "leptospirosis" } }
)
```

**Eliminar:**
```javascript
db.mascotas.remove({ _id: 101 })
db.mascotas.drop()
db.dropDatabase()
```

## 4. Índices — cardinalidad y estructura B-Tree

MongoDB construye índices como árboles B (B-Tree). **Cardinalidad:** un índice es más eficiente cuanto más únicos son sus valores.

- ❌ Mal candidato: `edad` (muchos valores repetidos)
- ✅ Buen candidato: `microchip` (único)
- ✅ Alternativa: crear un campo derivado tipo rango (`"0-2 años"`) en vez del valor exacto

```javascript
db.mascotas.createIndex({ "especie": 1 })
db.mascotas.createIndex({ "especie": 1, "estado": 1 })          // compuesto
db.mascotas.createIndex({ "dueño.telefono": 1 })                 // subdocumento
db.mascotas.createIndex({ "vacunas": 1 })                        // array (solo uno por índice)

db.mascotas.getIndexes()
db.mascotas.dropIndex({ "especie": 1 })
db.mascotas.dropIndexes()
```

## 5. Planes de ejecución

```javascript
db.mascotas.find({ especie: "Perro", estado: "en tratamiento" }).explain("executionStats")
```

| `stage` | Significado |
|---|---|
| COLLSCAN | Recorrió TODA la colección — sin índice (lento) |
| IXSCAN | Usó un índice — rápido |

**Consulta totalmente cubierta (covered query):** todos los campos consultados y devueltos ya están en el índice — no requiere leer el documento completo.

## 6. Consultas y funciones de agregación

```javascript
db.mascotas.find({ especie: "Gato" })
db.mascotas.find({ edad: { $lt: 3 } })
db.mascotas.find({ especie: "Perro", estado: "en tratamiento" })

db.mascotas.find({ especie: "Perro" }).count()
db.mascotas.distinct("especie")
```

## 7. Ventajas e inconvenientes de los índices

| ✅ Ventajas | ❌ Inconvenientes |
|---|---|
| Reduce tiempo de respuesta | Ralentiza inserciones |
| Reduce carga de disco | Índice compuesto: mejor para búsquedas, peor para ordenar por campos individuales |

---

## 📚 Referencias

Guía de la Unidad 11 — Universidad DaVinci (2026). Introducción a un sistema de Base de Datos NoSQL, MongoDB.
