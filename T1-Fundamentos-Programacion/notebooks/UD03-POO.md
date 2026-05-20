# UD3 — Programación Orientada a Objetos (POO)

**Trimestre 1 · Universidad DaVinci · Maestría en Ciencia de Datos**

---

## 📌 Conceptos clave

- La POO organiza el código en **clases** (plantillas) y **objetos** (instancias).
- Una clase define **propiedades** (datos) y **métodos** (comportamientos).
- Los **getters** leen propiedades de forma controlada; los **setters** las modifican con validación.
- La **herencia** permite que una clase hija reutilice el código de una clase padre.
- `super()` llama al constructor de la clase padre desde la clase hija.

---

## 📚 Contenido

- [¿Qué es la POO?](#qué-es-la-poo)
- [Clases y objetos](#clases-y-objetos)
- [Propiedades y métodos](#propiedades-y-métodos)
- [Getters y Setters](#getters-y-setters)
- [Herencia](#herencia)

---

## ¿Qué es la POO?

La POO organiza el software en torno a **objetos** que combinan datos y comportamiento.

| Concepto | Analogía | En código |
|---|---|---|
| **Clase** | Plano de una casa | `class Mascota {}` |
| **Objeto** | La casa construida | `let m = new Mascota()` |
| **Propiedad** | Color de las paredes | `this.nombre = "Rex"` |
| **Método** | Abrir la puerta | `saludar() { ... }` |

---

## Clases y objetos

```javascript
class Mascota {
  constructor(nombre, especie, edad) {
    this.nombre = nombre;
    this.especie = especie;
    this.edad = edad;
  }
}

let mascota1 = new Mascota("Rex", "Perro", 3);
let mascota2 = new Mascota("Luna", "Gato", 5);

console.log(mascota1);        // Mascota { nombre: 'Rex', especie: 'Perro', edad: 3 }
console.log(mascota2.nombre); // "Luna"
```

> `constructor()` se ejecuta automáticamente al crear un objeto con `new`.

---

## Propiedades y métodos

```javascript
class Mascota {
  constructor(nombre, especie, edad) {
    this.nombre = nombre;
    this.especie = especie;
    this.edad = edad;
  }

  saludar() {
    return `Hola, soy ${this.nombre} y soy un ${this.especie}`;
  }

  edadHumana() {
    return this.edad * 7;
  }
}

let rex = new Mascota("Rex", "Perro", 3);
console.log(rex.saludar());    // "Hola, soy Rex y soy un Perro"
console.log(rex.edadHumana()); // 21
```

---

## Getters y Setters

```javascript
class Mascota {
  constructor(nombre, edad) {
    this.nombre = nombre;
    this._edad = edad; // _ indica propiedad "privada por convención"
  }

  get edad() {
    return `${this._edad} años`;
  }

  set edad(nuevaEdad) {
    if (nuevaEdad < 0) {
      console.log("Error: la edad no puede ser negativa");
    } else {
      this._edad = nuevaEdad;
    }
  }
}

let rex = new Mascota("Rex", 3);
console.log(rex.edad); // "3 años" — usa el getter
rex.edad = 4;          // usa el setter
rex.edad = -1;         // "Error: la edad no puede ser negativa"
```

---

## Herencia

```javascript
class Animal {
  constructor(nombre, especie) {
    this.nombre = nombre;
    this.especie = especie;
  }

  describir() {
    return `${this.nombre} es un ${this.especie}`;
  }
}

class Mascota extends Animal {
  constructor(nombre, especie, duenio) {
    super(nombre, especie); // llama al constructor del padre
    this.duenio = duenio;
  }

  presentar() {
    return `${this.describir()} y su dueño es ${this.duenio}`;
  }
}

let luna = new Mascota("Luna", "Gato", "Fredys");
console.log(luna.describir());  // "Luna es un Gato"
console.log(luna.presentar());  // "Luna es un Gato y su dueño es Fredys"
```

---

## 💡 Conexión con experiencia profesional

En **Odoo ERP**, el backend está construido en Python con POO — cada modelo (cliente, factura, producto) es una clase con propiedades y métodos, exactamente el mismo concepto.

En **HubSpot CRM**, los objetos (Contacto, Empresa, Negocio) son instancias de clases con propiedades predefinidas — la misma lógica que `new Mascota()`.

---

## ❓ Preguntas de repaso

1. ¿Cuál es la diferencia entre una clase y un objeto?
2. ¿Para qué sirve `constructor()`?
3. ¿Qué ventaja tiene un setter frente a modificar la propiedad directamente?
4. ¿Qué hace `super()` en una clase hija?
5. ¿En qué se diferencia `this.nombre` de `this._nombre`?

---

## 📖 Referencias

- Haverbeke, M. (2018). *Eloquent JavaScript* (3a ed.). https://eloquentjavascript.net/
- MDN Web Docs. (2024). *Classes*. https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Classes

---

[← Volver a la asignatura](../README.md) · [← Volver al inicio](../../README.md)
