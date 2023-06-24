from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import secrets

key = secrets.token_hex(64)


class MyForm(FlaskForm):
    email = StringField(label="Email:- ", validators=[DataRequired()])
    password = PasswordField(label="Password:- ", validators=[DataRequired()])
    login = SubmitField(label="login")


app = Flask(__name__)
app.config["SECRET_KEY"] = key


@app.route("/", methods=["GET", "POST"])
def home():
    em_ps_form = MyForm()
    if request.method == "POST":
        if em_ps_form.validate_on_submit():
            email = request.form["email"]
            password = request.form["password"]
            print(f"Email:- {email}, Password:- {password}")

            return redirect("/")
    return render_template("index.html", form=em_ps_form)


if __name__ == "__main__":
    app.run(debug=True)
