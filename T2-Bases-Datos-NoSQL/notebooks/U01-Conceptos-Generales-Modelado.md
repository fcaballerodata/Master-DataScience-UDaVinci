# 🗄️ U1 — Conceptos Generales y Modelado de BD

**Asignatura:** Bases de Datos y Bases de Datos NoSQL  
**Semana:** S1 (8–13 Jun 2026)

---

## 🎯 Conceptos clave

El modelado de datos es el plano arquitectónico antes de construir una base de datos. Un mal diseño inicial es carísimo de corregir después.

---

## 1. Del sistema de archivos al DBMS

### El problema original

Sin DBMS, la información vivía en archivos aislados (Excel, CSV por departamento):

| Problema | Consecuencia |
|---|---|
| **Duplicidad de datos** | "Juan Pérez" en 3 archivos distintos — si cambia el teléfono, hay que actualizarlo en todos |
| **Conflictos de acceso** | Dos personas editando el mismo archivo simultáneamente |
| **Dificultad de cruce** | No hay forma eficiente de responder: ¿cuántas consultas tuvo la mascota de Juan el último año? |

### La solución: DBMS

Un **DBMS** (Database Management System) actúa como intermediario entre las aplicaciones y los datos físicos. El usuario nunca toca los archivos físicos — simplemente escribe una consulta SQL.

> **Contexto Movet/Snowflake:** cuando escribías consultas SQL en Snowflake, estabas usando un DBMS cloud de 4ª generación. Snowflake es el intermediario — nunca tocaste los archivos subyacentes.

**Ejemplos de DBMS:** MySQL, SQL Server, Oracle, PostgreSQL, Snowflake, MongoDB.

---

## 2. Evolución histórica — Las 4 generaciones

| Generación | Época | Tipo | Aporte clave |
|---|---|---|---|
| 1ª | 1960s | Archivos | Búsquedas básicas |
| 2ª | 1970s | Navegacional (redes/jerarquías) | Estándares CODASYL |
| 3ª | 1980s | **Relacional** | SQL, lenguajes no procedurales |
| 4ª | 1990s–hoy | Objeto / Multimedia / Cloud | Data warehouse, NoSQL, cloud |

> Snowflake y MongoDB son **4ª generación**. Por eso este curso los estudia juntos.

---

## 3. ¿Qué contiene una Base de Datos?

Una BD no es solo tablas — contiene 4 tipos de datos:

1. **Datos del usuario** — las tablas con información real (clientes, mascotas, consultas)
2. **Metadatos** — descripción de la estructura ("la tabla `consultas` tiene los campos: id, fecha, diagnóstico...")
3. **Índices** — estructuras internas que aceleran búsquedas (como el índice de un libro)
4. **Metadatos de aplicación** — información sobre formularios y reportes que usan la BD

---

## 4. Modelado de Datos

### Tipos de modelos

| Modelo | Estructura | Uso típico |
|---|---|---|
| **Jerárquico** | Árbol (padre-hijo) | Sistemas legacy, XML |
| **En red** | Nodos con múltiples conexiones | CODASYL |
| **Relacional** | Tablas relacionadas | SQL — el más usado hoy |
| **Orientado a objetos** | Objetos con herencia | Ingeniería, CAD |
| **Transaccional** | Optimizado para alto volumen | Sistemas bancarios |

---

## 5. Modelo Entidad-Relación (E-R)

Herramienta para diseñar una BD **antes** de implementarla.

### Diagrama E-R — Movet

```
[DUEÑO] ──────(tiene)────── [MASCOTA] ──────(tiene)────── [CONSULTA]
  │                              │                              │
  ├─ id_dueño                    ├─ id_mascota                 ├─ id_consulta
  ├─ nombre                      ├─ nombre                     ├─ fecha
  ├─ teléfono                    ├─ especie                    ├─ diagnóstico
  └─ dirección                   ├─ raza                       ├─ costo
                                 └─ fecha_nacimiento            └─ id_veterinario

Cardinalidades:
  DUEÑO ──(1:N)── MASCOTA    → un dueño puede tener muchas mascotas
  MASCOTA ──(1:N)── CONSULTA → una mascota puede tener muchas consultas
```

### E-R vs Modelo Relacional

| Modelo E-R | Modelo Relacional |
|---|---|
| Alto nivel, conceptual | Bajo nivel, implementable |
| Habla de entidades y relaciones | Habla de tablas y columnas |
| Para **diseñar** | Para **implementar en SQL** |

> **El flujo:** E-R → Normalización → Modelo Relacional → SQL

---

## 6. Normalización — Las reglas de oro

Normalizar = organizar datos para eliminar redundancia y garantizar integridad.

### Tabla MAL diseñada (sin normalizar)

| id_consulta | fecha | mascota | especie | dueño | teléfono | veterinario |
|---|---|---|---|---|---|---|
| 1 | 2025-01-10 | Firulais | Perro | Juan Pérez | 3001234567 | Dra. López |
| 2 | 2025-01-15 | Firulais | Perro | Juan Pérez | 3001234567 | Dr. Gómez |

**Problema:** si Juan cambia de teléfono → hay que actualizar múltiples filas.

### Formas Normales

| Forma Normal | Elimina |
|---|---|
| **1FN** | Grupos repetidos — cada celda tiene un solo valor atómico |
| **2FN** | Dependencias parciales — cada columna depende de TODA la clave |
| **3FN** | Dependencias transitivas — ninguna columna depende de otra no-clave |

### Tabla BIEN diseñada (3FN)

```sql
-- Tabla DUEÑOS
CREATE TABLE duenos (
    id_dueno   INT PRIMARY KEY,
    nombre     VARCHAR(100),
    telefono   VARCHAR(20)
);

-- Tabla MASCOTAS
CREATE TABLE mascotas (
    id_mascota      INT PRIMARY KEY,
    nombre          VARCHAR(50),
    especie         VARCHAR(20),
    id_dueno        INT REFERENCES duenos(id_dueno)
);

-- Tabla CONSULTAS
CREATE TABLE consultas (
    id_consulta     INT PRIMARY KEY,
    fecha           DATE,
    diagnostico     VARCHAR(200),
    id_mascota      INT REFERENCES mascotas(id_mascota)
);
```

Ahora si Juan cambia el teléfono → se actualiza **un solo registro** en `duenos`. ✅

> **Excepción real:** en data warehouses como Snowflake, a veces se **desnormaliza** intencionalmente para mejorar el rendimiento de queries analíticas. En Movet probablemente tenías tablas anchas para los dashboards de Power BI — eso es desnormalización controlada.

---

## 🗺️ Mapa mental

```
U1: CONCEPTOS GENERALES Y MODELADO DE BD
│
├── Del archivo al DBMS
│     ├── Problema: duplicidad, rigidez, conflictos de acceso
│     └── Solución: DBMS como intermediario
│
├── 4 generaciones
│     └── Archivo → Navegacional → Relacional → Objeto/Cloud
│
├── Modelado de datos
│     ├── Tipos: Jerárquico, Red, Relacional, OO, Transaccional
│     └── Resultado: esquema + transacciones
│
├── Modelo E-R
│     ├── Entidades (fuertes y débiles)
│     ├── Atributos y relaciones
│     └── Cardinalidad: 1:1, 1:N, N:M
│
└── Normalización
      ├── 1FN → valores atómicos
      ├── 2FN → dependencia total de la clave
      └── 3FN → sin dependencias transitivas
```

---

## 📚 Referencias

Beynon-Davies, P. (2018). *Sistemas de bases de datos*. Reverté.
