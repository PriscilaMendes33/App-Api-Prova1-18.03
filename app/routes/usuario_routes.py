from fastapi import APIRouter, Response, Depends, status, Query
from sqlalchemy.orm import Session
from db.database import engine,SessionLocal
from db.models import Usuarios as UsuariosModel
from schemas.usuario import Usuarios as UsuariosOutput
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException
from db.base import Base
from db.models import Usuarios

Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/usuarios")

def get_db():
    try:
        db = SessionLocal()
        #TODO 
        yield db
    finally:
        db.close()
        

@router.post("/addComSchema", status_code=status.HTTP_201_CREATED, description='Adicionar Usuario')
def add_produto(request:UsuariosOutput, db: Session = Depends(get_db)):
        usuario_on_db = UsuariosModel(id=request.id, nome=request.nome, email=request.email, senha=request.senha, sexo=request.sexo)
        usuario_on_db = UsuariosModel(**request.dict())
        db.add(usuario_on_db)
        db.commit()
        return Response(status_code=status.HTTP_201_CREATED)  
    
@router.get("/{usuario_name}", description="Listar usuario pelo nome")
def get_usuarios(usuario_name,db: Session = Depends(get_db)):
    usuario_on_db= db.query(UsuariosModel).filter(UsuariosModel.item == usuario_name).first()
    return usuario_on_db
    

@router.get("/usuarios/listar")
async def get_usuarios(db: Session = Depends(get_db)):
    usuarios= db.query(UsuariosModel).all()
    return usuarios

@router.delete("/{id}", description="Deletar usuario pelo id")
def delete_usuario(id: int, db: Session = Depends(get_db)):


    usuario_on_db = db.query(UsuariosModel).filter(UsuariosModel.id == id).first()
    if usuario_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuario nao encontrado com este id')
    db.delete(usuario_on_db)
    db.commit()
    return f"Banco with id {id} deletado.", Response(status_code=status.HTTP_200_OK)


@router.put('/update/{id}', description='Update usuario')
def update_usuario(
    id: int,
    usuario: UsuariosOutput,
    db: Session = Depends(get_db)
    
    ):
    usuario_on_db = db.query(UsuariosModel).filter_by(id=id).first()
    if usuario_on_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Nenhum usuario foi encontrado com id fornecido')
        
    usuario_on_db.item = usuario.item
    usuario.peso = usuario.peso
    usuario.numero_caixas = usuario.numero_caixas
    
    db.add(usuario_on_db)
    db.commit()
    return "ok"