# from flask import Flask
# import heapq

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"



# if __name__ == "__main__":
#     app.run()


def add(a,b):
    return a + b


def subtract(a,b):
    return a- b

def divide(a,b):
    return a/b

def multiply (a,b):
    return a*b

def calculator (calculator_function, n1, n2):
    return calculator_function(n1, n2)

print(calculator(add, 23,34))


