from flask import Blueprint
from flask import render_template

Cowboys_Allen_bp = Blueprint('Cowboys_Allen', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='assets')


@Cowboys_Allen_bp.route('/')
def index():
    return "Y2021 tri1 Home Site"


@Cowboys_Allen_bp.route("/upload")
def upload():
    return render_template("/y2021/tri1/upload.html", )
