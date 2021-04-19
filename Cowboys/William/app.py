from flask import Blueprint, render_template, request
from Cowboys.William.williamminilab import Person, Exponent

Cowboys_William_bp = Blueprint('Cowboys_William', __name__,
                               template_folder='templates',
                               static_folder='static', static_url_path='assets')


@Cowboys_William_bp.route("/")
def upload():
    return render_template("homepage2.html")


@Cowboys_William_bp.route("/williamminilab", methods=["POST", "GET"])
def minilab():
    if request.method == 'POST':
        num1 = request.form.get('number1')
        num2 = request.form.get('number2')

        x = int(num1)
        y = int(num2)
        calc = Exponent(x, y)
        answer = calc.power()
        return render_template("williamminilab.html",  answer=answer)
    people = [Person("Billy", 17, "Soccer"), Person("Marc", 17, " Basketball"), Person("Allen", 17, " Coding")]
    return render_template("williamminilab.html", people=people)

