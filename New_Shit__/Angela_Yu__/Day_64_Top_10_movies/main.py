from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

db = SQLAlchemy()

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
Bootstrap5(app)
db.init_app(app)


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    year = db.Column(db.String(5), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(1000), nullable=True, unique=True)
    description = db.Column(db.String(1000), nullable=True)
    comment = db.Column(db.String(1000), nullable=True)


with app.app_context():
    db.create_all()

class AddMovies():
    name = StringField(label="Movie Name:- ", validators=[DataRequired()])


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
