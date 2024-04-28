from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return  "<h1 id='hello' class='h1_start' style='text-align : center' >Hello, World!</h1>" \
            "<img src='https://media.tenor.com/bK1qpWGyQKkAAAAd/kitty.gif' width='200px' height='300px'>" \
            "<img src='https://media.tenor.com/9SRPROM5RAcAAAAM/kitten-kitty.gif'>" \
            "<img src='https://media4.giphy.com/media/8OPbx53X3mFoWMw5aO/giphy.gif?cid=ecf05e478r12d5viparm6qitml85ox8gg462oki26kiqm4c0&ep=v1_gifs_search&rid=giphy.gif&ct=g'>" \
            "<img src='https://media4.giphy.com/media/3GRwYzxwdceaI/giphy.gif?cid=ecf05e478r12d5viparm6qitml85ox8gg462oki26kiqm4c0&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"

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
