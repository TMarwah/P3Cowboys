from flask import Blueprint
from flask import render_template, request, redirect, url_for
from Cowboys.Tanmay.tanmayminilab import  Counters

Cowboys_Tanmay_bp = Blueprint('Cowboys_Tanmay', __name__,
                              template_folder='templates',
                              static_folder='static', static_url_path='assets')



@Cowboys_Tanmay_bp.route('/login',methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'admin@gmail.com' or request.form['psw'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('Cowboys_Allen.upload'))
    return render_template('login.html', error=error)


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