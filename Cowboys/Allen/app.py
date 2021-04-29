from flask import Blueprint
from flask import render_template, request
from Cowboys.Allen.allenminilab import Prime, Vowel


backgrounds = ["https://www.teahub.io/photos/full/193-1933361_laptop-aesthetic-wallpapers-anime.jpg"]

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

    if(request.method == 'POST'):
        if(request.form["select"] == "prime"):

            number = request.form.get('number')
            n = int(number)
            return render_template("allenminilab.html", output = Prime(n).solution)
        else:
            string = request.form.get('number')
            word = str(string)
            return render_template("allenminilab.html", output = Vowel(word).vowel_count)

    return render_template("allenminilab.html", output = "Select Option")




