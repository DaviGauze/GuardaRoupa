from sqlalchemy import Column, Integer, String, ForeignKey
from backend.banco import Base

class ocasiao(Base):
    __tablename__ = "ocasiao"

    id_ocasiao = Column(Integer, primary_key=True, index=True)
    nome_ocasiao = Column(String(50), nullable=False)