from flask import Flask, render_template, request
import pymysql
from dotenv import load_dotenv
from app.database.engine import SessionLocal
from







app = Flask(__name__)

@app.route("/")
def hello_world():
    conn = pymysql.connect(
        host= "localhost",
        user='root', 
        password = "uimm",
        database='Tourneur',
        )
    
    cur = conn.cursor()
    cur.execute("select 1")
    output = cur.fetchone()
    print("sortie")
    print(output)
    return "<p> Bonjour, World ! <p>"


@app.route("/artistes")
def artistes():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password="uimm",
        database='Tourneur',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    cur = conn.cursor()

    query = "SELECT nom FROM Artiste"
    cur.execute(query)
    artistes = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('artistes.html', artistes=artistes)


@app.route("/injection", methods=["GET", "POST"])
def show_artists():
    artists = None
    if request.method == "POST":
        query = request.form.get("query")
        conn = pymysql.connect(
            user="root",
            password="uimm",
            host="localhost",  # ou le nom du service mysql/mariadb du docker-compose
            port=3306,
            database="tourneur")
        cursor = conn.cursor(dictionary=True)
        print(f"SELECT * FROM artiste WHERE nom LIKE '{query}'")
        # cursor.execute(f"SELECT * FROM artiste WHERE nom LIKE '{query}'")
        cursor.execute("SELECT * FROM artiste WHERE nom LIKE %s", (f"{query}",))
        result = cursor.fetchall()
        artists = [artist["nom"] for artist in result]
    return render_template("index.html", artists=artists)


@app.route("/artistes_easy")
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

@app.route("/injection", methods=["GET", "POST"])
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

@app.route("/sqlalchemy")
def sqlalchemy_artistes():
    session = SessionLocal()
    try:
        artistes = session.query(Artiste).all()
        return render_template('join-alchemy.html', artistes=artistes)
    finally:
        session.close()



