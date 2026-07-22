# 🍃 U8 — Presentación a las Bases de Datos NoSQL

**Asignatura:** Bases de Datos y Bases de Datos NoSQL
**Semana:** S7

---

## 1. SQL vs. NoSQL — 6 dimensiones de comparación

### Integridad de datos

| SQL | NoSQL |
|---|---|
| Restricciones estrictas (claves primarias, tipos definidos, relaciones) | Más flexible, no obliga estructura fija |

### Operaciones atómicas

Una operación atómica se ejecuta completa o no se ejecuta en absoluto.

- **SQL:** con tablas relacionadas, una sola transacción puede modificar varias tablas atómicamente.
- **NoSQL:** al no estar las colecciones relacionadas, coordinar cambios requiere actualizar una por una — más engorroso, pero evita el costo de rendimiento de garantizar atomicidad.

### Redundancia y consistencia

| Concepto | Definición |
|---|---|
| Redundancia | Un mismo dato repetido en varios lugares |
| Consistencia | Un dato único aparece una sola vez y no se desincroniza |

SQL usa normalización para minimizar redundancia. NoSQL acepta cierta redundancia a propósito (duplicar dentro de un documento) para evitar JOINs.

### Velocidad

- **SQL:** con más volumen y JOINs, las búsquedas pueden ralentizarse — se mitiga optimizando índices y rediseñando el esquema.
- **NoSQL:** al consultar una sola colección sin relaciones que resolver, tiende a tiempos de carga más bajos a gran escala.

### Escalabilidad

| Tipo | SQL | NoSQL |
|---|---|---|
| Vertical (mejorar un servidor) | Fortaleza natural | Funciona, no es su punto fuerte |
| Horizontal (varios servidores) | Posible pero complejo | Fortaleza natural |

### Comodidad y herramientas

SQL: más comunidad, documentación y herramientas maduras (phpMyAdmin, etc.). NoSQL: menos configuración inicial, curva de aprendizaje distinta.

---

## 2. Guía de decisión rápida

| Usa SQL si... | Usa NoSQL si... |
|---|---|
| Necesitas datos consistentes, sin errores ni pérdidas | Necesitas velocidad de lectura/escritura por encima de todo |
| Tus datos se relacionan entre sí | No necesitas relaciones estructuradas |
| Necesitas el máximo ecosistema de herramientas | Estructura de datos muy variable |
| No tienes equipos muy potentes | Tienes varios equipos modestos, necesitas escalar horizontalmente |

**Patrón real de la industria:** muchos proyectos usan ambas — NoSQL para lo que requiere respuesta rápida (catálogo, logs, sesiones) y SQL para lo que requiere integridad (facturación, contabilidad).

---

## 3. Ventajas resumidas

| SQL | NoSQL |
|---|---|
| Mayor soporte, herramientas y comunidad | Escalabilidad horizontal |
| Atomicidad | No requiere equipos muy potentes |
| Estándares bien definidos | Facilidad de optimización |
| Sencillez conceptual (tablas) | Versatilidad de estructura |

---

## 📚 Referencias

Guía de la Unidad 8 — Universidad DaVinci (2026). Presentación a las bases de datos NoSQL.
