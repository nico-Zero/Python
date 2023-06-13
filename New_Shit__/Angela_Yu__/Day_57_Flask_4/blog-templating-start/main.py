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

    return render_template("index.html", blog_posts=blogs)


@app.route("/post/<int:blog_id>")
def blog_post(blog_id: int):
    with open("data.json") as data_file:
        blog_data = json.load(data_file)
        blog = [post for post in blog_data if post["id"] == blog_id]

    return render_template("post.html", post=blog[0])


if __name__ == "__main__":
    app.run(debug=True)
