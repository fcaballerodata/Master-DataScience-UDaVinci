# 📊 UD13-14 — Open Data, SPARQL y Fases de Proyecto

**Trimestre 1 · S9 (May 2026)**

---

## 1. Open Data

Open Data son datos de acceso libre y gratuito que cualquier persona puede usar, reutilizar y redistribuir.

### Los 8 principios del Open Data (Sunlight Foundation)

1. **Completos** — todos los datos públicos disponibles
2. **Primarios** — datos originales, no agregados
3. **Actuales** — tan actualizados como sea posible
4. **Accesibles** — disponibles para el mayor número de usuarios
5. **Procesables por máquinas** — formatos estructurados (CSV, JSON)
6. **No discriminatorios** — sin registro requerido
7. **No propietarios** — formatos abiertos
8. **Libres de licencia** — sin restricciones de copyright

---

## 2. Linked Data y SPARQL

**Linked Data** conecta datasets entre sí usando URIs y el estándar RDF (Resource Description Framework). Permite consultar datos distribuidos en la web como si fueran una sola BD.

**SPARQL** es el lenguaje de consulta para datos RDF — el equivalente a SQL para Linked Data.

```sparql
-- SQL: SELECT nombre FROM mascotas WHERE especie = 'Perro'
-- SPARQL equivalente:
SELECT ?nombre WHERE {
  ?mascota rdf:type movet:Mascota .
  ?mascota movet:especie "Perro" .
  ?mascota movet:nombre ?nombre .
}
```

---

## 3. Fases de un proyecto Big Data

1. **Diagnóstico** — identificar el problema de negocio y las fuentes de datos disponibles
2. **Diseño** — arquitectura del pipeline, selección de herramientas, modelo de datos
3. **Implementación** — desarrollo del pipeline, ingesta, transformación, carga
4. **Control** — monitoreo de calidad, alertas, SLAs
5. **Recursos** — equipo, infraestructura, costos
6. **Calendarización** — cronograma, hitos, entregables

---

## 📚 Referencias

Bizer, C., Heath, T., & Berners-Lee, T. (2009). Linked data — the story so far. *International Journal on Semantic Web and Information Systems*, 5(3), 1-22.
