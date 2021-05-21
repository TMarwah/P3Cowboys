from flask import Blueprint
from flask import render_template, request
from Cowboys.Allen.minilab1 import CreateTask


backgrounds = ["https://www.teahub.io/photos/full/193-1933361_laptop-aesthetic-wallpapers-anime.jpg"]

Cowboys_minilab1_bp = Blueprint('Cowboys_Allen', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='assets')


@Cowboys_minilab1_bp.route('/')
def index():
    return "Y2021 tri1 Home Site"

@Cowboys_minilab1_bp.route('/browse')
def browse():
    return render_template("browse.html")

@Cowboys_minilab1_bp.route("/upload")
def upload():
    return render_template("upload.html")


@Cowboys_minilab1_bp.route("/minilab", methods=["POST", "GET"])
def minilab():

    if(request.method == 'POST'):
        if(request.form["select"] == "average"):
            number = request.form.get('number')
            return render_template("minilab1.html", output = CreateTask(number, "average").testproc)

        if(request.form["select"] == "sort"):
            number = request.form.get('number')
            return render_template("minilab1.html", output = CreateTask(number, "sort").testproc)

    return render_template("minilab1.html", output = "Select Option")




