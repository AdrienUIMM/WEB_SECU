from flask import render_template, current_app, request
from ..db import get_db_connection
from app.database.engine import SessionLocal
from app.models.artistes import Artiste



@main.route("/")
def hello_world():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("select 1")
    output = cur.fetchone()
    print("sortie")
    print(output)
    cur.close()
    conn.close()
    return "<p> Bonjour, World ! <p>"

@main.route("/artistes")
def artistes():
    conn = get_db_connection(dictionary_cursor=True) # Utilise DictCursor pour des résultats sous forme de dictionnaires
    cur = conn.cursor()

    query = "SELECT nom FROM Artiste"
    cur.execute(query)
    artistes = cur.fetchall()

    cur.close()
    conn.close()
    # Note: Idéalement, utilisez un template ici aussi
    return render_template('artistes.html', artistes=artistes)

@main.route("/injection", methods=["GET", "POST"])
def show_artists():
    artists = None
    if request.method == "POST":
        query = request.form.get("query")
        # Utilisation de la connexion centralisée définie dans db.py
        conn = get_db_connection(dictionary_cursor=True)
        cursor = conn.cursor()
        # Requête paramétrée pour éviter les injections SQL (bonne pratique)
        cursor.execute("SELECT * FROM artiste WHERE nom LIKE %s", (f"{query}",))
        result = cursor.fetchall()
        artists = [artist["nom"] for artist in result]
        cursor.close()
        # Pas besoin de fermer conn ici, c'est géré par teardown_appcontext dans db.py
    
    return render_template("index.html", artists=artists)

@main.route("/sqlalchemy")
def sqlalchemy_artistes():
    session = SessionLocal()
    try:
        artistes = session.query(Artiste).all()
        return render_template('join-alchemy.html', artistes=artistes)
    finally:
        session.close()


