from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, URLField, IntegerField
from wtforms.validators import DataRequired, NumberRange
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


class AddMovies(FlaskForm):
    name = StringField(label="Movie Name:- ", validators=[DataRequired()])
    year = IntegerField(
        label="Year:- ",
        validators=[
            DataRequired(),
            NumberRange(min=1900, max=2500, message="Enter a valid year."),
        ],
    )
    rating = FloatField(
        label="Rating:- ",
        validators=[
            DataRequired(),
            NumberRange(min=0, max=10, message="Rating Must be 0-10."),
        ],
    )
    image_url = URLField(label="Image URL:- ", validators=[DataRequired()])
    description = StringField(label="Description:- ")
    comment = StringField(label="Comment:- ")
    add = SubmitField(
        label="Add",
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_movies():
    form = AddMovies()
    if form.validate_on_submit():
        movie = Movies(
            name=form.data.name,
            year=form.data.year,
            rating=form.data.rating,
            image_url=form.data.image_url,
            description=form.data.description,
            comment=form.data.comment,
        )

        db.session.add(movie)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html", form=form)


@app.route("/update", methods=["GET", "POST"])
def update_movie():
    return render_template("update.html")


@app.route("/delete")
def delete_movie():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
