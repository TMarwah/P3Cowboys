from flask import Blueprint, render_template, request
from .marcminilab import Robot, Calculator, Robot1


Cowboys_Marc_bp = Blueprint('Cowboys_Marc', __name__,
                            template_folder='templates',
                            static_folder='static', static_url_path='assets')


@Cowboys_Marc_bp.route("/marcminilab", methods=["POST", "GET"])
def minilab():
    if(request.method == 'POST'):
        num1 = request.form.get('number1')
        num2 = request.form.get('number2')

        x = int(num1)
        y = int(num2)
        calc = Calculator(x,y)
        sum = calc.add()
        diff = calc.sub()
        product = calc.mul()
        quotient = calc.div()
        robots = []
        robots.append(Robot1("Tom", 55, "Red"))
        robots.append(Robot1("Michael", 67, "Magenta"))
        robots.append(Robot1("Suzan", 50, "Orange"))
        robots.append(Robot1("Bob", 100, "Baby Blue"))
        return render_template("marcminilab.html", Robot=Robot(), robots=robots,sum=sum,diff=diff, product=product,quotient=quotient)

    robots = []
    robots.append(Robot1("Tom", 55, "Red"))
    robots.append(Robot1("Michael", 67, "Magenta"))
    robots.append(Robot1("Suzan", 50, "Orange"))
    robots.append(Robot1("Bob", 100, "Baby Blue"))
    return render_template("marcminilab.html", Robot=Robot(), robots=robots)

