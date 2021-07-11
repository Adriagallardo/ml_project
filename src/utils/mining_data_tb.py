#Este archivo tiene las funciones asociadas al data wrangling que elaboramos en el proyecto.
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import tensorflow as tf
import pandas as pd


def delete_corrupted_images(folders, folders_dir):
    """Esta función borra imágenes corruptas dentro de un dataset compuesta por subsets correspondientes a carpetas que contienen agrupaciones de imágenes."""
    
    num_skipped = 0
    for folder_name in folders:
        folder_path = os.path.join(folders_dir, folder_name)
        for fname in os.listdir(folder_path):
            fpath = os.path.join(folder_path, fname)
            try:
                fobj = open(fpath, "rb")
                is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
            finally:
                fobj.close()

            if not is_jfif:
                num_skipped += 1
                os.remove(fpath)

    print(f"Borradas {num_skipped} imágenes")


def clas_dict_to_data_vis(report):
    """Esta función, a partir de un reporte en formato de diccionario. Genera un dataframe que retorna y crea una visualización para los datos del reporte"""

    df = pd.DataFrame(report).T[:-3]
    df.drop(df.columns[-1], axis=1, inplace=True)

    fig, axes = plt.subplots(1, 3, sharey=True, figsize=(15,5))

    for i, k in enumerate(df.columns):
        axes[i].set_title(k, fontsize=20)
        sns.barplot(y=df.index, x=df[k].values,data=df, color="dodgerblue", ax=axes[i])


    plt.savefig(".." + os.sep + "reports" + os.sep + "from_main" + os.sep + "images" + os.sep + "classification_report.jpg")
    plt.show()
            
    return df