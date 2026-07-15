# 🗄️ U6 — Bases de Datos Relacionales (a fondo)

**Asignatura:** Bases de Datos y Bases de Datos NoSQL
**Semana:** S6

---

## 1. Modelo de datos — 3 niveles de abstracción

| Nivel | Qué describe | Ejemplo |
|---|---|---|
| **Conceptual** | Estructura y reglas del negocio, sin pensar en tecnología | "Una Mascota pertenece a un Dueño" (diagrama E-R) |
| **Lógico** | Cómo se traduce a un modelo implementable | Tabla MASCOTAS con columna id_dueño |
| **Físico** | Cómo lo guarda el DBMS en disco | Estructura de archivos e índices |

Dos sub-lenguajes:
- **DDL** (Data Definition Language): `CREATE`, `ALTER`, `DROP`
- **DML** (Data Manipulation Language): `SELECT`, `INSERT`, `UPDATE`, `DELETE`

---

## 2. Tipos de datos

| Tipo genérico | Ejemplo |
|---|---|
| Texto | Nombre de la mascota |
| Numérico | Peso en kg |
| Fecha/hora | Fecha de la consulta |
| Sí/No | ¿Está vacunado? |
| Autonumérico | id_mascota |
| Moneda | Costo de la consulta |

---

## 3. Claves primarias — 3 reglas

1. No puede contener valores NULL
2. No se puede repetir en ninguna fila (unicidad)
3. Cada tabla solo puede tener UNA clave primaria

```sql
CREATE TABLE Mascotas (
    id_mascota INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    especie VARCHAR(30)
);
```

---

## 4. Índices

Estructura auxiliar de búsqueda rápida, como el índice de un libro.

```sql
CREATE INDEX idx_especie ON Mascotas (especie);
DROP INDEX idx_especie ON Mascotas;
```

**Trade-off:** aceleran `SELECT`/`WHERE`, pero ralentizan `INSERT`/`UPDATE` (el índice también debe actualizarse).

---

## 5. El valor NULL

NULL significa "desconocido", no "vacío" ni "cero". No se compara con `=`, se usa `IS`/`IS NOT`.

```sql
SELECT * FROM Mascotas WHERE apodo IS NULL;
SELECT * FROM Mascotas WHERE apodo IS NOT NULL;
```

---

## 6. Claves ajenas (foreign keys)

```sql
CREATE TABLE Consultas (
    id_consulta INT PRIMARY KEY,
    id_mascota INT,
    fecha DATE,
    FOREIGN KEY (id_mascota) REFERENCES Mascotas(id_mascota)
);
```

Solo puede contener valores que ya existan como clave primaria en la tabla referenciada — garantiza integridad referencial.

---

## 7. Vistas (VIEWS)

"Tablas virtuales" — no almacenan datos propios, son un `SELECT` guardado.

```sql
CREATE VIEW ConsultasResumen AS
SELECT m.nombre AS mascota, c.fecha, c.costo
FROM Consultas c
INNER JOIN Mascotas m ON c.id_mascota = m.id_mascota;
```

**Usos:** control de acceso (exponer solo columnas necesarias), reutilización de consultas complejas, mantenimiento de integridad ante cambios de esquema.

---

## 8-9. DDL y DCL

| Lenguaje | Verbos | Propósito |
|---|---|---|
| DDL | CREATE, ALTER, DROP | Definir/modificar estructura |
| DCL | GRANT, REVOKE | Dar/quitar permisos |

```sql
GRANT SELECT ON Mascotas TO analista_bi;
REVOKE SELECT ON Mascotas FROM analista_bi;
```

---

## 📚 Referencias

Guía de la Unidad 6 — Universidad DaVinci (2026). Bases de datos relacionales.
