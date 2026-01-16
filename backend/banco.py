from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends


DATABASE_URL = "postgresql://postgres:1205@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuario"
    
    id_usuario = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)

class Imagem(Base):
    __tablename__ = "imagem"
    
    id_imagem = Column(Integer, primary_key=True, index=True)
    nome_imagem = Column(String, nullable=False)
    caminho = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    data_upload = Column(DateTime, default=datetime.utcnow)