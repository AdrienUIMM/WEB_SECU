from flask import Flask, render_template
import pymysql
from dotenv import load_dotenv

app = Flask(__name__)

@app.route("/")
def hello_world():
    conn = pymysql.connect(
        host='localhost',
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