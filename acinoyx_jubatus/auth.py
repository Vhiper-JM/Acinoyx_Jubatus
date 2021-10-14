from flask import Blueprint
from flask.templating import render_template

auth = Blueprint('auth', __name__)

@auth.route("/", methods=["GET" "POST"])
def registro():
    return render_template("registro.html")
    




