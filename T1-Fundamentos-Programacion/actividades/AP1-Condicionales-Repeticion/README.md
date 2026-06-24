# 🛠️ AP1 — Condicionales y Repetición

**Asignatura:** Fundamentos de Programación (JavaScript) · T1 S5  
**Estado:** ✅ Entregada

---

## 📋 Descripción

Actividad práctica que integra sentencias condicionales (if/else, switch) y estructuras de repetición (for, while) en un sistema de gestión básico para clínicas veterinarias.

---

## 🎯 Objetivos

- Implementar lógica condicional con if/else y switch
- Usar loops para procesar colecciones de datos
- Combinar POO con condicionales en un caso de uso real

---

## 💡 Concepto del ejercicio

Sistema de clasificación de mascotas por peso y tipo de consulta para Movet, usando condicionales para categorizar y loops para procesar registros.

```javascript
// Ejemplo de estructura implementada
function clasificarMascota(nombre, peso, tipoConsulta) {
    let talla;
    if (peso < 5)       talla = "XS";
    else if (peso < 15) talla = "S-M";
    else if (peso < 30) talla = "L";
    else                talla = "XL";

    let descripcionConsulta;
    switch (tipoConsulta) {
        case "VAC": descripcionConsulta = "Vacunación";     break;
        case "CIR": descripcionConsulta = "Cirugía";         break;
        case "CON": descripcionConsulta = "Consulta general"; break;
        default:    descripcionConsulta = "Otro";
    }

    return `${nombre} (Talla ${talla}) — ${descripcionConsulta}`;
}

const mascotas = [
    { nombre: "Firulais", peso: 22, tipo: "CON" },
    { nombre: "Michi",    peso: 4,  tipo: "VAC" },
    { nombre: "Rex",      peso: 35, tipo: "CIR" }
];

for (const m of mascotas) {
    console.log(clasificarMascota(m.nombre, m.peso, m.tipo));
}
```
