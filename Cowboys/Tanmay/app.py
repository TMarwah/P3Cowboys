from flask import Blueprint
from flask import render_template, request
from Cowboys.Tanmay.tanmayminilab import  Counters

Cowboys_Tanmay_bp = Blueprint('Cowboys_Tanmay', __name__,
                              template_folder='templates',
                              static_folder='static', static_url_path='assets')



@Cowboys_Tanmay_bp.route('/login')
def login():
    return render_template("login.html")

@Cowboys_Tanmay_bp.route('/minilab', methods=["POST", "GET"])
def minilab():
    if(request.method == 'POST'):
        sentence = request.form.get('sentence')
        sentencesort = request.form.get('sentencesort')
        input = sentence
        input2 = sentencesort
        return render_template("tanmayminilab.html",wordcount = Counters(input).wordcount(),
                               lettercount = Counters(input).lettercount(), sorted = Counters(input2).bubblesort())

    return render_template("tanmayminilab.html",wordcount = Counters(2).wordcount(),
                           lettercount = Counters(2).lettercount(), sorted = Counters(2).bubblesort())