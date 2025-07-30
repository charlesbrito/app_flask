from flask import Flask, render_template, request, g, make_response
from database import models
from database.conexao import engine, SessionLocal
from sqlalchemy.orm import session
from typing import Annotated
from weasyprint import HTML

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = SessionLocal()
    return g.db
    
@app.teardown_appcontext
def fechar_conexao(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()




@app.route("/", methods=['GET', 'POST' ])
def ola_mundo():
    db = get_db()
    if request.method == "POST":
       nome = request.form.get('nome')
       senha = request.form.get('senha')

       usuario = db.query(models.Usuario).filter_by(nome=nome, senha=senha).first()
       if usuario:
           return render_template("formulario.html")
       else:
            return render_template("index.html")
        
    return render_template("inicio.html")

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    db = get_db()
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        cadastro = models.Usuario(
            nome = nome,
            email = email,
            senha = senha
        )
        db.add(cadastro)
        db.commit()


        return f"<h2>Usuário: {nome} email: {email} cadastrado com sucesso!</h2>"
    
    return render_template("index.html")


@app.route("/formulario", methods=['GET', 'POST'])
def gerar_formulario():
    if request.method == 'POST':
        comprador = request.form.get('comprador')
        produto = request.form.get('produto')
        quantidade = request.form.get('quantidade')
        valor_total = request.form.get("valor")
        data_compra = request.form.get('data')
        assinatura = request.form.get('assinatura')
        layout = render_template('layout.html', comprador=comprador, produto=produto, quantidade=quantidade, valor_total=valor_total, data_compra=data_compra, assinatura=assinatura)
        
        pdf = HTML(string=layout).write_pdf()

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=recibo.pdf'
        return response

    return render_template('formulario.html')


if __name__ == "__main__":
    app.run(debug=True)