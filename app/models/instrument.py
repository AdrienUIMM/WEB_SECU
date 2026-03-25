from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.base import Base

class Instrument(Base):
    __tablename__ = "instrument"

    id_instrument = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(40), nullable=False, unique=True)
    famille = Column(String(40), nullable=False, unique=False)
    poids = Column(Integer, nullable=False, unique=False)
    longueur = Column(Integer, nullable=False, unique=False)
    largeur = Column(Integer, nullable=False, unique=False) 
    hauteur = Column(Integer, nullable=False, unique=False)

    artistes = relationship("Artiste", back_populates="instrument")