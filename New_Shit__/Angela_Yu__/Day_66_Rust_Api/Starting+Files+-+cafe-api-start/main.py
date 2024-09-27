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


@app.route("/add", methods=["POST"])
def add_cafe():
    data = request.args.to_dict()
    cafe = Cafe(
        name=data["name"],
        map_url=data["map_url"],
        img_url=data["img_url"],
        location=data["location"],
        seats=data["seats"],
        has_toilet=bool(int(data["has_toilet"])),
        has_wifi=bool(int(data["has_wifi"])),
        has_sockets=bool(int(data["has_sockets"])),
        can_take_calls=bool(int(data["can_take_calls"])),
        coffee_price=data["coffee_price"],
    )

    db.session.add(cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:id>", methods=["PATCH"])
def patch_cafe_price(id):
    cafe = db.get_or_404(Cafe, id)
    if cafe:
        cafe.coffee_price = request.args.get("price")
        db.session.commit()

        return jsonify(success={"success": "Successfully updated the price."}), 200
    else:
        return (
            jsonify(
                error={
                    "Not Found": "Sorry a cafe with that ID was not found in the database."
                }
            ),
            404,
        )


@app.route("/report-closed/<int:id>", methods=["DELETE"])
def delete_cafe(id):
    cafe = db.get_or_404(Cafe, id)
    apikey = "TopSecretAPIKey"
    if apikey == request.args.get("apikey"):
        if cafe:
            db.session.delete(cafe)
            db.session.commit()

            return jsonify(success={"success": "Successfully deleted the cafe."}), 200
        else:
            return (
                jsonify(
                    error={
                        "Not Found": "Sorry a cafe with that ID was not found in the database."
                    }
                ),
                404,
            )
    else:
        return (
            jsonify(
                error={
                    "Wrong API Key": "Sorry, that's not allowed. Make sure you have the correct api_key."
                }
            ),
            403,
        )


if __name__ == "__main__":
    app.run(debug=True)
