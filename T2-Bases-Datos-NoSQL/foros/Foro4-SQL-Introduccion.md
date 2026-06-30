# 💬 Foro 4 — SQL Introducción

**Asignatura:** Bases de Datos y Bases de Datos NoSQL  
**Semana:** S4 (Jun-Jul 2026)

---

## 📋 Preguntas

1. Menciona 3 datos históricos de SQL.
2. ¿Qué son las sentencias DDL y ejemplifique?
3. Explique la función de las sentencias INSERT, DELETE y UPDATE.
4. Ejemplifica la sentencia DELETE.

---

## ✍️ Respuesta publicada

SQL es el lenguaje estándar para gestionar bases de datos relacionales, con una historia que se remonta a los años 70 y una estructura que combina definición y manipulación de datos.

**3 datos históricos de SQL**

Primero, SQL fue desarrollado originalmente por IBM a principios de los años 70 bajo el nombre de **Sequel**, como parte del proyecto System R. Segundo, en 1986 **ANSI** (American National Standards Institute) publicó la primera norma oficial del lenguaje, denominada SQL-86, seguida de una versión ampliada en 1989 (SQL-89). Tercero, en 1992 se publicó **SQL-92** (también llamada SQL2), considerada la versión más importante e influyente, ya que sentó las bases del SQL que se utiliza ampliamente hoy en día en motores como Oracle, MySQL, SQL Server y PostgreSQL (ISO/IEC, 2016).

**¿Qué son las sentencias DDL y ejemplo?**

Las sentencias DDL (Data Definition Language) son los comandos que permiten definir y modificar la estructura de una base de datos: crear, alterar o eliminar tablas, índices y otros objetos. A diferencia del DML, que manipula los datos contenidos, el DDL define el "contenedor" donde esos datos vivirán.

```sql
CREATE TABLE mascotas (
    id_mascota INT,
    nombre     VARCHAR(50),
    especie    VARCHAR(20)
);
```

**Función de las sentencias INSERT, DELETE y UPDATE**

Estas tres sentencias son parte del DML y controlan la información dentro de las tablas ya creadas. **INSERT** agrega nuevos registros a una tabla. **UPDATE** modifica la información de registros existentes. **DELETE** elimina registros de una tabla. Las tres operan sobre los datos, nunca sobre la estructura.

```sql
INSERT INTO mascotas VALUES (1, 'Firulais', 'Perro');

UPDATE mascotas SET especie = 'Canino' WHERE id_mascota = 1;
```

**Ejemplo de sentencia DELETE**

```sql
DELETE FROM mascotas
WHERE especie = 'Conejo';
```

Esta sentencia elimina todos los registros de la tabla `mascotas` cuya especie sea "Conejo". Es importante destacar que `DELETE` sin una cláusula `WHERE` eliminaría **todos** los registros de la tabla, por lo que siempre debe usarse con precaución y verificando la condición de filtro antes de ejecutar.

---

## 📚 Referencias

ISO/IEC. (2016). *ISO/IEC 9075-1:2016 — Information technology — Database languages — SQL*. https://www.iso.org/standard/63555.html
