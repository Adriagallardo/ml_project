#Este archivo contiene las funciones de visualización (pandas, matplolib y seaborn) que elaboramos en el proyecto.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn.palettes import color_palette
import squarify as sq
import os
import matplotlib.image as mpimg

def sns_gstyle():
    """Esta función cambia los gráficos de seaborn que vienen por defecto"""
    sns.set(style="ticks")
   

def pie_chart(data):
    """Esta función configura un 'piechart' para el Series que le pasamos"""
    plt.figure(1, figsize=(24,12))
    labels = data.keys()
    a = plt.pie(data, labels=labels, autopct='%.0f%%', radius=0.7, textprops= {"weight":"bold"})
    return a

def visualize_countplot(x,y,xlabel,ylabel,title,jpgname):
    """Esta función genera una visualización de conteo de Y para X, en barras."""
    sns.barplot(x=x, y=y, color="deepskyblue")
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(rotation=50)
    plt.savefig(".." + os.sep + "reports" + os.sep + "from_main" + os.sep + "images" + os.sep + jpgname + ".jpg")

def imageset_intro_vis(download_folders, ds_path):
    """Esta función genera una visualización que representa una imagen ejemplo de cada label para el dataset que se está trabajando."""

    image_indexes = [1]
    selected_image_file_paths = dict()

    for classification in download_folders:
        image_directory = os.path.join(ds_path, classification)
        image_file_names = os.listdir(image_directory)
        selected_image_file_paths[classification] = [os.path.join(image_directory, image_file_names[i]) for i in image_indexes]
    plt.figure(figsize=(8,16))
    
        
    for i,classification in enumerate(download_folders):
        for j,image in enumerate(selected_image_file_paths[classification]):
            image_number = (i * len(image_indexes)) + j + 1
            ax = plt.subplot(10,3,image_number)
            plt.title(classification)
            plt.axis("off")
            plt.imshow(mpimg.imread(image))
    
    plt.savefig(".." + os.sep + "reports" + os.sep + "from_main" + os.sep + "images" + os.sep + "image_label_example.jpg")

def labels_intro_vis(download_folders, training):
    """Esta función muestra por pantalla un ejemplo de como se organizan los labels en tensorflow, por visualización"""

    plt.figure(figsize=(10, 10))
    for images, labels in training.take(1):
        for i in range(9):
            for t, classification in enumerate(download_folders):
                ax = plt.subplot(3, 3, i + 1)
                plt.imshow(images[i].numpy().astype("uint8"))
                plt.title(str(labels.numpy()[i]))
                plt.axis("off")
    plt.savefig(".." + os.sep + "reports" + os.sep + "from_main" + os.sep + "images" + os.sep + "onehot_labels_example.jpg")

def accuracy_evolution_vis(model_history):
    """Esta función muestra una visualización de la evolución de la precisión y del loss, de entrenamiento y validación, a lo largo de las épocas."""
    
    acc = model_history.history['accuracy']
    val_acc = model_history.history['val_accuracy']
    loss = model_history.history['loss']
    val_loss = model_history.history['val_loss']
    epochs_range = range(len(acc))

    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')
    plt.subplot(2, 1, 2)
    
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()

    plt.savefig(".." + os.sep + "reports" + os.sep + "from_main" + os.sep + "images" + os.sep + "accuracy_evolution.jpg")