from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!<p>"


@app.route("/bye")
def bye_world():
    return "<p>Bye, World!<p>"

@app.route('/user/<name>')
def greet(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    app.run(debug=True)

