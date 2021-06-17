from flask import Blueprint
from flask import render_template,request, url_for, Response, redirect, Flask, jsonify
from Cowboys.Allen.minilab1 import CreateTask
from Cowboys.Allen.model import Review
import random, json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from .db import db, db_init
#with open('cowboys.allen.config.json') as file:
    #config = json.load(file)

#app = Flask(__name__)
# SQLAlchemy config. Read more: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db_init(app)

#db = SQLAlchemy()

backgrounds = ["https://www.teahub.io/photos/full/193-1933361_laptop-aesthetic-wallpapers-anime.jpg"]

Cowboys_minilab1_bp = Blueprint('Cowboys_Allen', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='assets')


@Cowboys_minilab1_bp.route('/')
def index():
    return "Y2021 tri1 Home Site"

@Cowboys_minilab1_bp.route('/browse')
def browse():
    return render_template("browse.html")

#@Cowboys_minilab1_bp.route('/browse')
#def browse():
    #backgrounds = ["https://cdn.discordapp.com/attachments/784178874303905792/818606015494094868/812382.png"]
    #review_query = Review.query.all()
    #reviews = []

    #for review in review_query:

        #review_dict = {
            #'website': review.website,
            #'content': review.content,
        #}
        #reviews.append(review_dict)
    #return render_template("browse.html", reviews=reviews, background=random.choice(backgrounds))

#@Cowboys_minilab1_bp.route('/upload', methods=["POST", 'GET'])
#def upload():
    #background = random.choice(backgrounds)
    #if request.method == "POST":
        #name = request.form["website"]
        #content = request.form["content"]

        #review = Review(website=name, content=content)
        #db.session.add(review)
        #db.session.commit()
        #return redirect(url_for("browse.html"))
    #return render_template("upload.html", background=background)

@Cowboys_minilab1_bp.route("/upload", methods=["POST", "GET"])
def feedback():
    if request.method == 'POST':
        name = request.form.get('website')
        comment = request.form.get('content')
        input1 = name
        input2 = comment
        return render_template("browse.html", name=name, comment=comment, input1=input1, input2=input2)
    return render_template("upload.html")


#@Cowboys_minilab1_bp.route("/upload")
#def upload():
    #return render_template("upload.html")


@Cowboys_minilab1_bp.route("/minilab", methods=["POST", "GET"])
def minilab():

    if(request.method == 'POST'):
        if(request.form["select"] == "average"):
            number = request.form.get('number')
            return render_template("minilab1.html", output = CreateTask(number, "average").testproc)

        if(request.form["select"] == "sort"):
            number = request.form.get('number')
            return render_template("minilab1.html", output = CreateTask(number, "sort").testproc)

    return render_template("minilab1.html", output = "Select Option")




