from flask import Flask, request, render_template
import os, sys
import argparse

#Para correr este archivo es necesario abrir el cmd y aplicar la ruta a este archivo.
#A continuación se ejecuta el comando server.py -x 8642 y cogemos la ruta http que se indica.
#Seguidamente seguimos las instrucciones que indica la página. La contraseña es M21755015


# ---------- Append de ruta ----------
"""Con este comando de 5 líneas añadimos al archivo la ruta a la carpeta src, que contiene utils.
que nos valdrá para importar las funciones que utilizaremos para generar la API."""

if __name__ == '__main__':
    dir = os.path.dirname
    src_path = dir(dir(__file__))
    print(src_path)
    sys.path.append(src_path)

    import utils.api_tb as api
    from utils.folders_tb import read_json
   
# ---------- Llamada función de requisito de argumento ----------
api.argparse_password()


app = Flask(__name__)   

# ---------- Funciones flask ----------

@app.route("/")  
def home():
    return "Hola, para acceder a los datos, añada el endpoint /get_token?password= y escriba la contraseña"

@app.route("/get_token", methods=["GET"])
def get_token():
    print("Escribe a continuación la contraseña para acceder al archivo .json")
    x = request.args["password"]
    if x == "M21755015":
        return read_json("../../data/cleaned_data.json")
    else:
        return "No es la contraseña correcta"


# ---------- Llamada función inicio ----------
if __name__ == "__main__":
    api.main(main_path = dir(__file__), app=app)