from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField, TimeField
from wtforms.validators import DataRequired, URL
import csv
import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = URLField(
        "Cafe Location on Google Map (URL)", validators=[DataRequired(), URL()]
    )
    open_ = TimeField(
        "Opening Time e.g. 8AM", validators=[DataRequired()], format="%H:%M"
    )
    close = TimeField(
        "Closing Time e.g. 5:30PM", validators=[DataRequired()], format="%H:%M"
    )
    coffee = SelectField(
        "Coffee Rating",
        validators=[DataRequired()],
        choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],  # type:ignore
    )
    wifi = SelectField(
        "Wifi Strength Rating",
        validators=[DataRequired()],
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],  # type:ignore
    )
    power = SelectField(
        "Power Socket Availability",
        validators=[DataRequired()],
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],  # type:ignore
    )

    submit = SubmitField("Add")


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
        with open("cafe_data.csv", "+a", newline="", encoding="utf8") as csv_file:
            data = csv.writer(csv_file, delimiter=",")
            ass = [
                i.strftime("%H:%M%p") if type(i).__name__ == "time" else i
                for i in list(form.data.values())[:-2]
            ]
            data.writerow(ass)
            print(f"{ass}")
            return redirect(url_for("cafes"))

    return render_template("add.html", form=form)


@app.route("/delete")
def delete_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    return render_template("delete.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
