__author__ = "Fernando Talavera"
__name__ = "Hello world"
__doc__ = """
En la pagina web oficial de Flask podemos encontrar un ejemplo minimalista
("Hola Mundo") en el que se utiliza el framework para crear un aplicacion
web extremadamente sencilla que saluda al usuario. Copie dicho codigo, ejecutelo,
compruebe que funciona e intente entender cada parte de dicho programa.
Es posible que necesite consultar la API o el "Libro de Recetas" de la
biblioteca.

Para entrar en debug:
export FLASK_ENV=development
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)