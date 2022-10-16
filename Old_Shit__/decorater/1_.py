import functools

# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print("Start")
#         result = func(*args,**kwargs)
#         print("End")
#         return result
#     return wrapper

# # @start_end_decorator
# # def add_69(number: int):
# #     return number + 69

# # # print_name = start_end_decorator(print_name)

# # # num = add_69(69)
# # print(help(add_69))
# # print(add_69.__name__)
# # # print(num)

# #######################################
# #######################################

# # def repeat(num_times):
# #     def decorator_repeat(func):
# #         @functools.wraps(func)
# #         def wrapper(*args,**kwargs):
# #             for _ in range(num_times):
# #                 result = func(*args,**kwargs)
# #             return result
# #         return wrapper
# #     return decorator_repeat

# # @repeat(num_times = 5)

# # @debug
# @start_end_decorator
# def greet(name):
#     print(f"Hello {name}")

# greet("Zero")

class CountCalls:
    def __init__(self,func):
        self.func = func
        self.num_calls = 0
    def __call__(self,*args,**kwargs):
        self.num_calls += 1
        print(f"This function has exicuted {self.num_calls} times.")
        return self.func(*args,**kwargs)
        
@CountCalls
def say_hello():
    print("hello")

say_hello()
say_hello()
say_hello()