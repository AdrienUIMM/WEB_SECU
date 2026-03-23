from flask import Blueprint, render_template, current_app
from .db import get_db_connection

# Crée un Blueprint pour les routes principales
main = Blueprint('main', __name__)

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

    # Idéalement, vous utiliseriez un template Jinja2 ici:
    # return render_template("artistes.html", artistes=artistes)
    html = "<h1>Liste des artistes</h1><ul>"
    for a in artistes:
        html += f"<li>{a['nom']}</li>"
    html += "</ul>"
    return html