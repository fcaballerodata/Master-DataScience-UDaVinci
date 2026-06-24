# 📘 UD7 — Funciones

**Trimestre 1 · S7 (Abr 2026)**

---

## 1. Declaración de funciones

```javascript
// Función declarada — se eleva (hoisting), se puede llamar antes de definir
function sumar(a, b) {
    return a + b;
}

// Función expresión — no se eleva
const restar = function(a, b) {
    return a - b;
};

// Arrow function — sintaxis moderna, no tiene su propio 'this'
const multiplicar = (a, b) => a * b;
const saludar     = nombre => `Hola, ${nombre}`;  // un parámetro, sin paréntesis
const pi          = () => 3.14159;                  // sin parámetros
```

---

## 2. Parámetros y valores por defecto

```javascript
function crearConsulta(mascota, fecha = new Date().toLocaleDateString(), costo = 50000) {
    return { mascota, fecha, costo };
}

console.log(crearConsulta("Firulais"));
// { mascota: "Firulais", fecha: "24/6/2026", costo: 50000 }
```

---

## 3. Scope (ámbito)

```javascript
const global = "Soy global";    // accesible en todo el código

function demo() {
    const local = "Soy local";  // solo dentro de demo()
    console.log(global);        // ✅ puede acceder a global
    console.log(local);         // ✅
}

console.log(global);    // ✅
console.log(local);     // ❌ ReferenceError — no existe fuera
```

---

## 4. Arrow functions y this

```javascript
// En arrow functions, 'this' hereda del contexto exterior
class Contador {
    constructor() { this.valor = 0; }

    incrementarTradicional() {
        setTimeout(function() {
            // this.valor++ ← ERROR: 'this' aquí es undefined en strict mode
        }, 1000);
    }

    incrementarArrow() {
        setTimeout(() => {
            this.valor++;  // ✅ 'this' sigue siendo el objeto Contador
        }, 1000);
    }
}
```

---

## 🗺️ Mapa mental

```
FUNCIONES
├── Declarada    → hoisting, function nombre() {}
├── Expresión    → const f = function() {}
├── Arrow        → const f = () => {} — hereda 'this'
├── Parámetros   → valores por defecto, rest (...args)
└── Scope        → global → función → bloque
```

## 📚 Referencias

MDN Web Docs. (2024). *Functions — JavaScript*. https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Functions
