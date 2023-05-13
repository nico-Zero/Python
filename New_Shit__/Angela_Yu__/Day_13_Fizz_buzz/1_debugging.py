# from random import randint, choice

x = "❌🯀❌"

# def my_function():
#     for i in range(1,21):
#         if i == 20:
#             print("You get it.")

# my_function()
#################################################################################################
# dice_image = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
# dice_num = randint(0, len(dice_image)-1)

# print(dice_image[dice_num])
#################################################################################################

# year = int(input("What is your birth year? "))
# if 1994 > year >= 1980 :
#     print("You are millennial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

#################################################################################################

# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")
#################################################################################################

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_pages = int(input("Number of words per pages: "))
# total_words = pages * word_per_pages
# print(total_words)
#################################################################################################


def mutate_list(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate_list(range(1, 15, 2))

