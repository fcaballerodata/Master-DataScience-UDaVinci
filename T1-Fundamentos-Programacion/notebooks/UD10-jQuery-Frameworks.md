# 📘 UD10 — Frameworks y jQuery

**Trimestre 1 · S9-S10 (May 2026)**

---

## 1. ¿Qué es jQuery?

jQuery es una librería JavaScript que simplifica la manipulación del DOM, eventos y AJAX con una sintaxis concisa. Fue dominante en los 2010s y sigue siendo relevante en proyectos legacy.

```html
<!-- Incluir jQuery via CDN -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```

---

## 2. Selección y manipulación

```javascript
// Selección — usando $ en lugar de document.querySelector
$("#titulo")              // por ID
$(".btn")                 // por clase
$("p")                    // por etiqueta
$("[data-tipo='vip']")    // por atributo

// Manipulación
$("#titulo").text("Nuevo título");       // innerText
$("#titulo").html("<b>Negrita</b>");     // innerHTML
$("#titulo").css("color", "blue");       // estilo
$("#titulo").addClass("activo");         // agregar clase
$("#titulo").hide();                     // display: none
$("#titulo").show();                     // display: block
$("#titulo").toggle();                   // alternar visibilidad
```

---

## 3. Eventos con jQuery

```javascript
$(document).ready(function() {
    // Se ejecuta cuando el DOM está cargado (equivale a DOMContentLoaded)

    $("#btnGuardar").on("click", function() {
        const nombre = $("#inputNombre").val();
        $("#resultado").text(`Guardado: ${nombre}`);
    });
});

// Versión moderna con arrow function
$(document).ready(() => {
    $(".mascota").on("mouseenter", () => {
        $(this).css("background", "lightyellow");
    });
});
```

---

## 4. AJAX con jQuery

```javascript
$.ajax({
    url: "https://api.ejemplo.com/mascotas",
    method: "GET",
    success: function(data) {
        console.log("Datos:", data);
    },
    error: function(err) {
        console.error("Error:", err);
    }
});

// Versión simplificada
$.get("https://api.ejemplo.com/mascotas", data => console.log(data));
$.post("https://api.ejemplo.com/mascotas", { nombre: "Firulais" }, res => console.log(res));
```

---

## 5. JS moderno vs jQuery

| Tarea | jQuery | JS Moderno |
|---|---|---|
| Selección | `$("#id")` | `document.getElementById("id")` |
| Evento | `$.on("click", fn)` | `addEventListener("click", fn)` |
| AJAX | `$.ajax()` | `fetch()` |
| DOM ready | `$(document).ready()` | `DOMContentLoaded` |

> En proyectos nuevos se prefiere JS puro o frameworks como React/Vue. jQuery sigue siendo válido para mantener código legacy o proyectos simples.

---

## 🗺️ Mapa mental

```
JQUERY
│
├── Selección: $("selector")
├── Manipulación: .text(), .html(), .css(), .addClass()
├── Eventos: .on("evento", callback)
├── AJAX: $.ajax(), $.get(), $.post()
└── DOM Ready: $(document).ready()
```

## 📚 Referencias

jQuery Foundation. (2024). *jQuery API Documentation*. https://api.jquery.com/
