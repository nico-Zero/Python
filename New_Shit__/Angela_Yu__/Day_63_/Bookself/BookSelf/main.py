from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class Input_form(FlaskForm):
    name = StringField(label='Book Name:-', validators=[DataRequired()])
    author = StringField(label='Book Author:-', validators=[DataRequired()])
    rating = StringField(label='Rating:-', validators=[DataRequired()])
    add = SubmitField("Add")

app = Flask(__name__)
Bootstrap(app)

all_books = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add():
    form = Input_form()

    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
