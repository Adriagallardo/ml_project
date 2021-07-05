#Este archivo tiene las funciones asociadas al data wrangling que elaboramos en el proyecto.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def null_in_dataframe(data): 
    """Esta función retorna el número de valores nulos que tiene el dataframe"""
    a = data.isnull().sum().sum()

    if a > 0:
        print(f"El dataframe tiene {a} valores nulos.")
    
    else:
        print("El dataframe no contiene valores nulos.")

def dulicate_in_dataframe(data):
    """Esta función retorna el número de valores nulos que tiene el dataframe"""
    return data[data.duplicated()]

def outlier_clean(data, kind, dict_cols_max):
    """Esta función limpia de outliers un dataframe. Con posibilidad estándard o customizada para este proyecto"""

    if kind == "custom":
        if isinstance(dict_cols_max, dict):
            data_clean = data
            for column, max_value in dict_cols_max.items():
                
                if column == "age":
                    data_clean = data_clean[data_clean["age"] <= max_value]

                elif column == "absences":
                    data_clean = data_clean[data_clean["absences"] <= max_value]

            print("La forma de la data resultante es:", data_clean.shape)
            
        else:
            raise Exception("El argumento dict_cols_max tiene que ser un diccionario")
            
    else:
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = (Q1 - 1.5 * IQR)
        limite_superior = (Q3 + 1.5 * IQR)
        limite_superior
        data_clean = data[~((data < limite_inferior) | (data > limite_superior)).any(axis=1)]
        print("La forma de la data resultante es:", data_clean.shape)

    return data_clean
    

def conc_columns(data, name_column, list_column):
    """Esta función genera una nueva columna a partir de las columnas que deseemos de un dataframe"""
    data[name_column] = 0
    for column in list_column:
        data[name_column] += data[column]   

    return data

def check_columns_unique(data):
    """Esta función imprime los valores únicos que nos encontramos para cada columna en un dataframe"""
    for col in data:
        print(f"La columna {col} tiene estos valores únicos:", data[col].unique())

def bin_obj_to_int(data):    
    for col in data:
        """Esta función cambia los valores binarios de tipo objeto a valores binarios de tipo int en un dataframe"""
        if len(data[col].unique()) == 2:
            change = {data[col].unique()[0]: 1, data[col].unique()[1]: 0}
            data[col] = [change[item] for item in data[col]]
        else:
            pass

def max_values(qvalues, data, columns):
    """Esta formula muestra por pantalla los primeros valores más altos para la columna elegida de un DataFrame"""
    for i in columns:
        print(f"Primeros {qvalues} valores de la columna {i}")
        print(data[i].sort_values(ascending=False).head(qvalues))


def comp_data(data, column, mask_value):
    """Esta función retorna un DataFrame resultante de comparar las medias de un dataframe asignandole para mayor
    a un valor concreto de una columna específica, con las medias del mismo DataFrame sin poner asignaciones de 
    valor."""
    
  
    a = data.sort_values(by=column ,ascending=False).mean()
    b = data[data[column] > mask_value].sort_values(by=column ,ascending=False).mean()
    frame = {"Total": a, f"{column} > {mask_value}" : b}
    data_comp = pd.DataFrame(frame)
    
    return data_comp


def comp_multiple_data(data, column, mask_list):
    """Esta función retorna un DataFrame resultante de comparar las medias de un dataframe asignandole un valor específico,
    a una columna, proporcionado en modo lista en la función, con las medias del mismo DataFrame sin poner asignaciones de 
    valor."""

    mean_total = data.sort_values(by=column ,ascending=False).mean()
    frame_total = {"Total" : mean_total}
    data_mult_comp = pd.DataFrame(frame_total)
    
    for i in mask_list:
        mean_ = data[data[column] == i].sort_values(by=column ,ascending=False).mean()
        frame = {f"{column} = {i}" : mean_}
        semi_data = pd.DataFrame(frame)
        data_mult_comp = data_mult_comp.join(semi_data)

    return data_mult_comp

def get_unique_counts(data):
    """Esta función recoge un conteo de los valores únicos que hay para cada y lo retorna
    como un Series"""

    list_uniques = []
    for col in data:
        x = len(data[col].unique())
        list_uniques.append(x)
        
    ser = pd.Series(list_uniques, index=data.columns)
    return ser