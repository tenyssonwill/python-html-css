import sqlite3
from flask import Flask, request, session, g, redirect,\
	abort, render_template, flash

# CONFIGURACAO
DATABASE = 'blog.db'
SECRET_KEY = 'pudim'


app = Flask(__name__)
app.config.from_object(__name__)

def connectar_bd():
	return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def antes_requisicao():
	g.bd = connectar_bd()

@app.teardown_request
def depois_request(exc):
	g.bd.close()

@app.route('/')
def exibir_entradas():
	return render_template('exibir_entradas.html')

@app.route('/hello')
def pagina_inicial():
	return 'Hello World'