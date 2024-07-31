import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np

# Interfaz de Streamlit
st.title("Clasificación de Enfermedades en Plantas")
st.write("Carga una imagen de la hoja de una planta para predecir su enfermedad.")

# Cargar el modelo entrenado
model_path = 'models/best_model_plants.keras'

# Intentar cargar el modelo
try:
    model = tf.keras.models.load_model(model_path)
    st.write("Modelo cargado exitosamente.")
except Exception as e:
    st.write(f"Error al cargar el modelo: {e}")
    st.stop()
    
# Interfaz de usuario para cargar una imagen
uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Mostrar la imagen cargada
    st.image(uploaded_file, caption='Imagen cargada.', use_column_width=True)

    # Preprocesar la imagen
    try:
        img = image.load_img(uploaded_file, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        st.write("Imagen cargada y preprocesada exitosamente.")
    except Exception as e:
        st.write(f"Error al cargar o preprocesar la imagen: {e}")
        st.stop()

    # # Realizar la predicción
    # try:
    #     predictions = model.predict(img_array)
    #     st.write("Predicciones:", predictions)
    # except Exception as e:
    #     st.write(f"Error al realizar la predicción: {e}")

    # Hacer la predicción
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]

    # Mapeo de etiquetas: {'BLB': 0, 'Blast': 1, 'healthy': 2, 'hispa': 3, 'leaf_spot': 4}
    class_labels = ['BLB', 'Blast', 'healthy', 'hispa', 'leaf_spot']  
    predicted_label = class_labels[predicted_class]

    st.write(f"La imagen es clasificada como: {predicted_label}")
    st.write(f"Con una probabilidad de: {np.max(predictions) * 100:.2f}%")