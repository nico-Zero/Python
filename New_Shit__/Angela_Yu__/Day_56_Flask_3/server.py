from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/my_cv')
def my_cv():
    return render_template('cv_index.html')

if __name__ == "__main__":
    app.run(debug=True)
