from flask import Flask , render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# TODO : Will make a really good potfolio site for my self.