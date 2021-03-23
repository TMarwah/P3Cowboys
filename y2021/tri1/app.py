from flask import Blueprint
from flask import render_template

y2021_tri1_bp = Blueprint('y2021_tri1', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@y2021_tri1_bp.route('/')
def index():
    return "Y2021 tri1 Home Site"

@y2021_tri1_bp.route("/upload")
def upload():
    return render_template("/y2021/tri1/upload.html",)
