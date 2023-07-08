from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from csv import reader, writer


class Input_form(FlaskForm):
    name = StringField(label="Book Name:-", validators=[DataRequired()])
    author = StringField(label="Book Author:-", validators=[DataRequired()])
    rating = SelectField(
        label="Rating:-",
        validators=[DataRequired()],
        choices=("❌", "⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"),
    )
    add = SubmitField("Add")


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


@app.route("/")
def home():
    all_books = []
    with open("books.csv", newline="", encoding="utf8") as csv_file:
        file = reader(csv_file, delimiter=",")
        for row in file:
            all_books.append(row)
    parsed_books = [
        {"name": name, "author": author, "rating": rating}
        for name, author, rating in all_books[1:]
    ]

    return render_template("index.html", library=bool(parsed_books), books=parsed_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = Input_form()
    if form.validate_on_submit():
        data = {key: value for key, value in list(form.data.items())[:-2]}
        with open("books.csv", "+a", newline="", encoding="utf8") as csv_file:
            file = writer(csv_file, delimiter=",")
            file.writerow(data.values())
            return redirect(url_for("home"))

    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
