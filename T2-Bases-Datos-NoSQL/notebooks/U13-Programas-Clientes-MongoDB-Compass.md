# 🍃 U13 — Programas Clientes para NoSQL y MongoDB Compass

**Asignatura:** Bases de Datos y Bases de Datos NoSQL
**Semana:** S9

---

## 1. Programas clientes más populares para MongoDB

| Programa | Lo distintivo |
|---|---|
| NoSQL Booster | Centrado en la Shell, Mac/Linux/Windows, gratuita y comercial |
| Studio 3T | Migra proyectos de SQL a MongoDB, automatiza tareas, de pago |
| Nucleon Database Master | Editor de archivos JSON muy potente |
| NoSQL Manager | Interfaz sencilla, importa tablas desde MySQL y SQL Server |
| Mongo Management Studio | Versión gratuita + Enterprise de pago |
| Aqua Data Studio | Ejecuta comandos JavaScript en su propia Shell |
| NoSQLclient | Gratis, código abierto, sin instalación, multiplataforma |
| **MongoDB Compass** | Programa oficial de MongoDB Inc. |

## 2. Drivers vs. programas clientes

Un **driver** conecta tu aplicación/código con MongoDB (traduce entre el lenguaje de programación y el formato de documentos). Un **programa cliente** es para que tú administres visualmente la base de datos. Ya se usó el driver de Java en la Unidad 12.

## 3. Instalación de MongoDB Compass

1. `mongodb.com` → "Try Free"
2. "Tools" → "Compass"
3. Elegir sistema operativo, descargar última versión estable
4. Al abrir: "Next" en las ventanas de configuración → "Connect"

## 4. Crear una base de datos con Compass

1. Click en "My Cluster"
2. Click en "Create Database"
3. Definir nombre de base de datos + nombre de la primera colección
4. Click en "Create Database"

## 5. CRUD completo en Compass

**Insertar:** "Insert Document" → editor tipo formulario JSON, eligiendo tipo de dato explícito (String, Double, Boolean) → "Insert"

**Editar:** cursor sobre el documento → ícono editar → modificar campos → "Update"

**Eliminar:** cursor sobre el documento → ícono eliminar → confirmar "Delete" (no recuperable)

**Buscar (Filter):** en la barra "Filter" se escribe solo el objeto JSON de filtro, sin el nombre del método:

```javascript
// Shell: db.mascotas.find({ Raza: "Labrador" })
// Compass Filter:
{ Raza: "Labrador" }

// Combinando campos (AND implícito):
{ Raza: "Labrador", Vacunado: true }
```

## 6. Ejercicio práctico (base de datos "Perros")

Documentos a insertar:

| Nombre | Raza | Edad | Vacunado |
|---|---|---|---|
| Agustín | Pug | 3 | true |
| Álvaro | Rottweiler | 5 | false |
| Sara | Beagle | 2 | false |
| Joaquín | Pug | 7 | true |

Edición: renombrar Sara→Niebla, cambiar edad de Álvaro a 1, cambiar vacunación de Agustín a false.
Eliminación: borrar a Niebla.

Búsquedas:
```javascript
{ Nombre: /va/i }
{ Nombre: "Joaquín" }
{ Raza: "Pug" }
{ Vacunado: true }
{ Edad: { $gt: 2 } }
```

---

## 📚 Referencias

Guía de la Unidad 13 — Universidad DaVinci (2026). Posibles soluciones y casos prácticos en bases de datos NoSQL.

MongoDB Inc. (2026). *MongoDB Compass Documentation*. https://www.mongodb.com/docs/compass/
