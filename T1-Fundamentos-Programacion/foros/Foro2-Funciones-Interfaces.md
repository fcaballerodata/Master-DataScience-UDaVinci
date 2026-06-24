# 💬 Foro II — Funciones e Interfaces

**Asignatura:** Fundamentos de Programación (JavaScript) · T1 S8

---

## 📋 Preguntas

1. ¿Qué son las funciones en programación y cuál es su importancia?
2. ¿Cuál es la diferencia entre una función declarada y una arrow function?
3. ¿Qué es el DOM y cómo lo manipula JavaScript?
4. Describe un caso donde el uso de AJAX mejoraría la experiencia de usuario en una aplicación.

---

## ✍️ Respuesta publicada

Las funciones y las interfaces son los dos pilares sobre los que se construye cualquier aplicación web interactiva. Las funciones organizan la lógica; las interfaces (DOM, eventos, AJAX) conectan esa lógica con el usuario.

**¿Qué son las funciones y cuál es su importancia?**

Una función es un bloque de código reutilizable que encapsula una tarea específica y puede ser invocado múltiples veces con diferentes argumentos. Su importancia radica en tres principios: reutilización (evita duplicar código), abstracción (oculta la complejidad interna) y mantenibilidad (un cambio en la función se refleja en todos los lugares donde se usa). Como señala Haverbeke (2018), las funciones son el mecanismo principal para controlar la complejidad en los programas, ya que permiten construir bloques más grandes sobre bloques más pequeños y bien definidos.

**Diferencia entre función declarada y arrow function**

La función declarada (`function nombre() {}`) tiene su propio contexto `this` y se eleva (hoisting) al inicio del scope, lo que permite llamarla antes de definirla. La arrow function (`() => {}`) no tiene su propio `this` — hereda el del contexto exterior — y no se eleva. La diferencia práctica más importante es el comportamiento de `this`: dentro de una clase o un callback de evento, las arrow functions son más predecibles porque mantienen la referencia al objeto que las contiene, mientras que las funciones tradicionales pueden perder el contexto.

**¿Qué es el DOM y cómo lo manipula JavaScript?**

El DOM (Document Object Model) es la representación en árbol del documento HTML que el navegador construye en memoria, y que JavaScript puede leer y modificar en tiempo real. Cada etiqueta HTML se convierte en un nodo del árbol, y JS puede seleccionarlos (`querySelector`, `getElementById`), modificar su contenido (`innerText`, `innerHTML`), cambiar sus estilos o atributos, agregar nuevos nodos o eliminar existentes, y escuchar eventos del usuario (clics, teclado, scroll). Según MDN Web Docs (2024), el DOM es la interfaz de programación que permite a los lenguajes de script acceder y modificar el contenido, estructura y estilo de un documento.

**Caso real: AJAX en dashboards de Movet**

En los dashboards de Power BI Embedded que construí para Movet, los reportes requerían recargar la página completa para actualizar los datos. Con AJAX, ese flujo se transforma: cuando el usuario selecciona un filtro (sede, período), una petición asíncrona obtiene solo los datos necesarios y actualiza únicamente la sección relevante del dashboard, sin recargar la página. El resultado es una experiencia más fluida, menor consumo de ancho de banda y tiempos de respuesta más rápidos — exactamente la diferencia entre una aplicación web estática y una dinámica.

---

## 📚 Referencias

Haverbeke, M. (2018). *Eloquent JavaScript* (3a ed.). https://eloquentjavascript.net/

MDN Web Docs. (2024). *Document Object Model (DOM)*. https://developer.mozilla.org/es/docs/Web/API/Document_Object_Model
