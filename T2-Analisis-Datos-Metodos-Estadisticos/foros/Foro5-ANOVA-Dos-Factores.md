# 💬 Foro 5 — ANOVA de Dos Factores

**Asignatura:** Análisis de Datos y Métodos Estadísticos
**Semana:** S5 (6-11 Jul 2026)

---

## 📋 Preguntas

1. ¿Cuáles son las ventajas de usar un ANOVA de dos factores frente a uno de un solo factor?
2. ¿Qué es un experimento factorial?
3. ¿Qué es un efecto principal?
4. ¿Qué es un efecto de interacción?
5. ¿Es posible tener un efecto principal significativo sin interacción?

---

## ✍️ Respuesta publicada

**Ventajas del ANOVA de dos factores**

Un ANOVA de dos factores permite detectar **interacción** entre dos variables categóricas, algo que un análisis de un solo factor simplemente no puede capturar. Además, es más eficiente: en lugar de correr dos análisis separados (uno por factor), se evalúan ambos efectos —y su posible interacción— en un solo modelo, con menor riesgo de inflar el error tipo I y aprovechando mejor el tamaño de muestra disponible (Montgomery & Runger, 2010).

**Experimento factorial**

Un experimento factorial es aquel en el que se prueban **todas las combinaciones posibles de niveles** de dos o más factores. Por ejemplo, si el Factor A tiene 2 niveles y el Factor B tiene 3 niveles, un diseño factorial completo evalúa las 6 combinaciones resultantes, permitiendo estudiar tanto los efectos individuales como su interacción.

**Efecto principal**

Es el efecto promedio de un factor sobre la variable de respuesta, calculado ignorando el nivel del otro factor. Por ejemplo, el efecto principal del "tipo de tratamiento" sería la diferencia promedio en el resultado entre los tratamientos, promediando a través de todos los niveles del segundo factor.

**Efecto de interacción**

Ocurre cuando el efecto de un factor **depende del nivel** del otro factor. En términos prácticos, significa que las líneas de respuesta no son paralelas: un tratamiento puede funcionar muy bien en un grupo y no en otro. La interacción es, en muchos casos, el hallazgo más interesante de un diseño factorial, porque revela que el efecto real depende del contexto, no de los factores por separado.

**¿Efecto principal sin interacción?**

Sí, es perfectamente posible. Un factor puede tener un efecto principal significativo sin que exista interacción, siempre que su efecto sea consistente (paralelo) a través de todos los niveles del otro factor. De la misma forma, también puede darse el caso contrario: interacción significativa sin que ninguno de los efectos principales lo sea por separado, lo cual obliga a interpretar los resultados con cuidado y priorizando siempre el análisis de la interacción antes que los efectos principales aislados.

---

## 📚 Referencias

Montgomery, D. C., & Runger, G. C. (2010). *Probabilidad y estadística aplicadas a la ingeniería*. Limusa Wiley.
