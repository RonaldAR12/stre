import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Cargar los datos
df = pd.read_csv('C:/Users/RONALD/Downloads/data/dataset.csv', encoding='latin1')

# Eliminar duplicados y llenar valores faltantes
df.drop_duplicates(inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Configuración de Streamlit
st.title("Reportes de Playlist")

# Sidebar para navegación
st.sidebar.title("Menú de Reportes")
opciones = [
    "Distribución de Popularidad (Violin Plot)",
    "Promedio de Popularidad por Artista",
    "Relación entre Duración y Popularidad",
    "Evolución de la Popularidad por Año",
    "Distribución de la Energía (Boxplot)",
    "Distribución de Danceability",
    "Top 10 Tracks por Popularidad",
    "Top 10 Artistas por Cantidad de Tracks",
    "Top 10 Tracks por Duración",
    "Relación entre Popularidad y Energía"
]
seleccion = st.sidebar.radio("Selecciona un reporte:", opciones)

# Funciones de visualización
def mostrar_distribucion_popularity():
    plt.figure(figsize=(10, 6))
    sns.violinplot(x=df['popularity'])
    plt.title('Distribución de Popularidad')
    plt.xlabel('Popularidad')
    st.pyplot(plt)

def mostrar_promedio_popularidad_artistas():
    promedio_popularidad_artistas = df.groupby('artists')['popularity'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=promedio_popularidad_artistas.values, y=promedio_popularidad_artistas.index)
    plt.title('Promedio de Popularidad por Artista')
    plt.xlabel('Popularidad Promedio')
    plt.ylabel('Artista')
    st.pyplot(plt)

def mostrar_relacion_duracion_popularidad():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='duration_ms', y='popularity')
    plt.title('Relación entre Duración y Popularidad')
    plt.xlabel('Duración (ms)')
    plt.ylabel('Popularidad')
    st.pyplot(plt)

def mostrar_evolucion_popularidad_por_ano():
    df['release_date'] = pd.to_datetime(df['release_date'])
    df['year'] = df['release_date'].dt.year
    evolucion_popularidad = df.groupby('year')['popularity'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=evolucion_popularidad, x='year', y='popularity')
    plt.title('Evolución de la Popularidad por Año')
    plt.xlabel('Año')
    plt.ylabel('Popularidad Promedio')
    st.pyplot(plt)

def mostrar_distribucion_energia():
    plt.figure(figsize=(10, 6))
    sns.boxplot(y=df['energy'])
    plt.title('Distribución de la Energía')
    plt.ylabel('Energía')
    st.pyplot(plt)

def mostrar_distribucion_danceability():
    plt.figure(figsize=(10, 6))
    sns.histplot(df['danceability'], bins=50, kde=True)
    plt.title('Distribución de Danceability')
    plt.xlabel('Danceability')
    plt.ylabel('Frecuencia')
    st.pyplot(plt)

def mostrar_top_tracks_popularity():
    top_tracks_popularity = df.sort_values(by='popularity', ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_tracks_popularity, x='popularity', y='track_name', hue='artists')
    plt.title('Top 10 Tracks por Popularidad')
    plt.xlabel('Popularidad')
    plt.ylabel('Track')
    st.pyplot(plt)

def mostrar_top_artistas_tracks():
    top_artists_tracks = df['artists'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(y=top_artists_tracks.index, x=top_artists_tracks.values)
    plt.title('Top 10 Artistas por Cantidad de Tracks')
    plt.xlabel('Cantidad de Tracks')
    plt.ylabel('Artista')
    st.pyplot(plt)

def mostrar_top_tracks_duration():
    top_tracks_duration = df.sort_values(by='duration_ms', ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_tracks_duration, x='duration_ms', y='track_name', hue='artists')
    plt.title('Top 10 Tracks por Duración')
    plt.xlabel('Duración (ms)')
    plt.ylabel('Track')
    st.pyplot(plt)

def mostrar_relacion_popularidad_energia():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='energy', y='popularity')
    plt.title('Relación entre Popularidad y Energía')
    plt.xlabel('Energía')
    plt.ylabel('Popularidad')
    st.pyplot(plt)

# Mostrar el reporte seleccionado
if seleccion == "Distribución de Popularidad (Violin Plot)":
    mostrar_distribucion_popularity()
elif seleccion == "Promedio de Popularidad por Artista":
    mostrar_promedio_popularidad_artistas()
elif seleccion == "Relación entre Duración y Popularidad":
    mostrar_relacion_duracion_popularidad()
elif seleccion == "Evolución de la Popularidad por Año":
    mostrar_evolucion_popularidad_por_ano()
elif seleccion == "Distribución de la Energía (Boxplot)":
    mostrar_distribucion_energia()
elif seleccion == "Distribución de Danceability":
    mostrar_distribucion_danceability()
elif seleccion == "Top 10 Tracks por Popularidad":
    mostrar_top_tracks_popularity()
elif seleccion == "Top 10 Artistas por Cantidad de Tracks":
    mostrar_top_artistas_tracks()
elif seleccion == "Top 10 Tracks por Duración":
    mostrar_top_tracks_duration()
elif seleccion == "Relación entre Popularidad y Energía":
    mostrar_relacion_popularidad_energia()
