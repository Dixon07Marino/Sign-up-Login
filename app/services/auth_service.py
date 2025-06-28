from app.repository.user_repository import insert_user, get_user_by_email
from app.core.security import hash_password, verify_password
from app.core.auth import generate_token, decode_token
from app.models.users import UserRegister
from fastapi import HTTPException

def register_user_service(user: UserRegister) -> dict:
    try:
        hashed_pwd = hash_password(user.password)
        msg = insert_user(user.email, hashed_pwd)
        if "err" in msg:
            raise HTTPException(status_code=400, detail=msg["err"])
        return msg
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno al registrar usuario: {e}")

def login_user_service(user: UserRegister) -> dict:
    try:
        data = get_user_by_email(user.email)
        if not data:
            raise HTTPException(status_code=404, detail="El usuario no existe")
        if not verify_password(user.password, data["password"]):
            raise HTTPException(status_code=400, detail="Password invalida")
        token = generate_token(data["id"])
        return {"msg": "Has iniciado sesion exitosamente", "token": token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=F"Error interno al registrar usuario: {e}")

def validate_token(token: str) -> dict:
    try:
        payload = decode_token(token)
        if not payload["id"]:
            raise HTTPException(status_code=401, detail="Token no existe")
        return {"msg": f"Usuario con id: {payload["id"]} tiene acceso a la app"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno al validar token: {e}")