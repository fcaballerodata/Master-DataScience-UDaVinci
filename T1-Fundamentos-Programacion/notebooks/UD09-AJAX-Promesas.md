# UD9 — Interfaces II: AJAX, fetch y Promesas

**Trimestre 1 · Universidad DaVinci · Maestría en Ciencia de Datos**

---

## 📌 Conceptos clave

- **AJAX** = Asynchronous JavaScript And XML — actualiza la página **sin recargarla**.
- **XHR** es el original (legacy); **fetch** es el estándar moderno.
- Una **Promesa** representa una operación asíncrona futura — puede resolverse (`resolve`) o rechazarse (`reject`).
- **async/await** es syntactic sugar sobre Promesas — hace el código más legible.
- `try/catch` captura errores en código asíncrono.

---

## 📚 Contenido

- [¿Qué es AJAX?](#qué-es-ajax)
- [XMLHttpRequest (XHR)](#xmlhttprequest-xhr)
- [fetch API](#fetch-api)
- [Promesas](#promesas)
- [async / await](#async--await)
- [¿Cuándo usar cada tecnología?](#cuándo-usar-cada-tecnología)

---

## ¿Qué es AJAX?

AJAX permite que una página web **se comunique con un servidor** y actualice su contenido sin necesidad de recargar la página completa.

| Sin AJAX | Con AJAX |
|---|---|
| Cada acción recarga la página entera | Solo se actualiza la parte necesaria |
| Experiencia lenta y discontinua | Experiencia fluida como una app |
| Ejemplo: webs de los años 90 | Ejemplo: Gmail, Google Maps, Netflix |

---

## XMLHttpRequest (XHR)

```javascript
// XHR — tecnología original (2000), hoy considerada legacy
let xhr = new XMLHttpRequest();

xhr.open("GET", "https://api.github.com/users/1");

xhr.onload = function() {
  if (xhr.status === 200) {
    let usuario = JSON.parse(xhr.responseText);
    console.log(usuario);
  } else {
    console.log("Error:", xhr.status);
  }
};

xhr.send();
```

> ⚠️ Ejecutar desde una página web (ej: github.com en DevTools), no desde `chrome://new-tab-page`.

---

## fetch API

```javascript
// fetch — estándar moderno, basado en Promesas
fetch("https://api.github.com/users/1")
  .then(function(response) {
    return response.json(); // convierte la respuesta a objeto JS
  })
  .then(function(usuario) {
    console.log(usuario);
    console.log("Login:", usuario.login);
  })
  .catch(function(error) {
    console.log("Error:", error);
  });

// Extraer solo las keys
fetch("https://api.github.com/users/1")
  .then(r => r.json())
  .then(usuario => {
    console.log("Keys:", Object.keys(usuario));
  });

// Extraer solo los values
fetch("https://api.github.com/users/1")
  .then(r => r.json())
  .then(usuario => {
    console.log("Values:", Object.values(usuario));
  });
```

---

## Promesas

```javascript
// Crear una Promesa explícita
function obtenerUsuario() {
  return new Promise(function(resolve, reject) {
    fetch("https://api.github.com/users/1")
      .then(r => r.json())
      .then(usuario => resolve(usuario))  // éxito
      .catch(error => reject(error));     // error
  });
}

// Consumir la Promesa
obtenerUsuario()
  .then(function(usuario) {
    console.log("Values:", Object.values(usuario));
  })
  .catch(function(error) {
    console.log("Error:", error);
  });
```

| Estado | Descripción |
|---|---|
| **pending** | La operación está en curso |
| **fulfilled** | Se llamó a `resolve()` — éxito |
| **rejected** | Se llamó a `reject()` — error |

---

## async / await

```javascript
// async/await — la forma más moderna y legible
async function obtenerUsuarios() {
  try {
    // await pausa hasta que fetch() resuelva
    let response = await fetch("https://api.github.com/users");
    let usuarios = await response.json();

    console.log("Total de registros:", usuarios.length);
    console.log(usuarios);

  } catch (error) {
    console.log("Error:", error);
  }
}

obtenerUsuarios();
```

> `await` solo puede usarse **dentro de una función `async`**.

---

## ¿Cuándo usar cada tecnología?

| Tecnología | Estado | Cuándo usar |
|---|---|---|
| **XHR** | Legacy | Solo mantenimiento de código antiguo |
| **fetch** | Estándar | Peticiones simples en proyectos modernos |
| **Promesas** | Estándar | Coordinar múltiples peticiones simultáneas |
| **async/await** | Recomendado ✅ | Siempre que se pueda — más legible |

---

## 💡 Conexión con experiencia profesional

En producción real, **async/await con fetch** es lo que se usa en frameworks como React, Vue y Angular para consumir APIs.

En **Power BI con APIs REST**, el mismo concepto aplica: cada vez que Power BI llama a un endpoint REST, internamente hace algo equivalente a un `fetch` — obtiene datos, los convierte a JSON y los procesa.

---

## ❓ Preguntas de repaso

1. ¿Qué significa que AJAX es asíncrono?
2. ¿Cuál es la diferencia entre XHR y fetch?
3. ¿Cuáles son los tres estados posibles de una Promesa?
4. ¿Por qué `await` solo puede usarse dentro de una función `async`?
5. ¿Qué reemplaza `try/catch` en código async respecto a las Promesas?

---

## 📖 Referencias

- Haverbeke, M. (2018). *Eloquent JavaScript* (3a ed.). https://eloquentjavascript.net/
- MDN Web Docs. (2024). *Fetch API*. https://developer.mozilla.org/es/docs/Web/API/Fetch_API
- MDN Web Docs. (2024). *Promise*. https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Promise
- MDN Web Docs. (2024). *async function*. https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/async_function

---

[← Volver a la asignatura](../README.md) · [← Volver al inicio](../../README.md)
