#!/usr/bin/env python3
# import corpusmanager
import sqlite3
from flask import Flask, request, render_template

collegamento = sqlite3.connect("corpus.db")
cursore = collegamento.cursor()

cursore.execute("""
create table if not exists testi (
    nome text primary key,
    contenuti text
);""")

cursore.execute("""
create table if not exists etichette (
    testo text,
    etichetta text
);""")

def aggiungi_testo(nome: str, testo: str):
    nome = nome.replace('\'', '\'\'')
    testo = testo.replace('\'', '\'\'')
    cursore.execute(f"insert into testi values('{nome}', '{testo}')")
    collegamento.commit()

app = Flask(__name__)

dati = cursore.execute("select * from testi;").fetchall()
testi = {}
for i in dati:
    testi[i[0]] = i[1]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/gestiretesti')
def gestiretesti():
    return render_template("gestisci.html", nomi=testi.keys())

@app.route('/gestiretesti/<testo>')
def gestiretesto(testo):
    return render_template("gestisci.html", nomi=testi.keys(), contenuti=testi[testo].split('\n'))

if __name__ == "__main__":
    app.run(debug=True)

# corpus = corpusmanager.Corpus("la_lingua_italiana")
