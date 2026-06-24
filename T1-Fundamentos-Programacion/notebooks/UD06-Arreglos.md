# 📘 UD6 — Arreglos (Arrays)

**Trimestre 1 · S6 (Abr 2026)**

---

## 1. Declaración y acceso

```javascript
const mascotas = ["Firulais", "Michi", "Rex", "Luna"];

console.log(mascotas[0]);       // "Firulais" — índice 0
console.log(mascotas.length);   // 4
console.log(mascotas[mascotas.length - 1]);  // "Luna" — último elemento
```

---

## 2. Métodos principales

```javascript
mascotas.push("Toby");          // agrega al final
mascotas.pop();                  // elimina del final
mascotas.unshift("Bobby");       // agrega al inicio
mascotas.shift();                // elimina del inicio

// Búsqueda
mascotas.indexOf("Michi");       // 1 — posición
mascotas.includes("Rex");        // true
mascotas.find(m => m.length > 4); // "Firulais" — primer elemento que cumple

// Transformación (no mutan el original)
const mayusculas = mascotas.map(m => m.toUpperCase());
const largos = mascotas.filter(m => m.length > 4);
const total = [10, 20, 30].reduce((acc, val) => acc + val, 0);  // 60

// Ordenar
mascotas.sort();                 // alfabético (muta el array)
[3,1,4,1,5].sort((a,b) => a-b); // numérico ascendente
```

---

## 3. Arrays multidimensionales

```javascript
const historial = [
    ["Firulais", "2025-01-10", "Otitis"],
    ["Michi",    "2025-01-15", "Vacuna"],
    ["Rex",      "2025-02-01", "Parásitos"]
];

console.log(historial[0][2]);  // "Otitis"

// Recorrer
historial.forEach(consulta => {
    console.log(`${consulta[0]} — ${consulta[2]}`);
});
```

---

## 🗺️ Mapa mental

```
ARRAYS
│
├── Declaración: [], new Array()
├── Acceso: arr[i], arr.length
├── Mutación: push, pop, unshift, shift, splice
├── Búsqueda: indexOf, includes, find, findIndex
└── Funcional (no mutan):
      ├── map    → transforma cada elemento
      ├── filter → filtra según condición
      └── reduce → acumula a un solo valor
```
