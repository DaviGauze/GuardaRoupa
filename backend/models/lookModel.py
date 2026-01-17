from sqlalchemy import Column, Integer, String, DateTime
from backend.banco import Base

class look(Base):
    __tablename__ = "look"

    id_look = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(
        Integer,
        ForeignKey("usuario.id_usuario"),
        nullable=False
    )
    nome_look = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=True)
    ocasiao_id = Column(
        Integer,
        ForeignKey("ocasiao.id_ocasiao"),
        nullable=False
    )
    caminho_imagem = Column(
        Integer,
        ForeignKey("imagem.id_imagem"),
        nullable=False
    )
    data_criacao = Column(datetime, nullable=False)