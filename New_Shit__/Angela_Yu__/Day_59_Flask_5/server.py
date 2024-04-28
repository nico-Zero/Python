from flask import Flask, render_template
from datetime import date
import requests
import json


app = Flask(__name__)


@app.route("/")
def home():
    blogs = requests.get("https://api.npoint.io/b319f78fbe9660d688d9")
    blogs.raise_for_status()
    blogs = blogs.json()
    with open("data.json", "w") as data_file:
        data_file.write(json.dumps(blogs, indent=4))

    image = "../static/assets/img/home-bg.jpg"
    year = date.today().year

    return render_template("index.html", img=image, blog_posts=blogs, current_year=year)


@app.route("/contact")
def contact():
    image = "../static/assets/img/contact-bg.jpg"
    year = date.today().year

    return render_template("contact.html", img=image, current_year=year)


@app.route("/about")
def about():
    image = "../static/assets/img/about-bg.jpg"
    year = date.today().year

    return render_template("about.html", img=image, current_year=year)


@app.route("/post/<int:blog_id>")
def post(blog_id: int):
    with open("data.json") as data_file:
        blog_data = json.load(data_file)
        blog = [post for post in blog_data if post["id"] == blog_id][0]

    image = "../static/assets/img/post-bg.jpg"
    year = date.today().year

    return render_template("post.html", img=image, post=blog, current_year=year)


@app.route("/page/<int:page_number>")
def page(page_number: int):
    with open("data.json") as data_file:
        blogs = json.load(data_file)

    year = date.today().year
    image = "../static/assets/img/home-bg.jpg"

    return render_template(
        "page.html",
        img=image,
        current_year=year,
        blog_posts=blogs,
        page_=page_number,
        next_page=page_number + 1,
        previous_page=page_number - 1,
    )


if __name__ == "__main__":
    app.run(debug=True)
