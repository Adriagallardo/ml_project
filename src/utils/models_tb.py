import tensorflow as tf
import os
from sklearn.metrics import confusion_matrix



def train_val_split_from_dir():
    """Esta función define, desde un directorio con subcarpetas, un split de entrenamiento y uno de validación para todas las imagenes contenidas.
    Los parámetros que se encuentran modificados dentro de las subfunciones están adaptados al proyecto. El argumento 'directory' es donde se encuentran
    las carpetas de test y train"""

    print("Conjunto de entrenamiento:")

    train_dir = ".." + os.sep + "data" + os.sep + "train"

    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        train_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(64, 64),
        batch_size=32,
        labels="inferred",
        label_mode="categorical",
        color_mode="rgb"
    )

    print("\nConjunto de validación:")

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        train_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(64, 64),
        batch_size=32,
        labels="inferred",
        label_mode="categorical",
        color_mode="rgb",
    )

    print("\nConjunto de test:")

    test_dir = ".." + os.sep + "data" + os.sep + "test"
    
    test_ds = tf.keras.preprocessing.image_dataset_from_directory(
        test_dir,
        shuffle=False,
        image_size=(64, 64),
        labels="inferred",
        label_mode="categorical",
        color_mode="rgb"
    )

    return train_ds, val_ds, test_ds

def save_model(path, model, model_filename):

    model.save(path + model_filename)
    print("El modelo ha sido guardado correctamente")

def load_model(path):
    model  = tf.keras.models.load_model(path)
    return model

def generate_confusion_matrix(test, model):
    "Esta función genera una matriz de confusión a partir de un dataset de test y el modelo entrenado"
    
    predictions = model.predict(test)
    predicted_categories = tf.argmax(predictions, axis=1)
    
    true_categories = tf.argmax(tf.concat([tf.cast(y, tf.int64) for x, y in test], axis=0), axis=1)
    
    matrix = confusion_matrix(true_categories, predicted_categories)
    print(matrix)

    return matrix, true_categories, predicted_categories

