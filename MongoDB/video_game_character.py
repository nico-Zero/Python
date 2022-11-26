import copy
import numpy as np

from pymongo import MongoClient


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
potion = Item("health_potion", 2, [{"heal": 10}])


# TODO:
# 1) Initalize a MongoDB Client object to connect to your database with
client = MongoClient("mongodb://localhost:27017")
game_db = client["video_game"]

# TODO:
# 2) Create a function that takes in a Player object and inserts it into the database,
#    Extra Challenge: check for duplicate player entries, if so, do not insert again

tom = Player("tom", 100, 200, [potion, potion])


def insert_player(player):
    for data in player:
        will_i_data = {
            "name": data.name,
            "max_health": data.max_health,
            "max_energy": data.max_energy,
            "items": [
                {"name": x.name, "quantity": x.quantity, "effects": x.effects}
                for x in data.items
            ],
        }
        print("Inserted")


insert_player([tom])

# 3) Create a function that is able to find a Player in the databse by searching for their name


# 4) Create a function that loads the data from the above function and returns a Player object configured with that data

# TODO:
# 5) Create at least 2 players, optionally give them items


# 6) Insert Players into MongoDB


# 7) Load the player data from MongoDB into new player variables
