# Actividad Práctica 2 — U6 a U13

**Asignatura:** Bases de Datos y Bases de Datos No SQL II
**Semana:** S9

Objetivo general: analizar tendencias de bases de datos SQL, NoSQL y en la nube, reflexionando sobre competencias y conocimiento propio.

---

## Producto 1 — Infografía: Tendencias de BD en la Nube y SQL/NoSQL

*(Entregada como imagen/PDF diseñada aparte — este documento resume su contenido en texto.)*

### Parte 1 — Tendencia de las bases de datos en la nube

El modelo Database as a Service (DBaaS) —donde el proveedor administra parches, backups y escalado— es el segmento de más rápido crecimiento dentro del mercado de bases de datos. Empresas de todos los tamaños migran cargas de trabajo completas hacia la nube por su escalabilidad y menor costo operativo.

**Datos clave:**

| Estadística | Valor | Fuente |
|---|---|---|
| Tamaño estimado del mercado global de BD en la nube y DBaaS (2026) | $201B | Business Research Insights, 2026 |
| Tasa de crecimiento anual compuesta (CAGR) proyectada hacia 2030 | ~20% | Mordor Intelligence, 2026 |
| Despliegues de BD en la nube que usarán funciones de IA para 2026 | 60% | Platform 3 Solutions, vía Mordor Intelligence, 2026 |

**Impulsores de la tendencia:**

1. **Autonomía impulsada por IA** — motores como Oracle Autonomous Database se auto-ajustan, auto-reparan y auto-protegen sin intervención constante del DBA (visto en Unidad 5).
2. **Multi-nube** — AWS, Microsoft Azure, Google Cloud y Oracle compiten activamente; muchas empresas combinan más de un proveedor para evitar el "vendor lock-in".
3. **Seguridad** — el cumplimiento normativo y la protección de datos sensibles son ahora criterios de decisión tan importantes como el precio o el rendimiento.

### Parte 2 — SQL, NoSQL y sus tendencias futuristas

Durante más de una década se habló de SQL contra NoSQL como una competencia con un ganador. En 2026 esa narrativa cambió: las líneas se difuminan, y las decisiones de arquitectura giran en torno a combinar ambos mundos según la carga de trabajo específica.

**SQL se vuelve más flexible:**
- Soporte nativo de JSON en PostgreSQL y MySQL
- Extensiones como `pgvector` para búsqueda vectorial dentro del motor relacional
- NewSQL (CockroachDB, YugabyteDB, Google Spanner): ACID + escalado horizontal, antes exclusivo de NoSQL

**NoSQL se vuelve más estricto:**
- MongoDB incorpora transacciones multi-documento y cifrado avanzado
- Búsqueda vectorial nativa para aplicaciones de IA generativa (RAG)
- Bases multi-modelo (ArangoDB, Couchbase) combinan documentos, grafos y relaciones en un solo motor

**Tendencias futuristas a observar:** bases de datos vectoriales, NewSQL, persistencia políglota, bases multi-modelo, consultas generadas con IA, serverless databases.

**Dato clave:** Gartner proyecta que más del 40% de las aplicaciones de IA dependerán de búsqueda vectorial para 2026, frente a menos del 5% pocos años atrás — el motor detrás de la convergencia SQL/NoSQL (Apidots, 2026, citando a Gartner, 2024).

---

## 📚 Referencias

Business Research Insights. (2026). *Cloud Database and DBaaS Market Size, Trends*.

Mordor Intelligence. (2026). *Cloud Database and DBaaS Market Size & Share Analysis*.

Fortune Business Insights. (2026). *Cloud Database Market Size, Share*.

AI2SQL. (2026). *SQL vs NoSQL in 2026: Key Differences & How to Choose*.

Instaclustr. (2026). *11 amazing use cases for NoSQL in 2026*.

Apidots. (2026). *SQL vs NoSQL in the Age of AI* (cita a Gartner, 2024).

Universidad DaVinci. (2026). Guías académicas Unidades 5, 8 y 10 — BDNS.
