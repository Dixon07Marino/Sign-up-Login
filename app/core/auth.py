from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import jwt, os

#llave secreta
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise Exception(f"Falta llave secreta")

#Generar token
def generate_token(id_user: int) -> str:
    payload = {
        "id": id_user,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms="HS256")
    except jwt.ExpiredSignatureError:
        raise Exception("El token ha expirado")
    except jwt.InvalidTokenError:
        raise Exception("El token es invalido")
    