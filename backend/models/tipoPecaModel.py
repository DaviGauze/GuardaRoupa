from sqlalchemy import Column, Integer, String, ForeignKey
from backend.banco import Base

class TipoPeca(Base):
    __tablename__ = "tipo_peca"

    id_tipo_peca = Column(Integer, primary_key=True, index=True)
    nome_tipo_peca = Column(String(50), nullable=False)

    parte_corpo_id = Column(
        Integer,
        ForeignKey("parte_corpo.id_parte_corpo"),
        nullable=False
    )