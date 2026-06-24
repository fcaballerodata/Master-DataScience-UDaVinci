# 📘 UD3 — Programación Orientada a Objetos (POO)

**Trimestre 1 · S3 (Mar 2026)**

---

## 🎯 Conceptos clave

La POO organiza el código en **clases** (plantillas) y **objetos** (instancias). Una clase define propiedades (datos) y métodos (comportamientos).

---

## 1. Clases y Objetos

```javascript
class Mascota {
    constructor(nombre, especie, edad) {
        this.nombre  = nombre;
        this.especie = especie;
        this._edad   = edad;    // _ indica "propiedad privada por convención"
    }

    // Método
    presentarse() {
        return `Soy ${this.nombre}, un ${this.especie} de ${this._edad} años.`;
    }

    // Getter — accede a _edad de forma controlada
    get edad() {
        return this._edad;
    }

    // Setter — valida antes de asignar
    set edad(nuevaEdad) {
        if (nuevaEdad < 0) {
            console.log("La edad no puede ser negativa.");
        } else {
            this._edad = nuevaEdad;
        }
    }
}

// Instanciar objetos
const firulais = new Mascota("Firulais", "Perro", 3);
const michi    = new Mascota("Michi", "Gato", 5);

console.log(firulais.presentarse());  // Soy Firulais, un Perro de 3 años.
firulais.edad = 4;                    // Usa el setter
console.log(firulais.edad);           // 4 — usa el getter
```

---

## 2. Getters y Setters

| | Getter | Setter |
|---|---|---|
| **Propósito** | Leer una propiedad de forma controlada | Modificar con validación |
| **Se llama como** | Propiedad: `obj.prop` | Propiedad: `obj.prop = valor` |
| **Ventaja** | Puede calcular/formatear el valor al retornarlo | Evita datos inválidos |

```javascript
get nombreCompleto() {
    return `${this.nombre} (${this.especie})`;  // calcula al vuelo
}
```

---

## 3. Herencia

```javascript
class MascotaVIP extends Mascota {
    constructor(nombre, especie, edad, plan) {
        super(nombre, especie, edad);   // llama al constructor del padre
        this.plan = plan;
    }

    presentarse() {
        return `${super.presentarse()} — Plan VIP: ${this.plan}`;
    }
}

const rex = new MascotaVIP("Rex", "Perro", 2, "Premium");
console.log(rex.presentarse());
// Soy Rex, un Perro de 2 años. — Plan VIP: Premium
```

> `super()` siempre debe llamarse **antes** de usar `this` en el constructor hijo.

---

## 4. Ejemplo completo — Sistema Movet

```javascript
class Veterinario {
    constructor(nombre, especialidad) {
        this.nombre        = nombre;
        this.especialidad  = especialidad;
        this._consultas    = 0;
    }

    atender(mascota) {
        this._consultas++;
        return `${this.nombre} atendió a ${mascota.nombre}. Total consultas: ${this._consultas}`;
    }

    get totalConsultas() { return this._consultas; }
}

const dra = new Veterinario("Dra. López", "Dermatología");
console.log(dra.atender(firulais));  // Dra. López atendió a Firulais. Total: 1
console.log(dra.atender(michi));     // Dra. López atendió a Michi. Total: 2
```

---

## 🗺️ Mapa mental

```
POO EN JAVASCRIPT
│
├── Clase → plantilla (new ClassName())
├── Objeto → instancia de una clase
├── Constructor → método especial que inicializa propiedades
├── this → referencia al objeto actual
├── Getter/Setter → acceso controlado a propiedades
└── Herencia (extends + super) → reutilización de código
```

---

## 📚 Referencias

Haverbeke, M. (2018). *Eloquent JavaScript* (3a ed.). https://eloquentjavascript.net/

MDN Web Docs. (2024). *Classes — JavaScript*. https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Classes
