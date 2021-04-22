from flask import Blueprint, render_template, request
from Cowboys.William.williamminilab import Person, Exponent, Dog, D

Cowboys_William_bp = Blueprint('Cowboys_William', __name__,
                               template_folder='templates',
                               static_folder='static', static_url_path='assets')


@Cowboys_William_bp.route("/")
def upload():
    return render_template("homepage2.html")


@Cowboys_William_bp.route("/response")
def response():
    return render_template("response.html")


@Cowboys_William_bp.route("/feedback", methods=["POST", "GET"])
def feedback():
    if request.method == 'POST':
        return render_template("response.html")
    return render_template("feedback.html")


@Cowboys_William_bp.route("/williamminilab", methods=["POST", "GET"])
def minilab():
    if request.method == 'POST':
        num1 = request.form.get('number1')
        num2 = request.form.get('number2')

        x = int(num1)
        y = int(num2)
        calc = Exponent(x, y)
        answer1 = calc.power()
        variable = int(num1)
        variable2 = int(num2)
        dispanswers = [answer1]
        return render_template("williamminilab.html", D=D, Dog=Dog(), answer1=answer1, dispanswers=dispanswers,
                               variable=variable, variable2=variable2)
    people = [Person("Billy", 17, "Soccer"), Person("Marc", 17, " Basketball"), Person("Allen", 17, " Coding")]
    return render_template("williamminilab.html", people=people, Dog=Dog(), D=D)
