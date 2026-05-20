# UD4 — Condicionales

**Trimestre 1 · Universidad DaVinci · Maestría en Ciencia de Datos**

---

## 📌 Conceptos clave

- `===` compara valor **y** tipo — siempre preferir sobre `==`.
- `if/else if/else` evalúa condiciones en cadena — solo ejecuta el primer bloque verdadero.
- `switch` es ideal cuando hay muchas condiciones sobre el **mismo valor**.
- El operador ternario `condicion ? valorSi : valorNo` es la forma compacta del if/else.
- Los operadores lógicos `&&`, `||`, `!` permiten combinar condiciones.

---

## 📚 Contenido

- [Operadores de comparación](#operadores-de-comparación)
- [Operadores lógicos](#operadores-lógicos)
- [if / else if / else](#if--else-if--else)
- [switch](#switch)
- [Operador ternario](#operador-ternario)

---

## Operadores de comparación

```javascript
// == compara solo VALOR (hace conversión de tipos) ⚠️
console.log(5 == "5");   // true

// === compara VALOR y TIPO ✅ recomendado
console.log(5 === "5");  // false
console.log(5 === 5);    // true

console.log(5 !== "5");  // true
console.log(10 > 5);     // true
console.log(10 >= 10);   // true
console.log(3 < 5);      // true
console.log(3 <= 2);     // false
```

---

## Operadores lógicos

```javascript
// AND — ambas condiciones deben ser true
console.log(true && true);   // true
console.log(true && false);  // false

// OR — al menos una condición debe ser true
console.log(true || false);  // true
console.log(false || false); // false

// NOT — invierte el valor
console.log(!true);  // false
console.log(!false); // true

// Ejemplo combinado
let edad = 25;
let tieneCarnet = true;
if (edad >= 18 && tieneCarnet) {
  console.log("Puede conducir");
}
```

---

## if / else if / else

```javascript
let nota = 75;

if (nota >= 90) {
  console.log("Excelente");
} else if (nota >= 70) {
  console.log("Aprobado");
} else if (nota >= 50) {
  console.log("Regular");
} else {
  console.log("Reprobado");
}
// Resultado: "Aprobado"
```

> Solo se ejecuta el **primer bloque** cuya condición sea verdadera. Los demás se ignoran.

---

## switch

```javascript
let dia = "lunes";

switch (dia) {
  case "lunes":
    console.log("Inicio de semana");
    break;
  case "viernes":
    console.log("Fin de semana laboral");
    break;
  case "sabado":
  case "domingo":
    console.log("Fin de semana");
    break;
  default:
    console.log("Día entre semana");
}
// Resultado: "Inicio de semana"
```

> Sin `break`, la ejecución continúa al siguiente `case` (comportamiento llamado *fall-through*).

---

## Operador ternario

```javascript
// Sintaxis: condicion ? valorSiTrue : valorSiFalse
let edad = 20;
let acceso = edad >= 18 ? "Permitido" : "Denegado";
console.log(acceso); // "Permitido"

// Equivale a:
let acceso2;
if (edad >= 18) {
  acceso2 = "Permitido";
} else {
  acceso2 = "Denegado";
}
```

---

## 💡 Conexión con experiencia profesional

En **Power BI con DAX**, la función `IF()` es equivalente al `if/else` de JS:
```
// DAX
Resultado = IF(Ventas[Monto] >= 1000, "Alto", "Bajo")

// JS equivalente
let resultado = monto >= 1000 ? "Alto" : "Bajo";
```

En **SQL con Snowflake**, el `CASE WHEN` es equivalente al `switch`:
```sql
CASE
  WHEN nota >= 90 THEN 'Excelente'
  WHEN nota >= 70 THEN 'Aprobado'
  ELSE 'Reprobado'
END
```

---

## ❓ Preguntas de repaso

1. ¿Por qué se recomienda `===` sobre `==`?
2. ¿Qué ocurre en un `switch` si olvidamos el `break`?
3. ¿Cuándo es más conveniente usar `switch` que `if/else if`?
4. Reescribe este ternario como if/else: `let x = a > b ? a : b`
5. ¿Qué resultado da `false || (3 > 1)`?

---

## 📖 Referencias

- Haverbeke, M. (2018). *Eloquent JavaScript* (3a ed.). https://eloquentjavascript.net/
- MDN Web Docs. (2024). *if...else*. https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/if...else
- MDN Web Docs. (2024). *switch*. https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/switch

---

[← Volver a la asignatura](../README.md) · [← Volver al inicio](../../README.md)
