#Este archivo contiene las funciones asociadas al archivo app.py que se ejecuta en streamlit.
import streamlit as st
import pandas as pd


st.cache(suppress_st_warning=True)
def load_json_df(uploaded_file):
    df = None
    if uploaded_file != None:
        df = pd.read_json(uploaded_file, orient='split')
    return df

def welcome():
    """Esta función imprime en pantalla un mensaje de bienvenida para la pantalla de inicio"""
    st.title('Proyecto EDA')
    st.write('Bienvenido al proyecto EDA de Adrià. Selecciona en el menú a la izquierda\
            que sección quieres visitar')


def browse_json_todf():
    """Esta función genera un navegador que permite seleccionar un archivo json en el equipo
     para mostrarlo como dataframe en pantalla"""
    slider_json = st.sidebar.file_uploader("Selecciona un JSON", type=['json'])
    st.write('Selecciona en el buscador de la izquierda un archivo json\
            que quieras cargar')
    if type(slider_json) != type(None):
        df_slider = load_json_df(slider_json)
        st.table(df_slider)

def api_flask_menu(URL):
    """Esta función coje el json de un string URL que le pasamos, lo muestra por panalla como
    dataframe primero y, a continuación, lo muestra en formato json con una codificación
    orient='split'"""
    a = pd.read_json(URL, orient='split')
    st.title("DataFrame de Flask")
    st.write(a)
    st.title("API de DataFrame de Flask")
    st.write("Al descargar, tener en cuenta que se ha codificado con orientación: split")
    st.write(a.to_json(orient='split'))