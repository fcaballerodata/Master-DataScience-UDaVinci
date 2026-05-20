# UD8 — Interfaces: DOM y BOM

**Trimestre 1 · Universidad DaVinci · Maestría en Ciencia de Datos**

---

## 📌 Conceptos clave

- El **DOM** conecta JavaScript con el HTML — permite manipular la página sin recargarla.
- El **BOM** permite interactuar con el **navegador** — más allá del contenido de la página.
- `getElementById`, `querySelector` seleccionan elementos del DOM.
- `window` es el objeto raíz del BOM del que se desprenden `location`, `history`, `navigator`.
- Los formularios permiten **capturar, validar y procesar** datos del usuario en tiempo real.

---

## 📚 Contenido

- [¿Qué es el DOM?](#qué-es-el-dom)
- [Selección de elementos](#selección-de-elementos)
- [Manipulación dinámica](#manipulación-dinámica)
- [¿Qué es el BOM?](#qué-es-el-bom)
- [Formularios y validación](#formularios-y-validación)

---

## ¿Qué es el DOM?

El **Document Object Model** es una representación en forma de árbol jerárquico del contenido HTML de una página. JS puede acceder y modificar cualquier nodo de ese árbol.

```
document
└── html
    ├── head
    │   └── title
    └── body
        ├── h1
        ├── p
        └── div
            └── button
```

---

## Selección de elementos

```javascript
// Por ID — devuelve UN elemento
let titulo = document.getElementById("miTitulo");

// Por clase — devuelve HTMLCollection (varios)
let items = document.getElementsByClassName("item");

// Por selector CSS — el más flexible
let btn = document.querySelector("#miBoton");        // primer elemento
let todos = document.querySelectorAll(".tarjeta");   // todos los elementos
```

---

## Manipulación dinámica

```javascript
// Cambiar el contenido
let titulo = document.getElementById("titulo");
titulo.innerHTML = "<b>Nuevo título</b>"; // interpreta HTML
titulo.innerText = "Solo texto";          // texto plano

// Cambiar estilos
titulo.style.color = "blue";
titulo.style.fontSize = "24px";

// Cambiar atributos
let img = document.querySelector("img");
img.src = "nueva-imagen.jpg";
img.alt = "Descripción de la imagen";

// Crear y agregar elementos
let nuevoParrafo = document.createElement("p");
nuevoParrafo.innerText = "Este párrafo fue creado con JS";
document.body.appendChild(nuevoParrafo);

// Eventos
let boton = document.getElementById("miBoton");
boton.addEventListener("click", function() {
  console.log("¡Botón clickeado!");
});
```

---

## ¿Qué es el BOM?

El **Browser Object Model** permite interactuar con el navegador. Su objeto principal es `window`, del que se desprenden todos los demás.

```
window
├── document    ← el DOM
├── location    ← URL actual
├── history     ← historial de navegación
├── navigator   ← información del navegador
└── screen      ← información de la pantalla
```

```javascript
// location — controlar la URL
console.log(window.location.href);      // URL actual
window.location.href = "https://google.com"; // redirigir

// history — navegación
window.history.back();    // simula el botón "atrás"
window.history.forward(); // simula el botón "adelante"

// navigator — información del navegador/dispositivo
console.log(navigator.userAgent);   // info del navegador
console.log(navigator.language);    // idioma del navegador

// Geolocalización
navigator.geolocation.getCurrentPosition(function(pos) {
  console.log("Latitud:", pos.coords.latitude);
  console.log("Longitud:", pos.coords.longitude);
});

// screen — tamaño de la pantalla
console.log(screen.width);  // ancho en píxeles
console.log(screen.height); // alto en píxeles
```

---

## Formularios y validación

```html
<!-- HTML del formulario -->
<form id="miFormulario">
  <input type="text" id="nombre" placeholder="Tu nombre">
  <button type="submit">Enviar</button>
  <p id="mensaje"></p>
</form>
```

```javascript
// Validación en tiempo real con JS
let formulario = document.getElementById("miFormulario");
let nombre = document.getElementById("nombre");
let mensaje = document.getElementById("mensaje");

formulario.addEventListener("submit", function(evento) {
  evento.preventDefault(); // Evita que la página se recargue

  if (nombre.value.trim() === "") {
    mensaje.innerHTML = "<span style='color:red'>El nombre es requerido</span>";
  } else {
    mensaje.innerHTML = `<span style='color:green'>Hola, ${nombre.value}!</span>`;
  }
});
```

---

## 💡 Conexión con experiencia profesional

En **Power BI Embedded**, JS se usa para controlar el comportamiento del reporte desde el navegador — exactamente el mismo concepto de manipulación del DOM.

En el desarrollo web moderno, frameworks como **React y Vue** abstraen la manipulación del DOM — pero por debajo siguen usando los mismos métodos que aprendimos aquí.

---

## ❓ Preguntas de repaso

1. ¿Cuál es la diferencia entre el DOM y el BOM?
2. ¿Qué diferencia hay entre `getElementById` y `querySelector`?
3. ¿Para qué sirve `evento.preventDefault()` en un formulario?
4. ¿Qué objeto del BOM usarías para redirigir al usuario a otra página?
5. ¿Cómo agregarías un elemento nuevo al final del `body` con JS?

---

## 📖 Referencias

- Haverbeke, M. (2018). *Eloquent JavaScript* (3a ed.). https://eloquentjavascript.net/
- MDN Web Docs. (2024). *Document Object Model*. https://developer.mozilla.org/es/docs/Web/API/Document_Object_Model
- MDN Web Docs. (2024). *Window*. https://developer.mozilla.org/es/docs/Web/API/Window

---

[← Volver a la asignatura](../README.md) · [← Volver al inicio](../../README.md)
