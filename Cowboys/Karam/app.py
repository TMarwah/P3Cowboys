from flask import Blueprint, render_template, request

from .karamminilab import Caracal , Calculator

Cowboys_Karam_bp = Blueprint('Cowboys_Karam', __name__,
                               template_folder='templates',
                               static_folder='static', static_url_path='assets')
@Cowboys_Karam_bp.route("/")
def upload():
    return render_template ("homepage2.html")

@Cowboys_Karam_bp.route("/karamminilab",methods=["POST", "GET"])
def minilab():
    if(request.method == 'POST'):
        x = request.form.get('number1')
        y = request.form.get('number2')
        num1 = int(x)
        num2 = int(y)
        calc = Calculator(num1,num2)
        add = calc.add()
        diff = calc.subtract()
        product = calc.multiply()
        quotient = calc.divide()
        caracals= [Caracal("skinny", "beige"), Caracal("fat", "brown")]
        return render_template("karamminilab.html", caracals=caracals, add=add,diff=diff, product=product,quotient=quotient)
    caracals= [Caracal("skinny", "beige"), Caracal("fat", "brown")]
    return render_template("karamminilab.html", caracals=caracals)