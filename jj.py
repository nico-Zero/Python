# import csv


# def remember_score(name, score):
#     with open("/media/zero/Software/Python/jj.csv", "a") as file:
#         file_mark_2 = csv.writer(file)
#         file_mark_2.writerow([name, score])


# while 1:
#     name = input("what is your name? ")
#     highest_score = input("What's the highest score? ")
#     remember_score(name, highest_score)

from customtkinter import *

set_appearance_mode("Dark")

display = CTk()
display.title("What is your name? ")
display.geometry("600x300")
label = CTkLabel(text="What is your name? ")
label.pack()

name = CTkEntry()
name.pack()


display.mainloop()
# # import csv


# # def remember_score(name, score):
# #     with open("/media/zero/Software/Python/jj.csv", "a") as file:
# #         file_mark_2 = csv.writer(file)
# #         file_mark_2.writerow([name, score])


# # while 1:
# #     name = input("what is your name? ")
# #     highest_score = input("What's the highest score? ")
# #     remember_score(name, highest_score)

# from customtkinter import *

# set_appearance_mode("Dark")

# display = CTk()
# display.title("What is your name? ")
# display.geometry("600x300")
# label = CTkLabel(text="What is your name? ")
# label.pack()

# name = CTkEntry()
# name.pack()


# display.mainloop()
