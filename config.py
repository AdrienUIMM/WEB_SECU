import os

class Config:
    # Clé secrète pour la sécurité des sessions Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une_cle_secrete_par_defaut_peu_sure'
    # Paramètres de connexion à la base de données
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_USER = os.environ.get('DB_USER') or 'root'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'uimm'
    DB_NAME = os.environ.get('DB_NAME') or 'Tourneur'