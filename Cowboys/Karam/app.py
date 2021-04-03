from flask import Blueprint, render_template, request

from .karamminilab import Caracal

Cowboys_Karam_bp = Blueprint('Cowboys_Karam', __name__,
                               template_folder='templates',
                               static_folder='static', static_url_path='assets')


@Cowboys_Karam_bp.route("/karamminilab")
def minilab():
    return render_template("karamminilab.html", Caracal=Caracal())
