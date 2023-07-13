from flask import Flask, render_template, redirect, url_for
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
    image_url = db.Column(db.String(1000), nullable=False, unique=True)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    review = db.Column(db.String(1000), nullable=True)


with app.app_context():
    db.create_all()


class AddMovie(FlaskForm):
    name = StringField(label="Movie Name:- ", validators=[DataRequired()])
    add = SubmitField(
        label="Add",
    )


class UpdateMovie(FlaskForm):
    rating = FloatField(
        label="Rating:- ",
        validators=[
            DataRequired(),
            NumberRange(min=0, max=10, message="Rating Must be 0-10."),
        ],
    )
    review = StringField(label="Review:- ")
    update = SubmitField(
        label="Update",
    )


@app.route("/")
def home():
    movies_data = db.session.execute(
        db.select(Movies).order_by(Movies.rating)
    ).scalars()

    parsed_movies_data = [
        {
            "rank": rank + 1,
            "id": movie.id,
            "name": movie.name,
            "year": movie.year,
            "rating": movie.rating,
            "image_url": movie.image_url,
            "description": movie.description,
            "review": movie.review,
        }
        for rank, movie in enumerate(movies_data.all()[::-1])
    ]

    return render_template("index.html", data=parsed_movies_data)


@app.route(
    "/add",
    defaults={"get": "get_1", "movie_id": 0},
    methods=["GET", "POST"],
)
@app.route("/add/<int:movie_id>/<get>", methods=["GET", "POST"])
def add_movie(get, movie_id):
    form = AddMovie()
    if get == "get_2":
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
        img_url = "https://image.tmdb.org/t/p/w500"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2YmIwN2U2OTU1Zjg2ZTg4MTJkYzdhYWJmZTc1NmY5NiIsInN1YiI6IjY0YWZjOWM4ZDY1OTBiMDBhZjkyM2QyZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.qOnBOMhQya-62PhLUPt8tLuepoUhPIq6CpKXoFNmVFU",
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response = response.json()
        movie = Movies(
            name=response["original_title"],
            year=response["release_date"][:4],
            image_url=img_url + response["poster_path"],
            description=response["overview"],
            rating=None,
            review=None,
        )

        db.session.add(movie)
        db.session.commit()

        return redirect(url_for("edit_movie", movie_name=response["original_title"]))

    if form.validate_on_submit():
        return redirect(url_for("select_movie", movie_name=form.data["name"]))

    return render_template("add.html", form=form)


@app.route("/select/<string:movie_name>", methods=["GET", "POST"])
def select_movie(movie_name):
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2YmIwN2U2OTU1Zjg2ZTg4MTJkYzdhYWJmZTc1NmY5NiIsInN1YiI6IjY0YWZjOWM4ZDY1OTBiMDBhZjkyM2QyZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.qOnBOMhQya-62PhLUPt8tLuepoUhPIq6CpKXoFNmVFU",
    }
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_name}&include_adult=false&language=en-US&page=1"
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    parsed_data = [
        [
            movie["id"],
            movie["original_title"],
            movie["release_date"],
        ]
        for movie in response.json()["results"]
    ]

    return render_template("select.html", parsed_data=parsed_data)


@app.route("/edit/<movie_name>", methods=["GET", "POST"])
def edit_movie(movie_name):
    movie = db.session.execute(
        db.select(Movies).where(Movies.name == movie_name)
    ).scalar_one()

    form = UpdateMovie(
        rating=movie.rating,
        review=movie.review,
    )

    if form.validate_on_submit():
        movie.rating = form.data["rating"]
        movie.review = form.data["review"]

        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", form=form)


@app.route("/delete/<movie_id>")
def delete_movie(movie_id):
    db.session.delete(db.get_or_404(Movies, movie_id))
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

for i in enumerate(range(10)):
    ...
