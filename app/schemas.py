from pydantic import BaseModel, EmailStr
from typing import Optional

# Quando a gente cria um usuário
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Quando a gente retorna info de usuário (não mostra senha)
class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True  # permite retornar direto do SQLAlchemy

        