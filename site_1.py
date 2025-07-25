from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def ola_mundo():
    nome = "Charles"
    return render_template("index.html", nome=nome)