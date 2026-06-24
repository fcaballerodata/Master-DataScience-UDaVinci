# 📘 UD5 — Sentencias de Repetición

**Trimestre 1 · S5 (Abr 2026)**

---

## 1. while

```javascript
let i = 0;
while (i < 5) {
    console.log(`Iteración ${i}`);
    i++;
}
// Usar cuando no sabes cuántas veces repetir — condición al inicio
```

## 2. do...while

```javascript
let intentos = 0;
do {
    console.log(`Intento ${intentos + 1}`);
    intentos++;
} while (intentos < 3);
// Siempre ejecuta al menos UNA vez — condición al final
```

## 3. for

```javascript
// for clásico — cuando sabes exactamente cuántas veces
for (let i = 0; i < 10; i++) {
    console.log(i);
}

// for...of — iterar sobre arrays
const mascotas = ["Firulais", "Michi", "Rex"];
for (const mascota of mascotas) {
    console.log(mascota);
}

// for...in — iterar sobre propiedades de un objeto
const paciente = { nombre: "Firulais", especie: "Perro", edad: 3 };
for (const clave in paciente) {
    console.log(`${clave}: ${paciente[clave]}`);
}
```

---

## 4. break y continue

```javascript
for (let i = 0; i < 10; i++) {
    if (i === 5) break;      // sale del loop completamente
    if (i % 2 === 0) continue; // salta esta iteración, continúa el loop
    console.log(i);          // imprime solo impares menores que 5: 1, 3
}
```

---

## 🗺️ Mapa mental

```
LOOPS
├── while       → condición al inicio, puede no ejecutarse
├── do...while  → condición al final, ejecuta al menos una vez
├── for         → contador explícito (inicio; condición; paso)
├── for...of    → iterar arrays/iterables
└── for...in    → iterar propiedades de objetos
```
