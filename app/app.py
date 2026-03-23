from flask import Flask, render_template, request
import pymysql
from dotenv import load_dotenv


app = Flask(__name__)

@app.route("/")
def hello_world():
    conn = pymysql.connect(
        host= "localhost",
        user='root', 
        password = "uimm",
        db='Tourneur',
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
        db='Tourneur',
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