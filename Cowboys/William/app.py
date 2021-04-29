from flask import Blueprint, render_template, request
from Cowboys.William.williamminilab import Person, Exponent, Animal

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


@Cowboys_William_bp.route("/animals", methods=["POST", "GET"])
def animals():
    if request.method == 'POST':
        animal1 = request.form.get('animal1')
        animal2 = request.form.get('animal2')
        input1 = animal1
        input2 = animal2
        animal = [Animal('Dog', 'Yorky'), Animal('Dog', 'Weiner'), Animal('Dog', 'Pug'), Animal('Cat', 'Tom')]
        return render_template("animals.html", animal=animal, animal1=animal1, input1=input1, animal2=animal2, input2=input2)
    animal = [Animal('Dog', 'Yorky'), Animal('Dog', 'Weiner'), Animal('Dog', 'Pug'), Animal('Cat', 'Tom')]
    return render_template("animals.html", animal=animal)


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
        dispanswers = answer1
        animals = [Animal('Dog', 'Yorky'), Animal('Dog', 'Weiner'), Animal('Dog', 'Pug'), Animal('Cat', 'Tom')]
        return render_template("williamminilab.html", animals=animals, answer1=answer1, dispanswers=dispanswers,
                               variable=variable, variable2=variable2)
    return render_template("williamminilab.html")
