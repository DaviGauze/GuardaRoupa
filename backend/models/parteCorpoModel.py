from sqlalchemy import Column, Integer, String, ForeignKey
from backend.banco import Base

class parteCorpo(Base):
    __tablename__ = "parte_corpo"

    id_parte_corpo = Column(Integer, primary_key=True, index=True)
    nome_parte_corpo = Column(String(50), nullable=False)