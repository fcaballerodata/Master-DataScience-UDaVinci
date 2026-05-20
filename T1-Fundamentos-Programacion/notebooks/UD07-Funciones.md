# UD7 — Funciones

**Trimestre 1 · Universidad DaVinci · Maestría en Ciencia de Datos**

---

## 📌 Conceptos clave

- Una función es un bloque de código **reutilizable** que se ejecuta al ser invocado.
- Toda función sin `return` explícito devuelve `undefined`.
- `let` tiene **ámbito de bloque**; `var` tiene ámbito de función.
- Las **arrow functions** `=>` son una sintaxis más compacta.
- Las funciones predefinidas (`Math`, `parseInt`, `String`) ya vienen en JS.

---

## 📚 Contenido

- [Declaración e invocación](#declaración-e-invocación)
- [Parámetros y argumentos](#parámetros-y-argumentos)
- [Valor de retorno](#valor-de-retorno)
- [Ámbito de variables](#ámbito-de-variables)
- [Funciones predefinidas](#funciones-predefinidas)
- [Arrow functions](#arrow-functions)

---

## Declaración e invocación

```javascript
// Declaración
function saludar() {
  console.log("¡Hola mundo!");
}

// Invocación
saludar(); // "¡Hola mundo!"
saludar(); // Se puede llamar múltiples veces
```

---

## Parámetros y argumentos

```javascript
// Parámetros: variables en la definición
function sumar(a, b) {
  return a + b;
}

// Argumentos: valores al invocar
console.log(sumar(3, 4));   // 7
console.log(sumar(10, 20)); // 30

// Parámetros con valor por defecto
function saludar(nombre = "visitante") {
  return `Hola, ${nombre}`;
}
console.log(saludar("Fredys")); // "Hola, Fredys"
console.log(saludar());         // "Hola, visitante"
```

---

## Valor de retorno

```javascript
// Con return — devuelve un valor
function cuadrado(n) {
  return n * n;
}
let resultado = cuadrado(5);
console.log(resultado); // 25

// Sin return — devuelve undefined
function sinReturn() {
  let x = 10;
}
console.log(sinReturn()); // undefined

// return detiene la función
function verificar(n) {
  if (n < 0) {
    return "Negativo";
  }
  return "Positivo o cero";
}
console.log(verificar(-5)); // "Negativo"
console.log(verificar(3));  // "Positivo o cero"
```

---

## Ámbito de variables

```javascript
// Variable global — accesible en todo el programa
let global = "Soy global";

function miFuncion() {
  // Variable local — solo accesible dentro de la función
  let local = "Soy local";
  console.log(global); // ✅ Puede acceder a la global
  console.log(local);  // ✅ Puede acceder a la local
}

miFuncion();
console.log(global); // ✅ Accesible
console.log(local);  // ❌ ReferenceError: local is not defined

// let vs var en bloques
if (true) {
  let conLet = "solo en este bloque";
  var conVar = "accesible fuera";
}
// console.log(conLet); // ❌ Error
console.log(conVar);    // ✅ "accesible fuera"
```

---

## Funciones predefinidas

```javascript
// Math — operaciones matemáticas
console.log(Math.round(4.7));   // 5
console.log(Math.floor(4.9));   // 4
console.log(Math.ceil(4.1));    // 5
console.log(Math.max(1,5,3));   // 5
console.log(Math.min(1,5,3));   // 1
console.log(Math.abs(-7));      // 7
console.log(Math.sqrt(16));     // 4
console.log(Math.pow(2,10));    // 1024
console.log(Math.random());     // número entre 0 y 1

// parseInt y parseFloat — convertir strings a números
console.log(parseInt("42px"));    // 42
console.log(parseFloat("3.14m")); // 3.14

// String — convertir a texto
console.log(String(42));    // "42"
console.log(String(true));  // "true"

// toFixed — formatear decimales
console.log((3.14159).toFixed(2)); // "3.14"
```

---

## Arrow functions

```javascript
// Función tradicional
function sumar(a, b) {
  return a + b;
}

// Arrow function equivalente
const sumar = (a, b) => a + b;

// Con un solo parámetro — sin paréntesis
const doble = n => n * 2;

// Con cuerpo de bloque
const verificar = (n) => {
  if (n < 0) return "Negativo";
  return "Positivo";
};

console.log(sumar(3, 4));    // 7
console.log(doble(5));       // 10
console.log(verificar(-3));  // "Negativo"

// Muy usadas en métodos de arreglos
let numeros = [1, 2, 3, 4, 5];
let pares = numeros.filter(n => n % 2 === 0);
console.log(pares); // [2, 4]
```

---

## 💡 Conexión con experiencia profesional

En **Power BI con DAX**, las medidas son funciones:
```
// DAX — función
TotalVentas = SUM(Ventas[Monto])

// JS equivalente
function totalVentas(ventas) {
  return ventas.reduce((sum, v) => sum + v.monto, 0);
}
```

En **Python**, las funciones son idénticas en concepto — `def` en Python equivale a `function` en JS. Las **lambda** de Python equivalen a las **arrow functions** de JS.

---

## ❓ Preguntas de repaso

1. ¿Qué devuelve una función que no tiene `return`?
2. ¿Cuál es la diferencia entre parámetro y argumento?
3. ¿Por qué se prefiere `let` sobre `var` para variables locales?
4. ¿Cuándo una arrow function no necesita llaves `{}`?
5. ¿Qué hace `Math.floor()` diferente a `Math.round()`?

---

## 📖 Referencias

- Haverbeke, M. (2018). *Eloquent JavaScript* (3a ed.). https://eloquentjavascript.net/
- MDN Web Docs. (2024). *Functions*. https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Functions
- MDN Web Docs. (2024). *Math*. https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Math

---

[← Volver a la asignatura](../README.md) · [← Volver al inicio](../../README.md)
