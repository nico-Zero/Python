import functools

# def start_end_decorator(func):
#     def wrapper():
#         print("Start")
#         func()
#         print("End")
#     return wrapper

# @start_end_decorator
# def name():
#     print("Zero")
# # name = start_end_decorator(name) 
# name()

# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Start")
#         r =func(*args, **kwargs)
#         print("End")
#         return r
#     return wrapper

# @start_end_decorator
# def add69(x):
#     return print(x + 69)
# # add69 = start_end_decorator(name) 
# add69(44)


# print(help(add69))
# print(add69.__name__)

# def repeat(num_times):
#     def decorator_r(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kwargs):
#             for _ in range(num_times):
#                 r = func(*args, **kwargs)
#             return r
#         return wrapper
#     return decorator_r

# @repeat(num_times=10)
# def greet(name):
#     print(f"Hello, {name}")

# greet("Zero")
        
