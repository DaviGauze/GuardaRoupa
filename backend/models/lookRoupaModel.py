from sqlalchemy import Column, Integer, String, ForeignKey
from backend.banco import Base

class lookRoupa(Base):
    __tablename__ = "look_roupa"

    id_look = Column(
        Integer,
        ForeignKey("look.id_look"),
        primary_key=True,
        index=True
    )
    id_roupa = Column(
        Integer,
        ForeignKey("roupa.id_roupa"),
        primary_key=True,
        index=True
    )