from flask import Flask, render_template
from random import randint
from datetime import date


app = Flask(__name__)

@app.route('/')
def home():
    current_year = date.today().year
    random_num = randint(1,100)
    return render_template("index.html",random_number = random_num, year = current_year)

if __name__ == "__main__":
    app.run(debug=True)
