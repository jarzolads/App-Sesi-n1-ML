import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Configuración de la página
st.set_page_config(page_title="Aprende Machine Learning", layout="wide")

st.title("Introducción al Desarrollo y Despliegue de Modelos de Machine Learning")
st.markdown("Autor: Dr. Jesús Andrés Arzola Flores[cite: 1]")
st.write("Esta aplicación interactiva te guiará a través de los conceptos fundamentales, una actividad práctica y una evaluación para consolidar tu aprendizaje.")

st.sidebar.header("Navegación")
seccion = st.sidebar.radio("Ir a:", ["1. Conceptos Básicos", "2. Actividad Práctica", "3. Evaluación y Retroalimentación"])

if seccion == "1. Conceptos Básicos":
    st.header("Conceptos Básicos de Machine Learning")
    st.write("""
    El **Machine Learning (Aprendizaje Automático)** permite a las computadoras aprender de los datos sin ser programadas explícitamente para cada tarea. 
    
    *   **Datos de Entrenamiento:** El conjunto de ejemplos (con sus respuestas o etiquetas) que se utiliza para enseñar al modelo.
    *   **Datos de Prueba:** Un subconjunto de datos que el modelo nunca ha visto, utilizado para evaluar qué tan bien generaliza.
    *   **Algoritmo:** Las matemáticas y la lógica subyacente (ej. Regresión Logística, Random Forest) que extraen patrones de los datos.
    *   **Despliegue:** El proceso de integrar un modelo entrenado en un entorno de producción (como esta misma aplicación en Streamlit) para que pueda realizar predicciones sobre datos nuevos.
    """)
    st.info("💡 Explora la siguiente sección para ver cómo estos conceptos se aplican en código en tiempo real.")

elif seccion == "2. Actividad Práctica":
    st.header("Entrenamiento Interactivo de un Modelo")
    st.write("Ajusta los parámetros para entrenar un modelo de clasificación usando un conjunto de datos sintético y observa cómo cambia el rendimiento.")
    
    # Generar datos sintéticos
    np.random.seed(42)
    X = np.random.rand(200, 2)
    y = (X[:, 0] + X[:, 1] > 1).astype(int)
    
    col1, col2 = st.columns(2)
    with col1:
        test_size = st.slider("Porcentaje de Datos de Prueba", min_value=0.1, max_value=0.5, value=0.2, step=0.05)
        n_estimators = st.slider("Número de Árboles (Random Forest)", min_value=1, max_value=100, value=10, step=1)
        
    with col2:
        st.write("### Resultados del Entrenamiento")
        if st.button("Entrenar Modelo"):
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
            
            modelo = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
            modelo.fit(X_train, y_train)
            predicciones = modelo.predict(X_test)
            
            precision = accuracy_score(y_test, predicciones)
            st.success(f"Modelo entrenado exitosamente.")
            st.metric(label="Precisión (Accuracy) en Datos de Prueba", value=f"{precision * 100:.2f}%")
            st.write(f"- Datos de entrenamiento: {len(X_train)} muestras")
            st.write(f"- Datos de prueba: {len(X_test)} muestras")

elif seccion == "3. Evaluación y Retroalimentación":
    st.header("Pon a prueba tu conocimiento")
    st.write("Responde las siguientes preguntas para evaluar tu comprensión de los conceptos de Machine Learning.")
    
    # Pregunta 1
    st.subheader("Pregunta 1")
    p1 = st.radio(
        "¿Para qué se utilizan los 'Datos de Prueba' en Machine Learning?",
        options=["Para enseñar al modelo los patrones iniciales.", "Para evaluar el rendimiento del modelo en datos no vistos.", "Para desplegar la aplicación en un servidor web."],
        index=None
    )
    if p1:
        if p1 == "Para evaluar el rendimiento del modelo en datos no vistos.":
            st.success("¡Correcto! Los datos de prueba simulan situaciones reales para asegurar que el modelo no se haya memorizado simplemente las respuestas (sobreajuste).")
        else:
            st.error("Incorrecto. Recuerda que la evaluación requiere datos que el algoritmo no haya procesado durante su fase de aprendizaje.")
            
    # Pregunta 2
    st.subheader("Pregunta 2")
    p2 = st.radio(
        "¿Qué representa el despliegue (deployment) de un modelo?",
        options=["La división de la base de datos en conjuntos más pequeños.", "La integración del modelo en un entorno donde puede recibir nuevos datos y emitir predicciones.", "La limpieza de datos faltantes en el código Python."],
        index=None
    )
    if p2:
        if p2 == "La integración del modelo en un entorno donde puede recibir nuevos datos y emitir predicciones.":
            st.success("¡Excelente! Desplegar un modelo (como hacerlo accesible mediante IALabs o Streamlit) es lo que le da valor práctico en el mundo real.")
        else:
            st.error("Incorrecto. El despliegue es la fase final del ciclo de vida, donde el modelo se pone 'en producción' para ser consumido por usuarios o sistemas.")
