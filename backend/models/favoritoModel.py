from sqlalchemy import Column, Integer, String, DateTime
from backend.banco import Base

class favoritos(Base):
    __tablename__ = "favoritos"

    id_favorito = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(
        Integer,
        ForeignKey("usuario.id_usuario"),
        nullable=False
    )
    id_look = Column(
        Integer,
        ForeignKey("look.id_look"),
        nullable=False
    )
    data_favorito = Column(DateTime, nullable=False)


    