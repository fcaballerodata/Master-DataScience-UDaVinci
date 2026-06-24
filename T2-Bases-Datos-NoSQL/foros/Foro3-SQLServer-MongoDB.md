# 💬 Foro 3 — DBMS SQL Server y MongoDB

**Asignatura:** Bases de Datos y Bases de Datos NoSQL  
**Semana:** S3 (Jun 2026)

---

## 📋 Preguntas

1. Menciona uno de los antecedentes del SQL Server.
2. Ventajas del uso de SQL Server 2019.
3. Entorno de Instalación de SQL Server 2019 (requisitos).
4. Mencione 5 sentencias y su uso.
5. Desarrolle un cuadro comparativo: Oracle vs SQL Server 2019.

---

## ✍️ Respuesta publicada

SQL Server y MongoDB representan dos enfoques complementarios para la gestión de datos: uno consolidado en el modelo relacional y el otro diseñado para escalar en entornos de datos masivos y semiestructurados. Conocer ambos amplía significativamente la capacidad de un profesional de datos para elegir la herramienta adecuada según el problema.

**Antecedente del SQL Server**

Uno de los antecedentes más relevantes de SQL Server es su origen en una colaboración entre Microsoft y Sybase en 1989, cuando se desarrolló la primera versión del sistema para el sistema operativo OS/2, en ese entonces copropiedad de Microsoft e IBM. Esta primera versión fue concebida como un sistema de gestión de bases de datos relacionales basado en el lenguaje SQL, heredando parte del código fuente de Sybase. Con el paso del tiempo, Microsoft desarrolló versiones propias para Windows NT (1993) y fue reescribiendo el motor hasta llegar a una arquitectura completamente propia desde la versión 7.0 en adelante (Microsoft, 2019).

**Ventajas del uso de SQL Server 2019**

SQL Server 2019 introduce mejoras significativas respecto a versiones anteriores. Entre sus principales ventajas destacan: la compatibilidad multiplataforma al ejecutarse no solo en Windows sino también en Linux y contenedores Docker; los clústeres de Big Data que permiten integrar SQL Server con Apache Spark y HDFS corriendo sobre Kubernetes; la función *Siempre cifrado* que protege datos sensibles incluso durante el procesamiento; el enmascaramiento dinámico de datos para controlar qué usuarios ven información confidencial; y la corrección automática del plan de ejecución, que detecta y resuelve pérdidas de rendimiento sin intervención manual (Softtrader, 2025).

**Entorno de Instalación de SQL Server 2019**

Según la documentación oficial de Microsoft (2022), los requisitos mínimos son:

- **Procesador:** arquitectura x64, mínimo 1.4 GHz (recomendado: 2.0 GHz o superior)
- **RAM:** mínimo 1 GB (Express) / mínimo 4 GB (otras ediciones)
- **Disco duro:** mínimo 6 GB disponibles en la unidad del sistema
- **Pantalla:** resolución 800×600 px o superior
- **SO:** Windows Server 2016 o posterior; también disponible para Linux y Docker
- **Software:** .NET Framework 4.6+ (se instala automáticamente)

Referencia de instalación paso a paso: Datamania. (2021). *Descargar e Instalar SQL Server 2019 Español – Paso a Paso – Gratis*. https://www.youtube.com/watch?v=Nezgx-MgiSM

**5 sentencias SQL y su uso**

- **CREATE:** crea objetos en la BD. `CREATE TABLE pacientes (id INT, nombre VARCHAR(100))`.
- **ALTER:** modifica una estructura existente. `ALTER TABLE pacientes ADD telefono VARCHAR(20)`.
- **DROP:** elimina un objeto permanentemente. `DROP TABLE pacientes`.
- **INSERT:** agrega nuevos registros. `INSERT INTO pacientes VALUES (1, 'Juan Pérez')`.
- **SELECT:** consulta y recupera datos. `SELECT nombre FROM pacientes WHERE id = 1`.

**Cuadro comparativo: Oracle vs SQL Server 2019**

| Criterio | Oracle Database | SQL Server 2019 |
|---|---|---|
| Fabricante | Oracle Corporation | Microsoft |
| Año de origen | 1979 | 1989 |
| Lenguaje propietario | PL/SQL | T-SQL |
| Plataformas | Windows, Linux, Unix | Windows, Linux, Docker |
| Escalabilidad | Oracle RAC (clustering) | Big Data Clusters con Spark/HDFS |
| Seguridad | Auditoría avanzada, cifrado | Siempre cifrado, enmascaramiento dinámico |
| Cloud | Oracle Cloud Infrastructure | Azure SQL |
| Licenciamiento | Propietario, costo elevado | Edición Developer gratuita |
| Ecosistema BI | Oracle Analytics Cloud | Power BI + SSRS |
| Curva de aprendizaje | Alta | Media (natural con ecosistema Microsoft) |

En mi experiencia con Snowflake y herramientas Microsoft, la elección entre ambos depende del entorno existente: Oracle es preferido en grandes corporaciones con infraestructura Unix/Linux crítica, mientras que SQL Server encaja en empresas con ecosistema Microsoft.

---

## 📚 Referencias

Microsoft. (2022). *Requisitos de hardware y software para instalar SQL Server 2019*. Microsoft Learn. https://learn.microsoft.com/es-es/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server-2019

Microsoft. (2019). *Historia y versiones de SQL Server*. Microsoft Docs.

Softtrader. (2025). *Microsoft SQL Server 2019: requerimientos y características*. https://softtrader.es/todo-lo-que-necesitan-saber-sobre-microsoft-sql-server-2019/

Datamania. (2021). *Descargar e Instalar SQL Server 2019 Español – Paso a Paso – Gratis* [Video]. YouTube. https://www.youtube.com/watch?v=Nezgx-MgiSM
