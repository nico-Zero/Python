from flask import Flask
from random import randint
from markupsafe import escape


app = Flask(__name__)
lucky_number = randint(1,10)
x = 0


@app.route("/")
def home():
    return "<h1>Guess the lucky Number between 1 and 10.</h1>" \
            "<h1>And right the input in URL Bar.</h1>" \
            "<img src='https://media3.giphy.com/media/l378khQxt68syiWJy/200w.webp?cid=ecf05e47m7f9svgzot3oqfigiybal5avh5fkxvuxhg7whxi8&ep=v1_gifs_search&rid=200w.webp&ct=g' width='500px' hight='1000px'>"

@app.route("/<int:number>")
def high_low(number):
    global x, lucky_number
    if x >= 3:
        x=1
        lucky_number = randint(1,10)
    else:
        x += 1
    
    print(lucky_number)
    if not 1 <= number <= 10:
        return f"<h1>{escape(number)} FOR REAL NIGGER!!!</h1>" \
            "<img src='https://media3.giphy.com/media/2NABZ6SkKNTGjD6D2D/200.webp?cid=ecf05e47l1db6o0lxqvdrn6o55laqq2uywclopuia9xlmkkl&ep=v1_gifs_search&rid=200.webp&ct=g' width='500px' hight='1000px'>"
    elif number == lucky_number:
        return f"<h1>Yes {escape(number)} is the lucky Number.</h1>" \
            "<img src='https://media2.giphy.com/media/5exwXWg9u7yow/giphy.webp?cid=ecf05e47f6m1isnx40bg3locofjnscuj75w5tvdz0y4ehtsa&ep=v1_gifs_search&rid=giphy.webp&ct=g' width='500px' hight='1000px'>"
    elif number < lucky_number:
        return f"<h1>No {escape(number)} is lower then the lucky Number.</h1>" \
            "<img src='https://media1.giphy.com/media/Ib6HtcZMKdPHaBj1R2/giphy.webp?cid=ecf05e471vx80lh1d1eakpkgv50b0e591s375ixvvzcpohh9&ep=v1_gifs_search&rid=giphy.webp&ct=g' width='500px' hight='1000px'>"
    elif number > lucky_number:
        return f"<h1>No {escape(number)} is higher then the lucky Number.</h1>" \
            "<img src='https://media3.giphy.com/media/y9hjvnO2bwJbO/200.webp?cid=ecf05e476jrjf4358srip2820a4xuq1o4cmh6e4muyousbao&ep=v1_gifs_search&rid=200.webp&ct=g' width='500px' hight='1000px'>"
    else:
        return f"<h1>{escape(number)} FOR REAL NIGGER!!!</h1>" \
            "<img src='https://media3.giphy.com/media/2NABZ6SkKNTGjD6D2D/200.webp?cid=ecf05e47l1db6o0lxqvdrn6o55laqq2uywclopuia9xlmkkl&ep=v1_gifs_search&rid=200.webp&ct=g' width='500px' hight='1000px'>"

if __name__ == "__main__":
    app.run(debug=True)
