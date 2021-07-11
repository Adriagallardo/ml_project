import tensorflow as tf
import os
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
import numpy as np



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
    model = tf.keras.models.load_model(path)
    return model

def generate_confusion_matrix(test, model):
    "Esta función genera una matriz de confusión a partir de un dataset de test y el modelo entrenado"
    
    predictions = model.predict(test)
    predicted_categories = tf.argmax(predictions, axis=1)
    
    true_categories = tf.argmax(tf.concat([tf.cast(y, tf.int64) for x, y in test], axis=0), axis=1)
    
    matrix = confusion_matrix(true_categories, predicted_categories)
    print(matrix)

    return matrix, true_categories, predicted_categories

def single_predictions(model):
    "Esta función genera predicciones individuales sobre el modelo señalado pasando imágenes 64x64"

    test_dir = ".." + os.sep + "data" + os.sep + "test"
    
    test_ds = tf.keras.preprocessing.image_dataset_from_directory(
        test_dir,
        shuffle=False,
        image_size=(64, 64),
        color_mode="rgb"
    )

def create_test_and_train(train, test):
    """Esta función separa los splits de train y test de un tensorflow.dataset para trabajar con modelos que no sean de deeplearning"""

    """Se está trabajando con metadata de tensorflow, para trabajar con otros modelos, es necesario extraer 'y' y 'X' de los modelos de data de tensorflow. Las Y están   en formato one-hot encoding, por lo que hay que pasar la función argmax para utilizar las dimensiones deseadas."""

    X_train = np.concatenate([x for x, y in train], axis=0)
    y_train = np.argmax(np.concatenate([y for x, y in train], axis=0),axis=1)

    X_test = np.concatenate([x for x, y in test], axis=0)
    y_test = np.argmax(np.concatenate([y for x, y in test], axis=0),axis=1)

    X_train = X_train.reshape(X_train.shape[0],X_train.shape[1]*X_train.shape[2]*X_train.shape[3])
    X_test = X_test.reshape(X_test.shape[0],X_test.shape[1]*X_test.shape[2]*X_test.shape[3])


    return X_train, y_train, X_test, y_test

def scale_X(train,test):
    """Esta función escala los valores de X de los conjuntos que se le pasan"""

    Xscaler = preprocessing.StandardScaler().fit(train)
    scaler = preprocessing.StandardScaler().fit(test)
    
    X_train_scaled = Xscaler.transform(train)
    X_test_scaled = scaler.transform(test)

    return X_train_scaled, X_test_scaled
