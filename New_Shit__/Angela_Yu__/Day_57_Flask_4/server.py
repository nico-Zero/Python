from flask import Flask, render_template
from random import randint
from datetime import date
import requests


app = Flask(__name__)


@app.route("/")
def home():
    current_year = date.today().year
    random_num = randint(1, 100)
    return render_template("index.html", random_number=random_num, year=current_year)


@app.route("/guess/<string:name>")
def guess(name: str):
    gender = requests.get(f"https://api.genderize.io/?name={name}")
    gender.raise_for_status()
    gender = gender.json()["gender"]

    age = requests.get(f"https://api.agify.io/?name={name}")
    age.raise_for_status()
    age = age.json()["age"]

    return render_template("guess.html", name=name.capitalize(), gender=gender, age=age)


@app.route("/blogs/<int:l_number>")
def blog(l_number):
    current_year = date.today().year
    blogs = requests.get(" https://api.npoint.io/8c3e6fb14d194fc2c75c")
    blogs.raise_for_status()
    blogs = blogs.json()

    return render_template(
        "blog.html", all_posts=blogs, year=current_year, lucky_number=l_number
    )


if __name__ == "__main__":
    app.run(debug=True)
