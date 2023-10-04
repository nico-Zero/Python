# # # # from email.message import EmailMessage
# # # # import smtplib
# # # # import ssl

# # # # our_email = "zandaxheart955@gmail.com"
# # # # password = "slemixowrmjmezyt"

# # # # email = "nico.zero.0x@gmail.com"

# # # # subject = "Contact By Blog Site"
# # # # message = "Hello NicoZero!"


# # # # em = EmailMessage()
# # # # em["From"] = our_email
# # # # em["To"] = email
# # # # em["subject"] = subject
# # # # em.set_content(message)

# # # # context = ssl.create_default_context()

# # # # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
# # # #     smtp.login(our_email, password)
# # # #     smtp.sendmail(our_email, email, em.as_string())

# # # # print("successfully sent👌👌")


# # # from bs4 import BeautifulSoup
# # # import requests


# # # anime = [
# # #     "https://sanji.to/user/watch-list?type=1&sort=",
# # #     "https://sanji.to/user/watch-list?type=1&sort=&page=2",
# # #     "https://sanji.to/user/watch-list?type=1&sort=&page=3",
# # # ]

# # # x = []

# # # for site in anime:
# # #     with open("100_html_data1.html") as file:
# # #         html = file.read()

# # #     soup_data = BeautifulSoup(html, "html.parser")
# # #     data = soup_data.find_all(name="a", class_="dynamic-name")
# # #     for i in data:
# # #         i = i.getText()
# # #         x.append(i)

# # # x = set(x)
# # # with open("anime.txt","a") as file:
# # #     for i,j in enumerate(x):
# # #         file.write(f"{str(i)}. {j}\n")

# # # print(*x,sep="\n")


# # # def grater_then(a, b):
# # #     if a > b:
# # #         return a
# # #     else:
# # #         return b


# # # def grater_then_2(a, b):
# # #     return a * (a >= b) + b * (a < b)


# # # def test(*args, functions=[]):
# # #     for function in functions:
# # #         print(function(*args))


# # # test(5, 5, functions=[grater_then, grater_then_2])


# # def add_numbers(a, b):
# #     """
# #     This function adds two numbers and returns the result.
# #     Parameters:
# #         a (int): The first number.
# #         b (int): The second number.
# #     Returns:
# #         int: The sum of the two numbers.
# #     """
# #     return a + b


# # # To access the docstring of the function:
# # print(help(add_numbers))

# print(ord("h"))


from prettytable import PrettyTable
from prettytable import SINGLE_BORDER,FRAME
x = PrettyTable()
x.set_style(SINGLE_BORDER)
x.header = False
x.hrules = FRAME.

x.add_row(["🌕","🌕","🌕","🌕"],divider=True)
x.add_row(["🌕","🌕","🌕","🌕"],divider=True)
x.add_row(["🌕","🌕","🌕","🌕"],divider=True)
x.add_row(["🌕","🌕","🌕","🌕"],divider=True)
x.add_row(["🌕","🌕","🌕","🌕"],divider=True)
x.add_row(["🌕","🌕","🌕","🌕"],divider=True)

print(x)