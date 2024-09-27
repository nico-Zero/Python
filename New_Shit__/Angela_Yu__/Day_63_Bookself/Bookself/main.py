from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book_keeping.db"
Bootstrap(app)
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


class Input_form(FlaskForm):
    title = StringField(label="Book Name:-", validators=[DataRequired()])
    author = StringField(label="Book Author:-", validators=[DataRequired()])
    rating = FloatField(
        label="Rating(out of 10):-",
        validators=[
            DataRequired(),
            NumberRange(max=10, min=0, message="Rating must be 0-10."),
        ],
    )
    add = SubmitField("Add")


class Edit_rating(FlaskForm):
    rating = FloatField(
        label="Rating(out of 10):-",
        validators=[
            DataRequired(),
            NumberRange(max=10, min=0, message="Rating must be 0-10."),
        ],
    )
    edit = SubmitField("Edit")


@app.route("/")
def home():
    data = db.session.execute(db.select(Books).order_by(Books.id)).scalars()

    parsed_books = [
        {"id": i.id, "title": i.title, "author": i.author, "rating": i.rating}
        for i in data.all()
    ]

    return render_template("index.html", library=bool(parsed_books), books=parsed_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = Input_form()
    if form.validate_on_submit():
        data = {key: value for key, value in list(form.data.items())[:-2]}
        try:
            book = Books(
                title=data["title"], author=data["author"], rating=data["rating"]
            )
            db.session.add(book)
            db.session.commit()
        except Exception as e:
            print(e)
            title = data["name"]
            return render_template(
                "add.html",
                form=form,
                error=f"'{title}' already exists in the database.",
            )
        else:
            return redirect(url_for("home"))

    return render_template("add.html", form=form)


@app.route(
    "/edit_rating/<int:id>/<string:title>/<float:rating>", methods=["GET", "POST"]
)
def edit_rating(id, title, rating):
    form = Edit_rating()
    if form.validate_on_submit():
        db.get_or_404(Books, id).rating = form.data["rating"]
        db.session.commit()
        return redirect(url_for("home"))

    return render_template(
        "edit_rating.html", form=form, item={"title": title, "rating": rating}
    )


@app.route("/delete/<int:id>")
def delete(id):
    book = db.get_or_404(Books, id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
