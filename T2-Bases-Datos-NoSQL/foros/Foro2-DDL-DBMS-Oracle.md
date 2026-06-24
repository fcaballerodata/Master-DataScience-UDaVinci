# 💬 Foro 2 — DDL y DBMS Oracle

**Asignatura:** Bases de Datos y Bases de Datos NoSQL  
**Semana:** S2 (Jun 2026)

---

## 📋 Preguntas

1. ¿Cuál es la diferencia entre modelo y modelado de B.D.?
2. ¿Diferencias entre el Modelo E-R y el Modelo Relacional?
3. ¿Significado de DDL?
4. ¿Mencione 3 sentencias DDL y cuál es su función?

---

## ✍️ Respuesta publicada

El modelado de bases de datos y el lenguaje DDL son dos piezas que trabajan juntas: primero se diseña la base de datos a nivel conceptual, y luego el DDL permite materializar ese diseño en estructuras reales dentro del motor de base de datos.

**¿Cuál es la diferencia entre modelo y modelado de B.D.?**

El **modelo** es el resultado: la representación o el esquema que describe cómo están organizados los datos (por ejemplo, un diagrama E-R o un conjunto de tablas relacionales ya definidas). El **modelado**, en cambio, es el proceso mediante el cual se diseña ese modelo: analizar el negocio, identificar entidades, atributos y relaciones, y documentar cómo se va a estructurar la información antes de implementarla. En pocas palabras, el modelado es el camino y el modelo es el destino.

**¿Diferencias entre el Modelo E-R y el Modelo Relacional?**

El **Modelo E-R** es conceptual y de alto nivel: se enfoca en identificar entidades (por ejemplo, Mascota, Dueño), sus atributos y las relaciones entre ellas, sin preocuparse todavía por cómo se implementará técnicamente. El **Modelo Relacional**, en cambio, es de bajo nivel e implementable: traduce esas entidades en tablas, los atributos en columnas, y las relaciones en claves foráneas. El flujo natural es diseñar primero en E-R y luego convertirlo en relacional para poder crearlo en SQL (Beynon-Davies, 2018).

**¿Significado de DDL?**

DDL significa **Data Definition Language** (Lenguaje de Definición de Datos). Es el conjunto de comandos que permiten definir la estructura de una base de datos: crear, modificar o eliminar tablas, índices, vistas y esquemas. A diferencia del DML, que manipula los datos dentro de las tablas, el DDL se encarga exclusivamente de definir esa estructura.

**3 sentencias DDL y su función**

- **CREATE** — crea nuevas estructuras: `CREATE TABLE` para definir una tabla, `CREATE VIEW` para crear una vista, `CREATE SCHEMA` para un esquema.
- **ALTER** — modifica una estructura existente: `ALTER TABLE` para añadir o eliminar una columna sin perder los datos almacenados.
- **DROP** — elimina una estructura por completo: `DROP TABLE` borra la tabla y toda su definición. Puede usarse con `RESTRICT` (solo si está vacío) o `CASCADE` (borra todo el contenido también).

---

## 📚 Referencias

Beynon-Davies, P. (2018). *Sistemas de bases de datos*. Reverté.
