from flask import render_template
from app import app 

@app.route('/')
def home():
    return "<b>There has been a change</b>"

@app.route('/template')
def template():
    return render_template('home.html')

@app.route('/hora')
def hora():
    from datetime import datetime
    return f'Data/Hora: {datetime.now()}'

@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1 = 12, n2 = 12):
    return f'Soma: {n1 + n2}'
