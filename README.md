# 📊 Aplicación de Clustering K-Means desde CSV

Esta aplicación permite realizar análisis de **clustering** utilizando el algoritmo **K-Means** a partir de un conjunto de datos cargado desde un archivo CSV. Fue desarrollada con **Gradio** para ofrecer una interfaz amigable e interactiva, y utiliza **Plotly** para una visualización clara y dinámica de los resultados.

## 🧩 Funcionalidades

- ✅ Carga de archivos en formato `.csv`.
- 👁️ Vista previa de los datos cargados.
- 🧮 Selección manual de variables **numéricas** a utilizar.
- 🎯 Definición del número de clusters mediante un control deslizante.
- 📈 Visualización de los clusters en un gráfico 2D usando **PCA**.
- 🌈 Gráfica interactiva con **Plotly** para explorar los agrupamientos.

## 🛠️ Tecnologías utilizadas

- [Gradio](https://gradio.app/) – para la interfaz gráfica.
- [Pandas](https://pandas.pydata.org/) – para el manejo de datos.
- [Scikit-learn](https://scikit-learn.org/stable/modules/clustering.html#k-means) – para el modelo de K-Means y PCA.
- [Plotly](https://plotly.com/python/) – para las visualizaciones interactivas.

## ▶️ Cómo usar

1. Ejecuta la aplicación en tu entorno local.
2. Sube un archivo `.csv` con datos numéricos.
3. Selecciona las variables a analizar.
4. Ajusta el número de clusters.
5. Presiona el botón **“Generar gráfico”** para ver los resultados.

## 📁 Estructura recomendada del CSV

- Debe contener al menos **dos columnas numéricas**.
- Las columnas con texto o categorías serán ignoradas automáticamente.
- Asegúrate de que los nombres de columnas estén correctamente formateados.

## 📌 Ejemplo de uso

Una aplicación útil para:

- Análisis exploratorio de datos.
- Agrupamiento de clientes o productos.
- Segmentación de patrones en bases de datos multivariadas.

---

Desarrollado por **Marbin Seca**
