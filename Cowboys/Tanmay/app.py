from flask import Blueprint
from flask import render_template, request
from Cowboys.Tanmay.tanmayminilab import  Counters

Cowboys_Tanmay_bp = Blueprint('Cowboys_Tanmay', __name__,
                              template_folder='templates',
                              static_folder='static', static_url_path='assets')


@Cowboys_Tanmay_bp.route('/minilab', methods=["POST", "GET"])
def minilab():
    if(request.method == 'POST'):
        sentence = request.form.get('sentence')
        input = sentence
        return render_template("tanmayminilab.html",wordcount = Counters(input).wordcount(), lettercount = Counters(input).lettercount())

    return render_template("tanmayminilab.html",wordcount = Counters(2).wordcount(), lettercount = Counters(2).lettercount())