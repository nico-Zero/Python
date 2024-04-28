# from flask import Flask
# import heapq

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


# if __name__ == "__main__":
#     app.run()

from time import time

def speed_calculation_decorator(function):
    def speed_calculation():
        start_time = time()
        function()
        finish_time = time()

        return finish_time - start_time

    return speed_calculation


@speed_calculation_decorator
def fast_function():
    for i in range(10**4):
        print(f"\n{i}")

@speed_calculation_decorator
def slow_function():
    for i in range(10**5):
        print(f"\n{i}")

fast_function_completion_time = fast_function()
slow_function_completion_time = slow_function()

print(fast_function_completion_time)
print(slow_function_completion_time)

print(f"The Difference in time:- {slow_function_completion_time - fast_function_completion_time}")

