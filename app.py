import pandas as pd
import numpy as np
import gradio as gr
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import plotly.express as px

def kmeans_clustering(file, n_clusters, feature1, feature2):
    try:
        # Leer el archivo CSV
        df = pd.read_csv(file.name)
        
        # Seleccionar las características para el agrupamiento
        features = df[[feature1, feature2]]
        
        # Escalar las características
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features)
        
        # Realizar agrupamiento K-means
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        df['Cluster'] = kmeans.fit_predict(features_scaled)
        
        # Crear gráfico de dispersión usando plotly
        fig = px.scatter(df, x=feature1, y=feature2, color='Cluster',
                        title=f'K-means Clustering with {n_clusters} clusters',
                        color_continuous_scale='viridis')
        
        return fig
    
    except Exception as e:
        return f"Error: {str(e)}"

def create_interface():
    with gr.Blocks() as app:
        gr.Markdown("# K-means Clustering App")
        
        with gr.Row():
            file_input = gr.File(label="Upload CSV file")
            n_clusters = gr.Slider(minimum=2, maximum=10, step=1, value=3,
                                 label="Number of Clusters")
        
        with gr.Row():
            # Estos serán rellenados después de cargar el archivo
            feature1 = gr.Dropdown(label="Select first feature")
            feature2 = gr.Dropdown(label="Select second feature")
        
        output_plot = gr.Plot()
        
        def update_features(file):
            if file is None:
                return gr.Dropdown(), gr.Dropdown()
            df = pd.read_csv(file.name)
            columns = df.select_dtypes(include=[np.number]).columns.tolist()
            return gr.Dropdown(choices=columns), gr.Dropdown(choices=columns)
        
        file_input.change(fn=update_features, 
                         inputs=[file_input],
                         outputs=[feature1, feature2])
        
        inputs = [file_input, n_clusters, feature1, feature2]
        
        gr.Interface(fn=kmeans_clustering,
                    inputs=inputs,
                    outputs=output_plot,
                    live=True)
    
    return app

if __name__ == "__main__":
    app = create_interface()
    app.launch()