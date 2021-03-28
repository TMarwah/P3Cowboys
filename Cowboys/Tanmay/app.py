from flask import Blueprint, render_template

Cowboys_Tanmay_bp = Blueprint('Cowboys_Tanmay', __name__,
                              template_folder='templates',
                              static_folder='static', static_url_path='assets')


@Cowboys_Tanmay_bp.route('/login')
def login():
    return render_template("login.html")
