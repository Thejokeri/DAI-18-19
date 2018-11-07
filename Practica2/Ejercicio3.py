__author__ = "Fernando Talavera"
__name__ = "Manejo de URLs"
__doc__ = """
Averigue el mecanismo de Flask para el analisis y manejo de distintas URLs.
Cree una nueva aplicacion para servir paginas distintas dependiendo de la URL
introducida. Asimismo, sera conveniente ser capaces de obtener los parametros
de una llamada GET. Compruebe que puede utilizar variables en parte de la url
(por ejemplo, mostrar contenidos distintos para las siguientes urls:
http://<ip:puerto>/user/pepe
http://<ip:puerto>/user/zerjillo
http://<ip:puerto>/user/[cualquierUsuario]
Por ultimo, defina una pagina para el caso en que una URL no este definida
(error HTTP 404, not found [4]).
"""

from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>',methods=['GET'])
def profile(username):
    if username == "manolo":
        return "olonam"
    elif username == "zerjillo":
        return "ollijrez"
    else:
        return "hola"

@app.errorhandler(404)
def page_not_found(error):
    return "Que haces aqui fuera", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)