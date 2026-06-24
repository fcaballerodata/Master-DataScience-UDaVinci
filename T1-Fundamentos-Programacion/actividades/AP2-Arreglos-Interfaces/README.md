# 🛠️ AP2 — Arreglos e Interfaces AJAX

**Asignatura:** Fundamentos de Programación (JavaScript) · T1 S9-S10  
**Estado:** ✅ Entregada

---

## 📋 Descripción

Actividad práctica que combina manipulación de arrays, DOM e interfaces asíncronas (Fetch/AJAX) para construir un módulo de consulta de datos veterinarios.

---

## 🎯 Objetivos

- Manipular arrays con map, filter y reduce
- Interactuar con el DOM para mostrar resultados dinámicamente
- Realizar peticiones asíncronas con Fetch API y async/await

---

## 💡 Concepto del ejercicio

Módulo web que consulta una API de mascotas, filtra por especie y muestra los resultados en el DOM sin recargar la página.

```javascript
async function cargarMascotas(filtroEspecie = null) {
    try {
        const response = await fetch("https://api.movet.co/mascotas");
        const mascotas = await response.json();

        const filtradas = filtroEspecie
            ? mascotas.filter(m => m.especie === filtroEspecie)
            : mascotas;

        const lista = document.getElementById("listaMascotas");
        lista.innerHTML = filtradas
            .map(m => `<li>${m.nombre} — ${m.especie} — ${m.peso}kg</li>`)
            .join("");

        const total = filtradas.reduce((acc, m) => acc + m.peso, 0);
        document.getElementById("pesoTotal").innerText =
            `Peso total: ${total}kg`;

    } catch (error) {
        console.error("Error al cargar mascotas:", error);
    }
}

document.getElementById("btnPerros").addEventListener("click",
    () => cargarMascotas("Perro"));
document.getElementById("btnTodos").addEventListener("click",
    () => cargarMascotas());
```
