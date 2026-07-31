# 🍃 U10 — Bases de Datos NoSQL y Almacenamiento Escalable

**Asignatura:** Bases de Datos y Bases de Datos NoSQL
**Semana:** S8

---

## 1. Repaso: ¿qué es NoSQL?

"Not Only SQL" — surgió después del año 2000 para resolver volumen masivo de datos, alta velocidad, y estructuras de datos poco definidas o cambiantes.

## 2. Sistemas centralizados vs. distribuidos

| | Centralizado | Distribuido |
|---|---|---|
| Arquitectura | Un solo servidor | Varios nodos interconectados, se ven como una unidad |
| Ventajas | Simplicidad | Económico, velocidad, disponibilidad, flexibilidad |
| Desventajas | No escala bien | Requiere coordinación, depuración y manejo de fallos más complejo |

## 3. Estrategias de distribución de datos

| Estrategia | Qué hace |
|---|---|
| Fragmentación horizontal | Divide filas según una condición |
| Fragmentación vertical | Divide columnas/atributos en grupos |
| Fragmentación híbrida | Combina ambas |
| Replicación | Guarda copias completas/parciales en varios nodos |

| | Fragmentación | Replicación |
|---|---|---|
| ✅ | Más concurrencia y paralelismo | Mayor disponibilidad |
| ❌ | Rendimiento empeora al juntar fragmentos de varios nodos | Inserciones/actualizaciones menos eficientes |

## 4. Teorema CAP

Un sistema distribuido no puede garantizar simultáneamente las 3 propiedades — máximo dos a la vez.

| Propiedad | Significado |
|---|---|
| C — Consistencia | Todos los nodos ven la misma información al mismo tiempo |
| A — Disponibilidad | El sistema siempre responde algo válido |
| P — Tolerancia a particiones | Sigue funcionando aunque haya fallos de comunicación entre nodos |

Las particiones de red son inevitables → P es obligatoria → la decisión real es entre C o A:

| Prioriza | Ejemplos |
|---|---|
| AP (disponibilidad) | Cassandra, Riak |
| CP (consistencia) | MongoDB, HBase |

Las bases de datos relacionales distribuidas son sistemas **CA**.

## 5. Modelo ACID vs. BASE

| ACID (relacional) | BASE (NoSQL tipo AP) |
|---|---|
| Atomicidad, Consistencia, Aislamiento, Durabilidad | Basically Available, Soft state, Eventually consistent |

MongoDB usa *replica sets* (variante maestro-esclavo): escrituras y lecturas van a la copia primaria por defecto (comportamiento CP), aunque se puede configurar leer de secundarias (comportamiento más AP).

## 6. Modelos de datos NoSQL

| Modelo | Cómo almacena | Sistema | Cuándo usarlo |
|---|---|---|---|
| Clave-valor | Par (clave, valor), motor no conoce estructura interna | Cassandra, HBase | Accesos muy rápidos por clave |
| Documental | Documentos JSON/XML, estructura implícita | MongoDB | Datos heterogéneos, estructura variable |
| Columnas | Filas agrupadas en "familias de columnas" | Big Table, Cassandra | Grandes volúmenes analíticos |
| Grafos | Nodos + aristas | Neo4j | Cuando importan más las relaciones que los datos en sí |

---

## 📚 Referencias

Guía de la Unidad 10 — Universidad DaVinci (2026). Bases de Datos NoSQL y el Almacenamiento Escalable.

Brewer, E. A. (2000). *Towards robust distributed systems* [Conferencia]. PODC 2000, ACM Symposium on Principles of Distributed Computing.
