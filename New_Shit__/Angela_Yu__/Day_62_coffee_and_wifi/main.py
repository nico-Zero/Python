from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField, TimeField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    Location = URLField("Location", validators=[DataRequired(), URL()])
    open_ = TimeField("Open", validators=[DataRequired()], format="%H:%M")
    close = TimeField("Close", validators=[DataRequired()], format="%H:%M")
    coffee = SelectField(
        "Coffee",
        validators=[DataRequired()],
        choices=["✘", "☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
    )
    wifi = SelectField(
        "Wifi",
        validators=[DataRequired()],
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
    )
    power = SelectField(
        "Power",
        validators=[DataRequired()],
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
    )

    submit = SubmitField("Submit")


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def cafes():
    with open("cafe_data.csv", newline="", encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template("cafes.html", cafes=list_of_rows)


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe_data.csv', "+a" ,newline="", encoding="utf8") as csv_file:
            data = csv.writer(csv_file, delimiter=",")
            # data.writerow()
            print(form.data)
            print([type(i) for i in list(form.data.values())[:-2]])

    return render_template("add.html", form=form)


@app.route("/delete")
def delete_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    return render_template("delete.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
