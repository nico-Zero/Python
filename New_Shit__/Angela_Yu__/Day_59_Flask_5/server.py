from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def home():
    blogs = requests.get(" https://api.npoint.io/8c3e6fb14d194fc2c75c")
    blogs.raise_for_status()
    blogs = blogs.json()
    with open("data.json", "w") as data_file:
        data_file.write(json.dumps(blogs, indent=4))

    image = "../static/assets/img/home-bg.jpg"

    return render_template("index.html", img=image, blog_posts=blogs)


@app.route("/contact")
def contact():
    image = "../static/assets/img/contact-bg.jpg"
    return render_template("contact.html", img=image)


@app.route("/about")
def about():
    image = "../static/assets/img/about-bg.jpg"
    return render_template("about.html", img=image)


@app.route("/post/<int:blog_id>")
def post(blog_id):
    with open("data.json") as data_file:
        blog_data = json.load(data_file)
        blog = [post for post in blog_data if post["id"] == blog_id][0]

    image = "../static/assets/img/post-bg.jpg"

    return render_template("post.html", img=image, post=blog)


if __name__ == "__main__":
    app.run(debug=True)
