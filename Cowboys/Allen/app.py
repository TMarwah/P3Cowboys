from flask import Blueprint
from flask import render_template, request
from Cowboys.Allen.allenminilab import Prime, Vowel


backgrounds = ["https://i.pinimg.com/736x/09/a0/e8/09a0e8ef1de9a29ed53238de10c39540.jpg"]

Cowboys_Allen_bp = Blueprint('Cowboys_Allen', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='assets')


@Cowboys_Allen_bp.route('/')
def index():
    return "Y2021 tri1 Home Site"

@Cowboys_Allen_bp.route('/browse')
def browse():
    return render_template("browse.html")

@Cowboys_Allen_bp.route("/upload")
def upload():
    return render_template("upload.html")


@Cowboys_Allen_bp.route("/minilab", methods=["POST", "GET"])
def minilab():
    background = backgrounds
    if(request.method == 'POST'):

        if(request.form["select"] == "prime"):
            number = request.form.get('number')
            n = int(number)
            return render_template("allenminilab.html", output = Prime(n).solution, background = background)
        else:
            string = request.form.get('number')
            word = str(string)
            return render_template("allenminilab.html", output = Vowel(word).vowel_count, background = background)

    return render_template("allenminilab.html")




