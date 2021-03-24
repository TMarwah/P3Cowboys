from flask import Blueprint

Cowboys_Marc_bp = Blueprint('Cowboys_Marc', __name__,
                            template_folder='templates',
                            static_folder='static', static_url_path='assets')


@Cowboys_Marc_bp.route('/')
def index():
    return "Cowboys Marc"
