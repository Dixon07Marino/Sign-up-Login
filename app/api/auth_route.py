from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.models.users import UserRegister, MessageRegister, TokenResponse
from app.services.auth_service import register_user_service, login_user_service, validate_token

router = APIRouter()

auth_context = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

#Registrar usuario
@router.post("/register", response_model=MessageRegister)
async def register(user: UserRegister):
    return register_user_service(user)

#Loguear usuario
@router.post("/login", response_model=TokenResponse)
async def login(user: UserRegister):
    return login_user_service(user)

#Ruta protegida para usar token
@router.get("/protected", response_model=MessageRegister)
async def protected(token: str = Depends(auth_context)):
    return validate_token(token)