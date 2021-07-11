#Este archivo contiene el app.py donde corremos el streamlit del proyecto.
import streamlit as st
import pandas as pd
import os, sys

#Para correr este archivo es necesario tener server.py en ejecución.
#Para correr este archivo, se abre el cmd con la ruta al archivo.
#A continuación se ejecuta el comando streamlit run 


# ---------- Append de ruta ----------

#Con este comando de 5 líneas añadimos al archivo la ruta a la carpeta src, que contiene utils.
#que nos valdrá para importar las funciones que utilizaremos para trabajar con el dashboard.

if __name__ == '__main__':
    dir = os.path.dirname
    
    src_path = dir(dir(os.path.abspath(__file__)))
    print(src_path)
    sys.path.append(src_path)

    upper_path = dir(dir(dir(os.path.abspath(__file__))))
    sys.path.append(upper_path)

import utils.dashboard_tb as dash

menu = st.sidebar.selectbox('Menu:',
            options=['Inicio', 'Visualizaciones','Predicción de modelo','Modelos de SQL Database'])

# ---------- Opciones del sidebar y paginaciones ----------

if menu == 'Inicio':

    dash.welcome()


if menu == 'Visualizaciones':
    
    dash.visualization()


#La sección de mostrar DataFrame por Api de Flask no se inserta porque se trabaja con un proyecto que opera imágenes, no DataFrames.
#if menu == 'API':

    #dash.api_flask_menu('http://127.0.0.1:4004/get_token?password=M21755015')


if menu == 'Predicción de modelo':

    dash.predict(upper_path)


if menu == 'Modelos de SQL Database':

    dash.table_from_mysql()