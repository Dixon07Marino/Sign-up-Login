from fastapi import FastAPI
from app.api import auth_route

app = FastAPI()

app.include_router(auth_route.router, prefix="/api/auth", tags=["Auth"])