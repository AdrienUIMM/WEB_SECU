import pymysql
import os
from flask import current_app, g

def get_db_connection(dictionary_cursor=False):
    """
    Établit et retourne une connexion à la base de données.
    La connexion est stockée dans l'objet 'g' de Flask pour être réutilisée
    pendant la durée de la requête.
    """
    if 'db_conn' not in g:
        cursor_class = pymysql.cursors.DictCursor if dictionary_cursor else pymysql.cursors.Cursor
        g.db_conn = pymysql.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            db=current_app.config['DB_NAME'],
            cursorclass=cursor_class
        )
    return g.db_conn

def close_db_connection(e=None):
    """Ferme la connexion à la base de données si elle existe."""
    db_conn = g.pop('db_conn', None)
    if db_conn is not None:
        db_conn.close()

def init_db_app(app):
    """
    Enregistre la fonction de fermeture de la connexion DB
    pour qu'elle soit appelée à la fin de chaque contexte d'application.
    """
    app.teardown_appcontext(close_db_connection)