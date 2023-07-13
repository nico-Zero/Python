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
    ranking = db.Column(db.Integer, nullable=True)
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
    review = StringField(label="Review:- ")
    update = SubmitField(
        label="Update",
    )


@app.route("/")
def home():
    movies_data = db.session.execute(db.select(Movies).order_by(Movies.id)).scalars()

    parsed_movies_data = [
        {
            "id": movie.id,
            "name": movie.name,
            "year": movie.year,
            "rating": movie.rating,
            "image_url": movie.image_url,
            "description": movie.description,
            "review": movie.review,
        }
        for movie in movies_data.all()[::-1]
    ]

    return render_template("index.html", data=parsed_movies_data)


@app.route("/add/<str:get=get_1>/<movie_id>", methods=["GET", "POST"])
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
            ranking=None,
            rating=None,
            review=None,
        )

        db.session.add(movie)
        db.session.commit()

        return redirect(url_for('edit_movie'))
        
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
        {
            "id": movie["id"],
            "title": movie["original_title"],
            "release_date": movie["release_date"],
        }
        for movie in response.json()["results"]
    ]

    return render_template("select.html", parsed_data=parsed_data)


@app.route("/edit/<movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = db.get_or_404(Movies, movie_id)

    form = UpdateMovie(
        name=movie.name,
        year=movie.year,
        rating=movie.rating,
        image_url=movie.image_url,
        description=movie.description,
        review=movie.review,
    )

    if form.validate_on_submit():
        movie.name = form.data["name"]
        movie.year = form.data["year"]
        movie.rating = form.data["rating"]
        movie.image_url = form.data["image_url"]
        movie.description = form.data["description"]
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
