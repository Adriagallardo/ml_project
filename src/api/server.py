from flask import Flask, request, render_template
import os, sys
import argparse
import pandas as pd

#Para correr este archivo es necesario abrir el cmd y aplicar la ruta a este archivo.
#A continuación se ejecuta el comando server.py -x 8642 y cogemos la ruta http que se indica.
#Seguidamente seguimos las instrucciones que indica la página. La contraseña es M21755015


# ---------- Append de ruta ----------
"""Con este comando de 5 líneas añadimos al archivo la ruta a la carpeta src, que contiene utils.
que nos valdrá para importar las funciones que utilizaremos para generar la API."""

if __name__ == '__main__':
    dir = os.path.dirname

    src_path = dir(dir(os.path.abspath(__file__)))
    print(src_path)
    sys.path.append(src_path)

    upper_path = dir(dir(dir(os.path.abspath(__file__))))
    sys.path.append(upper_path)

    import utils.api_tb as api
    from utils.folders_tb import read_json
    from utils.mysql_tb import MySQL, connect_mysql
   
# ---------- Llamada función de requisito de argumento ----------
api.argparse_password()


app = Flask(__name__)   

# ---------- Funciones flask ----------

@app.route("/")  
def home():
    return "Hola, para acceder a los datos, añada el endpoint /get_token?password= y escriba la contraseña. También puede añadir el endpoint /get_token_2?password=subir para subir el Dataframe a la base de datos especificada"

@app.route("/get_token", methods=["GET"])
def get_token():
    print("Escriba a continuación la contraseña para acceder al archivo .json que corresponde con la metadata")
    S = request.args["password"]
    if S == "M21755015":
        return read_json("metadata.json")
    else:
        return "No es la contraseña correcta"


@app.route("/get_token_2", methods=["GET"])
def data_mysql():
    print("Escriba a continuación la contraseña para acceder al archivo .json que corresponde con subir la metadata")
    z = request.args["password"]
    
    json_dict = read_json("metadata.json")
    data = pd.DataFrame(json_dict)

    print(data)

    if z == "subir":
        print(data)
        db_connection = connect_mysql(IP_DNS="consciencesai.com", USER="21755015m", PASSWORD="adriagallardo96", BD_NAME="21755015m_ds_april_2021_db", PORT=30001)
        data.to_sql(name="adria_gallardo_viñas", con=db_connection, if_exists="replace", index=False)
        
        return "\n\n\n Los metadatos se han subido al Database de MySQL correctamente"



# ---------- Llamada función inicio ----------
if __name__ == "__main__":
    api.main(main_path = dir(__file__), app=app)