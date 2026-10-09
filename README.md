# Modelo No Supervisado para el Análisis del Transporte Masivo

## Descripción del proyecto

Este proyecto desarrolla un modelo de aprendizaje automático no supervisado aplicado al análisis de patrones de uso del sistema de transporte masivo.

El objetivo es identificar grupos de comportamiento similares entre diferentes estaciones y franjas horarias, utilizando variables relacionadas con la demanda y las características operativas del sistema.

Para realizar el agrupamiento se utiliza el algoritmo **K-Means**, que permite organizar los registros en grupos o *clusters* sin necesidad de contar con una variable objetivo previamente etiquetada.

Este proyecto corresponde a una actividad académica relacionada con Inteligencia Artificial y aprendizaje automático.

---

## Objetivo

Desarrollar un modelo de aprendizaje no supervisado capaz de identificar patrones similares en los datos relacionados con el transporte masivo, utilizando técnicas de agrupamiento mediante K-Means.

### Objetivos específicos

- Identificar fuentes de datos relacionadas con el transporte masivo.
- Construir una muestra de datos para permitir la ejecución reproducible del modelo.
- Preparar y estandarizar las variables utilizadas por el algoritmo.
- Aplicar el algoritmo K-Means para realizar agrupamiento.
- Evaluar diferentes cantidades de *clusters*.
- Utilizar el coeficiente de silueta para seleccionar el agrupamiento más adecuado.
- Generar resultados que permitan interpretar diferentes patrones de comportamiento del sistema de transporte.

---

## Fuentes de datos

Para el desarrollo del proyecto se identificaron fuentes de datos abiertos relacionadas con el sistema de transporte de Bogotá.

Entre las fuentes identificadas se encuentran:

- Estaciones Troncales de TransMilenio.
- Servicios y rutas troncales y zonales.
- Validaciones del sistema por franja horaria.
- Salidas diarias del sistema troncal.

Estas fuentes permiten obtener información relacionada con estaciones, rutas, demanda y operación del sistema de transporte.

### Dataset utilizado

Para esta entrega se desarrolló un **dataset de muestra sintético con fines académicos**.

El dataset permite ejecutar y probar el modelo de manera reproducible sin depender de una conexión externa o de la disponibilidad de los servicios de datos durante la ejecución.

Los valores utilizados en el dataset no representan mediciones oficiales de TransMilenio y se utilizan exclusivamente para demostrar el funcionamiento del modelo.

Como trabajo futuro, el dataset puede ser reemplazado o ampliado utilizando datos reales provenientes de las fuentes oficiales identificadas.

---

## Dataset

El archivo utilizado es:

`dataset_transporte_muestra.csv`

El dataset contiene **60 registros** y las siguientes variables:

| Variable | Descripción |
|---|---|
| `estacion` | Nombre de la estación analizada |
| `franja_horaria` | Periodo del día asociado al registro |
| `entradas_promedio` | Promedio simulado de entradas de usuarios |
| `salidas_promedio` | Promedio simulado de salidas de usuarios |
| `ocupacion_pct` | Porcentaje simulado de ocupación |
| `tiempo_espera_min` | Tiempo promedio simulado de espera |
| `transbordos_promedio` | Promedio simulado de transbordos |
| `distancia_km` | Distancia aproximada asociada al tramo |

---

## Metodología

El proyecto utiliza un proceso de aprendizaje no supervisado compuesto por las siguientes etapas:

### 1. Carga de datos

El programa carga el archivo CSV utilizando la librería `pandas`.

### 2. Selección de variables

Se seleccionan las variables numéricas relacionadas con las características del transporte:

- Entradas promedio.
- Salidas promedio.
- Ocupación.
- Tiempo de espera.
- Transbordos.
- Distancia.

La estación y la franja horaria se conservan principalmente para facilitar la interpretación de los resultados.

### 3. Estandarización

Las variables se encuentran en diferentes escalas. Por esta razón se utiliza `StandardScaler` de Scikit-learn para estandarizar los datos antes de aplicar K-Means.

Este proceso permite que una variable con valores numéricos mayores no tenga una influencia desproporcionada sobre el cálculo de las distancias.

### 4. Agrupamiento mediante K-Means

Se utiliza el algoritmo **K-Means**, un método de aprendizaje no supervisado que permite dividir los registros en grupos según la similitud de sus características.

Para determinar una cantidad adecuada de grupos se prueban diferentes valores de `k`.

En este proyecto se evalúan:

- K = 2
- K = 3
- K = 4
- K = 5

### 5. Evaluación mediante coeficiente de silueta

Para comparar los agrupamientos se utiliza el **coeficiente de silueta**.

El programa selecciona automáticamente el valor de `k` que obtiene el mayor resultado de silueta entre los valores evaluados.

Un valor de silueta más alto indica que los registros de un mismo grupo presentan mayor similitud y que existe una mejor separación respecto a los demás grupos.

### 6. Visualización

Finalmente, se utiliza **PCA (Principal Component Analysis)** para reducir las variables a dos componentes y representar visualmente los grupos encontrados por el algoritmo.

---

## Resultado del modelo

En la ejecución realizada sobre la muestra de datos, el modelo evaluó diferentes cantidades de *clusters*.

El mejor resultado correspondió a:

```text
Número de clusters: 2
Coeficiente de silueta: 0.3653

## Referencias
Palma Méndez, J. T. (2008). Inteligencia artificial: métodos, técnicas y aplicaciones. McGraw-Hill España.

ENTREGA - MODELO NO SUPERVISADO TRANSPORTE MASIVO

Archivos:
1. dataset_transporte_muestra.csv
2. modelo_transporte_no_supervisado.py
3. 01_Descripcion_de_los_datos.docx
4. 02_Pruebas_del_componente.docx

Ejecución:
1) Abrir la carpeta en VS Code.
2) Instalar dependencias:
   pip install pandas numpy scikit-learn matplotlib
3) Ejecutar:
   python modelo_transporte_no_supervisado.py

El dataset es una MUESTRA SINTÉTICA creada con fines académicos.
Las fuentes oficiales identificadas se describen en el documento de datos.
