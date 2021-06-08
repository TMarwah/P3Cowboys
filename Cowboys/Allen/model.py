from .db import db


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=True)
