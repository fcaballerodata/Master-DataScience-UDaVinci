# 📘 UD1-2 — Introducción a JavaScript

**Trimestre 1 · S1-S2 (Mar 2026)**

---

## 🎯 Conceptos clave

JavaScript es un lenguaje interpretado, de tipado dinámico, que se ejecuta en el navegador (client-side) y en el servidor con Node.js. Es el único lenguaje nativo del navegador para manipular el DOM.

---

## 1. ¿Qué es JavaScript?

- Lenguaje interpretado (no necesita compilación)
- Tipado dinámico: el tipo de una variable puede cambiar en tiempo de ejecución
- Basado en prototipos (POO diferente a Java/Python)
- Multiparadigma: imperativo, funcional y orientado a objetos

---

## 2. Variables y Tipos de Datos

```javascript
// 3 formas de declarar variables
var nombre = "Fredys";      // scope global/función — evitar en código moderno
let edad = 30;              // scope de bloque — para valores que cambian
const PI = 3.14159;         // scope de bloque — para valores constantes

// Tipos primitivos
let texto    = "Hola mundo";   // String
let numero   = 42;             // Number
let decimal  = 3.14;           // Number (JS no distingue int/float)
let activo   = true;           // Boolean
let vacio    = null;           // Null (ausencia intencional de valor)
let indefinido;                // Undefined (no asignado)

// Tipo complejo
let lista    = [1, 2, 3];      // Array
let objeto   = { nombre: "Firulais", especie: "Perro" };  // Object
```

> **Diferencia clave con Python:** en JS no hay `int` vs `float` — todo número es `Number`. Y `null` ≠ `undefined`: null es "sin valor a propósito", undefined es "nunca se le asignó valor".

---

## 3. Salidas: console.log vs innerHTML vs innerText

```javascript
// Consola del navegador (F12 → Console) — para desarrollo/debug
console.log("Hola desde la consola");
console.log("Mascota:", objeto.nombre);

// Modificar contenido HTML — para mostrar en la página
document.getElementById("resultado").innerHTML = "<b>Firulais</b>";  // acepta HTML
document.getElementById("resultado").innerText = "Firulais";          // solo texto plano
```

> `innerHTML` renderiza HTML (útil para formatear). `innerText` es más seguro contra inyección de código.

---

## 4. Operadores

```javascript
// Aritméticos
let suma = 10 + 5;      // 15
let mod  = 10 % 3;      // 1 (residuo)
let pot  = 2 ** 8;      // 256 (potencia)

// Comparación
5 == "5"    // true  — igualdad débil (convierte tipos)
5 === "5"   // false — igualdad estricta (tipo + valor) ← SIEMPRE usar esta
5 !== "5"   // true

// Lógicos
true && false   // false (AND)
true || false   // true  (OR)
!true           // false (NOT)
```

> Regla de oro: **siempre usa `===` y `!==`** en lugar de `==` y `!=`. La igualdad débil tiene comportamientos confusos entre tipos.

---

## 5. Sintaxis esencial

```javascript
// Comentarios
// Comentario de una línea
/* Comentario
   de varias líneas */

// Template literals (strings con variables)
let mascota = "Firulais";
let mensaje = `La mascota se llama ${mascota} y tiene ${edad} años`;

// Typeof — verificar tipo
typeof "hola"    // "string"
typeof 42        // "number"
typeof true      // "boolean"
typeof {}        // "object"
typeof []        // "object" (los arrays también son objetos en JS)
```

---

## 🗺️ Mapa mental

```
JAVASCRIPT FUNDAMENTOS
│
├── Variables
│     ├── var   → scope global (evitar)
│     ├── let   → scope bloque, valor mutable
│     └── const → scope bloque, valor constante
│
├── Tipos de Datos
│     ├── Primitivos: String, Number, Boolean, null, undefined
│     └── Complejos: Array, Object
│
├── Salidas
│     ├── console.log  → consola del navegador
│     ├── innerHTML    → HTML en el DOM
│     └── innerText    → texto plano en el DOM
│
└── Operadores
      ├── Aritméticos: + - * / % **
      ├── Comparación: === !== > < (siempre estrictos)
      └── Lógicos: && || !
```

---

## 📚 Referencias

Haverbeke, M. (2018). *Eloquent JavaScript* (3a ed.). https://eloquentjavascript.net/

MDN Web Docs. (2024). *JavaScript — MDN*. https://developer.mozilla.org/es/docs/Web/JavaScript
