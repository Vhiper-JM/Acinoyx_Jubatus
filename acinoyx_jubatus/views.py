#Aqui se definen y se guardan las rutas estandar de la pagina (a donde los usuarios pueden ir)
from flask import Blueprint, render_template, request, flash  #Estos importes permiten tener este archivo como un plano para la pagina (Blueprint), a renderizar las vistas html
                                                              #A pedir informacion (request) y mostrar mensajes en la pantalla (flash)

views = Blueprint('views', __name__)    #Asi es como se definira el "plano" (Blueprint)

@views.route('/', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@views.route('/feed', methods=['GET', 'POST'])
def feed():
    return render_template("feed.html")

@views.route('/resultados_busqueda', methods=['GET', 'POST'])
def resultados_busqueda():
    return render_template("resultados_busqueda.html")

@views.route('/registro', methods=['GET', 'POST'])
def registro():
    return render_template("registro.html")
