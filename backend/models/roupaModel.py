from sqlalchemy import Column, Integer, String, DateTime
from backend.banco import Base

class Usuario(Base):
    __tablename__ = "roupa"

    id_roupa = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(
        Integer,
        ForeignKey("usuario.id_usuario"),
        nullable=False
    )
    nome = Column(String(100), nullable=False)
    tipo_peca = Column(
        Integer,
        ForeignKey("tipo_peca.id_tipo_peca"),
        nullable=False
    )
    categoria = Column(
        Integer,
        ForeignKey("categoria.id_categoria"),
        nullable=False
    )
    cor = Column(String(30), nullable=False)
    estacao = Column(
        Integer,
        ForeignKey("estacao.id_estacao"),
        nullable=False
    )
    caminho_imagem = Column(
        Integer,
        ForeignKey("imagem.id_imagem"),
        nullable=False
    )
    data_adicao = Column(DateTime)
