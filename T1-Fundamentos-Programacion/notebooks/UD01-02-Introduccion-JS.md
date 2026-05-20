[UD01-02-Introduccion-JS.md](https://github.com/user-attachments/files/28076685/UD01-02-Introduccion-JS.md)# UD1-2 — Introducción a JavaScript

**Trimestre 1 · Universidad DaVinci · Maestría en Ciencia de Datos**

---

## 📌 Conceptos clave

- JavaScript es un lenguaje **interpretado, orientado a objetos y basado en prototipos**.
- Se ejecuta en el **navegador** (client-side) y en el **servidor** con Node.js.
- Todo valor en JS tiene un tipo: `String`, `Number`, `Boolean`, `null`, `undefined`, `Object`, `Array`.
- JS es **dinámicamente tipado** — no se declara el tipo de una variable, JS lo infiere.

---

## 📚 Contenido

- [¿Qué es JavaScript?](#qué-es-javascript)
- [Variables y tipos de datos](#variables-y-tipos-de-datos)
- [Operadores](#operadores)
- [Salidas: console.log vs innerHTML vs innerText](#salidas)
- [Buenas prácticas](#buenas-prácticas)

---

## ¿Qué es JavaScript?

JavaScript (JS) es el lenguaje de programación de la web. Junto con HTML y CSS forma la triada del desarrollo web:

| Tecnología | Rol |
|---|---|
| **HTML** | Estructura y contenido de la página |
| **CSS** | Estilos y apariencia visual |
| **JavaScript** | Comportamiento e interactividad |

JS permite que las páginas web reaccionen a las acciones del usuario, actualicen contenido sin recargar la página, consuman APIs y construyan aplicaciones completas tanto en el navegador como en el servidor (Node.js).

---

## Variables y tipos de datos

### Declaración de variables

```javascript
// let — ámbito de bloque (recomendado)
let nombre = "Fredys";

// const — valor constante, no se puede reasignar
const PI = 3.14159;

// var — ámbito de función (legacy, evitar en código moderno)
var edad = 30;
```

### Tipos de datos primitivos

```javascript
// String — texto
let saludo = "Hola mundo";

// Number — números enteros y decimales
let entero = 42;
let decimal = 3.14;

// Boolean — verdadero o falso
let activo = true;
let inactivo = false;

// null — ausencia intencional de valor
let resultado = null;

// undefined — variable declarada sin valor asignado
let sinValor;
console.log(sinValor); // undefined
```

### Tipos de datos compuestos

```javascript
// Array — colección ordenada de valores
let frutas = ["manzana", "pera", "uva"];

// Object — colección de pares clave:valor
let persona = {
  nombre: "Fredys",
  edad: 30,
  profesion: "BI Analyst"
};
```

### typeof — verificar el tipo de una variable

```javascript
console.log(typeof "Hola");    // "string"
console.log(typeof 42);        // "number"
console.log(typeof true);      // "boolean"
console.log(typeof undefined); // "undefined"
console.log(typeof null);      // "object" ← comportamiento histórico de JS
console.log(typeof []);        // "object"
console.log(typeof {});        // "object"
```

---

## Operadores

### Operadores aritméticos

```javascript
let a = 10, b = 3;

console.log(a + b);  // 13 — suma
console.log(a - b);  // 7  — resta
console.log(a * b);  // 30 — multiplicación
console.log(a / b);  // 3.33 — división
console.log(a % b);  // 1  — módulo (residuo)
console.log(a ** b); // 1000 — potencia
```

### Operadores de comparación

```javascript
// == compara VALOR (convierte tipos)
console.log(5 == "5");   // true ⚠️

// === compara VALOR y TIPO (recomendado)
console.log(5 === "5");  // false ✅
console.log(5 === 5);    // true

console.log(5 != "5");   // false
console.log(5 !== "5");  // true ✅
console.log(10 > 5);     // true
console.log(10 >= 10);   // true
```

### Operadores lógicos

```javascript
console.log(true && false); // false — AND (ambos deben ser true)
console.log(true || false); // true  — OR (al menos uno debe ser true)
console.log(!true);         // false — NOT (invierte el valor)
```

---

## Salidas

### console.log — salida en consola del navegador

```javascript
console.log("Hola mundo");
console.log("Suma:", 2 + 3);
console.log("Array:", [1, 2, 3]);
```
> Usar en DevTools (F12 → Console) o Node.js

### innerHTML — inserta HTML en un elemento

```javascript
document.getElementById("resultado").innerHTML = "<b>Hola</b> mundo";
// Renderiza el HTML — muestra "Hola" en negrita
```

### innerText — inserta texto plano

```javascript
document.getElementById("resultado").innerText = "<b>Hola</b> mundo";
// Muestra el texto literal: <b>Hola</b> mundo (sin renderizar)
```

| Método | ¿Renderiza HTML? | Uso recomendado |
|---|---|---|
| `console.log` | No | Depuración y desarrollo |
| `innerHTML` | ✅ Sí | Insertar contenido HTML dinámico |
| `innerText` | No | Insertar texto plano seguro |

---

## Buenas prácticas

- Usar `let` y `const` — evitar `var`
- Usar `===` en lugar de `==` para comparaciones
- Nombrar variables en **camelCase**: `miVariable`, `precioTotal`
- Nombrar constantes en **UPPER_SNAKE_CASE**: `MAX_INTENTOS`
- Comentar el código con `//` para líneas y `/* */` para bloques
- Una variable = una responsabilidad

---

## 💡 Conexión con experiencia profesional

En el trabajo con **Power BI y DAX**, muchos conceptos son equivalentes:
- `let` en JS ≈ variable en DAX
- `typeof` en JS ≈ `TYPE()` en DAX para verificar tipos
- `console.log` en JS ≈ la vista de datos en Power BI para depurar

En **Google Apps Script** (automatización de Google Sheets), el código es 100% JavaScript — todo lo aprendido aquí aplica directamente para automatizar reportes.

---

## ❓ Preguntas de repaso

1. ¿Cuál es la diferencia entre `==` y `===` en JavaScript?
2. ¿Qué retorna `typeof null` y por qué?
3. ¿Cuándo usarías `innerHTML` vs `innerText`?
4. ¿Qué diferencia hay entre `let`, `const` y `var`?
5. ¿Qué es el operador módulo `%` y para qué sirve?

---

## 📖 Referencias

- Haverbeke, M. (2018). *Eloquent JavaScript* (3a ed.). https://eloquentjavascript.net/
- MDN Web Docs. (2024). *JavaScript — MDN*. https://developer.mozilla.org/es/docs/Web/JavaScript
- MDN Web Docs. (2024). *typeof*. https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Operators/typeof

---

[← Volver a la asignatura](../README.md) · [← Volver al inicio](../../README.md)


