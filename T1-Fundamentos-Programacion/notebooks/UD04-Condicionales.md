# 📘 UD4 — Sentencias Condicionales

**Trimestre 1 · S4 (Mar 2026)**

---

## 1. Operadores de comparación y lógicos

```javascript
// Siempre usar === (estricto) en lugar de == (débil)
10 === 10       // true
10 === "10"     // false (diferente tipo)
10 !== 5        // true

// Lógicos
(edad >= 18) && (activo === true)   // AND — ambas deben ser true
(rol === "admin") || (rol === "dev") // OR — al menos una true
!(activo)                            // NOT — invierte
```

---

## 2. if / else if / else

```javascript
function clasificarMascota(peso) {
    if (peso < 5) {
        return "Talla XS";
    } else if (peso < 15) {
        return "Talla S-M";
    } else if (peso < 30) {
        return "Talla L";
    } else {
        return "Talla XL";
    }
}

console.log(clasificarMascota(3));   // Talla XS
console.log(clasificarMascota(22));  // Talla L
```

> **Buena práctica:** no uses `else if` cuando las condiciones son mutuamente excluyentes con muchos casos — considera `switch`.

---

## 3. switch

```javascript
function tipoConsulta(codigo) {
    switch (codigo) {
        case "VAC":
            return "Vacunación";
        case "CIR":
            return "Cirugía";
        case "CON":
            return "Consulta general";
        default:
            return "Tipo desconocido";
    }
}

console.log(tipoConsulta("VAC"));  // Vacunación
console.log(tipoConsulta("XYZ"));  // Tipo desconocido
```

> Siempre incluye `default` en un switch — es el equivalente del `else` final.

---

## 4. Operador ternario

```javascript
// condición ? valor_si_true : valor_si_false
let estado = (activo) ? "Activo" : "Inactivo";
let descuento = (esMiembro) ? precio * 0.9 : precio;
```

---

## 🗺️ Mapa mental

```
CONDICIONALES
│
├── if / else if / else → condiciones múltiples con rangos
├── switch              → condiciones discretas (muchos casos exactos)
├── Ternario            → condición simple en una línea
└── Operadores
      ├── === !== > < >= <=  (comparación — siempre estrictos)
      └── && || !             (lógicos)
```
