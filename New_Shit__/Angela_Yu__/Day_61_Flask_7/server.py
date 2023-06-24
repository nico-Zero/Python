from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    form = MyForm()
    if form.validate_on_submit():
        return redirect("/")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
