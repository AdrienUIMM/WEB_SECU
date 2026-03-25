from flask import render_template, request
from app.database.engine import SessionLocal
from ..db import get_db_connection
from sqlalchemy import select
from app.models.artistes import Artiste
from app.models.instrument import Instrument
from app.models.groupes import Groupe
from app.models.contrats import Contrat
from sqlalchemy.orm import joinedload
from app import app

@app.route("/")
def hello_world():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("select 1")
    output = cur.fetchone()
    cur.close()
    return "<p> Bonjour, World ! <p>"

@app.route("/artistes")
def artistes():
    conn = get_db_connection(dictionary_cursor=True)
    cur = conn.cursor()
    query = "SELECT nom FROM Artiste"
    cur.execute(query)
    artistes = cur.fetchall()
    cur.close()
    return render_template('artistes.html', artistes=artistes)

@app.route("/injection", methods=["GET", "POST"])
def injection():
    artists = None
    if request.method == "POST":
        query = request.form.get("query")
        conn = get_db_connection(dictionary_cursor=True)
        cursor = conn.cursor()
        # Utilisation de requêtes paramétrées pour la sécurité
        cursor.execute("SELECT * FROM artiste WHERE nom LIKE %s", (f"{query}",))
        result = cursor.fetchall()
        artists = [artist["nom"] for artist in result]
        cursor.close()
    return render_template("index.html", artists=artists)

@app.route("/join-alchemy", methods=["GET", "POST"])
def join_alchemy():
    result = []
    if request.method == "POST":
        query = request.form.get("query")
        with SessionLocal() as session:
            # Correction : Artiste.instrument au lieu de Artistes.instrument
            q = select(Artiste).options(joinedload(Artiste.instrument)).where(Artiste.nom.like(f"%{query}%"))
            result = session.execute(q).scalars().all()
    return render_template("join-alchemy.html", artistes=result)
