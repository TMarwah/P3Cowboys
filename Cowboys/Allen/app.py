from flask import Blueprint
from flask import render_template


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
@Cowboys_Allen_bp.route("/minilab")
def minilab():
    return render_template("allenminilab.html")



