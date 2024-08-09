# Clasificación de Patrones de Estrés en Plantas con Redes Neuronales Convolucionales (EfficientNetB0)

<p align="center">
  <img src="img/stress-abiotic.png" alt="App" width="300px">
</p>

<p align="center">
  <i>Fuente de la imagen: https://kcenter.lallemandplantcare.com/</i>
</p>

<p align="center">
  <b>Streamlit App 📱 disponible </b><a href="https://plant-stress-recognition.streamlit.app/">aquí</a>!
</p>

Este proyecto implementa redes neuronales convolucionales (CNN) utilizando TensorFlow y Keras para la clasificación del estrés vegetal, específicamente enfermedades causadas por microorganismos o insectos en hojas de arroz. Se incluyen técnicas de aumento de datos (*Data Augmentation*) y preprocesamiento y optimización usando el modelo preentrenado **EfficientNetB0** para la mejora del rendimiento de la red neuronal, consiguiendo una precisión del **92.16 %**.

<span style="color:red">EfficientNetB0 ha demostrado ser altamente eficiente en términos de rendimiento de precisión y uso de recursos computacionales. Esto hace que sea una opción popular para aplicaciones de clasificación de imágenes que requieren alta precisión y eficiencia, como en dispositivos móviles o sistemas con recursos limitados.</span>

## Introducción 🔬

Las plantas, al igual que otros organismos vivos, pueden experimentar diversos tipos de estrés que afectan su crecimiento, desarrollo y productividad. Los factores de estrés en plantas se clasifican en dos categorías principales: factores **abióticos** y **bióticos**.

- Los factores **abióticos** se refieren a las condiciones ambientales adversas que pueden causar daño a las plantas (sequía, temperaturas extremas, acumulación de sales, contaminantes o luz excesiva o insuficiente).
- Los factores **bióticos** son los organismos vivos que interactúan con las plantas (plagas o enfermedades causadas por patógenos).

**Comprender los diferentes tipos de estrés en plantas y sus mecanismos de respuesta es fundamental para desarrollar estrategias de manejo que permitan mitigar los efectos negativos del estrés y mejorar la productividad de los cultivos.**

Este proyecto trata de identificar 4 de los estreses bióticos más comunes y destructivos de los cultivos de arroz: 

- 🌾**Tizón bacteriano** (*Bacterial Leaf Blight*), causado por el grupo de bacterias *Xanthomonas oryzae*.
- 🍂**Piricularia o añublo del arroz** (*Rice blast*), causada por el hongo *Pyricularia oryzae*.
- 🍃**Mancha foliar** (*Leaf spot*), cuasada por varios patógenos, incluyendo hongos.
- 🐛**Hispa del arroz** (*Rice hispa*), causada por el insecto *Dicladispa armigera*.

## Estructura del proyecto 📂

El proyecto consiste en los siguientes archivos:

- ``data/``: Carpeta que contiene las imágenes descargadas de Kaggle (*https://www.kaggle.com/datasets/ritikbompilwar/plantstressidentification*) para el entrenamiento de la red neuronal.
- ``notebook/``: Carpeta que contiene el notebook de Jupyter con el código utilizado para realizar el entrenamiento de la red neuronal, con explicaciones detalladas de cada paso.
- ``models/``: Carpeta que contiene el mejor modelo obtenido durante el entrenamiento de la red neuronal, en formato *.h5*.
- ``img/``: Carpeta que contiene imágenes del proyecto.
- ``plant_stress.py``: Script de Python para la aplicación de Streamlit.

## Tecnologías utilizadas 🛠️

![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  
## Descripción del proyecto 📝

El dataset contiene un conjunto de 602 imágenes térmicas de hojas enfermas y sanas de cultivos de arroz, divididas en 3 conjuntos: *train, test y validation*. Las imágenes se clasifican en 5 clases, 4 de ellas son enfermedades de las hojas (en inglés ***Bacterial Leaf Blight, Blast, Leaf Spot, Hispa***) y hojas sanas.

Este proyecto se centra en la creación de una Red Neuronal Convolucional (CNN) utilizando **TensorFlow**, una de las bibliotecas más utilizadas en el campo del aprendizaje automático y la inteligencia artificial. Las **CNN** son muy efectivas para tareas de clasificación de imágenes y reconocimiento de objetos, ya que pueden identificar y aprender características espaciales de las imágenes de manera eficiente. 

Se ha utilizado el modelo preentrenado **EfficientNetB0** para el preprocesamiento, optimización y mejora del rendimiento de la red neuronal. El uso de este modelo permite preparar las imágenes para un entrenamiento eficiente y proporcionar una base sólida con características previamente aprendidas, acelerando el proceso de entrenamiento y mejorando la precisión del modelo final.

---
**EfficientNetB0** es parte de la familia de modelos de EfficientNet desarrollados por Google. Estos modelos se destacan por su alta eficiencia y rendimiento en la clasificación de imágenes, logrando un equilibrio óptimo entre precisión y consumo de recursos computacionales.

EfficientNet introduce una técnica llamada *compound scaling*, que ajusta de manera coordinada la profundidad, la resolución y el ancho de la red para lograr mejores resultados. En particular, EfficientNetB0 es el modelo base de la serie y se ha demostrado que es altamente eficiente para diversas tareas de visión por computadora.

## Instrucciones de ejecución 💻
Para ejecutar este proyecto en tu máquina local, sigue los siguientes pasos:

1. Clona este repositorio en tu máquina local.
2. Descarga las carpetas ``data``,``models`` y ``notebook``, así como el script de Python ``plant_stress.py``.
3. Instala las dependencias necesarias ejecutando ``pip install -r requirements.txt``.
4. Ejecuta el archivo ``plant_stress.py`` y asegúrate de que has descargado las carpetas en el mismo entorno. A continuación, abre la terminal y ejecuta el siguiente comando: ``streamlit run plant_stress.py``. Esto abrirá el navegador web ``http://localhost:8501/`` que te llevará a la aplicación.
5. Carga una imagen desde tu ordenador y presiona el botón de **Clasificar imagen** para ver la clasificación de la enfermedad de la hoja. 

## Contacto 📧
Si tienes alguna pregunta o sugerencia sobre este proyecto, no dudes en ponerte en contacto conmigo. Puedes hacerlo a través de mis redes sociales.
 
