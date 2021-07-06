#Este archivo contiene las funciones de visualización (pandas, matplolib y seaborn) que elaboramos en el proyecto.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import squarify as sq

def sns_gstyle():
    """Esta función cambia los gráficos de seaborn que vienen por defecto"""
    sns.set(style="ticks")
   
def corr_onevalue_graphic_abs(data, variable):
    """Esta función muestra un gráfico para un Series correspondiente a un mostreo de correlación
    de una columna con las demás del dataframe. No estudia la negatividad o positividad de los valores
    ya que trabaja con valores absolutos"""
    current_palette = sns.color_palette("crest")
    plt.figure(figsize=(18,9))
    sq.plot(label=data.keys(), sizes=data.sort_values()[:-1].abs().values, color=current_palette, text_kwargs={'fontsize':13,'color':'white'})
    plt.title(f"Correlación de las variables en estudio con {variable}")
    plt.axis('off')

def corr_onevalue_graphic_n(data, variable):
    """Esta función muestra un gráfico para un Series correspondiente a un mostreo de correlación
    de una columna con las demás del dataframe"""
    plt.figure(figsize=(12,9))
    current_palette = sns.color_palette("Greens")
    data.sort_values()[:-1].plot.bar(width=1,color=current_palette, rot=60)
    plt.title(f"Correlación de las variables en estudio con {variable}")
    plt.ylabel('Coeficiente de correlación en valor absoluto')
    plt.xlabel('Variables en estudio')
    


def doble_barplot(x, y1, y2, hue, figsize, data):
    """Esta función configura dos gráficos de barras con un mismo valor de x con hue"""
    fig, ax = plt.subplots(1,2, figsize=figsize)
    sns.barplot(data=data, x=x, y=y1, hue=hue, palette="husl", ax=ax[0])
    sns.barplot(data=data, x=x, y=y2, hue=hue, palette="husl", ax=ax[1])

def line_count(x1, x2, y, hue, figsize, data):
    """Esta función configura una lineplot y un countplot con mismo hue para hacer una comparativa"""
    fig, ax = plt.subplots(1,2, figsize=figsize)
    sns.lineplot(data=data, x=x1, y=y, hue=hue, ax=ax[0])
    sns.countplot(data=data, x=x2, hue =hue, ax=ax[1])



def multi_subplot(data):
    """Esta función está adaptada únicamente al proyecto por su extensión. Es decir, llamará directamente
    a las variables que ya se encuentran dentro del archivo main. Esta función se utiliza para mostrar
    una gran cantidad de subplots que reflejan valores del DataFrame limpio."""

    fig, ax = plt.subplots(3,3, figsize=(22,11))
    sns.set(palette="husl")
    sns.barplot(data=data, x="age", y="studytime", hue="sex", ax=ax[0,0])
    sns.barplot(data=data, x="age", y="goout", hue="sex", ax=ax[0,1])
    sns.barplot(data=data, x="age", y="absences", hue="sex", ax=ax[0,2])
    sns.countplot(data=data, x="paid", hue ="sex", ax=ax[1,0])
    sns.countplot(data=data, x="activities", hue ="sex", ax=ax[1,1])
    sns.countplot(data=data, x="romantic", hue ="sex", ax=ax[1,2])
    sns.countplot(data=data, x="internet", hue ="sex", ax=ax[2,0])
    sns.countplot(data=data, x="schoolsup", hue ="sex", ax=ax[2,1])
    sns.countplot(data=data, x="nursery", hue ="sex", ax=ax[2,2])

def pie_chart(data):
    """Esta función configura un 'piechart' para el Series que le pasamos"""
    plt.figure(1, figsize=(24,12))
    labels = data.keys()
    a = plt.pie(data, labels=labels, autopct='%.0f%%', radius=0.7, textprops= {"weight":"bold"})
    return a