#Este archivo tiene las funciones asociadas al data wrangling que elaboramos en el proyecto.
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import tensorflow as tf


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
