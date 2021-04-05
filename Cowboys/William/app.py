from flask import Blueprint, render_template
from Cowboys.William.williamminilab import Person

Cowboys_William_bp = Blueprint('Cowboys_William', __name__,
                               template_folder='templates',
                               static_folder='static', static_url_path='assets')


@Cowboys_William_bp.route("/")
def upload():
    return render_template("homepage2.html")


@Cowboys_William_bp.route("/williamminilab")
def minilab():
    people = []
    people.append(Person("Billy", 17, "Soccer"))
    people.append(Person("Marc", 17, " Basketball"))
    people.append(Person("Allen", 17, " Coding"))
    return render_template("williamminilab.html", people=people)
