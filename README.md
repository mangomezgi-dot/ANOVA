# ANOVA
Este repositorio contiene un script en Python para realizar un ANOVA multivariado (Type I) con el objetivo de analizar la influencia de diferentes factores experimentales sobre la viabilidad celular en ensayos de resazurina.   

El objetivo es identificar cuáles factores afectan significativamente los resultados de ensayos basados en resazurina, similar a la metodología empleada en estudios experimentales de cultivos celulares.

---

Características principales

- Carga y procesamiento de datos experimentales (archivo `.txt` delimitado por TAB).
- Conversión automática de variables categóricas.
- Ajuste de un modelo lineal mediante `statsmodels`.
- Cálculo de ANOVA tipo I.
- Generación de una gráfica tipo barplot basada en `-log10(p)`.
- Exportación de la figura en formato PNG.
- Ordenamiento de variables según su impacto en la viabilidad.


---

##  Requisitos
 Dependencias principales:

* pandas
* numpy
* statsmodels
* matplotlib
* seaborn

 Cómo ejecutar el análisis

1. Coloca el archivo **ANOVA_input.txt** en el mismo directorio.
2. Ejecuta el script:

```bash
python ANOVA_test_v2.py
```

El programa generará:

* Una tabla ANOVA en consola
* La figura **ANOVA.png**
* Variables ordenadas por significancia (mayor a menor)

##  Sobre la gráfica generada

El script produce una figura donde:

* El eje Y representa **−log10(p)** de cada factor.
* El eje X muestra las covariables del modelo.
* Una línea roja indica el nivel de significancia **p = 0.05**.
* Valores más altos → mayor impacto sobre la viabilidad.

---

## 📝 Formato del archivo de entrada

El archivo debe tener columnas como:

* `cell_viability`
* `cell_line`
* `agent`
* `dose`
* `treatment_time`
* `medium_type`
* `medium_volume`
* `seeding_density`
* `resazurin_concentration`
* `resazurin_time`
* `medium_replacement`
* `antibiotics`

Variables categóricas son identificadas automáticamente.

---

## 🧠 Interpretación de resultados

La tabla ANOVA incluye:

| Columna       | Significado                                |
| ------------- | ------------------------------------------ |
| **sum_sq**    | Contribución del factor al modelo          |
| **df**        | Grados de libertad                         |
| **F**         | Estadístico F                              |
| **PR(>F)**    | p-valor del factor                         |
| **−log10(p)** | Medida visual para comparar significancias |


##  Licencia

Este proyecto se distribuye bajo la licencia **MIT License**.





```
```
