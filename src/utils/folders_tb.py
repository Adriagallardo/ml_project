#Este archivo contiene las funciones del proyecto utilizadas para abrir, crear, leer y escribir archivos que se llevan a cabo en el proyecto.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json

def read_my_csv(path_file):
    """Esta función lee el un archivo .csv introduciendo su ruta"""
    data = pd.read_csv(path_file)
    return data

def create_json(path_file, data):
    """Esta función crea un archivo json en la ruta que pongamos, sobre un dataframe escogido"""
    json_written = data.to_json(orient="split")
    with open(path_file, 'w') as created:  
        created.write(json_written)

def read_json(path_file):
    """Esta función lee un archivo json y lo guarda como variable json_readed"""
    with open(path_file, 'r+') as outfile:
        json_readed = json.load(outfile)
    return json_readed

def create_json_from_dict(path_file, dict):
    """Esta función crea un archivo json en la ruta que pongamos, sobre un diccionario escogido"""
    with open(path_file, 'w') as created:  
        json.dump(dict, fp=created, indent = 4)