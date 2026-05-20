# UD5 — Sentencias de Repetición

**Trimestre 1 · Universidad DaVinci · Maestría en Ciencia de Datos**

---

## 📌 Conceptos clave

- `while` evalúa la condición **antes** — puede no ejecutarse nunca.
- `do...while` evalúa la condición **después** — siempre ejecuta al menos una vez.
- `for` es ideal cuando se conoce el número de iteraciones.
- `for...of` recorre los **valores** de un arreglo directamente.
- `break` detiene el bucle; `continue` salta a la siguiente iteración.

---

## 📚 Contenido

- [while](#while)
- [do...while](#dowhile)
- [for](#for)
- [for...of](#forof)
- [break y continue](#break-y-continue)
- [¿Cuándo usar cada uno?](#cuándo-usar-cada-uno)

---

## while

```javascript
// Cuenta del 1 al 5
let i = 1;
while (i <= 5) {
  console.log(i);
  i++;
}
// 1, 2, 3, 4, 5

// Si la condición es falsa desde el inicio, no se ejecuta
let x = 10;
while (x < 5) {
  console.log("Nunca se ejecuta");
}
```

---

## do...while

```javascript
// Siempre ejecuta el bloque al menos UNA vez
let i = 10;
do {
  console.log("Se ejecutó:", i);
  i++;
} while (i < 5);
// "Se ejecutó: 10" — aunque la condición es falsa, ejecuta una vez
```

---

## for

```javascript
// Estructura: for (inicio; condición; incremento)
for (let i = 0; i < 5; i++) {
  console.log(i);
}
// 0, 1, 2, 3, 4

// Recorrer un arreglo con for
let frutas = ["manzana", "pera", "uva"];
for (let i = 0; i < frutas.length; i++) {
  console.log(frutas[i]);
}
// "manzana", "pera", "uva"

// Suma de elementos
let numeros = [10, 20, 30, 40];
let suma = 0;
for (let i = 0; i < numeros.length; i++) {
  suma += numeros[i];
}
console.log("Suma:", suma); // 100
```

---

## for...of

```javascript
// Recorre directamente los VALORES del arreglo
let frutas = ["manzana", "pera", "uva"];
for (let fruta of frutas) {
  console.log(fruta);
}
// "manzana", "pera", "uva"

// Más limpio que el for tradicional cuando no necesitas el índice
```

---

## break y continue

```javascript
// break — detiene el bucle completamente
for (let i = 0; i < 10; i++) {
  if (i === 5) break;
  console.log(i);
}
// 0, 1, 2, 3, 4

// continue — salta la iteración actual y continúa
for (let i = 0; i < 5; i++) {
  if (i === 2) continue;
  console.log(i);
}
// 0, 1, 3, 4
```

---

## ¿Cuándo usar cada uno?

| Bucle | Úsalo cuando... |
|---|---|
| `while` | No sabes cuántas iteraciones necesitas |
| `do...while` | Necesitas ejecutar el bloque al menos una vez |
| `for` | Sabes exactamente cuántas iteraciones son |
| `for...of` | Quieres recorrer los valores de un arreglo sin índice |

---

## 💡 Conexión con experiencia profesional

En **Python para análisis de datos**, el equivalente es el mismo concepto:
```python
# Python
for i in range(10):
    print(i)

# JS
for (let i = 0; i < 10; i++) {
  console.log(i);
}
```

En **Power BI con DAX**, las funciones iteradoras como `SUMX()`, `AVERAGEX()` y `FILTER()` son equivalentes a los bucles — recorren una tabla fila por fila aplicando una expresión.

---

## ❓ Preguntas de repaso

1. ¿Cuál es la diferencia principal entre `while` y `do...while`?
2. ¿Para qué sirve `break` dentro de un bucle?
3. ¿Qué hace `continue` diferente a `break`?
4. ¿Cuándo preferirías `for...of` sobre un `for` tradicional?
5. ¿Qué pasa si olvidamos incrementar el contador en un `while`?

---

## 📖 Referencias

- Haverbeke, M. (2018). *Eloquent JavaScript* (3a ed.). https://eloquentjavascript.net/
- MDN Web Docs. (2024). *for*. https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/for
- MDN Web Docs. (2024). *while*. https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/while

---

[← Volver a la asignatura](../README.md) · [← Volver al inicio](../../README.md)
