# 📊 UD7-8 — Cloud Computing y Sistemas de Storage

**Trimestre 1 · S6-S8 (Abr 2026)**

---

## 1. Modelos de servicio cloud

| Modelo | El proveedor gestiona | El usuario gestiona | Ejemplo |
|---|---|---|---|
| **IaaS** | Hardware, red, virtualización | SO, runtime, apps, datos | AWS EC2, Azure VMs |
| **PaaS** | IaaS + SO + runtime | Apps y datos | Azure App Service, Heroku |
| **SaaS** | Todo | Solo la configuración | Salesforce, Office 365, Snowflake |

> **Snowflake es SaaS para datos:** no gestionas servidores, ni SO, ni runtime — solo tu SQL y tus datos.

### Modelos de despliegue

| Modelo | Descripción | Cuándo usarlo |
|---|---|---|
| **Nube pública** | Infraestructura compartida (AWS, Azure, GCP) | Escalabilidad, costo variable |
| **Nube privada** | Infraestructura dedicada on-premise | Regulación, datos sensibles |
| **Nube híbrida** | Combinación de pública y privada | Flexibilidad + cumplimiento |
| **Multicloud** | Múltiples proveedores públicos | Evitar vendor lock-in |

---

## 2. Sistemas de almacenamiento masivo

| Sistema | Tipo | Característica clave | Uso típico |
|---|---|---|---|
| **DAS** (Direct Attached Storage) | Local | Baja latencia, sin red | Servidor individual |
| **NAS** (Network Attached Storage) | Red | Acceso compartido por archivos | Oficinas, colaboración |
| **SAN** (Storage Area Network) | Red dedicada | Alto rendimiento, nivel bloque | Bases de datos críticas |
| **HDFS** | Distribuido | Tolerancia a fallos, alta capacidad | Hadoop Big Data |
| **Object Storage** (S3, Azure Blob) | Cloud | Escalabilidad ilimitada, bajo costo | Data Lakes, backups |
| **Data Lake** | Conceptual | Datos crudos de cualquier formato | Analytics, ML |
| **Data Warehouse** | Conceptual | Datos estructurados optimizados para análisis | BI, reportes |

---

## 📚 Referencias

Armbrust, M., et al. (2010). A view of cloud computing. *Communications of the ACM*, 53(4), 50-58.
