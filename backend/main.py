from typing import Union
from fastapi import FastAPI 
from pydantic import BaseModel


app = FastAPI() 

usuario = ()

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str  

class UsuarioResponse(BaseModel):
    id_usuario: int
    nome: str
    email: str
    data_criacao: str

class ImagemCreate(BaseModel):
    nome_imagem: str
    caminho: str
    descricao: str

class ImagemResponse(BaseModel):
    id_imagem: int
    nome_imagem: str
    caminho: str
    descricao: str
    data_upload: str

class ParteCorpo(BaseModel):
    id_parte_corpo: int
    nome_parte_corpo: str

class TipoPecaCreate(BaseModel):
    nome_tipo_peca: str
    parte_corpo_id: int

class TipoPecaResponse(BaseModel):
    id_tipo_peca: int
    nome_tipo_peca: str
    parte_corpo_id: int

class CategoriaRoupa(BaseModel):
    id_categoria: int
    nome_categoria: str

class Estacao (BaseModel):
    id_estacao: int
    nome_estacao: str

class Ocasiao(BaseModel):
    id_ocasiao: int
    nome_ocasiao: str

class RoupaCreate(BaseModel):
    id_usuario: int
    nome: str
    tipo_peca_id: int
    categoria_id: int
    cor: str
    estacao_id: int
    imagem_id: int
    ocasiao_id: int

class RoupaResponse(BaseModel):
    id_roupa: int
    id_usuario: int
    nome: str
    tipo_peca_id: int
    categoria_id: int
    cor: str
    estacao_id: int
    imagem_id: int
    ocasiao_id: int
    data_adicao: str

class LookCreate(BaseModel):
    nome_look: str
    descricao: str
    ocasiao_id: int
    imagem_id: int

class LookResponse(BaseModel):
    id_look: int
    id_usuario: int
    nome_look: str
    descricao: str
    ocasiao_id: int
    imagem_id: int
    data_criacao: str

class LookRoupaCreate (BaseModel):
    id_look: int
    id_roupa: int

class FavoritoCreate(BaseModel):
    id_look: int

class FavoritoResponse(BaseModel):
    id_favorito: int
    id_usuario: int
    id_look: int
    data_favorito: str
    

@app.get("/")
def read_root():
    return{"Hello": "World!"}

@app.get("/usuario/{id_usuario}")
def read_usuario(id_usuario: int):
    return{"id_usuario": id_usuario}

@app.post("/usuario/")
def create_usuario(user: Usuario):
    return user

@app.get("/roupa/{id_roupa}")
def read_roupa(id_roupa: int):
    return{"id_roupa": id_roupa}

@app.post("/roupa/")
def create_roupa(roupa: roupa):
    return roupa