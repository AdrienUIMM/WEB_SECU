from sqlalchemy import Column, Integer, String, Date
from app.database.base import Base

class Contrat(Base):
    __tablename__ = "Contrats"

    id_contrat = Column(Integer, primary_key=True, autoincrement=True)
    formulaire = Column(String(1000), nullable=False)
    date_debut = Column(Date, nullable=False)
    date_fin = Column(Date)