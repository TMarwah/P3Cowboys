from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import requests
app = Flask(__name__)

""" database locations """
dbURI = 'sqlite:///createDB'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

"""
Sample of table creation and data population
"""

"""DB creation"""
engine = create_engine(dbURI)
session = Session(bind=engine)


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    input1 = db.Column(db.String(255), unique=False, nullable=False)
    input2 = db.Column(db.String(255), unique=False, nullable=False)


if __name__ == "__main__":
    """create each table"""
    db.create_all()

    response = requests.request("GET", input1=input1, input2=input2)

    print(response.text)
    list = response.json()

    try:
        for item in list:
            #          print(item["name"], item["countryCode"])
            u1 = Users(name=item["name"], country=item["countryCode"], state=item["state"], address=item["address"], zip=item["zip"], website=item["website"])
            session.add_all([u1])
        session.commit()


    except:
        print("Records exist")

    print("Table: Users")
    list = Users.query.all()
    for row in list:
        print(row.user_id)
        print(row.name)
        print("country:", row.country)
        print("state:", row.state)
        print("address:", row.address)
        print("zip code:", row.zip)
        print("website:", row.website)
