from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template(
        "login.html", user_name=request.form["name_"], password=request.form["password"]
    )


if __name__ == "__main__":
    app.run(debug=True)
