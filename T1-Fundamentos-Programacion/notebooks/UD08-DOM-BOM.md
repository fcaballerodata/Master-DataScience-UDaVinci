# 📘 UD8 — Interfaces: DOM y BOM

**Trimestre 1 · S8 (Abr 2026)**

---

## 1. DOM — Document Object Model

El DOM es la representación en árbol del HTML que JavaScript puede manipular.

```javascript
// Seleccionar elementos
const titulo    = document.getElementById("titulo");
const botones   = document.querySelectorAll(".btn");
const primero   = document.querySelector("h1");

// Leer y modificar contenido
titulo.innerText  = "Nuevo título";
titulo.innerHTML  = "<strong>Título en negrita</strong>";

// Modificar estilos
titulo.style.color      = "blue";
titulo.style.fontSize   = "24px";

// Modificar atributos
const img = document.querySelector("img");
img.setAttribute("src", "nueva-imagen.jpg");
img.getAttribute("alt");

// Crear y agregar elementos
const parrafo = document.createElement("p");
parrafo.innerText = "Nuevo párrafo";
document.body.appendChild(parrafo);

// Eliminar
parrafo.remove();
```

---

## 2. Eventos

```javascript
const boton = document.getElementById("btnGuardar");

// Escuchar eventos
boton.addEventListener("click", function(evento) {
    console.log("Botón clickeado");
    evento.preventDefault();  // evita comportamiento por defecto (ej: submit de form)
});

// Eventos comunes
// click, dblclick, mouseover, mouseout
// keydown, keyup, keypress
// submit, change, input, focus, blur
// load, DOMContentLoaded
```

---

## 3. BOM — Browser Object Model

```javascript
// window — objeto global del navegador
console.log(window.innerWidth);   // ancho de la ventana
console.log(window.location.href); // URL actual
window.location.href = "https://movet.co";  // redirigir

// localStorage — persistencia en el navegador
localStorage.setItem("usuario", "Fredys");
const user = localStorage.getItem("usuario");
localStorage.removeItem("usuario");

// Timers
const id = setTimeout(() => console.log("Después de 2s"), 2000);
clearTimeout(id);  // cancelar

const intervalo = setInterval(() => console.log("Cada segundo"), 1000);
clearInterval(intervalo);
```

---

## 🗺️ Mapa mental

```
DOM / BOM
│
├── DOM → manipular el HTML
│     ├── Selección: getElementById, querySelector
│     ├── Modificación: innerText, innerHTML, style, setAttribute
│     ├── Creación: createElement, appendChild
│     └── Eventos: addEventListener
│
└── BOM → interactuar con el navegador
      ├── window.location → URL, redirigir
      ├── localStorage → persistencia local
      └── setTimeout / setInterval → timers
```
