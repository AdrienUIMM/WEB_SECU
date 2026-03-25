from app.database.engine import engine
from app.database.base import Base

# IMPORTANT : importer les modèles
from app.models.artistes import Artiste
from app.models.instrument import Instrument
from app.models.groupes import Groupe
from app.models.contrats import Contrat

def init_db():
    Base.metadata.create_all(bind=engine)