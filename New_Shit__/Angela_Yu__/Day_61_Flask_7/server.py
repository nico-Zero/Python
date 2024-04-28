from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, NumberRange, Email
from flask_bootstrap import Bootstrap

import secrets

key = secrets.token_hex(64)


class MyForm(FlaskForm):
    def Length(_form, field, min=8, max=30, messages="8-30 Character Please."):
        if not min <= len(field.data) <= max:
            raise ValidationError(messages)

    email = StringField(
        label="Email:- ",
        validators=[
            DataRequired(message="Just enter a valid email Mother Fucker!!!"),
            Email(
                message="I told you to enter a fucking god dam a valid email. BITCH!!!"
            ),
        ],
    )
    password = PasswordField(
        label="Password:- ",
        validators=[
            DataRequired(message="Just enter a valid Password Mother Fucker!!!"),
            Length,
        ],
    )
    login = SubmitField(label="login")


app = Flask(__name__)
app.config["SECRET_KEY"] = key
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    em_ps_form = MyForm()
    if em_ps_form.validate_on_submit():
        email = em_ps_form.email.data
        password = em_ps_form.password.data
        print(f"Email:- {email}, Password:- {password}")
        if email == "admin@email.com" and password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=em_ps_form)


if __name__ == "__main__":
    app.run(debug=True)
