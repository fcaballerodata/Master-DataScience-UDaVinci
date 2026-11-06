# UD09 · Construcción de una RNA — Fundamentos de Machine Learning (T3)

> **Fuentes:** guía académica de la unidad (10 pp.), Recursos y Bibliografía de la asignatura, el libro de Goodfellow et al. (2016) y fuentes verificadas (sección Referencias).
> **Convención:** **[guía]** = sale de la guía · **[complemento]** = fuente externa · **[propio]** = prueba que ejecuté yo.
> **Código:** [`construccion_rna.py`](../codigo/construccion_rna.py) · **Foro de la semana:** [Foro UD9](../foros/Foro-UD9-Diseno-Estructura-RNA.md)
> **Nota:** varios párrafos de la guía se extraen mezclados del PDF; lo dudoso va como **[verificar]**.

---

## 1. Resumen ejecutivo
Construir una RNA es tomar cuatro decisiones en este orden:
1. **Datos:** qué entra y cómo se prepara (la red solo acepta números).
2. **Topología:** feedforward, recurrente o convolucional, según el problema.
3. **Estructura:** número de capas y de neuronas, función de activación.
4. **Entrenamiento:** regularización y algoritmo de optimización para no memorizar.

Idea central: **más grande no es mejor.** Más capacidad aprende patrones más complejos, pero también memoriza más fácil.

## 2. Fundamentos técnicos

### 2.1 Tipos de datos y cómo entran a la red **[guía]**

| Tipo | Ejemplo | Preparación |
|---|---|---|
| Numéricos | edad, monto | Estandarizar |
| Categóricos | color, canal | Codificar (*one-hot*) |
| Ordinales | pequeño < mediano < grande | Número que respete el orden |
| Binarios | sí / no | 0 / 1 |
| Temporales | series de tiempo | Redes recurrentes (RNN, LSTM) |
| Textuales | frases | *Embeddings*, TF-IDF, vectorización |
| Imágenes, audio | píxeles, señales | Redes convolucionales (CNN) |

Por qué cada decisión:
- **Estandarizar:** una variable en miles domina a una en unidades.
- **One-hot** para nominales: web, tienda y app no tienen orden; codificarlas 0, 1, 2 inventa un orden.
- **Ordinal:** el número sí respeta el orden.
- Con montos muy sesgados, conviene aplicar `log` antes de estandarizar **[complemento]**.

### 2.2 Cómo elegir la topología **[guía]**
Naturaleza del problema · cantidad de datos · recursos computacionales · interpretabilidad (las redes complejas son "cajas negras") · validación cruzada · experiencia del equipo. El proceso es **iterativo**.

Mapa rápido: **tabla → feedforward, tiempo → recurrente, imagen → convolucional.**

### 2.3 Diseño de la estructura **[guía]**

| Decisión | Qué dice la guía |
|---|---|
| Número de capas | Pocas para problemas simples; multicapa para complejos |
| Neuronas por capa | Más neuronas = más capacidad, pero más riesgo de sobreajuste |
| Función de activación | ReLU, sigmoid, tanh |
| Conexiones | *Feedforward* o recurrentes |
| Regularización | Técnicas que penalizan la complejidad y mejoran la generalización |
| Optimización | Método para ajustar los pesos al entrenar |

**[complemento]** Capítulos de Goodfellow et al. (2016): 6 (feedforward), 7 (regularización), 8 (optimización), 9 (convolucionales), 10 (recurrentes), 11 (metodología práctica).

## 3. Ejemplos sencillos
- **Datos:** el canal "web / tienda / app" pasa a 3 columnas de 0 y 1; el tamaño "pequeño / mediano / grande" pasa a 0, 1, 2.
- **Topología:** churn con tabla de clientes → feedforward; ventas de la próxima semana → recurrente; foto de un producto → convolucional.
- **Capas y neuronas:** como un equipo de analistas. Pocos se pierden patrones sutiles; demasiados se aprenden los datos de memoria.

## 4. Python (ejecutado) **[propio]** — `construccion_rna.py`
4.000 clientes **simulados** (no son datos reales): 2 numéricos, 1 categórico, 1 ordinal y 1 binario, 21 % de positivos. Todo va en un `Pipeline` para que el preprocesamiento no filtre información entre entrenamiento y prueba.

```python
prep = ColumnTransformer([
  ("num", StandardScaler(), ["frecuencia","monto"]),
  ("nom", OneHotEncoder(), ["canal"]),
  ("ord", OrdinalEncoder(categories=[["pequeño","mediano","grande"]]), ["plan"]),
  ("bin", "passthrough", ["usa_app"])])
modelo = Pipeline([("p", prep),
    ("m", MLPClassifier((32,16), activation="relu", alpha=1e-4, max_iter=800, random_state=42))])
```

| Prueba | CV-AP | Acc. train | Acc. prueba | Qué muestra |
|---|---|---|---|---|
| Logística (sin capas ocultas) | 0.575 | 0.823 | 0.816 | Línea base |
| MLP (2,) | 0.582 | 0.833 | 0.828 | Casi igual a la base |
| MLP (16,) | 0.626 | 0.838 | 0.835 | Mejora |
| **MLP (32, 16)** | **0.651** | 0.865 | 0.836 | La mejor topología |
| MLP (128, 128, 128) | 0.575 | **0.895** | 0.828 | Sobreajuste |
| (128×3) con alpha = 1.0 | 0.672 | 0.851 | 0.835 | La regularización lo corrige |
| (16,) sin estandarizar | **0.302** | 0.785 | 0.784 | Se rompe |

### 4.1 Cómo leer las métricas
- **Acc. train:** % de aciertos sobre los datos con los que la red aprendió (el examen que ya viste). Un valor alto aquí no demuestra nada.
- **Acc. prueba:** % de aciertos sobre datos que nunca vio (el examen sorpresa); es la que cuenta.
- **La brecha entre las dos es el sobreajuste:** (16,) 0.838 vs 0.835 (brecha 0.003, sana); (128×3) 0.895 vs 0.828 (brecha 0.067, memoriza).
- **CV-AP:** *CV* es la validación cruzada (se divide el entrenamiento en 5 partes, se entrena con 4, se evalúa con la que quedó fuera y se rota, luego se promedia; sirve para comparar modelos **sin tocar la prueba**). *AP* es la *average precision* (UD8): premia que el modelo ponga los positivos reales arriba en su ranking. Se lee contra el azar: con 21 % de positivos, azar ≈ 0.21.
- **Con clases raras el accuracy engaña:** el modelo que siempre dice "no" ya saca ≈ 0.79, y mis accuracies (0.82 a 0.84) son apenas mejores. Por eso se usa AP.

### 4.2 Notación `MLP (32, 16)`
MLP = *Multi-Layer Perceptron*. La tupla lista **las neuronas de cada capa oculta** (la entrada y la salida no se cuentan).

| Notación | Significado | Pesos y sesgos* |
|---|---|---|
| `()` (logística) | Sin capa oculta | — |
| `(2,)` | 1 capa oculta, 2 neuronas | 19 |
| `(16,)` | 1 capa oculta, 16 neuronas | 145 |
| `(32, 16)` | 2 capas ocultas: 32 y 16 | 801 |
| `(128, 128, 128)` | 3 capas ocultas de 128 | 34.177 |

*Con 7 entradas tras preparar los datos (2 numéricas + 3 del one-hot de canal + 1 ordinal + 1 binaria) y 1 salida; son cálculos aritméticos, no salida de código. La coma de `(16,)` es sintaxis de Python (lista de una capa).

### 4.3 Lectura honesta de los resultados
- Más capas y neuronas = más piezas que ajustar. La red de 128×3 tiene 34.177 parámetros para 3.000 clientes de entrenamiento: sobreajusta.
- La regularización (`alpha` de 1e-4 a 1.0) hizo más que cambiar la arquitectura, y estandarizar pesó aún más.
- **Diferencias pequeñas no son concluyentes:** con 5 semillas el accuracy de prueba de la misma red varió entre 0.827 y 0.837. No concluyo que tanh (0.658) le gane a ReLU (0.626) ni cuál codificación del canal es mejor.
- *Early stopping* no ayudó aquí (0.602); no es una receta mágica.

## 5. R (no probado: R no está disponible en mi entorno)
```r
library(nnet)
set.seed(42)
d <- data.frame(frecuencia = rpois(500, 4), monto = rlnorm(500, 11, 1))
d$y <- factor(ifelse(d$frecuencia >= 5, 1, 0))
d[, 1:2] <- scale(d[, 1:2])                 # estandarizar
m <- nnet(y ~ ., data = d, size = 8, decay = 0.01, maxit = 300)   # decay = regularización
table(real = d$y, predicho = predict(m, d, type = "class"))
```

## 6. Aplicación real (BI)
Predecir qué clientes volverán a comprar con una tabla de Snowflake:
1. **Datos:** montos y frecuencias estandarizados; canal en one-hot; plan por orden; fechas convertidas en antigüedad o recencia.
2. **Línea base:** regresión logística. Si la red no la supera con claridad, se queda la logística (más explicable).
3. **Topología:** feedforward pequeña (por ejemplo 32-16). Crecer solo si la validación cruzada mejora.
4. **Control del sobreajuste:** comparar train contra validación y regularizar.
5. Publicar la probabilidad como columna en Power BI, acompañada de la métrica y la línea base.

## 7. Puntos de la guía que conviene manejar con cuidado
1. No explica **cómo se decide** el número de capas y neuronas más allá de "depende de la complejidad"; en la práctica se prueba con validación cruzada.
2. Dice "más capas = problemas más complejos", pero no que también aumentan el riesgo de sobreajuste y el costo.
3. No desarrolla el algoritmo de optimización ni las funciones de activación (Cap. 8 de Goodfellow cubre optimización).
4. Texto mezclado en el PDF: **[verificar]** en el campus.

## 8. Preguntas de comprensión y respuestas corregidas

**1. Preparar monto, canal, plan y uso de la app.**
Monto: estandarizar (y `log` si está sesgado). Canal: one-hot, porque no tiene orden. Plan: ordinal 0, 1, 2, porque sí tiene orden. Usa app: 0/1. La red solo acepta números, y cada codificación evita inventar orden o dejar que una escala domine.

**2. Criterios para elegir la topología.**
Tipo de dato, cantidad de datos, interpretabilidad, recursos y validación cruzada. Tabla → feedforward; serie de tiempo → recurrente (RNN/LSTM); imagen → convolucional (CNN). Siempre con una línea base simple al lado.

**3. Red grande (0.90 train, 0.82 prueba) vs pequeña (0.84, 0.83).**
La grande sobreajusta (brecha 0.08); la pequeña generaliza. Además de elegir la pequeña: regularizar la grande, probar una intermedia (en la prueba la mejor fue (32, 16)), conseguir más datos y **decidir con validación cruzada, no con la prueba**.

## 🧠 Lo que debes recordar
1. **La RNA solo acepta números:** numéricas se estandarizan, nominales en one-hot, ordinales conservan el orden, binarias en 0/1.
2. **Topología según los datos:** tabla → feedforward, tiempo → recurrente, imagen → convolucional.
3. **Más grande no es mejor:** más capas y neuronas dan más capacidad y más riesgo de sobreajuste.
4. **Acc. train** es el examen que ya viste; **Acc. prueba**, el examen sorpresa. Una brecha grande indica sobreajuste.
5. **CV-AP** compara modelos sin tocar la prueba; evalúala contra el azar (aquí ≈ 0.21).
6. Con clases raras el accuracy engaña (el "siempre no" ya saca ≈ 0.79).
7. **Notación MLP:** `(32, 16)` = dos capas ocultas, de 32 y 16 neuronas.
8. **Contra el sobreajuste:** regularizar, reducir la red, más datos; elegir con validación cruzada.
9. Empieza con una **línea base simple** y crece solo si la validación mejora de forma clara.

## Referencias (APA 7)
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT Press. *(Autores, editorial y capítulos 6 a 12 verificados en su tabla de contenidos; no leí los capítulos completos.)*
- Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830.
- Universidad DaVinci. (s. f.). *Construcción de una RNA* [Guía académica, Unidad 9]. Fundamentos de Machine Learning. LMS UDaVinci.
