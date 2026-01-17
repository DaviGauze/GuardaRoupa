from sqlalchemy import Column, Integer, String, DateTime
from backend.banco import Base

class imagem(Base):
    __tablename__ = "imagens"

    id_imagem = Column(Integer, primary_key=True, index=True)
    nome_imagem = Column(String(100), nullable=False)
    caminho = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=True)
    data_upload = Column(DateTime)
