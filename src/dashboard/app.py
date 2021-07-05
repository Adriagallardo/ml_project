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
    src_path = dir(dir(__file__))
    print(src_path)
    sys.path.append(src_path)

import utils.dashboard_tb as dash

menu = st.sidebar.selectbox('Menu:',
            options=['Inicio', 'Dataframe', 'API'])

# ---------- Opciones del sidebar y paginaciones ----------

if menu == 'Inicio':

    dash.welcome()


if menu == 'Dataframe':
        
    dash.browse_json_todf()


if menu == 'API':

    dash.api_flask_menu('http://127.0.0.1:4004/get_token?password=M21755015')
