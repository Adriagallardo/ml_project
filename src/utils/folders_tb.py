#Este archivo contiene las funciones del proyecto utilizadas para abrir, crear, leer y escribir archivos que se llevan a cabo en el proyecto.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json

import os
import shutil
import tensorflow as tf

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

def show_filenames(main_path):
    """Esta función se utiliza sobre un fichero que contiene un sistema de clasificación que consta de carpetas que contienen los archivos que son objeto de estudio. Muestra el
    nombre de los 10 primeros archivos que se encuentran dentro de cada carpeta del fichero."""
    
    folders = os.listdir(main_path)

    for folder in folders:
        filename_list = os.listdir(main_path + os.sep + folder)

        print(f"Diez primeros archivos dentro de la carpeta {folder}:\n\n{filename_list[:10]}\n\n")

    
def rename_files(main_path, fol_names=False, lower=False):
    """Esta función se utiliza sobre un fichero que contiene un sistema de clasificación que consta de carpetas que contienen los archivos que son objeto de estudio. Esta            función ofrece 2 acciones. Según si cambiamos los argumentos lower o le pasámos una lista a fol_names. Se ejecutará una parte de la función, ninguna o ambas."""
    
    if lower == True:
        """ Si asignamos True al argumento lower, se cambia el nombre de todos los archivos que contengan letras mayúsculas dentro de las carpetas que se encuentran en la ruta           designada en los argumentos. Las letras mayúsculas se sobreescriben por letras minúsculas."""

        folders = os.listdir(main_path)
        for folder in folders:
            filename_list_path = main_path + os.sep + folder
            filename_list = os.listdir(filename_list_path)
            
            for filename in filename_list:
                filename_path = main_path + os.sep + folder + os.sep
                destination = filename_path + filename.lower()
                source = filename_path + filename
                os.rename(source, destination)
        
        """Se añade un ejemplo para verificar que se ha ejecutado correctamente la función."""

        print("Todos los nombres han sido sobreescritos exitosamente")
        ejemplo = os.listdir(main_path + os.sep + folder)[0]
        print("\nEjemplo resultante:", ejemplo)
    
    else:
        pass

    if isinstance(fol_names, list):
        """ Si se le pasa una lista al argumento fol_names. Se cambia el nombre de todas las carpetas que se encuentran en la ruta designada en los argumentos.
        De Inglés a Castellano"""

        folders = os.listdir(main_path)
        new_folders = fol_names
        for i, folder in enumerate(folders):
            folder_path = main_path + os.sep
            destination = folder_path + new_folders[i]
            source = folder_path + folder
            os.rename(source, destination)

        """Se añade un ejemplo para verificar que se ha ejecutado correctamente la función."""

        print("Todos los nombres han sido sobreescritos exitosamente")
        ejemplo = os.listdir(main_path)[0]
        print("\nEjemplo resultante:", ejemplo)
            
    else:
        pass

def show_n_files(main_path):
    """Esta función se utiliza sobre un fichero que contiene un sistema de clasificación que consta de carpetas que contienen los archivos que son objeto de estudio. Muestra la      cantidad de archivos que se encuentran dentro de cada carpeta del fichero."""
    
    folders = os.listdir(main_path)
    len_values = []

    for folder in folders:
        filename_list_path = main_path + os.sep + folder
        filename_list = os.listdir(filename_list_path)
        len_values.append(len(filename_list))
        print(f"En la carpeta {folder} hay {len(filename_list)} archivos")

    print("\n\nMínimo y máximo de archivos en carpeta:",min(len_values),"y",max(len_values))

    return folders, len_values

def create_test_train_folders(ds_dir):
    """Esta función se utiliza para generar carpetas en la sección de data que corresponden a los labels con los que se clasifica el dataset. Dichas carpetas se utilizan para      contener todos los valores de train y test con los que se quiere trabajar"""
    
    list_path = os.listdir(ds_dir)
    
    """Sección de test"""

    for i in list_path:
        dest = ".." + os.sep + "data" + os.sep + "test" + os.sep + i
        
        try:
            os.makedirs(dest)    
            print("Directorio",i,"creado")
        except FileExistsError:
            print("Directorio",i,"ya existe")

    """Sección de train"""

    for j in list_path:
        dest = ".." + os.sep + "data" + os.sep + "train" + os.sep + j
        
        try:
            os.makedirs(dest)    
            print("Directorio",j,"creado")
        except FileExistsError:
            print("Directorio",j,"ya existe")

def split_files(n, ds_dir):
    """Esta función divide un conjunto de imágenes en train y split segun el 'n' (porcentaje de test) que le proporcionamos. Esta función está adaptada a la profundidad de las carpetas del proyecto de machine learning. 'ds_dir' es un argumento obligatorio donde postulamos la ruta de la carpeta matriz donde se encuentran las subcarpetas de las que queremos extraer los archivos."""

    """Sección test"""
    list_path=os.listdir(ds_dir)

    for i in range(len(list_path)):
        dest = ".." + os.sep + "data" + os.sep + "test" + os.sep + list_path[i] + os.sep
        dest2 = ".." + os.sep + "data" + os.sep + "train" + os.sep + list_path[i] + os.sep
        source = ".." + os.sep + "data" + os.sep + "downloads" + os.sep + "sentinel_2" + os.sep + list_path[i] + os.sep
        folder_lenght = len(os.listdir(ds_dir + os.sep + list_path[i]))

        """Sección test"""

        for f in os.listdir(ds_dir + os.sep + list_path[i]):
            if len(os.listdir(ds_dir + os.sep + list_path[i])) > folder_lenght * (100-n) / 100:
                    shutil.move(source+f, dest)
        
        print(f"Archivos de test de {list_path[i]} correctamente transportados")

        """Sección train (todo el restante después de operar test)"""

        for ff in os.listdir(ds_dir + os.sep + list_path[i]):
            if len(os.listdir(ds_dir + os.sep + list_path[i])) != 0:
                shutil.move(source+ff, dest2)

        print(f"Archivos de train de {list_path[i]} correctamente transportados")
