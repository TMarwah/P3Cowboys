"""
Flask(__name__) establishes resources on the filesystem (aka package).
1. app is control object for flask
2. the Flask initializer uses __name__ param to locate root of webserver
3. static and templates are of folders that are located relative to directory of Flask execution
"""

from flask import Flask, render_template
from Cowboys.Allen.app import Cowboys_Allen_bp
from Cowboys.Marc.app import Cowboys_Marc_bp
from Cowboys.Tanmay.app import Cowboys_Tanmay_bp
from Cowboys.William.app import Cowboys_William_bp
import requests
import random

app = Flask(__name__)
app.register_blueprint(Cowboys_Allen_bp, url_prefix='/cowboys/allen')
app.register_blueprint(Cowboys_Marc_bp, url_prefix='/cowboys/marc')
app.register_blueprint(Cowboys_Tanmay_bp, url_prefix='/cowboys/tanmay')
app.register_blueprint(Cowboys_William_bp, url_prefix='/')

backgrounds = ["https://wallpaperaccess.com/full/869.jpg"]


@app.route('/quote/')
def index():
    # response = requests.get('https://nekos.life/api/v2/img/wallpaper')
    # background = response.json()['url']
    response = requests.get('https://api.quotable.io/random?maxLength=60')
    quote = response.json()['content']
    author = response.json()['author']
    background = random.choice(backgrounds)
    return render_template("quotepage.html", background=background, quote=quote, author=author)

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5000")
