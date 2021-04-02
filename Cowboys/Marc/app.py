from flask import Blueprint, render_template, request
from .marcminilab import Robot


Cowboys_Marc_bp = Blueprint('Cowboys_Marc', __name__,
                            template_folder='templates',
                            static_folder='static', static_url_path='assets')


@Cowboys_Marc_bp.route("/marcminilab")
def minilab():
    return render_template("marcminilab.html", Robot=Robot())

