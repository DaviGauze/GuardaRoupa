from sqlalchemy import Column, Integer, String, DateTime
from backend.banco import Base

class estacao(Base):
    __tablename__ = "estacao"

    id_categoria = Column(Integer, primary_key=True, index=True)
    nome_categoria = Column(String(50), nullable=False)