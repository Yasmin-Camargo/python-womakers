"""
INSTALAÇÃO: 
    python3 -m venv .venv
    .\.venv\Scripts\activate
    pip install "fastapi[all]"
EXECUÇÃO: uvicorn app:app --reload
"""

from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("747329d5-91cc-44f8-8834-b50481e6f11b"), 
        first_name="Ana", 
        last_name="Maria", 
        email="email@gmail.com", 
        role=[Role.role_1]
    ),
    User(
        id=UUID("fea62e4f-13ee-40da-a803-ced05cf80318"), 
        first_name="Yasmin", 
        last_name="Camargo", 
        email="email@gmail.com", 
        role=[Role.role_2]
    ),
    User(
        id=UUID("539da8a9-4718-4afc-8b13-26ba4715c9f0"), 
        first_name="Camila", 
        last_name="Silva", 
        email="email@gmail.com", 
        role=[Role.role_3]
    ),
]

@app.get("/")
async def root():
    return {"message": "Olá WoMakers"}


@app.get("/api/users")
async def get_users():
    return db

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado"}

@app.post("/api/users")
async def add_user(user: User):
    """
    Adiciona um usuário na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    """
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o Id {id} não encontrado!"
    )