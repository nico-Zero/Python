# # coding challenge 1

# fruits = ["Apple", "Pear", "Orange"]


# def make_pie(index):
#     try:
#         fruit = fruits[int(index)]
#     except IndexError:
#         print("Fruit pie")
#     except ValueError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")


# while 1:
#     make_pie(input("Enter a index for pie:- "))


facebook_posts = [
    {'Likes': 21, 'Comments':2},
    {'Likes': 13, 'Comments':2,'Shares':1},
    {'Likes': 33, 'Comments':8,'Shares':3},
    {'Comments':4,'Shares':2},
    {'Comments':1,'Shares':1},
    {'Likes': 19, 'Comments':3},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        pass

print(total_likes)
