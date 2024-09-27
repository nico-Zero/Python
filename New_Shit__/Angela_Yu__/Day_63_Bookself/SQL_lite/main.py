from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

app = Flask(__name__)
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book_keeping.db"
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    author = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float(10), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    book = Books(title="Nova_The_Star", author="Nico_zero", rating=10)
    db.session.add(book)
    db.session.commit()

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
