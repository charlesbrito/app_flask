from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST' ])
def ola_mundo():
    nome = "admin"
    senha = "admin"
    if request.method == "POST":
        if request.form.get('nome') == nome and request.form.get("senha") == senha:
            return render_template("boasvindas.html", nome=nome)
        else:
            return render_template("index.html")
    return render_template("inicio.html")

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        return f"<h2>Usuário: {nome} email: {email} cadastrado com sucesso!</h2>"
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)