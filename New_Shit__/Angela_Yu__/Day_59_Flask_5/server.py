from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    image = "../static/assets/img/home-bg.jpg"
    return render_template("index.html", img=image)


@app.route("/contact")
def contact():
    image = "../static/assets/img/contact-bg.jpg"
    return render_template("contact.html", img=image)


@app.route("/about")
def about():
    image = "../static/assets/img/about-bg.jpg"
    return render_template("about.html", img=image)


@app.route("/post")
def post():
    image = "../static/assets/img/post-bg.jpg"
    return render_template("post.html", img=image)


if __name__ == "__main__":
    app.run(debug=True)
