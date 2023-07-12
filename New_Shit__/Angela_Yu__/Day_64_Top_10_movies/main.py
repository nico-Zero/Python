from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, URLField, IntegerField
from wtforms.validators import DataRequired, NumberRange

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
    review = db.Column(db.String(1000), nullable=True)


with app.app_context():
    db.create_all()


class AddMovie(FlaskForm):
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
            "rank": num + 1,
            "id": movie.id,
            "name": movie.name,
            "year": movie.year,
            "rating": movie.rating,
            "image_url": movie.image_url,
            "description": movie.description,
            "review": movie.review,
        }
        for num, movie in enumerate(movies_data.all()[::-1])
    ]

    return render_template("index.html", data=parsed_movies_data)


@app.route("/add", methods=["GET", "POST"])
def add_movies():
    form = AddMovie()
    if form.validate_on_submit():
        movie = Movies(
            name=form.data["name"],
            year=form.data["year"],
            rating=form.data["rating"],
            image_url=form.data["image_url"],
            description=form.data["description"],
            review=form.data["review"],
        )

        db.session.add(movie)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html", form=form)


@app.route("/update/<movie_id>", methods=["GET", "POST"])
def update_movie(movie_id):
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


@app.route("/delete")
def delete_movie():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
