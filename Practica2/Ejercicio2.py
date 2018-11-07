__author__ = "Fernando Talavera"
__name__ = "Hello world con imagen y estilo"
__doc__ = """
Averigüe el mecanismo mas habitual que ofrece Flask para servir contenidos
estaticos tales como imagenes u hojas de estilo. A~nada algunas imagenes
estaticas a su aplicacion y compruebe que el cliente es capaz de acceder a ellas
directamente a traves de una URL.
Aunque el metodo habitual para servir paginas web de Flask es el uso de
templates, modique el ejemplo original del punto anterior para generar en vez
de simplemente el codigo Hola Mundo!, generar codigo HTML correcto en el que
se incluya, entre los demas elementos necesarios, una pagina de estilo CSS y
alguna imagen estatica.
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def f():
    return '''
    <html>
        <head>
            <title>Ejercicio 2</title>
            <link href="./static/style.css" rel="stylesheet" type="type/css" />
        </head>
        <body>
            <h1> Hello world!!! </h1>
            <img src="./static/imagenes/meme.jpg">
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)