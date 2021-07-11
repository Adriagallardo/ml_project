#Este archivo contiene las funciones asociadas al archivo app.py que se ejecuta en streamlit.
from pathlib import WindowsPath
import streamlit as st
import pandas as pd
from PIL import Image, ImageOps
import os
import cv2
from keras.preprocessing.image import img_to_array
import tensorflow as tf
from tensorflow import keras
import numpy as np
from utils.mysql_tb import MySQL, connect_mysql


st.cache(suppress_st_warning=True)
def load_json_df(uploaded_file):
    df = None
    if uploaded_file != None:
        df = pd.read_json(uploaded_file, orient='split')
    return df

def welcome():
    """Esta función imprime en pantalla un mensaje de bienvenida para la pantalla de inicio"""
    st.title('Proyecto de Machine Learning: Clasificación de superficies terrestres reconocidas por vía satelital')
    st.write('En este proyecto se diseñan diversos modelos de inteligencia artificial capaces de reconocer imágenes tomadas por vía satelital,\
             sobre la superficie terrestre, y clasificarlas en grupos siguiendo los criterios de análisis exploratorio, aprendizaje automático\
             (machine learning), aprendizaje profundo (deep learning), visualización de datos y diseño experimental.')

def visualization():
    """Esta función muestra por pantalla visualizaciones del proyecto"""

    st.title('Visualizaciones')
    st.write('En esta sección se muestran algunas visualizaciones que se han elaborado durante el proyecto.')
    
    st.write('\nNúmero de imagenes que tiene el proyecto:')
    img = Image.open( '..' + os.sep + '..' + os.sep+ 'reports'+ os.sep+ 'from_main'+ os.sep+ 'images'+ os.sep + 'n_files_per_folder.jpg')
    st.image(img,use_column_width=True)

    st.write('\n\n\nComo son las imágenes del proyecto:')
    img = Image.open( '..' + os.sep + '..' + os.sep+ 'reports'+ os.sep+ 'from_main'+ os.sep+ 'images'+ os.sep + 'image_label_example.jpg')
    st.image(img,use_column_width=True)

    st.write('\nComo se trabajan las clases con onehot-encoding de tensorflow:')
    img = Image.open( '..' + os.sep + '..' + os.sep+ 'reports'+ os.sep+ 'from_main'+ os.sep+ 'images'+ os.sep + 'onehot_labels_example.jpg')
    st.image(img,use_column_width=True)

    st.write('\nMatriz de confusión del mejor modelo:')
    img = Image.open( '..' + os.sep + '..' + os.sep+ 'reports'+ os.sep+ 'from_main'+ os.sep+ 'images'+ os.sep + 'confusion_matrix.jpg')
    st.image(img,use_column_width=True)

    st.write('\n\n\nResultados de predicción del mejor modelo:')
    img = Image.open( '..' + os.sep + '..' + os.sep+ 'reports'+ os.sep+ 'from_main'+ os.sep+ 'images'+ os.sep + 'real_pred_samples.jpg')
    st.image(img,use_column_width=True)


def predict(upper_path):
    """Esta función permite poner en un dashboard un recogedor de imágenes que haga predicciones para el modelo que se propone"""
    
    st.title('Predicción')
    st.write('En esta sección puedes hacer tus propias predicciones. Sube una imagen "rgb" y el modelo intentará descubrir a que clase pertenece.')
    
    """Coge la imagen"""
    

    file = st.file_uploader("Sube el archivo", type=["png", "jpg", "jpeg"])
    show_file = st.empty()

    if not file:
        show_file.info("Por favor, mira que el archivo sea tipo: " + ", ".join(["png", "jpg", "jpeg"]))
        return

    image = Image.open(file)
    st.image(image)

    """Adecua la imagen al modelo"""

    size = (64,64)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image = np.asarray(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_reshape = img[np.newaxis,...]

    """Se aplica el modelo"""

    model = tf.keras.models.load_model(upper_path + os.sep + "models" + os.sep + "model1.h5")
    #model  = tf.saved_model.load(".." + ".." + os.sep + "models" + os.sep + "model1.pb")
    
    prediction = model.predict(img_reshape)
    test_dir = upper_path + os.sep + "data" + os.sep + "test"
    decoded_labels = os.listdir(test_dir)
    score = tf.nn.softmax(prediction[0])

    st.success('La imagen ha sido identificada')
    
    
    resultado = decoded_labels[np.argmax(prediction)]
    
    st.write('Resultado:', resultado)


   
def table_from_mysql():
    """Esta función llama a la tabla de sql donde se guardan los 5 mejores modelos utilizados en main.ipynb"""
    db_connection = connect_mysql(IP_DNS="consciencesai.com", USER="21755015m", PASSWORD="adriagallardo96", BD_NAME="21755015m_ds_april_2021_db", PORT=30001)
    
    a = pd.read_sql_table("table_comparasion", db_connection)

    st.title("DataFrame de 5 mejores modelos guardados en MySQL")
    st.write(a)

def browse_json_todf():
    """Esta función genera un navegador que permite seleccionar un archivo json en el equipo
     para mostrarlo como dataframe en pantalla"""
    slider_json = st.sidebar.file_uploader("Selecciona un JSON", type=['json'])
    st.write('Selecciona en el buscador de la izquierda un archivo json\
            que quieras cargar')
    if type(slider_json) != type(None):
        df_slider = load_json_df(slider_json)
        st.table(df_slider)

#A continuación se excluye una función del proyecto porque este trabaja con imagenes y no interesa trabajar con DataFrames. No obstante, se almacena por si fuera necesaria.

#def api_flask_menu(URL):
    #"""Esta función coje el json de un string URL que le pasamos, lo muestra por panalla como
    #dataframe primero y, a continuación, lo muestra en formato json con una codificación
    #orient='split'"""
    #a = pd.read_json(URL, orient='split')
    #st.title("DataFrame de Flask")
    #st.write(a)
    #st.title("API de DataFrame de Flask")
    #st.write("Al descargar, tener en cuenta que se ha codificado con orientación: split")
    #st.write(a.to_json(orient='split'))