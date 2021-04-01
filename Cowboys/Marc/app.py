from flask import Blueprint
from flask import render_template

Cowboys_Marc_bp = Blueprint('Cowboys_Marc', __name__,
                            template_folder='templates',
                            static_folder='static', static_url_path='assets')


@Cowboys_Marc_bp.route("/marcminilab")
def upload():
    return render_template("marcminilab.html")
