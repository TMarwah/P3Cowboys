from flask import Blueprint

y2021_tri4_bp = Blueprint('y2021_tri4', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@y2021_tri4_bp.route('/')
def index():
    return "Y2021 tri4 Home Site"
