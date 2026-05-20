# UD10 — Frameworks y jQuery

**Trimestre 1 · Universidad DaVinci · Maestría en Ciencia de Datos**

---

## 📌 Conceptos clave

- Un **framework** es una estructura predefinida que acelera el desarrollo evitando código repetitivo.
- Las ventajas clave son: ahorro de tiempo, código limpio, escalabilidad y seguridad.
- **jQuery** es una biblioteca JS con el lema *"escribe menos, haz más"*.
- El selector `$()` permite manipular el DOM con sintaxis CSS.
- jQuery sigue siendo válido para proyectos pequeños y legacy — no para apps modernas complejas.

---

## 📚 Contenido

- [¿Qué es un Framework?](#qué-es-un-framework)
- [Ventajas de los frameworks](#ventajas-de-los-frameworks)
- [¿Qué es jQuery?](#qué-es-jquery)
- [Selectores y manipulación del DOM](#selectores-y-manipulación-del-dom)
- [Eventos](#eventos)
- [Efectos y animaciones](#efectos-y-animaciones)
- [AJAX con jQuery](#ajax-con-jquery)
- [¿jQuery o React/Vue?](#jquery-o-reactvue)

---

## ¿Qué es un Framework?

Un framework es una **estructura de software predefinida** con herramientas, bibliotecas y convenciones que permiten desarrollar aplicaciones más rápido y con mejor calidad.

| Analogía | Sin framework | Con framework |
|---|---|---|
| Construir una casa | Fabricar cada ladrillo desde cero | Usar materiales prefabricados y planos estándar |

---

## Ventajas de los frameworks

| Ventaja | Descripción |
|---|---|
| **Ahorro de tiempo** | Componentes y funcionalidades predefinidas — no reinventar la rueda |
| **Código limpio** | Convenciones compartidas que hacen el código más legible y mantenible |
| **Escalabilidad** | Arquitectura modular que crece con el proyecto |
| **Seguridad** | Protecciones integradas contra XSS, SQL injection y otros ataques |
| **Trabajo en equipo** | Todos usan las mismas convenciones — menos conflictos |

---

## ¿Qué es jQuery?

jQuery es una **biblioteca JavaScript** creada por John Resig en 2006. Su filosofía: **"Write less, do more"** (escribe menos, haz más).

```javascript
// Sin jQuery — JS puro
document.getElementById("titulo").style.color = "blue";
document.getElementById("titulo").innerText = "Nuevo título";

// Con jQuery — más conciso
$("#titulo").css("color", "blue").text("Nuevo título");
```

> En 2023, el 22.87% de los desarrolladores aún usan jQuery (Stack Overflow).

---

## Selectores y manipulación del DOM

```javascript
// Seleccionar elementos con sintaxis CSS
$("#miId")         // por ID
$(".miClase")      // por clase
$("p")             // por etiqueta
$("div > p")       // selector anidado

// Manipular contenido
$("#titulo").text("Nuevo texto");          // texto plano
$("#contenedor").html("<b>HTML aquí</b>"); // HTML

// Manipular estilos
$("p").css("color", "red");
$(".tarjeta").css({
  "background": "#f0f0f0",
  "padding": "10px"
});

// Manipular atributos
$("img").attr("src", "nueva.jpg");
$("input").val("nuevo valor");
```

---

## Eventos

```javascript
// Click
$("#boton").click(function() {
  console.log("Botón clickeado");
});

// Hover
$(".tarjeta").hover(
  function() { $(this).css("background", "yellow"); }, // al entrar
  function() { $(this).css("background", "white"); }   // al salir
);

// Tecla presionada
$("input").keypress(function(e) {
  console.log("Tecla:", e.key);
});

// Submit de formulario
$("form").submit(function(e) {
  e.preventDefault();
  console.log("Formulario enviado");
});
```

---

## Efectos y animaciones

```javascript
// Mostrar y ocultar
$("#elemento").show();    // mostrar
$("#elemento").hide();    // ocultar
$("#elemento").toggle();  // alternar

// Con duración (ms)
$("#elemento").show(500);
$("#elemento").hide("slow");

// Fade
$("#elemento").fadeIn(400);
$("#elemento").fadeOut(400);
$("#elemento").fadeToggle();

// Slide
$("#elemento").slideDown();
$("#elemento").slideUp();
$("#elemento").slideToggle();

// Animación personalizada
$("#caja").animate({
  width: "300px",
  opacity: 0.5
}, 1000);
```

---

## AJAX con jQuery

```javascript
// $.ajax — completo y configurable
$.ajax({
  url: "https://api.github.com/users/1",
  method: "GET",
  success: function(usuario) {
    console.log("Login:", usuario.login);
  },
  error: function(error) {
    console.log("Error:", error);
  }
});

// $.get — versión simplificada
$.get("https://api.github.com/users/1", function(usuario) {
  console.log(usuario);
});
```

---

## ¿jQuery o React/Vue?

| Criterio | jQuery ✅ | React / Vue ✅ |
|---|---|---|
| **Proyectos pequeños** | Ideal | Excesivo |
| **Código legacy** | Mantener | Migrar gradualmente |
| **Aprendizaje JS** | Buen punto de partida | Después de dominar JS puro |
| **Apps modernas complejas** | No recomendado | Ideal |
| **Manejo de estado** | Limitado | Excelente |
| **Rendimiento** | Agrega ~90KB | Más optimizado |

> **Conclusión:** jQuery no está obsoleto — está especializado. Saber cuándo usarlo es señal de madurez técnica.

---

## 💡 Conexión con experiencia profesional

En muchos sistemas **legacy corporativos** (ERPs, CRMs antiguos), jQuery sigue siendo la tecnología de frontend. Entenderlo es clave para mantener esos sistemas.

**Odoo** usa jQuery internamente en algunos módulos de su interfaz web.

---

## ❓ Preguntas de repaso

1. ¿Cuáles son las 4 ventajas principales de usar un framework?
2. ¿Qué significa el lema de jQuery "Write less, do more"?
3. ¿Cuál es la diferencia entre `.text()` y `.html()` en jQuery?
4. ¿Por qué jQuery no es recomendado para aplicaciones modernas complejas?
5. ¿Qué agrega jQuery al peso de una página web?

---

## 📖 Referencias

- jQuery Foundation. (2024). *jQuery API Documentation*. https://api.jquery.com/
- Bouza, C. (2024). *Refrescando jQuery: ¿aún relevante en 2024?* https://carlosbouza.dev/refrescando-jquery-aun-relevante-en-2024/
- MDN Web Docs. (2024). *Fetch API*. https://developer.mozilla.org/es/docs/Web/API/Fetch_API

---

[← Volver a la asignatura](../README.md) · [← Volver al inicio](../../README.md)
