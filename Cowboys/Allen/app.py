from flask import Blueprint
from flask import render_template, request, url_for, Response, redirect, Flask
from Cowboys.Allen.allenminilab import Prime
from .model import Review
import random
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from .db import db, db_init

app = Flask(__name__)
# SQLAlchemy config. Read more: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

db = SQLAlchemy()

backgrounds = ["https://www.teahub.io/photos/full/193-1933361_laptop-aesthetic-wallpapers-anime.jpg"]

Cowboys_Allen_bp = Blueprint('Cowboys_Allen', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='assets')


@Cowboys_Allen_bp.route('/')
def index():
    return "Y2021 tri1 Home Site"

#@Cowboys_Allen_bp.route('/browse')
#def browse():
    #return render_template("browse.html")

#@Cowboys_Allen_bp.route("/upload")
##return render_template("upload.html")

@Cowboys_Allen_bp.route('/browse')
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
            'satisfaction': review.satisfaction,
            'image':  websiteurl
        }
        reviews.append(review_dict)
    return render_template("browse.html", reviews=reviews, background=random.choice(backgrounds))

@Cowboys_Allen_bp.route('/upload', methods=["POST", 'GET'])
def upload():
    background = random.choice(backgrounds)
    if request.method == "POST":
        name = request.form["username"]
        satisfaction = request.form["satisfaction"]
        content = request.form["content"]
        image = request.files.get('img')
        if not image:
            return 'bad news ur image did not make it to our servers :((((', 400

        filename = secure_filename(image.filename)
        mimetype = image.mimetype
        if not filename or not mimetype:
            return 'Bad upload', 400

        review = Review(username=name, content=content, img=image.read(), filename=filename, satisfaction=satisfaction,mimetype=mimetype)
        db.session.add(review)
        db.session.commit()
        return redirect(url_for("browse.html"))
    return render_template("upload.html", background=background)


@Cowboys_Allen_bp.route('/images/<int:id>')
def get_img(id):
    img = Review.query.filter_by(id=id).first()
    if not img:
        return 'No img with that id', 200

    return Response(img.img, mimetype=img.mimetype)


@Cowboys_Allen_bp.route("/minilab", methods=["POST", "GET"])
def minilab():

    if(request.method == 'POST'):

        number = request.form.get('number')
        n = int(number)
        return render_template("allenminilab.html", prime = Prime(n))

    return render_template("allenminilab.html", prime = Prime(2))




