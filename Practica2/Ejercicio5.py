__author__ = "Fernando Talavera"
__name__ = "Manejo de URLs"
__doc__ = """
Desarrolle una aplicacion web sencilla que nos permita crear una imagen
SVG [5] dinamica (que cambie cada vez que visitemos la pagina) y aleatoria. Por
ejemplo, que cada vez que se visite la pagina dibuje elipses, rectangulos, etc. de
colores y posiciones distintas.
"""
from flask import Flask
from flask import redirect
import random

app = Flask(__name__)

salida = ""

@app.route('/')
def function():
    global salida

    x = random.randint(50,100)
    y = random.randint(50,100)
    rx = random.randint(10,80)
    ry = random.randint(10,80)

    width = random.randint(10,300)
    height = random.randint(10,300)

    sr = random.randint(0,255)
    sg = random.randint(0,255)
    sb = random.randint(0,255)

    stroke = "rgb("+ str(sr) + "," + str(sg) + "," + str(sb) + ")"

    fr = random.randint(0,255)
    fg = random.randint(0,255)
    fb = random.randint(0,255)

    fill = "rgb("+ str(fr) + "," + str(fg) + "," + str(fb) + ")"

    figura = random.randint(0,1)

    url = 'http://0.0.0.0:8080/svg/'

    if figura == 0:
        salida = '<rect x="' + str(x) + '" y="' + str(y) + '" width="' + str(width) + '" height="' + str(height) + '" style="stroke:' + stroke + ';fill:' + fill + '"> </rect>'
    else:
        salida = '<ellipse cx="' + str(x) + '" cy="' + str(y) + '" rx="' + str(rx) + '" ry="' + str(ry) + '" width="' + str(width) + '" height="' + str(height) + '" style="stroke:' + stroke + ';fill:' + fill + '"> </ellipse>'
        
    return redirect(url, code=302)

    
@app.route('/svg/')
def svg():
    print(salida)
    return """
    <html>
        <head>
        </head>
        <body>
            <h1>SVG</h1>
            <svg width="1000" height="1000"> """ + salida + """ </svg>
        </body>
    </html>
    """
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)