# UD6 — Arreglos

**Trimestre 1 · Universidad DaVinci · Maestría en Ciencia de Datos**

---

## 📌 Conceptos clave

- Un arreglo es una **colección ordenada** de valores indexados desde 0.
- `.length` devuelve el número de elementos.
- `.push()` agrega al final; `.indexOf()` busca la posición de un elemento.
- `.sort()` sin función compara como texto — usar `(a,b) => a-b` para números.
- `.concat()` une arreglos sin modificar los originales.
- Los arreglos multidimensionales se acceden con doble índice `[fila][columna]`.

---

## 📚 Contenido

- [Declaración y creación](#declaración-y-creación)
- [Propiedad length](#propiedad-length)
- [Métodos principales](#métodos-principales)
- [Arreglos multidimensionales](#arreglos-multidimensionales)
- [Parámetros vararg](#parámetros-vararg)

---

## Declaración y creación

```javascript
// Con corchetes (recomendado)
let frutas = ["manzana", "pera", "uva"];
let numeros = [10, 20, 30, 40, 50];
let mixto = ["texto", 42, true, null];

// Acceder por índice (inicia en 0)
console.log(frutas[0]); // "manzana"
console.log(frutas[2]); // "uva"

// Modificar un elemento
frutas[1] = "naranja";
console.log(frutas); // ["manzana", "naranja", "uva"]
```

---

## Propiedad length

```javascript
let frutas = ["manzana", "pera", "uva"];
console.log(frutas.length); // 3

// Recorrer con length
for (let i = 0; i < frutas.length; i++) {
  console.log(frutas[i]);
}
```

---

## Métodos principales

```javascript
let numeros = [3, 1, 4, 1, 5, 9];

// push() — agrega al FINAL
numeros.push(2);
console.log(numeros); // [3, 1, 4, 1, 5, 9, 2]

// pop() — elimina el ÚLTIMO elemento
numeros.pop();
console.log(numeros); // [3, 1, 4, 1, 5, 9]

// indexOf() — busca la posición de un elemento (-1 si no existe)
console.log(numeros.indexOf(4)); // 2
console.log(numeros.indexOf(7)); // -1

// concat() — une dos arreglos en uno nuevo (no modifica los originales)
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];
let union = arr1.concat(arr2);
console.log(union); // [1, 2, 3, 4, 5, 6]

// sort() — ordenar como texto ⚠️
let letras = ["c", "a", "b"];
letras.sort();
console.log(letras); // ["a", "b", "c"]

// sort() — ordenar números CORRECTAMENTE con función de comparación ✅
let nums = [10, 2, 30, 5];
nums.sort((a, b) => a - b); // ascendente
console.log(nums); // [2, 5, 10, 30]

nums.sort((a, b) => b - a); // descendente
console.log(nums); // [30, 10, 5, 2]

// toString() — convierte el arreglo a string
console.log([1,2,3].toString()); // "1,2,3"
```

---

## Arreglos multidimensionales

```javascript
// Matriz 3x3
let matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

// Acceder con doble índice [fila][columna]
console.log(matriz[0][0]); // 1 — fila 0, columna 0
console.log(matriz[1][2]); // 6 — fila 1, columna 2
console.log(matriz[2][2]); // 9 — fila 2, columna 2 (diagonal)

// Recorrer la diagonal principal
for (let i = 0; i < matriz.length; i++) {
  console.log(matriz[i][i]); // 1, 5, 9
}
```

---

## Parámetros vararg

```javascript
// ... (rest/spread) permite recibir número variable de argumentos
function sumarTodos(...numeros) {
  let total = 0;
  for (let num of numeros) {
    total += num;
  }
  return total;
}

console.log(sumarTodos(1, 2, 3));       // 6
console.log(sumarTodos(10, 20, 30, 40)); // 100
```

---

## 💡 Conexión con experiencia profesional

En **Python con Pandas**, los arreglos equivalen a las Series y listas:
```python
# Python
numeros = [10, 20, 30]
numeros.append(40)  # equivale a push()
```

En **SQL con Snowflake**, el concepto de arreglo está en los arrays de Snowflake y en las filas de una tabla — recorrer un arreglo en JS es análogo a hacer un `SELECT` fila por fila.

---

## ❓ Preguntas de repaso

1. ¿Por qué `sort()` sin función da resultados incorrectos con números?
2. ¿Cuál es la diferencia entre `push()` y `concat()`?
3. ¿Qué devuelve `indexOf()` si el elemento no existe?
4. ¿Cómo accedes al elemento de la posición [2][1] de una matriz?
5. ¿Para qué sirve el operador `...` (spread/rest)?

---

## 📖 Referencias

- Haverbeke, M. (2018). *Eloquent JavaScript* (3a ed.). https://eloquentjavascript.net/
- MDN Web Docs. (2024). *Array*. https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array

---

[← Volver a la asignatura](../README.md) · [← Volver al inicio](../../README.md)
