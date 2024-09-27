# while 1:
#     try:
#         n = int(input("Enter a number:- "))
#         d = int(input("Enter a number:- "))
#         result = n/d
#         print(result)
#     except:
#         print("Error!!!")
from logging import exception


try:
    n = int(input("Enter a number:- "))
    d = int(input("Enter a number:- "))
    result = n/d
except ZeroDivisionError as e:
    print("Error!!! >>>",e)
    print("You can't divide by zero")
except ValueError as e:
    print("Error!!! >>>",e)
    print("you can't divide a string with a number.DUMB_ASS")
except Exception as e:
    print("Error!!! >>>",e)
else:
    print(result)
finally:
    print("Done...")