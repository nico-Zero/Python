# from functools import wraps
# from time import time

# # def speed_calculation_decorator(function):
# #     def speed_calculation():
# #         start_time = time()
# #         function()
# #         finish_time = time()

# #         return finish_time - start_time

# #     return speed_calculation


# # @speed_calculation_decorator
# # def fast_function():
# #     for i in range(10**4):
# #         print(f"\n{i}")

# # @speed_calculation_decorator
# # def slow_function():
# #     for i in range(10**5):
# #         print(f"\n{i}")

# # fast_function_completion_time = fast_function()
# # slow_function_completion_time = slow_function()

# # print(fast_function_completion_time)
# # print(slow_function_completion_time)

# # print(f"The Difference in time:- {slow_function_completion_time - fast_function_completion_time}") # type: ignore

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
    
#     def login(self):
#         self.is_logged_in = True
    
#     def logout(self):
#         self.is_logged_in = False

# def is_authenticated(name):
#     print("Hello World!")
#     def inner(function):
#         print(f"Hello {name}!")
#         def wrapper(user):
#             if user.is_logged_in:
#                 function(user)
#         return wrapper
#     return inner


# @is_authenticated("Nico_Zero")
# def create_blog_post(user):
#     print(f"This is {user.name}'s blog post.")


# new_user = User("Nico_Zero")
# new_user.login()
# create_blog_post(new_user)


def logging_decorator(function):
    def inner_function(*args):
        print(f"You called {function.__name__}(" , ",".join([str(i) for i in args[0]]) if isinstance(args[0],tuple) else ",".join([str(i) for i in args]) ,")",sep="")
        print(f"It returned: {function(args[0] if isinstance(args[0], tuple) else tuple(args))}")
    return inner_function

@logging_decorator
def add(l:tuple):
    return sum(l) 

add(tuple(range(1,100)))
