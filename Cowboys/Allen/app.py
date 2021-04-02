from flask import Blueprint
from flask import render_template, request
from Cowboys.Allen.allenminilab import Prime


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

        number = request.form.get('number')
        n = int(number)
        return render_template("allenminilab.html", prime = Prime(n).solution())

    return render_template("allenminilab.html", prime = Prime(2).solution())




