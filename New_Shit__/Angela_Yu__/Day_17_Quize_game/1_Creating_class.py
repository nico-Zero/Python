from faker import Faker


class User:
    def __init__(self, id, username="Nova", followers=0, following=0):
        self.id = id
        self.username = username
        self.followers = followers
        self.following = following

    def follow(self, user):
        user.followers += 1
        self.following += 1


class Car:
    def __init__(self, name="__car__", seats=4):
        self.name = name
        self.seats = seats

    def enter_race_mode(self):
        self.seats = 2


f = Faker()

user_1 = User(f.random_int(), f.name())
user_2 = User(f.random_int(), f.name())

user_1.follow(user_2)

print(
    "Id:",
    user_1.id,
    "User:",
    user_1.username,
    "followers:",
    user_1.followers,
    "following:",
    user_1.following,
)

print(
    "Id:",
    user_2.id,
    "User:",
    user_2.username,
    "followers:",
    user_2.followers,
    "following:",
    user_2.following,
)

# car = Car()

# car.enter_race_mode()


# print(car.name, car.seats)
