from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    email: EmailStr
    password: str

class MessageRegister(BaseModel):
    msg: str

class TokenResponse(BaseModel):
    msg: str
    token: str