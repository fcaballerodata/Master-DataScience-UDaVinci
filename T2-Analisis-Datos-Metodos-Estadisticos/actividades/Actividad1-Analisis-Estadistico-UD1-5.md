# Actividad Integradora 1 — UD1 a UD5

**Asignatura:** Análisis de Datos y Métodos Estadísticos
**Semana:** S5 (6-11 Jul 2026)

---

## Ejercicio 1 — JavaScript: Medidas de Tendencia Central y Dispersión

**Enunciado:** calcular media, mediana, moda, varianza y desviación estándar de un arreglo de 115 valores, implementado en JavaScript puro (consola del navegador).

```javascript
// Datos: arreglo de 115 valores numéricos
const datos = [/* ... 115 valores ... */];

// Media
function calcularMedia(arr) {
  return arr.reduce((a, b) => a + b, 0) / arr.length;
}

// Mediana
function calcularMediana(arr) {
  const ordenado = [...arr].sort((a, b) => a - b);
  const mid = Math.floor(ordenado.length / 2);
  return ordenado.length % 2 !== 0
    ? ordenado[mid]
    : (ordenado[mid - 1] + ordenado[mid]) / 2;
}

// Moda
function calcularModa(arr) {
  const frecuencias = {};
  arr.forEach(v => frecuencias[v] = (frecuencias[v] || 0) + 1);
  let moda = null, maxFrec = 0;
  for (const [valor, frec] of Object.entries(frecuencias)) {
    if (frec > maxFrec) { maxFrec = frec; moda = valor; }
  }
  return { moda: Number(moda), frecuencia: maxFrec };
}

// Varianza y Desviación Estándar
function calcularVarianza(arr, media) {
  return arr.reduce((sum, v) => sum + (v - media) ** 2, 0) / arr.length;
}
function calcularDesviacionEstandar(varianza) {
  return Math.sqrt(varianza);
}

const media = calcularMedia(datos);
const mediana = calcularMediana(datos);
const { moda, frecuencia } = calcularModa(datos);
const varianza = calcularVarianza(datos, media);
const desviacion = calcularDesviacionEstandar(varianza);
```

### Resultados

| Medida | Valor |
|---|---|
| Media | 6.2870 |
| Mediana | 5 |
| Moda | 5 (frecuencia = 17) |
| Varianza | 13.5264 |
| Desviación estándar | 3.6778 |

---

## Ejercicio 2 — Python: Distribución Normal

**Enunciado:** simular y graficar una distribución normal para una variable continua (altura poblacional), usando NumPy y Matplotlib, y documentar el proceso en un reporte académico.

**Contexto:** altura de una población (media teórica ≈ 170 cm, σ = 8 cm, n = 200), `np.random.seed(42)` para reproducibilidad.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(42)
media_teorica, sigma_teorica, n = 170, 8, 200

alturas = np.random.normal(media_teorica, sigma_teorica, n)
media_muestral = np.mean(alturas)
sigma_muestral = np.std(alturas)

# Eje X centrado en la media muestral (no en 0) para que la curva se vea correctamente
x_axis = np.arange(media_muestral - 20, media_muestral + 20, 0.01)

plt.figure(figsize=(8, 5))
plt.hist(alturas, bins=20, density=True, alpha=0.6, color="#1565C0", label="Datos simulados")
plt.plot(x_axis, norm.pdf(x_axis, media_muestral, sigma_muestral), color="#C74634", linewidth=2, label="Curva normal ajustada")
plt.title("Distribución Normal — Altura poblacional simulada")
plt.xlabel("Altura (cm)")
plt.ylabel("Densidad")
plt.legend()
plt.tight_layout()
plt.savefig("distribucion_normal_altura.png", dpi=150)
```

### Resultados

- Media muestral: **μ ≈ 169.67 cm**
- Desviación estándar muestral: **σ ≈ 7.45 cm**
- La curva resultante muestra la clásica forma de campana simétrica alrededor de la media, consistente con los parámetros teóricos usados en la simulación (170 cm, σ=8), con la pequeña variación esperada por el muestreo aleatorio (n=200).

*(Reporte completo de 5 páginas — portada, introducción, desarrollo, conclusión y gráfico — entregado como PDF aparte al documento maestro.)*

---

## Ejercicio 3 — Problemas Estadísticos (Correlación y Regresión)

### Problema 1 — Turistas en México (2021 vs 2022, n=14 meses)

Datos: turistas mensuales (millones) en 2021 y 2022.

- Media X̄ (2021) = 66.88 / 14 = **4.7771**
- Media Ȳ (2022) = 67.05 / 14 = **4.7893**

**a) Dispersión — ¿qué año tuvo mayor variación?**

| Año | Media | Varianza | Desv. Estándar |
|---|---|---|---|
| 2021 | 4.7771 | 4.6687 | **2.1607** |
| 2022 | 4.7893 | 4.5782 | **2.1397** |

Conclusión: **2021** presentó mayor dispersión, aunque la diferencia es pequeña.

**b) Matriz de covarianzas**

Usando las sumatorias: Σ(X-X̄)(Y-Ȳ) = 64.4411, Σ(X-X̄)² = 65.3615, Σ(Y-Ȳ)² = 64.0951

- Cov(X,Y) = 64.4411 / 14 = **4.6029**
- Var(X) = 65.3615 / 14 = **4.6687**
- Var(Y) = 64.0951 / 14 = **4.5782**

| Matriz | 2021 | 2022 |
|---|---|---|
| **2021** | 4.6687 | 4.6029 |
| **2022** | 4.6029 | 4.5782 |

**c) Coeficiente de correlación lineal**

```
r = Σ(X-X̄)(Y-Ȳ) / √[Σ(X-X̄)² · Σ(Y-Ȳ)²]
r = 64.4411 / √(65.3615 × 64.0951) = 64.4411 / 64.7252
r = 0.9956
```

Interpretación: correlación **positiva prácticamente perfecta** — el patrón mensual de afluencia turística se mantuvo casi idéntico entre 2021 y 2022.

---

### Problema 2 — Estaturas de Padres e Hijos (n=12)

Media X̄ (padre) = 2082/12 = **173.50 cm** | Media Ȳ (hijo) = 2111/12 = **175.9167 cm**

Sumatorias base: Sxy = 263.5000, Sxx = 547.0000, Syy = 270.9167

**a) Cuartiles y mediana de Y (hijos)**

Datos ordenados: 169, 169, 172, 172, 174, 177, 177, 177, 177, 180, 182, 185

| Medida | Valor |
|---|---|
| Q1 (25%) | 172.00 cm |
| Mediana (Q2) | 177.00 cm |
| Q3 (75%) | 178.50 cm |

**b) ¿Cuál estatura es más dispersa? (Coeficiente de Variación)**

| Variable | Media | Desv. Est. | CV |
|---|---|---|---|
| X (padres) | 173.50 | 7.0518 | **4.06%** |
| Y (hijos) | 175.9167 | 4.9627 | **2.82%** |

Conclusión: la estatura de los **padres** es más dispersa (CV=4.06% > 2.82%).

**c) Coeficiente de correlación lineal**

```
r = Sxy / √(Sxx · Syy) = 263.5000 / √(547.0000 × 270.9167)
r = 263.5000 / 384.9564 = 0.6845
```

Interpretación: correlación **positiva moderada-fuerte**.

**d) Recta de regresión de X sobre Y**

```
b = Sxy / Syy = 263.5000 / 270.9167 = 0.9726
a = X̄ - b·Ȳ = 173.5000 - (0.9726)(175.9167) = 2.3993

Ecuación: x = 2.3993 + 0.9726·y
```

- R² = r² = 0.4685 → **46.85%** de la varianza explicada
- Varianza residual = 1 - R² = **53.15%**

**e) Predicción — hijo de padre que mide 177 cm**

```
b = Sxy / Sxx = 263.5000 / 547.0000 = 0.4817
a = Ȳ - b·X̄ = 175.9167 - (0.4817)(173.5000) = 92.3385

Ecuación: y = 92.3385 + 0.4817·x
Para x = 177: y = 92.3385 + 0.4817(177) = 92.3385 + 85.2642 ≈ 177.60 cm
```

Conclusión: se estima que el hijo de un padre de 177 cm medirá aproximadamente **177.60 cm**.

---

## Ejercicio 4 — Resumen y Análisis del Método ANOVA

**Artículo analizado:** Bergado Rosado, J. A., Bergado Báez, G., Contrera Hernández, M., Díaz Domínguez, G., & Moreno Castillo, E. (2009). Ausencia de efectos de la terapia floral aplicada a adultos jóvenes con el fin de mejorar su memoria. *Revista Cubana de Investigaciones Biomédicas*, 28(4).

### Resumen

El artículo, publicado en la *Revista Cubana de Investigaciones Biomédicas*, reporta un estudio experimental controlado a doble ciegas diseñado para comprobar si las "esencias florales de Bach" mejoran las funciones de memoria en adultos jóvenes. Los autores reclutaron 39 estudiantes de primer año de Bioquímica de la Universidad de La Habana, distribuidos en un grupo control (n=10), un grupo placebo (n=12, agua y brandy) y un grupo experimental (n=17, esencias florales de Bach). La asignación fue aleatoria y doble ciego.

Para evaluar la memoria se utilizó el test verbal de Rey: recuerdo inmediato de 15 palabras en cinco repeticiones sucesivas (memoria a corto plazo) y, al día siguiente, reconocimiento de esas palabras en una historieta (memoria a largo plazo).

Los resultados no mostraron diferencias estadísticamente significativas entre los tres grupos en ninguna prueba. Los autores concluyen que la terapia floral de Bach no tiene efecto comprobable sobre la memoria, y que cualquier beneficio percibido corresponde a un efecto placebo.

### Análisis del método ANOVA

El estudio utilizó dos variantes de ANOVA:

| Prueba | Tipo de ANOVA | Qué comparaba |
|---|---|---|
| Día 1 — Evocación inmediata (5 repeticiones) | ANOVA de mediciones repetidas | Factor Tratamiento (3 grupos) y Factor Desarrollo (5 ensayos + lista 2) |
| Día 2 — Reconocimiento en historieta | ANOVA de una vía | Diferencias entre los 3 grupos en una sola medición |

**¿Por qué mediciones repetidas para el Día 1?** El mismo sujeto fue evaluado 5 veces sucesivas con la misma lista — las mediciones están correlacionadas intra-sujeto, por lo que un ANOVA simple (que asume independencia) sería incorrecto.

**Factor Tratamiento** (control vs. placebo vs. floral): F(3,33) = 2.365 → **no significativo**. Resultado clave: recibir el preparado floral no generó ninguna ventaja medible.

**Factor Desarrollo** (entre los 5 ensayos): F(15,165) = 37.732 → **sí significativo** (efecto de aprendizaje esperado, independiente del grupo).

**Post Hoc de Tukey:** aplicado porque el Factor Desarrollo fue significativo. Mostró que el primer ensayo (1.1) fue distinto de los siguientes, hasta "regresar" al nivel inicial con la segunda lista (2.1); los ensayos 1.2 a 1.5 no diferían entre sí — la curva de aprendizaje se estabilizó rápido.

**ANOVA de una vía (Día 2):** F(3,31) = 1.88 → **no significativo**. Al ser una sola medición por sujeto, no se requería controlar mediciones repetidas.

**Conclusión del análisis:** en ningún caso el Factor Tratamiento alcanzó significancia (α=0.05), llevando a los autores a **no rechazar H₀** — un uso apropiado y honesto del ANOVA, sin forzar conclusiones que los datos no respaldan.

---

## Ejercicio 5 — Datos Categóricos: Inventario de Vehículos

**Contexto:** inventario de 250 vehículos (`InfoCar.txt`) evaluados en 6 atributos: precio, mantenimiento, puertas, personas, tamaño, seguridad + clase de evaluación.

```python
import pandas as pd
import matplotlib.pyplot as plt

columnas = ["precio", "mantenimiento", "puertas", "personas", "tamano", "seguridad", "clase"]
df = pd.read_csv("InfoCar.txt", header=None, names=columnas)
```

**Observación clave:** este subconjunto de 250 registros solo contiene precios `med` y `vhigh` (no aparecen `low` ni `high`) — dato relevante para el punto 3.

### 1. Cuadro de contingencia (Precio × Seguridad)

```python
tabla_contingencia = pd.crosstab(df["precio"], df["seguridad"])
```

| Precio \ Seguridad | low | med | high | Total |
|---|---|---|---|---|
| **med** | 16 | 17 | 17 | **50** |
| **vhigh** | 69 | 67 | 64 | **200** |
| **Total** | 85 | 84 | 81 | **250** |

Interpretación: de 250 vehículos, 200 son `vhigh` y 50 `med`. La seguridad se distribuye de forma similar dentro de cada nivel de precio — no hay asociación fuerte entre ambas variables.

### 2. Gráfica de barras — vehículos según su seguridad

```python
conteo_seguridad = df["seguridad"].value_counts()
plt.bar(conteo_seguridad.index, conteo_seguridad.values)
```

| Nivel de Seguridad | Cantidad |
|---|---|
| low | 85 |
| med | 84 |
| high | 81 |

Interpretación: distribución muy pareja (~33% cada categoría), sin sesgo del inventario hacia ningún nivel de seguridad.

### 3. Gráfica de barras — vehículos con puertas=2 y precio entre 'high' y 'med'

```python
filtro = (df["puertas"] == "2") & (df["precio"].isin(["high", "med"]))
df_filtrado = df[filtro]
```

**Resultado: 0 vehículos.** Este inventario no tiene precio `low` ni `high` (solo `med`/`vhigh`), y los 61 vehículos con 2 puertas presentes son **todos** de precio `vhigh`. Por lo tanto, ningún vehículo cumple ambas condiciones simultáneamente.

Interpretación: es un hallazgo válido derivado directamente de los datos, no un error — refleja que los vehículos de 2 puertas en este inventario se concentran exclusivamente en la categoría de precio más alta.

### Conclusión general del ejercicio

- El inventario es un subconjunto del dataset completo, con solo dos niveles de precio representados.
- No hay asociación fuerte entre precio y seguridad.
- La seguridad está balanceada casi uniformemente entre sus tres niveles.
- El filtro puertas=2 & precio en [med, high] arroja 0 resultados — hallazgo válido, no error de cálculo.

---

## Referencias (APA 7)

Bergado Rosado, J. A., Bergado Báez, G., Contrera Hernández, M., Díaz Domínguez, G., & Moreno Castillo, E. (2009). Ausencia de efectos de la terapia floral aplicada a adultos jóvenes con el fin de mejorar su memoria. *Revista Cubana de Investigaciones Biomédicas*, 28(4).

Montgomery, D. C., & Runger, G. C. (2010). *Probabilidad y estadística aplicadas a la ingeniería*. Limusa Wiley.
