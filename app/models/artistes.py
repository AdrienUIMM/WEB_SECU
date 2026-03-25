from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Artiste(Base):
    __tablename__ = "Artiste"

    id_artiste = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(40), nullable=False)
    prenom = Column(String(40), nullable=False)
    id_contrat = Column(Integer, ForeignKey('Contrats.id_contrat'), nullable=False)
    id_instrument = Column(Integer, ForeignKey('instrument.id_instrument'))
    id_groupe = Column(Integer, ForeignKey('Groupes.id_groupe'), nullable=False)

    instrument = relationship("Instrument", back_populates="artistes")