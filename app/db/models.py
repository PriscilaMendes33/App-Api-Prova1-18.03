from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, func
from sqlalchemy.orm import relationship
from db.base import Base




class Produtos(Base):
    __tablename__ = "produtos"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    item = Column('item', String, nullable=False)
    peso = Column('peso', Float)
    numero_caixas = Column('numero_caixas', Integer)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())
    
# class User(Base):
#     __tablename__ = 'users'
#     id = Column('id', Integer, primary_key=True, autoincrement=True)
#     username = Column('username', String, nullable=False, unique=True)
#     password = Column('password', String, nullable=False)

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column('id', Integer, primary_key=True, autoincrement=True)   
    nome = Column('nome', String,  nullable=False) 
    email = Column('email', String,  unique=True, nullable=False)  
    senha = Column('senha', String, nullable=False)
    sexo = Column('sexo', String, nullable=False )
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())