# 📊 UD5-6 — Virtualización y Casos de Éxito

**Trimestre 1 · S5-S6 (Abr 2026)**

---

## 1. Virtualización

La virtualización permite crear recursos computacionales virtuales (servidores, redes, almacenamiento) sobre hardware físico compartido.

### Tipos de virtualización

| Tipo | Descripción | Ejemplo |
|---|---|---|
| **Máquinas Virtuales (VM)** | Emula un SO completo sobre un hipervisor | VMware, VirtualBox, Hyper-V |
| **Contenedores** | Empaqueta app + dependencias, comparte el kernel del SO | Docker, Podman |
| **Virtualización de red** | Redes definidas por software | SDN, VLAN |
| **Virtualización de almacenamiento** | Abstrae el almacenamiento físico | SAN, NAS virtualizados |

### VM vs Contenedores

| | Máquinas Virtuales | Contenedores (Docker) |
|---|---|---|
| **Peso** | Pesados (GB) — incluyen SO completo | Ligeros (MB) — solo la app y deps |
| **Inicio** | Minutos | Segundos |
| **Aislamiento** | Total (SO propio) | Parcial (comparten kernel) |
| **Uso ideal** | Entornos heterogéneos, más seguridad | Microservicios, CI/CD, portabilidad |

---

## 2. Casos de éxito reales

### Netflix — Streaming global con Big Data
Netflix procesa 500TB de datos diarios para alimentar su sistema de recomendaciones. Usa Spark para análisis en tiempo real, Cassandra para almacenamiento NoSQL y algoritmos de ML para personalizar la experiencia de 200M+ usuarios.

### Amazon — Supply chain predictivo
Amazon usa Big Data para predecir demanda, optimizar rutas de entrega y gestionar inventarios en tiempo real en miles de almacenes globales.

### Caso Movet — Pipeline Big Data para clínicas veterinarias
Un pipeline hipotético aplicado a Movet:
```
Odoo ERP → Kafka (streaming) → Azure Data Lake (raw) 
→ Spark (transformación) → Snowflake (DW) → Power BI (dashboards)
```

---

## 📚 Referencias

Marz, N., & Warren, J. (2015). *Big Data: Principles and best practices of scalable realtime data systems*. Manning Publications.
