from flask import Flask
from dotenv import load_dotenv
from . import config

# Charge les variables d'environnement depuis le fichier .env
load_dotenv()

app = Flask(__name__)

# On remplit la configuration de Flask avec les variables de config.py
app.config['DB_HOST'] = config.DB_HOST
app.config['DB_USER'] = config.DB_USER
app.config['DB_PASSWORD'] = config.DB_PASSWORD
app.config['DB_NAME'] = config.DB_NAME

# On importe les routes (le contrôleur) à la fin pour les enregistrer sur l'objet app
# On utilise un import local ici pour éviter les imports circulaires
from .controller import app as routes_controller