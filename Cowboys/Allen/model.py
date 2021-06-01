from .db import db


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=True)
    img = db.Column(db.Text, unique=False, nullable=True)
    filename = db.Column(db.Text, nullable=False)
