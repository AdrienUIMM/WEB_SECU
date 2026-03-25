from app import app
from app.db import init_db_app # Importez la fonction pour enregistrer le teardown de la DB

init_db_app(app) # Enregistre la fonction de fermeture de la connexion DB

if __name__ == '__main__':
    app.run(debug=True)