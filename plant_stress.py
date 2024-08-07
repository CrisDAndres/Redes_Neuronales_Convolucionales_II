import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np

####################### FUNCIONES ########################
# @st.cache_resource
def load_model():
    """
    Función para cargar el modelo
    """
    try:
        model = tf.keras.models.load_model('./models/plant_stress_model.keras')
        st.success("Modelo cargado exitosamente.")
        return model
    except Exception as e:
        st.error(f"Error al cargar el modelo: {str(e)}")
        return None

def preprocess_image(uploaded_file):
    """
    Función para preprocesar la imagen cargada
    """
    try:
        img = image.load_img(uploaded_file, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        return img_array
    except Exception as e:
        st.error(f"Error al cargar o preprocesar la imagen: {e}")
        return None

# @st.cache_data
def predict(_model, img_array):
    """
    Función para realizar la prediccion
    """
    return _model.predict(img_array)

####################### INTERFAZ GRÁFICA ########################

# Título y descripción de la aplicación
st.title("🌿 Clasificación de Enfermedades en Hojas de Cultivos de Arroz")
st.write("Carga una imagen de la hoja de una planta para clasificar su enfermedad.")
st.markdown("El modelo es capaz de identificar hojas **sanas** o con **enfermedades**. Dentro de las enfermedades, puede clasificar las siguientes:")

# Agregar iconos y descripciones de las enfermedades
st.markdown("""
- 🌾 **Bacterial Leaf Blight (BLB)**: Tizón bacteriano
- 🍂 **Blast**: Piricularia o añublo del arroz
- 🐛 **Hispa**: Causada por el insecto *Dicladispa armigera*
- 🍃 **Leaf Spot**: Mancha foliar
""")

# Cargar el modelo 
model = load_model()
    
# Cargar una imagen
uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])
            
if uploaded_file is not None:
    
    # Mostrar la imagen cargada
    st.image(uploaded_file, caption='Imagen cargada.', use_column_width=True)
        
    # Realizar la clasificación
    if st.button("Clasificar Imagen"):
        
        # Preprocesar la imagen
        img_array = preprocess_image(uploaded_file)
        if img_array is None:
            st.stop()
        
        # Predicción
        with st.spinner('Realizando la predicción...'):    
            predictions = predict(model, img_array)
            predicted_class = np.argmax(predictions, axis=1)[0]

        # Mapeo de etiquetas con iconos
        class_labels = [
            '🌾 Bacterial Leaf Blight (BLB)', 
            '🍂 Blast', 
            '🌿 Healthy', 
            '🐛 Hispa', 
            '🍃 Leaf Spot'
        ]
        predicted_label = class_labels[predicted_class]
        confidence = np.max(predictions) * 100

        # Mostrar el resultado de la predicción
        st.write(f"**La imagen es clasificada como:** {predicted_label}")
        st.write(f"**Con una probabilidad de:** {confidence:.2f}%")
        
