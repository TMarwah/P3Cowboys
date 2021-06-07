from flask import Blueprint
from flask import render_template,request, url_for, Response, redirect, Flask, jsonify
from Cowboys.Allen.minilab1 import CreateTask
from Cowboys.Allen.model import Review
import random, json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from .db import db, db_init
#with open('cowboys.allen.config.json') as file:
   # config = json.load(file)

app = Flask(__name__)
# SQLAlchemy config. Read more: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

db = SQLAlchemy()

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

@Cowboys_minilab1_bp.route('/cowboys/minilab1/browse')
def browse():
    backgrounds = ["https://cdn.discordapp.com/attachments/784178874303905792/818606015494094868/812382.png"]
    review_query = Review.query.all()
    reviews = []

    for review in review_query:
        websiteurl = url_for('get_img', id=review.id)

        review_dict = {
            'id': review.id,
            'username': review.username,
            'content': review.content,
            'image':  websiteurl
        }
        reviews.append(review_dict)
    return render_template("browse.html", reviews=reviews, background=random.choice(backgrounds))

@Cowboys_minilab1_bp.route('/cowboys/minilab1/upload', methods=["POST", 'GET'])
def upload():
    background = random.choice(backgrounds)
    if request.method == "POST":
        name = request.form["username"]
        content = request.form["content"]
        image = request.files.get('img')
        if not image:
            return 'bad news ur image did not make it to our servers :((((', 400

        filename = secure_filename(image.filename)
        mimetype = image.mimetype
        if not filename or not mimetype:
            return 'Bad upload', 400

        review = Review(username=name, content=content, img=image.read(), filename=filename, mimetype=mimetype)
        db.session.add(review)
        db.session.commit()
        return redirect(url_for("browse.html"))
    return render_template("upload.html", background=background)

@Cowboys_minilab1_bp.route('/images/<int:id>')
def get_img(id):
    img = Review.query.filter_by(id=id).first()
    if not img:
        return 'No img with that id', 200

    return Response(img.img, mimetype=img.mimetype)

@Cowboys_minilab1_bp.route('/api/review/id=<int:id>')
def get_review(id):
    review = Review.query.filter_by(id=id).first()
    if review:
        url = url_for('get_img', id=id)

        review_dict = {
            'id': review.id,
            'username': review.username,
            'content': review.content,
            'satisfaction_level': review.satisfaction,
            'image_url': config['websiteURL'] + url
        }
        return jsonify(review_dict)

    else:
        return Response("No review with that id ", status=400)

@Cowboys_minilab1_bp.route('/api/review/all')
def get_all_reviews():
    review_query = Review.query.all()
    reviews_dict = {}

    for review in review_query:
        websiteurl = url_for('get_img', id=review.id)
        review_dict = {
            'id': review.id,
            'username': review.username,
            'content': review.content,
            'satisfaction': review.satisfaction,
            'image':  websiteurl
        }
        reviews_dict[review.id] = review_dict

    return jsonify(reviews_dict)


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




