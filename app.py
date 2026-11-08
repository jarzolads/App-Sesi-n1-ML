import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Teoría de Machine Learning", layout="wide")

st.title("Introducción al Desarrollo y Despliegue de Modelos de Machine Learning")
st.markdown("Autor: Dr. Jesús Andrés Arzola Flores[cite: 1]")
st.write("Esta aplicación está diseñada exclusivamente para explorar los conceptos teóricos fundamentales del aprendizaje automático.")

# Menú de navegación lateral
st.sidebar.header("Índice Teórico")
seccion = st.sidebar.radio(
    "Selecciona un tema para aprender:",
    [
        "1. ¿Qué es el Machine Learning?",
        "2. Tipos de Aprendizaje",
        "3. Flujo de Desarrollo de un Modelo",
        "4. Despliegue de Modelos"
    ]
)

if seccion == "1. ¿Qué es el Machine Learning?":
    st.header("1. ¿Qué es el Machine Learning?")
    st.write("""
    El **Machine Learning (Aprendizaje Automático)** es una rama de la Inteligencia Artificial (IA) que se enfoca en el desarrollo de sistemas capaces de aprender y mejorar a partir de los datos, sin ser programados explícitamente para cada tarea.
    
    A diferencia de la programación tradicional, donde se ingresan datos y reglas para obtener respuestas, en Machine Learning se ingresan datos y respuestas para que el algoritmo descubra las reglas.
    """)
    st.info("💡 **Ejemplo:** En lugar de escribir reglas complejas para identificar correos spam, le mostramos al modelo miles de correos etiquetados como 'spam' o 'no spam' para que aprenda a distinguirlos por sí mismo.")

elif seccion == "2. Tipos de Aprendizaje":
    st.header("2. Tipos de Aprendizaje Automático")
    st.write("Los modelos de Machine Learning se clasifican principalmente por cómo aprenden de los datos:")
    
    st.subheader("Aprendizaje Supervisado")
    st.write("El algoritmo aprende de datos de entrenamiento que ya están etiquetados con la respuesta correcta. Su objetivo es mapear una entrada a una salida predecible.")
    st.write("- *Ejemplo:* Predecir el precio de una casa basado en su tamaño y ubicación (Regresión) o identificar si una imagen contiene un perro o un gato (Clasificación).")
    
    st.subheader("Aprendizaje No Supervisado")
    st.write("El modelo recibe datos sin etiquetas y debe encontrar patrones, estructuras o agrupaciones ocultas por su cuenta.")
    st.write("- *Ejemplo:* Segmentar clientes en diferentes grupos para marketing basado en sus hábitos de compra (Clustering).")
    
    st.subheader("Aprendizaje por Refuerzo")
    st.write("Un 'agente' aprende a tomar decisiones interactuando con un entorno, recibiendo recompensas por acciones correctas y penalizaciones por las incorrectas.")
    st.write("- *Ejemplo:* Entrenar a una inteligencia artificial para jugar ajedrez o conducir un auto autónomo.")

elif seccion == "3. Flujo de Desarrollo de un Modelo":
    st.header("3. Flujo de Desarrollo de un Modelo")
    st.write("Desarrollar un modelo de Machine Learning es un proceso iterativo que consta de varios pasos clave:")
    
    st.markdown("""
    1. **Recopilación de Datos:** Obtener los datos sin procesar necesarios para resolver el problema.
    2. **Limpieza y Preparación (Preprocesamiento):** Manejar valores nulos, normalizar variables y seleccionar las características (features) más importantes.
    3. **División de Datos:** Separar el conjunto de datos en **Datos de Entrenamiento** (para enseñar al modelo) y **Datos de Prueba** (para evaluar su rendimiento).
    4. **Entrenamiento del Modelo:** Aplicar el algoritmo seleccionado a los datos de entrenamiento para que ajuste sus parámetros internos.
    5. **Evaluación:** Medir la eficacia del modelo utilizando los datos de prueba y métricas específicas (precisión, error cuadrático medio, etc.).
    6. **Ajuste y Optimización:** Modificar hiperparámetros para mejorar los resultados obtenidos.
    """)

elif seccion == "4. Despliegue de Modelos":
    st.header("4. Despliegue de Modelos (Deployment)")
    st.write("""
    El **Despliegue** es la etapa final y crucial donde el modelo entrenado se hace accesible para ser utilizado en el mundo real. 
    Un modelo excelente no tiene valor si se queda en un cuaderno de experimentación (como Google Colab).
    """)
    
    st.write("### Formas comunes de despliegue:")
    st.markdown("""
    * **Aplicaciones Web Interactivas:** Utilizando frameworks como **Streamlit** para crear interfaces gráficas rápidamente donde los usuarios pueden interactuar con el modelo.
    * **APIs RESTful:** Exponer el modelo mediante servicios (usando Flask o FastAPI) para que otras aplicaciones, páginas web o software móviles envíen datos y reciban predicciones en tiempo real.
    * **Despliegue en la Nube:** Alojar el modelo en plataformas en la nube para asegurar escalabilidad y disponibilidad continua.
    """)
    st.success("🎯 **Objetivo final:** Integrar la predicción generada por el Machine Learning en los procesos de toma de decisiones o en el producto final.")
