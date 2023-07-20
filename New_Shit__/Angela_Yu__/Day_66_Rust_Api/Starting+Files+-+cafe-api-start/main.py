from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint
from inspect import getmembers
from functools import reduce

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    cafe = db.get_or_404(Cafe, randint(0, int(db.session.query(Cafe).count())))

    return jsonify(cafe=cafe.to_dict())


@app.route("/all")
def all_cafe():
    data = list(db.session.query(Cafe))
    cafes = {index + 1: i.to_dict() for index, i in enumerate(data)}

    return jsonify(all_cafe=cafes)


@app.route("/search")
def search_cafe_by_location():
    data = db.session.query(Cafe).filter(Cafe.location == request.args.get("loc"))

    if bool(list(data)):
        cafes = {index + 1: i.to_dict() for index, i in enumerate(data)}
        return jsonify(cafe=cafes)
    else:
        return jsonify(
            error={"Not Found": "Sorry, we don't have a cafe at that location."}
        )


## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == "__main__":
    app.run(debug=True)
