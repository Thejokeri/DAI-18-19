__author__ = "Fernando Talavera"
__name__ = "Manejo de URLs"
__doc__ = """
Ejercicio para crear una aplicacion web dinamica que a partir de ciertos
parametros (GET) sea capaz de generar imagenes utilizando la funcion sobre 
el ejercicio el fractal de Mandelbrot.
"""

import time
import os
from mandelbrot import renderizaMandelbrot, renderizaMandelbrotBonito
from flask import Flask
from flask import request, redirect, url_for
from pathlib import Path

app = Flask(__name__)

contador_peticiones = 0

# x1, y1, x2, y2, ancho, iteraciones, nombreFicheroPNG
# http://0.0.0.0:8080/mandelbrot?x1=-1.0&y1=-1.0&x2=1.0&y2=1.0&ancho=300

@app.route('/mandelbrot')
def prog():  
    clean_cache()
    x1 = request.args.get('x1')         # x1
    y1 = request.args.get('y1')         # y1
    x2 = request.args.get('x2')         # x2
    y2 = request.args.get('y2')         # y2
    ancho = request.args.get('ancho')   # ancho
    
    archivo = "fractal" + "_x1" + str(x1) + "_y1" + str(y1) + "_x2" + str(x2) + "_y2" + str(y2) + "_a" + str(ancho) + ".png"
    url = 'http://0.0.0.0:8080/png/' + archivo
    
    my_file = Path('./static/imagenes/fractales/archivo')

    if not my_file.exists():
        renderizaMandelbrot(float(x1), float(y1), float(x2), float(y2), int(ancho), 100, './static/imagenes/fractales/' + archivo)
    
    return redirect(url, code=302)
    

# http://0.0.0.0:8080/mandelbrotpaleta?x1=-1.0&y1=-1.0&x2=1.0&y2=1.0&ancho=300&r1=123&g1=255&b1=125&r2=175&g2=185&b2=150&r3=222&g3=34&b3=107&n=3

@app.route('/mandelbrotpaleta')
def prog1():
    clean_cache()
    x1 = request.args.get('x1')             # x1
    y1 = request.args.get('y1')             # y1
    x2 = request.args.get('x2')             # x2
    y2 = request.args.get('y2')             # y2
    ancho = request.args.get('ancho')       # ancho
    r1 = request.args.get('r1')             # r1
    g1 = request.args.get('g1')             # g1
    b1 = request.args.get('b1')             # b1
    r2 = request.args.get('r2')             # r2
    g2 = request.args.get('g2')             # g2
    b2 = request.args.get('b2')             # b2
    r3 = request.args.get('r3')             # r3
    g3 = request.args.get('g3')             # g3
    b3 = request.args.get('b3')             # b3
    n = request.args.get('n')               # n

    paleta = [(int(r1), int(g1), int(b1)), 
              (int(r2), int(g2), int(b2)),
              (int(r3), int(g3), int(b3))]

    archivo = "fractalb" + "_x1" + str(x1) + "_y1" + str(y1) + "_x2" + str(x2) + "_y2" + str(y2) + "_a" + str(ancho) + "_" + str(r1) + str(g1) + str(b1) + "_" + str(r2) + str(b2) + str(g2) + "_" + str(r3) + str(g3) + str(b3) + ".png"
    url = 'http://0.0.0.0:8080/png/' + archivo
    
    my_file = Path('./static/imagenes/fractales/archivo')

    if not my_file.exists():
        renderizaMandelbrotBonito(float(x1), float(y1), float(x2), float(y2), int(ancho), 100, './static/imagenes/fractales/' + archivo, paleta, int(n))
    
    return redirect(url, code=302)

@app.route('/png/<archivo>', methods=['GET'])
def png(archivo):
    return """
    <html>
        <body>
            <h1>Fractal</h1>
            <img src="/static/imagenes/fractales/"""+ archivo +"""">
        </body>
    </html>
    """

def clean_cache():
    global contador_peticiones

    if contador_peticiones > 10:
        contador_peticiones = 0
        ahora = time.time()
        
        path = "./static/imagenes/fractales/"
        for f in os.listdir(path):
            f = os.path.join(path,f)

            if os.stat(f).st_mtime < ahora - 1 * 86400:
                if os.path.isfile(f):
                    os.remove(f)
    else:
        contador_peticiones = contador_peticiones + 1
        print(str(contador_peticiones))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)