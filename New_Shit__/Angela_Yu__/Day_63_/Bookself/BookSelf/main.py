from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv

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

all_books = []


@app.route("/")
def home():
    
    return render_template("index.html",library = bool(all_books) ,books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = Input_form()
    if form.validate_on_submit():
        with open("books.csv", "+a") as csv_file:
            ...
        all_books.append({key: value for key, value in list(form.data.items())[:-2]})
        print(all_books)
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
