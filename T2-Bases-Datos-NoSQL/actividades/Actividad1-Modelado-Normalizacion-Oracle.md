# Actividad Práctica 1 — U1 a U5

**Asignatura:** Bases de Datos y Bases de Datos No SQL I
**Semana:** S5 (6-11 Jul 2026)

---

## PRODUCTO 1 — Documento: Modelado y Normalización

### 1. Concepto de "Modelado"

El modelado de bases de datos es el proceso mediante el cual se representa de forma abstracta y estructurada la información que una organización necesita almacenar, junto con las relaciones que existen entre los distintos elementos de esa información, antes de construir físicamente la base de datos en un sistema gestor. En otras palabras, es el "plano" o mapa conceptual que traduce las necesidades reales del negocio (qué datos existen, cómo se relacionan, qué reglas deben cumplir) en un esquema organizado que después servirá de guía para implementar tablas, columnas y relaciones en un DBMS como Oracle, SQL Server o MySQL.

Modelar no es simplemente "dibujar tablas": implica primero entender el dominio del negocio, identificar qué entidades son relevantes (por ejemplo, clientes, productos, transacciones), qué atributos las describen y cómo se conectan entre sí, para luego decidir la forma más eficiente y consistente de almacenar esa información evitando duplicidad y errores.

### 2. Reflexión personal — Modelado en la práctica (experiencia con Odoo ERP)

Trabajando con Odoo como ERP en un entorno de clínica veterinaria, pude comprobar de primera mano por qué el modelado de datos no es un paso teórico que se pueda saltar, sino la base que determina si un sistema funciona bien o se vuelve un dolor de cabeza con el tiempo.

Odoo organiza su información en módulos (inventario, citas/agenda, facturación, contactos) que internamente están modelados como un conjunto de tablas relacionadas entre sí mediante claves foráneas: un registro de "paciente" (mascota) se relaciona con un registro de "contacto" (dueño), y ese mismo contacto se relaciona a su vez con las facturas, las citas y los movimientos de inventario de productos o medicamentos utilizados. Cuando ese modelo de datos subyacente está bien diseñado, es posible construir reportes en Power BI conectándose directamente a esas tablas relacionales y obtener, por ejemplo, el historial completo de consultas de una mascota junto con el gasto total de su dueño, sin duplicar información ni arrastrar inconsistencias.

El problema aparece cuando el modelo no se respeta correctamente en el uso diario: contactos duplicados porque se crea un "dueño" nuevo en lugar de reutilizar el existente, o mascotas registradas sin vincular correctamente a su dueño. Estos errores no son fallas del software, sino fallas de disciplina sobre el modelo relacional que hay detrás. Desde mi rol analizando estos datos, aprendí que un buen modelado no solo facilita la vida del sistema transaccional, sino que es lo que hace posible —o imposible— construir análisis confiables después. Un modelo mal pensado se paga muchas veces más caro en la etapa de análisis de datos que en la etapa de diseño inicial.

### 3. Cuadro comparativo — Modelo E-R vs. Modelo Relacional

| Aspecto | Modelo Entidad-Relación (E-R) | Modelo Relacional |
|---|---|---|
| **Objetivo principal** | Representar conceptualmente la realidad del negocio: qué entidades existen y cómo se relacionan entre sí. | Representar los datos de forma lógica, lista para implementarse en un DBMS, usando tablas. |
| **Elementos principales** | Entidades, atributos y relaciones (con su cardinalidad: 1:1, 1:N, N:M). | Tablas (relaciones), filas (tuplas), columnas (atributos), claves primarias y foráneas. |
| **Representación gráfica** | Diagrama E-R: rectángulos (entidades), óvalos (atributos), rombos (relaciones). | Esquemas de tablas o diagramas relacionales con líneas que muestran claves foráneas. |
| **Nivel de abstracción** | Alto — es un modelo conceptual, independiente de la tecnología que se use después. | Más bajo — es un modelo lógico, ya pensado en cómo se implementará en SQL. |
| **Momento de uso en el proyecto** | Fase de análisis y diseño inicial, antes de tocar cualquier motor de base de datos. | Fase de diseño detallado e implementación, ya con el DBMS elegido (Oracle, MySQL, etc.). |
| **Ejemplo** | Entidad "Mascota" relacionada con entidad "Dueño" mediante la relación "pertenece a" (N:1). | Tabla MASCOTAS con columna id_dueño como clave foránea que referencia a la tabla DUEÑOS. |

### 4. Mapa conceptual — Normalización de bases de datos

```
NORMALIZACIÓN DE BASES DE DATOS
        │
        ▼
   Objetivo: Reducir redundancia y evitar anomalías de datos
        │
        ├──► 1FN — Primera Forma Normal
        │     Valores atómicos (indivisibles) · sin grupos repetidos · cada fila es única
        │        │
        │        ▼
        │    2FN — Segunda Forma Normal
        │     Cumple 1FN · sin dependencias parciales (todo atributo depende de la CLAVE COMPLETA)
        │        │
        │        ▼
        │    3FN — Tercera Forma Normal
        │     Cumple 2FN · sin dependencias transitivas (atributos no clave no dependen de otros no clave)
        │
        ├──► previene: Anomalía de Inserción (no se puede añadir un dato sin depender de otro innecesario)
        ├──► previene: Anomalía de Actualización (un mismo dato repetido en varias filas se desincroniza)
        └──► previene: Anomalía de Eliminación (al borrar una fila se pierde información que no debía perderse)
```

**Referencias (APA 7):**

Silberschatz, A., Korth, H. F., & Sudarshan, S. (2020). *Database System Concepts* (7.ª ed.). McGraw-Hill Education.
Beynon-Davies, P. (2018). *Sistemas de bases de datos*. Reverté.
Elmasri, R., & Navathe, S. B. (2017). *Fundamentals of Database Systems* (7.ª ed.). Pearson.

---

## PRODUCTO 2 — Presentación: Antecedentes de Oracle y Ventajas frente a otros DBMS

### Introducción

Dentro del ecosistema de Sistemas Gestores de Bases de Datos (DBMS), Oracle ocupa un lugar histórico como pionero de las bases de datos relacionales comerciales. Comprender su origen, evolución y posicionamiento actual frente a otros motores como MySQL, SQL Server o PostgreSQL permite entender por qué sigue siendo, más de 45 años después de su fundación, uno de los motores más utilizados en entornos empresariales críticos.

### Antecedentes históricos de Oracle (línea de tiempo)

| Año | Evento |
|---|---|
| **1977** | Larry Ellison, Bob Miner y Ed Oates fundan Software Development Laboratories (SDL) con una inversión inicial de apenas $2,000 USD. |
| **1979** | Se lanza comercialmente la primera versión del producto Oracle para computadoras PDP-11, basada en las teorías del modelo relacional de E. F. Codd. |
| **1982** | SDL se renombra formalmente como Oracle Corporation, alineándose con su producto insignia. |
| **1986** | Oracle sale a bolsa en el NASDAQ, consolidándose como una de las grandes tecnológicas de Silicon Valley. |
| **1992** | Lanzamiento de Oracle 7, que reencauza el crecimiento de la compañía tras una crisis financiera. |
| **2010–hoy** | Adquisición de Sun Microsystems (2010) y evolución hacia Oracle Autonomous Database, Exadata y servicios multi-nube (OCI, Azure). |

### Ventajas de Oracle frente a otros DBMS

| Ventaja | Descripción |
|---|---|
| **Robustez empresarial** | Diseñado para cargas críticas de alta disponibilidad, transacciones masivas (OLTP) y analítica (OLAP) simultáneamente. |
| **Seguridad avanzada** | Cifrado nativo, auditoría granular y control de acceso robusto — clave para datos sensibles en sectores regulados. |
| **Automatización con IA** | Oracle Autonomous Database se auto-ajusta, auto-repara y auto-protege usando machine learning, sin intervención constante del DBA. |
| **Estrategia multi-nube real** | Integración nativa con OCI, y también con Microsoft Azure vía Oracle Database Service for Azure — sin atarse a un solo proveedor. |
| **Soporte para SQL y NoSQL** | Un mismo motor puede administrar datos relacionales tradicionales y estructuras NoSQL (documentos, JSON) de forma convergente. |
| **Escalabilidad probada** | Infraestructura Exadata optimizada para procesar desde miles hasta millones de transacciones por segundo en clústeres consolidados. |

Frente a MySQL o PostgreSQL (código abierto, menor costo) Oracle destaca en soporte empresarial 24/7 y funciones avanzadas; frente a SQL Server, en portabilidad multiplataforma y multi-nube.

### Análisis del ejemplo práctico: SQL Multitabla

**Contexto genérico:** una clínica veterinaria almacena sus MASCOTAS y sus DUEÑOS en dos tablas relacionadas por una clave foránea (id_dueño). Se necesita un reporte de consultas por veterinario.

```sql
-- INNER JOIN + GROUP BY
SELECT v.nombre AS veterinario,
       COUNT(*) AS num_consultas,
       SUM(c.costo) AS total
FROM Consultas c
INNER JOIN Veterinarios v
  ON c.id_vet = v.id_vet
GROUP BY v.nombre;
```

**¿Qué hace esta consulta?**

1. El `INNER JOIN` combina cada fila de Consultas con la fila correspondiente de Veterinarios, usando la clave foránea `id_vet` — solo se conservan las coincidencias.
2. `GROUP BY` agrupa todas las filas resultantes por veterinario: en lugar de una fila por consulta, se obtiene una fila por veterinario.
3. `COUNT(*)` y `SUM()` son funciones de agregación: cuentan cuántas consultas atendió cada veterinario y suman el total facturado por cada uno.

**Conclusión del ejemplo:** este patrón (JOIN + GROUP BY + función de agregación) es la base de casi cualquier reporte gerencial sobre datos relacionales — desde facturación por vendedor hasta consultas por veterinario — y es exactamente el mismo principio que sostiene los reportes de Power BI construidos sobre bases de datos relacionales en un entorno empresarial real.

### Conclusión general de la unidad

1. Oracle nació en 1977 como una apuesta arriesgada de tres fundadores, y hoy sigue siendo referencia en bases de datos empresariales — su historia demuestra que la innovación técnica temprana (adoptar el modelo relacional de Codd antes que nadie) puede definir el liderazgo de una industria por décadas.
2. Sus ventajas frente a otros DBMS no son absolutas: dependen del contexto. Para cargas críticas, alta seguridad y automatización con IA, Oracle es líder; para proyectos con presupuesto ajustado, MySQL o PostgreSQL siguen siendo alternativas sólidas.
3. El SQL multitabla (JOIN + GROUP BY) es el mecanismo técnico que conecta esta teoría con la práctica diaria: sin importar el DBMS elegido, dominar estas operaciones es lo que permite convertir datos relacionales dispersos en información útil para la toma de decisiones.

### Bibliografía

- Oracle Corporation. (2026). Historia [Wikipedia]. https://es.wikipedia.org/wiki/Oracle_Corporation
- Ellison, L. (2026). Larry Ellison [Wikipedia]. https://es.wikipedia.org/wiki/Larry_Ellison
- IProUP. (2021). La historia de Oracle y de su fundador, Larry Ellison. https://www.iproup.com/innovacion/16030-la-historia-de-oracle-y-de-su-fundador-larry-ellison
- Dataustral. (2024). Comparativa Oracle Database vs. MySQL, SQL Server y PostgreSQL. https://dataustral.com/2024/11/19/comparativa-oracle-database-vs-mysql/
- LearnSQL.es. (s.f.). ¿Cuáles son las diferencias entre los motores de bases de datos? Una visión general para principiantes. https://learnsql.es/blog/cuales-son-las-diferencias-entre-los-motores-de-bases-de-datos-una-vision-general-para-principiantes/
- Astera. (2025). PostgreSQL vs Oracle: 8 diferencias que debes conocer. https://www.astera.com/es/knowledge-center/postgresql-vs-oracle/
- Silberschatz, A., Korth, H. F., & Sudarshan, S. (2020). *Database System Concepts* (7.ª ed.). McGraw-Hill Education.

