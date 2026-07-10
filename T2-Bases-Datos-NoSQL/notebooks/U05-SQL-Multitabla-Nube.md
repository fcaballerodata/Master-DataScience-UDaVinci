# 🗄️ U5 — SQL Multitabla y Bases de Datos en la Nube

**Asignatura:** Bases de Datos y Bases de Datos NoSQL
**Semana:** S5 (6-11 Jul 2026)

---

## PARTE 1 — SQL Multitabla

### Sintaxis SQL-86 vs SQL-92

```sql
-- SQL-86 (producto cartesiano + filtro en WHERE)
SELECT * FROM Mascotas, Dueños
WHERE Mascotas.id_dueño = Dueños.id_dueño;

-- SQL-92 (JOIN explícito) — estándar actual
SELECT * FROM Mascotas
INNER JOIN Dueños ON Mascotas.id_dueño = Dueños.id_dueño;
```

### Producto cartesiano (CROSS JOIN)

Combina cada fila de la tabla A con cada fila de la tabla B, sin filtro. Es la base teórica de todo JOIN: el INNER JOIN es ese producto cartesiano filtrado para conservar solo las coincidencias de clave.

### Tipos de JOIN

| Tipo | Qué devuelve |
|---|---|
| **INNER JOIN** | Solo filas con coincidencia en ambas tablas |
| **LEFT JOIN** | Todas las filas de la izquierda + coincidencias de la derecha (NULL si no hay) |
| **RIGHT JOIN** | Todas las filas de la derecha + coincidencias de la izquierda |
| **FULL OUTER JOIN** | Todo de ambas tablas, coincida o no |

```sql
SELECT m.nombre, d.nombre_dueño
FROM Mascotas m
INNER JOIN Dueños d ON m.id_dueño = d.id_dueño;
```

**⚠️ MySQL no implementa FULL OUTER JOIN nativamente.** Se simula con `UNION`:

```sql
SELECT m.nombre, d.nombre_dueño FROM Mascotas m
LEFT JOIN Dueños d ON m.id_dueño = d.id_dueño
UNION
SELECT m.nombre, d.nombre_dueño FROM Mascotas m
RIGHT JOIN Dueños d ON m.id_dueño = d.id_dueño;
```

### Self-JOIN

Une una tabla consigo misma; requiere alias obligatoriamente.

```sql
SELECT e.nombre AS empleado, s.nombre AS supervisor
FROM Empleados e
INNER JOIN Empleados s ON e.id_supervisor = s.id_empleado;
```

### GROUP BY y funciones de agregación

```sql
SELECT veterinario, COUNT(*) AS num_consultas, SUM(costo) AS total_facturado
FROM Consultas
GROUP BY veterinario;
```

Funciones más usadas: `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()`.

**Regla clave:** en el `SELECT`, toda columna debe estar en el `GROUP BY` o dentro de una función de agregación.

### DISTINCT

```sql
SELECT DISTINCT veterinario FROM Consultas;
```

---

## PARTE 2 — Bases de Datos en la Nube

### DBaaS vs modelo tradicional

| Modelo | Quién administra |
|---|---|
| Nube tradicional | El usuario instala y administra el DBMS sobre infraestructura rentada |
| **DBaaS** | El proveedor administra todo: parches, backups, escalado, seguridad |

### Ecosistema Oracle

- **Oracle Autonomous Database:** se auto-ajusta, auto-repara y auto-protege usando machine learning.
- **Oracle Exadata:** infraestructura hardware/software optimizada donde corre Autonomous Database.
- **Oracle Database Service for Azure:** estrategia multi-nube — Oracle dentro del ecosistema de Microsoft Azure.

### NoSQL en la nube

- **MongoDB Atlas:** MongoDB completamente gestionado, distribuido geográficamente.
- **Elasticsearch:** motor de búsqueda y análisis (no transaccional) — ideal para búsquedas de texto y monitoreo de logs.

### Tendencias actuales de bases de datos

1. Automatización de DBMS
2. SGBD aumentado (impulsado por IA)
3. Aumento de la seguridad
4. Bases de datos en memoria
5. DBMS de código abierto
6. Database as a Service (DBaaS)

---

## 📚 Referencias

Guía de la Unidad 5 — Universidad DaVinci (2026).
