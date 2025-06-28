from passlib.context import CryptContext

#Para lo relacionado a cifrar
pwd_context = CryptContext(schemes="bcrypt", deprecated="auto")

#Cifrar password
def hash_password(plain_pwd: str) -> str:
    return pwd_context.hash(plain_pwd)

#Verificar password

def verify_password(plain_pwd: str, hashed_pwd: str) -> bool:
    return pwd_context.verify(plain_pwd, hashed_pwd)