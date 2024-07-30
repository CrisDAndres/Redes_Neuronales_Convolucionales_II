# Clasificación de Patrones de Estrés en Plantas con Redes Neuronales Convolucionales (EfficientNetB0)

<p align="center">
  <img src="img/stress-abiotic.png" alt="App" width="300px">
</p>
<p align="center">
  <b>Streamlit App 📱 disponible </b><a href="https://digit-recognition0-9.streamlit.app/">aquí</a>!
</p>

Este proyecto implementa redes neuronales convolucionales (CNN) utilizando TensorFlow y Keras para la clasificación del estrés vegetal, específicamente en hojas de arroz. Se incluyen técnicas de aumento de datos (*Data Augmentation*) y pre-procesamiento y pre-entrenamiento mediante el modelo **EfficientNetB0** para la optimización y mejora del rendimiento de la red neuronal.

<span style="color:red">EfficientNetB0 ha demostrado ser altamente eficiente en términos de rendimiento de precisión y uso de recursos computacionales. Esto hace que sea una opción popular para aplicaciones de clasificación de imágenes que requieren alta precisión y eficiencia, como en dispositivos móviles o sistemas con recursos limitados.</span>

## Introducción 🔬

Las plantas, al igual que otros organismos vivos, pueden experimentar diversos tipos de estrés que afectan su crecimiento, desarrollo y productividad. Los factores de estrés en plantas se clasifican en dos categorías principales: factores **abióticos** y **bióticos**.

- Los factores abióticos se refieren a las condiciones ambientales adversas que pueden causar daño a las plantas (sequía, temperaturas extremas, acumulación de sales, contaminantes o luz excesiva o insuficiente).
- Los factores bióticos son los organismos vivos que interactúan con las plantas (plagas o enfermedades causadas por patógenos).

Las plantas han desarrollado mecanismos de respuesta y adaptación al estrés, como cambios génicos, morfológicos o bioquímicos.

**Comprender los diferentes tipos de estrés en plantas y sus mecanismos de respuesta es fundamental para desarrollar estrategias de manejo que permitan mitigar los efectos negativos del estrés y mejorar la productividad de los cultivos.**

## Estructura del proyecto 📂

El proyecto consiste en los siguientes archivos:

- ``data/``: Carpeta que contiene las imágenes descargadas de Kaggle para el entrenamiento de la red neuronal.
- ``notebook/``: Carpeta que contiene el notebook de Jupyter con el código utilizado para realizar el entrenamiento de la red neuronal, con explicaciones detalladas de cada paso.
- ``models/``: Carpeta que contiene el mejor modelo obtenido durante el entrenamiento de la red neuronal, en formato ``.keras``.
- ``img/``: Carpeta que contiene imágenes del proyecto.

## Tecnologías utilizadas 🛠️

![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  
## Descripción del proyecto 📝

El dataset MNIST contiene un conjunto de 60k imágenes de entrenamiento y 10k imágenes de prueba de dígitos manuscritos (de 0 a 9) en escala de grises, cada una de 28x28 píxeles. Es ampliamente utilizado en el entrenamiento de sistemas de procesamiento de imágenes y modelos de aprendizaje automático.

Este proyecto se centra en la creación de una Red Neuronal Convolucional (CNN) utilizando **TensorFlow**, una de las bibliotecas más utilizadas en el campo del aprendizaje automático y la inteligencia artificial. Las **CNN** son muy efectivas para tareas de clasificación de imágenes y reconocimiento de objetos, ya que pueden identificar y aprender características espaciales de las imágenes de manera eficiente. 

Para hacer el modelo más accesible e interactivo, se ha desarrollado una interfaz web sencilla usando Streamlit. Esto permite a los usuarios dibujar un dígito en un lienzo y recibir la predicción del modelo en tiempo real.

## Instrucciones de ejecución 💻
Para ejecutar este proyecto en tu máquina local, sigue los siguientes pasos:

1. Clona este repositorio en tu máquina local.
2. Descarga las carpetas ``models`` y ``notebook``, así como el scrip de Python.
3. Instala las dependencias necesarias ejecutando ``pip install -r requirements.txt``.
4. Ejecuta el archivo ``numeros.py`` y asegúrate de que has descargado las carpetas en el mismo entorno. A continuación, abre la terminal y ejecuta el siguiente comando: ``streamlit run numeros.py``. Esto abrirá el navegador web ``http://localhost:8501/`` que te llevará a la aplicación.
5. Dibuja✏️ un dígito del 0 al 9 en el lienzo y presiona el botón de **PREDECIR** para ver la predicción. 

### To do ⚙️

- [ ] Corrección de *warnings* en Streamlit.

## Contacto 📧
Si tienes alguna pregunta o sugerencia sobre este proyecto, no dudes en ponerte en contacto conmigo. Puedes hacerlo a través de mis redes sociales.
 
