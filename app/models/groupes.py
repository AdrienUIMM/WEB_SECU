from sqlalchemy import Column, Integer, String, Date
from app.database.base import Base

class Groupe(Base):
    __tablename__ = "Groupes"

    id_groupe = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(40), nullable=False)
    date_creation = Column(Date)