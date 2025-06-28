import mysql.connector, os
from dotenv import load_dotenv

#Verificar que las vars existan
load_dotenv()
vars_needed = ["DB_HOST", "DB_PASSWORD", "DB_NAME", "DB_USER"]
vars_missing = [var for var in vars_needed if not os.getenv(var)]

if vars_missing:
    raise Exception(f"Faltan vars de entorno: {vars_missing}")

#Crear conexion a la bd mysql
def connect_db():
    conection = mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        database = os.getenv("DB_NAME"),
        password = os.getenv("DB_PASSWORD"),
        user = os.getenv("DB_USER")
    )
    return conection