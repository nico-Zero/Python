from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bold():
        return f"<b>{function()}</b>"
    return bold

def make_italic(function):
    def italic():
        return f"<i>{function()}</i>"
    return italic

def make_emphasis(function):
    def emphasis():
        return f"<em>{function()}</em>"
    return emphasis

def make_underline(function):
    def underline():
        return f"<u>{function()}</u>"
    return underline

@app.route("/")
@make_bold
@make_italic
@make_emphasis
@make_underline
def hello_world():
    return  "<h1 id='hello' class='h1_start'>Hello, World!</h1>"


@app.route("/bye")
def bye_world():
    return "<h1>Bye, World!</h1>"

@app.route('/user/<name>')
def greet(name):
    return f"Hello, {name}"

@app.route("/user/<name>/<int:age>")
def info(name, age):
    return f"<h3>Your Name is {name} and Your age is {age}.</h3>"


if __name__ == "__main__":
    app.run(debug=True)
