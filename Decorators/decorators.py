import functools

# # Function without arguments.
# def start_end_decorator(func):
#     def wrapper():
#         print("Start")
#         func()
#         print("End")
#     return wrapper

# # A decorator below.
# @start_end_decorator
# def print_name():
#     print("Alex")


# #This line will do the same thing as above decorator.
# # print_name = start_end_decorator(print_name)

# print(print_name)


# # # # Function with argument


# def start_end_decorator(func):

#     # @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print("Start")
#         result = func(*args,**kwargs)
#         print("End")
#         return result

#     return wrapper

# # A decorator below.
# @start_end_decorator
# def add5(x):
#     return x + 5;

# # print(help(add5(10)))
# print(add5(10))


# # Decorator with an argument.

def repeat(num_times):

    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=(int(input("How many to run the function:- "))))
def greet(name):
    print(f"Hello {name}")

greet("Yuvraj")


# def start_end_decorator(func):

#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print("Start")
#         result = func(*args,**kwargs)
#         print("End")
#         return result
#     return wrapper

# def debug(func) :
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
#         signature = ",".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args,**kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper

# @debug
# @start_end_decorator
# def say_hello(name):
#     greeting = f"Hello {name}"
#     print(greeting)
#     return greeting

# say_hello("Alex")


# class CountCalls:
#     def __init__(self, func):
#         self.func = func
#         self.num_calls = 0

#     def __call__(self, *args, **kwargs):
#         self.num_calls += 1
#         print(f"Number of the function calls:- {self.num_calls}")
#         return self.func(*args, **kwargs)

# @CountCalls
# def say_hello():
#     print("Hello")


# say_hello()
# say_hello()
# say_hello()
