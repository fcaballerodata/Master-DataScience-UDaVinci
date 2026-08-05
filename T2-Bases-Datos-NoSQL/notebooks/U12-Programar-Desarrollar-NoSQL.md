# 🍃 U12 — Programar y Desarrollar con Bases de Datos NoSQL

**Asignatura:** Bases de Datos y Bases de Datos NoSQL
**Semana:** S9

---

## 1. Repaso — mapa mental NoSQL

| | |
|---|---|
| Características | Escalabilidad horizontal, flexibilidad de esquema |
| Ventajas | Comunidad activa, fiabilidad, mayor escalabilidad horizontal |
| Desventajas | Menor consistencia por defecto, sin JOINs nativos, requiere más conocimiento especializado |
| Tipos | Clave-valor, documentales, en grafo |
| Ejemplos | MongoDB, Cassandra, Redis, CouchDB |

## 2. Conexión de MongoDB con Java

1. Descargar el driver (`mongo-db.jar`)
2. Crear proyecto en Eclipse (JDK instalado)
3. Agregar el driver: click derecho → `Build Path → Add External JARs`
4. Convertir a Maven (`Configure → Convert to Maven Project`) para gestionar dependencias vía `pom.xml`
5. Crear clase de conexión (`ConexionMongo.java`)
6. Verificar que `mongod` esté corriendo antes de ejecutar el código

## 3. Shell de MongoDB

```javascript
help
db.help()
db.mascotas.help()
db.mascotas.find().help()
```

## 4. CRUD completo

```javascript
// Insertar
db.mascotas.insert({ Nombre: "Rocky", Raza: "Labrador", Edad: 2 })

// Buscar (con regex insensible a mayúsculas)
db.mascotas.find({ Nombre: /roc/i })

// Actualizar — update() reemplaza el documento COMPLETO
db.mascotas.update(
  { Nombre: "Rocky" },
  { Nombre: "Rocky", Raza: "Labrador", Edad: 3 }
)

// Eliminar — puede borrar VARIOS documentos si el filtro coincide con más de uno
db.mascotas.remove({ Nombre: "Rocky" })
```

## 5. Operadores de comparación, existencia y lógicos

```javascript
db.mascotas.find({ Edad: { $gt: 3 } })
db.mascotas.find({ Edad: { $lt: 3 } })
db.mascotas.find({ Edad: { $gte: 3 } })
db.mascotas.find({ Edad: { $lte: 3 } })

db.mascotas.find({ alergia_conocida: { $exists: true } })
db.mascotas.find({ alergia_conocida: { $exists: false } })

db.mascotas.find({ $and: [ { Raza: "Labrador" }, { Edad: 2 } ] })
db.mascotas.find({ $or: [ { Nombre: "Rocky" }, { Nombre: "Firulais" } ] })
```

## 6. Ordenación, conteo y paginación

```javascript
db.mascotas.find().pretty()
db.mascotas.find().sort({ Nombre: 1 })    // A→Z
db.mascotas.find().sort({ Nombre: -1 })   // Z→A
db.mascotas.find().count()
db.mascotas.find().limit(3)
db.mascotas.find().skip(2)
db.mascotas.find().skip(3).limit(3)       // paginación
```

## 7. Joins en NoSQL — `$lookup`

```javascript
db.mascotas.aggregate([
  {
    $lookup: {
      from: "duenos",
      localField: "id_dueno",
      foreignField: "_id",
      as: "info_dueno"
    }
  }
])
```

Equivalente funcional a un `INNER JOIN`, pero el resultado queda anidado dentro del mismo documento. Si la lógica de unión se vuelve compleja, reconsiderar el diseño: quizás esos datos debieron anidarse desde el inicio.

---

## 📚 Referencias

Guía de la Unidad 12 — Universidad DaVinci (2026). Programar y desarrollar con bases de datos NoSQL.
