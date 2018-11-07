__author__ = "Fernando Talavera"
__name__ = "Práctica 4"

from flask import Flask, render_template, session, redirect, url_for, escape, request
import pymongo

app = Flask(__name__, template_folder='./templates/')

conn = pymongo.MongoClient()

restaurants = conn['test'].restaurants

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta', methods=['GET','POST'])
def consulta():
    nombre = request.form['restaurante']
    lista = list(restaurants.find({"name": {'$regex': '^' + nombre}}))
        
    if not lista:
        return render_template('find.html', noresult = True)
    else:
        return render_template('find.html', rows = lista)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)