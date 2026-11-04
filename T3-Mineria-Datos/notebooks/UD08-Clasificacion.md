# UD08 · Clasificación — Minería de Datos (T3)

> **Fuentes:** guía académica de la unidad (15 pp.), Recursos y Bibliografía de la asignatura (no tratan clasificación en detalle) y fuentes académicas verificadas (sección Referencias).
> **Convención:** **[guía]** = sale de la guía · **[complemento]** = fuente externa · **[propio]** = prueba que ejecuté yo.
> **Código:** [`comparar_clasificadores.py`](../codigo/comparar_clasificadores.py) · [`evaluar_clasificador.py`](../codigo/evaluar_clasificador.py)
> **Nota:** algunos párrafos de la guía (Naive Bayes, SVM) se extraen mezclados del PDF; lo dudoso va como **[verificar]** en el campus.

---

## 1. Resumen ejecutivo
- **Clasificar** = asignar cada dato a una categoría conocida, aprendiendo de ejemplos con respuesta (aprendizaje **supervisado**) **[guía]**.
- **Binaria:** 2 clases (spam / no spam). **Multiclase:** más de 2 (tipo de cultivo, género musical).
- Diferencia con la UD7: el clustering **descubre** grupos sin etiquetas; la clasificación **predice** grupos ya definidos.
- Cinco algoritmos: Naive Bayes, SVM, KNN, árbol de decisión y Random Forest.
- **Medir bien** importa más que elegir el algoritmo (sección 6).

## 2. Los 5 algoritmos **[guía]**

| Algoritmo | Idea simple | Ventaja | Limitación |
|---|---|---|---|
| **Naive Bayes** | Probabilidad de cada clase con Bayes, **suponiendo variables independientes** | Muy rápido, pocos datos | "Mal estimador" de probabilidades; probabilidad cero (se corrige con Laplace) |
| **SVM** | **Hiperplano de margen máximo** entre clases | Eficaz en muchas dimensiones; usa pocos puntos (vectores de soporte) | Probabilidades costosas (validación cruzada de 5 pliegues); parámetros *kernel*, *gamma*, *C* |
| **KNN** | Toma la clase **más común entre sus k vecinos** | Simple, robusto al ruido | Hay que elegir k; costoso (compara con todas las muestras) |
| **Árbol de decisión** | Secuencia de preguntas (reglas) | Fácil de entender y visualizar | Se sobreajusta; inestable |
| **Random Forest** | Muchos árboles sobre submuestras con reemplazo; **votación** | Más preciso que un árbol | "Caja negra"; lento en tiempo real |

**Respaldo académico [complemento]**
- Naive Bayes: puede clasificar muy bien aunque la independencia se viole, pero sus **estimaciones de probabilidad** solo son óptimas si se cumple (Domingos & Pazzani, 1997).
- SVM: Cortes y Vapnik (1995). KNN: Cover y Hart (1967). Random Forest: Breiman (2001).

**Conceptos aclarados**
- **KNN es "perezoso":** no entrena; guarda los datos y calcula todo al predecir.
- **Estandarizar** para KNN y SVM: usan distancias y la variable de mayor escala domina. No hace falta en árboles ni Random Forest.
- **Elegir k:** con **validación cruzada** sobre una métrica de clasificación. El silhouette es de clustering, no de KNN.
- **Árbol 1.000 en train:** memoriza (sobreajuste = alta varianza). Random Forest lo reduce promediando árboles. `feature_importances_` da interpretabilidad parcial.

## 3. Ejemplos sencillos
- **Naive Bayes:** ¿este correo es spam? Según las palabras que trae.
- **SVM:** separar clientes "pagan" / "no pagan" con la frontera más ancha.
- **KNN:** un cliente nuevo se parece a sus 5 vecinos; si 4 renovaron, probablemente renueve.
- **Árbol:** "¿compró en los últimos 60 días? sí → ¿más de 3 compras? no → riesgo medio".
- **Random Forest:** 300 árboles votan.

## 4. Python (ejecutado) **[propio]** — `comparar_clasificadores.py`
Cáncer de mama (569 casos; 143 en prueba, partición estratificada, `random_state=42`).

| Modelo | CV (train) | Train | **Prueba** | Recall maligno |
|---|---|---|---|---|
| Naive Bayes | 0.941 | 0.946 | 0.937 | 0.868 |
| SVM | 0.965 | 0.979 | **0.979** | **0.981** |
| KNN (k=5) | 0.962 | 0.970 | **0.979** | 0.943 |
| Árbol | 0.930 | **1.000** | 0.923 | 0.925 |
| Random Forest | 0.962 | **1.000** | 0.958 | 0.925 |

**Cómo leerlo**
- **CV:** promedio de 5 validaciones dentro del entrenamiento; compara modelos sin tocar la prueba. **Prueba:** la nota final con datos nunca vistos.
- **Train = 1.000** en árbol y bosque = memorizan; en prueba bajan (0.923 y 0.958). El bosque sobreajusta menos.
- Las diferencias entre SVM, KNN y bosque son de **1 a 3 casos de 143**: no hay evidencia fuerte de que uno sea mejor.

| Prueba | Resultado | Significado |
|---|---|---|
| KNN sin escalar | 0.930 (vs 0.979 escalado) | Sin estandarizar, domina la variable de mayor escala |
| Árbol, profundidad 1 / 3 / 5 / 10 | prueba 0.923 / 0.944 / 0.937 / 0.923 | Más profundidad no mejora |
| KNN, k = 1 / 3 / 5 / 11 / 51 (CV) | 0.944 / **0.965** / 0.962 / 0.960 / 0.944 | k chico = ruido; k grande = suaviza de más |
| Probabilidad > 0.99 | Naive Bayes: 135 casos, 97 % de acierto · Random Forest: 57 casos, 100 % | Naive Bayes está sobreconfiado |

## 5. La trampa del desbalance **[propio]**
5.000 clientes simulados, 5,4 % de clase de interés (por ejemplo "cancela").

| Modelo | Accuracy | Precisión | Recall | F1 |
|---|---|---|---|---|
| Siempre responde "no" | **0.946** | 0.000 | 0.000 | 0.000 |
| Random Forest | 0.965 | 0.960 | 0.358 | 0.522 |
| RF `class_weight="balanced"` | 0.964 | 0.844 | 0.403 | 0.545 |

Un modelo que nunca detecta a nadie saca 94,6 %. El accuracy engaña cuando una clase es rara.

## 6. Complemento: cómo medir un clasificador — `evaluar_clasificador.py`

### 6.1 Matriz de confusión
Cáncer de mama (1 = maligno), Random Forest, 25 % de prueba estratificada.

| | Predice benigno | Predice maligno |
|---|---|---|
| **Real benigno** | VN = 90 | FP = 0 |
| **Real maligno** | FN = 5 | VP = 48 |

FP = falsa alarma. FN = maligno que se pasó.

### 6.2 Métricas

| Métrica | Fórmula | Pregunta que responde | Valor |
|---|---|---|---|
| Accuracy | (VP+VN)/total | ¿Cuántos acertó en total? | 0.965 |
| Precisión | VP/(VP+FP) | De los que marcó positivos, ¿cuántos lo eran? | 1.000 |
| Recall (sensibilidad) | VP/(VP+FN) | De los positivos reales, ¿cuántos encontró? | 0.906 |
| Especificidad | VN/(VN+FP) | De los negativos reales, ¿cuántos descartó bien? | 1.000 |
| F1 | media armónica de precisión y recall | Balance entre ambas | 0.950 |

- **Precisión** importa cuando un falso positivo es caro. **Recall** cuando un falso negativo es caro.
- **Baseline:** el accuracy se compara siempre contra el de "predecir siempre la clase mayoritaria".

### 6.3 El umbral de decisión
El modelo entrega una probabilidad; el corte por defecto es 0.5, pero se puede mover.

| Umbral | FP | FN | Precisión | Recall |
|---|---|---|---|---|
| 0.1 | 12 | 0 | 0.815 | 1.000 |
| 0.3 | 2 | 3 | 0.962 | 0.943 |
| 0.5 | 0 | 5 | 1.000 | 0.906 |
| 0.7 | 0 | 9 | 1.000 | 0.830 |
| 0.9 | 0 | 17 | 1.000 | 0.679 |

Bajar el umbral sube el recall y baja la precisión; subirlo hace lo contrario. Con un costo hipotético (FN = 10, FP = 1) el umbral de menor costo fue **0.15** (costo 8) frente a 50 con 0.5. **El umbral lo define el costo del error.**
💡 BI: en churn, si perder un cliente cuesta mucho más que una llamada de retención, conviene un umbral bajo.

### 6.4 ROC-AUC vs PR-AUC con desbalance
- **ROC-AUC:** qué tan bien ordena positivos sobre negativos en todos los umbrales (0.5 = azar; 1.0 = perfecto).
- **PR-AUC (average precision):** mira solo la clase positiva; no se infla por los negativos fáciles.

| Modelo (5 % de positivos) | ROC-AUC | AP |
|---|---|---|
| Random Forest | 0.890 | 0.635 |
| Regresión logística | 0.785 | 0.335 |
| Azar (referencia AP) | 0.5 | ≈ 0.054 |

Con validación cruzada de 5 pliegues: AP 0.726, ROC-AUC 0.92. El ROC-AUC de 0.89 suena excelente, pero el AP muestra que la precisión aún es limitada. Con desbalance, mirar el PR-AUC primero (Saito & Rehmsmeier, 2015; Davis & Goadrich, 2006).

### 6.5 Buenas prácticas
- Partición y validación cruzada **estratificadas**.
- **Sin fuga de datos:** escalado y selección de variables solo con entrenamiento (usar `Pipeline`).
- Desbalance: `class_weight="balanced"`, mover el umbral, reportar PR-AUC.
- Comparar siempre contra el baseline.

### 6.6 Código base
```python
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.25, stratify=y, random_state=42)
modelo = RandomForestClassifier(300, random_state=42).fit(Xtr, ytr)
p = modelo.predict_proba(Xte)[:, 1]      # probabilidad de la clase positiva
pred = (p >= 0.5).astype(int)            # el umbral lo eliges tú
tn, fp, fn, tp = confusion_matrix(yte, pred).ravel()
print(classification_report(yte, pred))
print("ROC-AUC:", roc_auc_score(yte, p), "| AP:", average_precision_score(yte, p))
```

## 7. R (no probado: R no está disponible en mi entorno)
```r
library(e1071); library(class); library(rpart); library(randomForest)
set.seed(42)
idx <- sample(nrow(iris), 100)
tr <- iris[idx, ]; te <- iris[-idx, ]
nb <- naiveBayes(Species ~ ., tr);  mean(predict(nb, te) == te$Species)
sv <- svm(Species ~ ., tr);         mean(predict(sv, te) == te$Species)
kn <- knn(scale(tr[,1:4]), scale(te[,1:4]), tr$Species, k = 5); mean(kn == te$Species)
ar <- rpart(Species ~ ., tr);       mean(predict(ar, te, type = "class") == te$Species)
rf <- randomForest(Species ~ ., tr); mean(predict(rf, te) == te$Species)
```
*(Para evaluación en R: matriz de confusión con `table(real, predicho)`; pendiente de validar.)*

## 8. Aplicación real (BI)
Tabla de clientes (frecuencia, monto, meses activos) para predecir **quién vuelve en 90 días**:
1. Línea base interpretable: árbol pequeño o regresión logística.
2. Comparar con SVM, KNN y Random Forest con validación cruzada.
3. Con clase rara, evaluar con **recall, precisión, F1 y PR-AUC**, no solo accuracy.
4. Publicar la probabilidad o clase como columna en Snowflake / Power BI para campañas de retención.
5. Conexión con la UD7: los segmentos RFM (Mejores, Regulares, Nuevos/ocasionales, Dormidos) pueden ser **etiquetas** para clasificar clientes nuevos.

## 9. Puntos de la guía que conviene manejar con cuidado
1. **Random Forest "alto sesgo (sobreajuste)":** el sobreajuste es **alta varianza**.
2. La guía omite que cada división considera solo un subconjunto aleatorio de variables (Breiman, 2001) **[complemento; detalle por confirmar en la fuente]**.
3. La guía no explica **cómo medir** un clasificador; la sección 6 lo cubre. El temario retoma la evaluación en la UD10.

## 10. Preguntas de comprensión y respuestas corregidas

**1. Modelo de cancelación con 95 % de accuracy y 5 % de cancelaciones.**
No necesariamente bueno: 95 % es el baseline de "siempre no". Mirar precisión (falsos positivos), recall (falsos negativos), F1 y PR-AUC, a partir de la matriz de confusión.

**2. Random Forest vs un árbol.**
Más preciso porque promedia muchos árboles (bootstrap + votación), lo que reduce la varianza. Desventajas: caja negra y lento en tiempo real. El árbol libre memoriza el entrenamiento (1.000) y baja en prueba.

**3. KNN.**
Estandariza porque usa distancias y domina la escala mayor. "Perezoso" = no entrena, calcula al predecir. El k se elige con **validación cruzada**, no con silhouette.

## 🧠 Lo que debes recordar
1. **Accuracy engaña** con clases desbalanceadas; compáralo con el baseline.
2. **Matriz de confusión** → precisión, recall, especificidad y F1.
3. **Precisión** cuida los falsos positivos; **recall**, los falsos negativos; **F1** los balancea.
4. **El umbral no es 0.5 por obligación**: se mueve según el costo del error.
5. **Con desbalance, mira PR-AUC**, no solo ROC-AUC.
6. **Estandariza para KNN y SVM**; no hace falta en árboles.
7. **El k de KNN se elige con validación cruzada**, no con silhouette.
8. **Random Forest** reduce varianza, pero es caja negra y lento en tiempo real.
9. **Partición estratificada, validación cruzada y sin fuga de datos** (`Pipeline`).

## Referencias (APA 7)
- Breiman, L. (2001). Random forests. *Machine Learning, 45*(1), 5–32. https://doi.org/10.1023/A:1010933404324
- Cortes, C., & Vapnik, V. (1995). Support-vector networks. *Machine Learning, 20*, 273–297. https://doi.org/10.1007/BF00994018
- Cover, T. M., & Hart, P. E. (1967). Nearest neighbor pattern classification. *IEEE Transactions on Information Theory, 13*(1), 21–27.
- Davis, J., & Goadrich, M. (2006). The relationship between precision-recall and ROC curves. En *International Conference on Machine Learning (ICML)* (pp. 233–240). *(Título completo de las actas por confirmar.)*
- Domingos, P., & Pazzani, M. (1997). On the optimality of the simple Bayesian classifier under zero-one loss. *Machine Learning, 29*, 103–130. https://doi.org/10.1023/A:1007413511361
- Fawcett, T. (2006). An introduction to ROC analysis. *Pattern Recognition Letters, 27*(8), 861–874.
- Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830.
- Saito, T., & Rehmsmeier, M. (2015). The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. *PLoS ONE, 10*(3), e0118432.
- Universidad DaVinci. (s. f.). *Clasificación* [Guía académica, Unidad 8]. Minería de Datos. LMS UDaVinci.
