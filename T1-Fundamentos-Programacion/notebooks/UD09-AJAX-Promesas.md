# 📘 UD9 — Interfaces II: AJAX, Fetch y Promesas

**Trimestre 1 · S8-S9 (May 2026)**

---

## 1. AJAX y la programación asíncrona

AJAX (Asynchronous JavaScript And XML) permite hacer peticiones al servidor sin recargar la página. La clave es que JS es **asíncrono**: no espera a que una operación termine para continuar.

---

## 2. Promesas (Promises)

```javascript
// Una promesa puede estar: pendiente, resuelta (fulfilled) o rechazada (rejected)
const promesa = new Promise((resolve, reject) => {
    const exito = true;
    if (exito) {
        resolve("¡Datos obtenidos!");
    } else {
        reject("Error al obtener datos");
    }
});

promesa
    .then(resultado => console.log(resultado))   // si se resuelve
    .catch(error    => console.error(error))      // si se rechaza
    .finally(()     => console.log("Finalizado")); // siempre
```

---

## 3. Fetch API

```javascript
// GET — obtener datos
fetch("https://api.ejemplo.com/mascotas")
    .then(response => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json();
    })
    .then(data => console.log(data))
    .catch(error => console.error("Error:", error));

// POST — enviar datos
fetch("https://api.ejemplo.com/mascotas", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre: "Firulais", especie: "Perro" })
})
.then(res => res.json())
.then(data => console.log("Creado:", data));
```

---

## 4. Async/Await — sintaxis moderna

```javascript
async function obtenerMascotas() {
    try {
        const response = await fetch("https://api.ejemplo.com/mascotas");
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const mascotas = await response.json();
        console.log(mascotas);
        return mascotas;
    } catch (error) {
        console.error("Error:", error);
    }
}

obtenerMascotas();
```

> `async/await` es "azúcar sintáctico" sobre Promises — hace el código asíncrono más legible, como si fuera síncrono.

---

## 🗺️ Mapa mental

```
ASINCRONÍA EN JS
│
├── Callback      → función pasada como argumento (antiguo)
├── Promise       → objeto con estados (pending/fulfilled/rejected)
│     ├── .then() → éxito
│     ├── .catch() → error
│     └── .finally() → siempre
└── Async/Await   → sintaxis moderna sobre Promises
```
