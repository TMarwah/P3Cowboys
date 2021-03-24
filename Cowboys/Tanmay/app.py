from flask import Blueprint

Cowboys_Tanmay_bp = Blueprint('Cowboys_Tanmay', __name__,
                              template_folder='templates',
                              static_folder='static', static_url_path='assets')


@Cowboys_Tanmay_bp.route('/')
def index():
    return "Cowboys Marc"
