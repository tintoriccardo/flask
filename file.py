
from flask import Flask, render_template, request, redirect, url_for

from models import db,ListaSpesa

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db' #definisce l'URI per il database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #disabilita il monitoraggio delle modifiche sugli oggetti del database

db.init_app(app)#è un metodo che crea le tabelle 
with app.app_context():
    db.create_all()

lista_spesa = []

@app.route('/')
def home():
    lista_spesa = ListaSpesa.query.all()
    return render_template('home.html', lista=lista_spesa)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista_spesa.append(elemento)
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista_spesa):
        lista_spesa.pop(indice)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
