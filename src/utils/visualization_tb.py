#Este archivo contiene las funciones de visualización (pandas, matplolib y seaborn) que elaboramos en el proyecto.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import matplotlib.image as mpimg
import random

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
    """Esta función genera una visualización de conteo de Y para X, en barras horizontalmente."""
    plt.figure(figsize=(10, 10))
    sns.barplot(x=y, y=x, color="lightsteelblue")
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.savefig(".." + os.sep + "reports" + os.sep + "from_main" + os.sep + "images" + os.sep + jpgname + ".jpg")

def imageset_intro_vis(download_folders, ds_path):
    """Esta función genera una visualización que representa una imagen ejemplo de cada label para el dataset que se está trabajando."""

    image_indexes = [1]
    selected_image_file_paths = dict()

    for classification in download_folders:
        image_directory = os.path.join(ds_path, classification)
        image_file_names = os.listdir(image_directory)
        selected_image_file_paths[classification] = [os.path.join(image_directory, image_file_names[i]) for i in image_indexes]
    plt.figure(figsize=(10,12))
    
        
    for i,classification in enumerate(download_folders):
        for j,image in enumerate(selected_image_file_paths[classification]):
            image_number = (i * len(image_indexes)) + j + 1
            ax = plt.subplot(4,3,image_number)
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
    plt.subplot(2, 1, 2)
    
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.xlabel("Épocas")

    plt.savefig(".." + os.sep + "reports" + os.sep + "from_main" + os.sep + "images" + os.sep + "accuracy_evolution.jpg")
    plt.show()

def real_pred_samples(test, predictions, model):
    """Esta función imprime por pantalla resultados de predicción de imágenes a partir de un conjunto de test y unos resultados de predicción,
    ambos en formato tensor, y pasando también el modelo."""

    """En esta sección se definen las clases"""
    test_dir = ".." + os.sep + "data" + os.sep + "test"
    decoded_labels = os.listdir(test_dir)

    """En esta sección creamos aleatoriedad para el muestreo de imágenes"""
    a = random.randint(0,10)

    rand_batch = []

    for i in range(15):
        rand_batch.append(random.randint(0,84))

    """En esta sección se imprime la visualización"""

    plt.figure(figsize=(13, 10))
    plt.suptitle("Resultado real"+"\n"+"Resultado predicho", fontsize=(20))
    #"\n"+"Resultado predicho"
    for i, j in enumerate(rand_batch):
        for images, labels in test.take(j):
            ax = plt.subplot(3, 5, i + 1)
            plt.imshow(images[a].numpy().astype("uint8"))
            random_predictions = model.predict(images)
            plt.title(decoded_labels[np.argmax(labels[a].numpy())] + "\n" + decoded_labels[np.argmax(random_predictions[a])])
            
            plt.axis("off")

    plt.savefig(".." + os.sep + "reports" + os.sep + "from_main" + os.sep + "images" + os.sep + "real_pred_samples.jpg")

def plot_confusion_matrix(cm, subset):
    "Esta función imprime por pantalla una visualización de una matriz de confusión en formato heatmap. 'cm' es el parámetro correspondiente con la matriz y subset son los niveles con los que clasificamos la matriz"

    # create figure
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 8))

    # plot heatmap - adjust font and label size
    sns.set(font_scale=1.0) 
    sns.heatmap(cm, annot=True, annot_kws={"size": 14}, fmt='d', ax=axes, vmin=0, vmax=100, cmap="Blues",xticklabels=subset, yticklabels=subset)
    plt.xlabel("Etiqueta de predicción")
    plt.ylabel("Etiqueta real")
    plt.savefig(".." + os.sep + "reports" + os.sep + "from_main" + os.sep + "images" + os.sep + "confusion_matrix.jpg")
    plt.show()