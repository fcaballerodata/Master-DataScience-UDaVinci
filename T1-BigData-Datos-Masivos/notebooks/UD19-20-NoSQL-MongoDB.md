# 📊 UD19-20 — NoSQL, Teorema CAP y MongoDB

**Trimestre 1 · S10 (May 2026)**

---

## 1. Teorema CAP

El Teorema CAP (Brewer, 2000) establece que un sistema de datos distribuido no puede garantizar simultáneamente las tres propiedades:

| Propiedad | Descripción |
|---|---|
| **C — Consistency** | Todos los nodos ven los mismos datos al mismo tiempo |
| **A — Availability** | Cada petición recibe una respuesta (no necesariamente la más reciente) |
| **P — Partition Tolerance** | El sistema sigue operando aunque fallen conexiones entre nodos |

**Solo puedes elegir 2 de las 3:**

| Sistema | Prioriza | Sacrifica |
|---|---|---|
| RDBMS (MySQL, PostgreSQL) | CA | P |
| MongoDB | CP | A (en partición) |
| Cassandra | AP | C |
| DynamoDB | AP | C |

---

## 2. Modelos NoSQL

| Tipo | Estructura | Ejemplo | Caso de uso |
|---|---|---|---|
| **Documentos** | JSON/BSON | MongoDB | Catálogos, perfiles de usuario |
| **Clave-Valor** | Par key:value | Redis, DynamoDB | Caché, sesiones |
| **Columnar** | Familias de columnas | Cassandra, HBase | Series temporales, IoT |
| **Grafos** | Nodos y aristas | Neo4j | Redes sociales, recomendaciones |

---

## 3. ACID vs BASE

| ACID (SQL) | BASE (NoSQL) |
|---|---|
| **A**tomicity — todo o nada | **B**asically **A**vailable — siempre responde |
| **C**onsistency — reglas de integridad | **S**oft state — estado puede cambiar |
| **I**solation — transacciones aisladas | **E**ventually consistent — consistencia eventual |
| **D**urability — cambios permanentes | Prioriza disponibilidad sobre consistencia |

---

## 4. MongoDB — CRUD básico

```javascript
// Insertar
db.mascotas.insertOne({ nombre: "Firulais", especie: "Perro", peso: 22.5 })
db.mascotas.insertMany([
    { nombre: "Michi", especie: "Gato", peso: 4.2 },
    { nombre: "Rex",   especie: "Perro", peso: 35.0 }
])

// Leer
db.mascotas.find()                              // todos
db.mascotas.find({ especie: "Perro" })          // filtrar
db.mascotas.findOne({ nombre: "Firulais" })     // primero que cumple
db.mascotas.find({ peso: { $gt: 20 } })         // peso > 20

// Actualizar
db.mascotas.updateOne(
    { nombre: "Firulais" },
    { $set: { peso: 23.0 } }
)

// Eliminar
db.mascotas.deleteOne({ nombre: "Firulais" })
db.mascotas.deleteMany({ especie: "Gato" })
```

---

## 📚 Referencias

Brewer, E. (2012). CAP twelve years later: How the "rules" have changed. *IEEE Computer*, 45(2), 23-29.

MongoDB Inc. (2024). *MongoDB documentation*. https://www.mongodb.com/docs/
