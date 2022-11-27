import copy
import numpy as np
from faker import Faker
from pymongo import MongoClient
from random import randint


class Player:
    def __init__(self, name, max_health, max_energy, items=[]):
        self.name = name
        self.health = max_health
        self.max_health = max_health
        self.energy = max_energy
        self.max_energy = max_energy
        self.items = copy.deepcopy(items)

    def attack(self, player):
        energy_cost = 5

        if self.energy >= energy_cost:
            attack_strength = np.random.randint(1, 6)
            player.health -= attack_strength
            self.energy -= energy_cost
            print(
                "{} attacked {} for {} damage".format(
                    self.name, player.name, attack_strength
                )
            )
        else:
            print(
                "{} does not have enough energy to attack {}".format(
                    self.name, player.name
                )
            )

    def heal(self, amount):
        self.health += amount

        if self.health > self.max_health:
            self.health = self.max_health

    def stats(self):
        return vars(self)

    def use_item(self, item_name):
        try:
            item = next(item for item in self.items if item.name == item_name)
            item.quantity -= 1

            for effect in item.effects:

                for method, value in effect.items():
                    class_method = getattr(self, method)
                    class_method(value)

            if item.quantity == 0:
                self.items.remove(item)

        except:
            print("{} does not have any {}s".format(self.name, item_name))


class Item:
    def __init__(self, name, quantity, effects=[]):
        self.name = name
        self.quantity = quantity
        self.effects = effects

    def __repr__(self):
        return "Item(name={}, quantity={}, effects={})".format(
            self.name, self.quantity, self.effects
        )


# Example usage of Item:
potion = Item("Health potion", 2, [{"heal": 10}])
sword = Item("Demon sword", 1, [{"damage": 100}])
bow = Item("Holy bow", 2, [{"heal": 90}])


# TODO:
# 1) Initalize a MongoDB Client object to connect to your database with
client = MongoClient("mongodb://localhost:27017")
game_db = client["video_game"]

# TODO:
# 2) Create a function that takes in a Player object and inserts it into the database,
#    Extra Challenge: check for duplicate player entries, if so, do not insert again

fake = Faker()


def insert_player(player):
    for data in player:
        list_of_player_names = [
            i["name"] for i in list(game_db["player"].find({}, {"_id": 0, "name": 1}))
        ]
        print(list_of_player_names)
        if data.name not in list_of_player_names:
            will_i_data = {
                "name": data.name,
                "max_health": data.max_health,
                "max_energy": data.max_energy,
                "items": [
                    {"name": x.name, "quantity": x.quantity, "effects": x.effects}
                    for x in data.items
                ],
            }
            game_db["player"].insert_one(will_i_data)
            print(f"Inserted player data of {data.name} to database.")
        else:
            print(f"Already a player named {data.name} in database.")


# 3) Create a function that is able to find a Player in the databse by searching for their name


def find_player(player_name):
    player = game_db["player"].find_one({"name": player_name})
    print("\n", player)
    return player


# print(find_player(input("Enter a player name to find:- ")))


# 4) Create a function that loads the data from the above function and returns a Player object configured with that data


def create_player_object(player_data):
    return Player(
        player_data["name"],
        player_data["max_health"],
        player_data["max_energy"],
        player_data["items"],
    )


# TODO:
# 5) Create at least 2 players, optionally give them items
player_objects = [
    Player(
        fake.name(),
        randint(10000, 100000),
        randint(10000, 100000),
        [potion, potion, sword, sword, bow],
    )
    for _ in range(int(input("Enter number of players:- ")))
]

# 6) Insert Players into MongoDB
insert_player(player_objects)


# 7) Load the player data from MongoDB into new player variables
player_x = create_player_object(find_player(input("Enter a player name to find:- ")))
print("\n", type(player_x))
