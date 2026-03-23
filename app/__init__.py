from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    # Charge les variables d'environnement depuis le fichier .env
    load_dotenv()

    app = Flask(__name__)
    # Charge la configuration depuis l'objet Config dans config.py
    app.config.from_object('config.Config')

    # Enregistre les Blueprints ici
    # Importation locale pour éviter les problèmes d'importation circulaire
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Vous pouvez également initialiser d'autres extensions ici
    # Par exemple, si vous utilisez SQLAlchemy, vous l'initialiseriez ici

    return app