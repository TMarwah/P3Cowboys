from flask import Blueprint, render_template

Cowboys_Karam_bp = Blueprint('Cowboys_Karam', __name__,
                               template_folder='templates',
                               static_folder='static', static_url_path='assets')


@Cowboys_Karam_bp.route("/")
def upload():
    return render_template("homepage2.html")
