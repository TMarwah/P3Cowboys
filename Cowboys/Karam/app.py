from flask import Blueprint, render_template, request

from .karamminilab import Caracal, Characters

Cowboys_Karam_bp = Blueprint('Cowboys_Karam', __name__,
                               template_folder='templates',
                               static_folder='static', static_url_path='assets')
@Cowboys_Karam_bp.route("/")
def upload():
    return render_template ("homepage2.html")

@Cowboys_Karam_bp.route("/karamminilab")
def minilab():
    caracals= [Caracal("skinny", "beige"), Caracal("fat", "brown")]
    return render_template("karamminilab.html", caracals=caracals)


@Cowboys_Karam_bp.route("/karambubblesort.html", methods=["POST", "GET"])
def qaracters():
    if request.method == 'POST':
        string = request.form.get('word')
        word = str(string)
        return render_template("karambubblesort.html", characters=Characters(word).characters)
    return render_template("karambubblesort.html")

