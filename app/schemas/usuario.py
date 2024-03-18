from pydantic import BaseModel
from pydantic import validator
import re


class Usuarios(BaseModel):
    id: int
    nome: str 
    email: str 
    senha: str
    sexo: str

    @validator('senha')
    def validate_senha(cls, value):
        if value <= 0:
            raise ValueError('Senha invalida')
        return value

    @validator('sexo')
    def validate_sexo(cls, value):
        if not re.match('^([a-z]|-|_)+$', value):
            raise ValueError('Sexo não encontrado')
        return value