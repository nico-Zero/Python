from os import system
from beautifultable import BeautifulTable

class Tic_Tac_Toe:
    def __init__(self, player_1="", player_2="") -> None:
        self.player_1: str = player_1
        self.player_2: str = player_2
        self.__game_map_array: list = []
        self.__game_map = BeautifulTable()
        self.__game_map.set_style(BeautifulTable.STYLE_BOX_ROUNDED)  # type: ignore
        self.__dimensions: int = 3
        self.__move_count: dict = {}
        self.__current_player: str = ""
        self.__current_move: tuple = ()
        self.__weapons: dict = {}
        system("cls")

    def run(self):
        self.setup()
        while True:
            self.__display()
            self.__take_move()
            self.__use_weapon()
            if self.__check_result() == "End":
                self.__display()
                print(f"🌟 🌟 🌟 {self.__current_player.capitalize()} Wno 🌟 🌟 🌟")
                break
            elif self.__check_result() == "Drew":
                self.__display()
                print(f"The Game Got Drew !!!")
                break
            self.__switch_player()
        self.__restart()
        
    def __restart(self):
        if input("Want to play again ('y' or 'n')?:- ").lower in ["y", "n"]:
            self.run()

    def setup(self):
        self.__dimensions = self.__get_dim()
        self.__game_map_array = self.__generate_map(
            self.__dimensions, self.__dimensions
        )
        if not (self.player_1 and self.player_2):
            self.player_1, self.player_2 = self.__get_players_name()
        self.__current_player = self.player_1
        self.__move_count = {self.player_1: 0, self.player_2: 0}
        self.__weapons = {self.player_1: "⭐", self.player_2: "🌑"}

    def __check_result(self):
        __result_array = self.__game_map_array.copy()
        for i in range(len(self.__game_map_array)):
            __result_array.append([j[i] for j in self.__game_map_array])
        __result_array.append(
            [
                y[x]
                for x, y in zip(
                    range(len(self.__game_map_array)), self.__game_map_array
                )
            ]
        )
        __result_array.append(
            [
                y[x]
                for x, y in zip(
                    range(len(self.__game_map_array) - 1, -1, -1), self.__game_map_array
                )
            ]
        )
        if any(
            [
                i.count(self.__weapons[self.__current_player]) == len(i)
                for i in __result_array
            ]
        ):
            return "End"
        elif not any([x == "" for i in self.__game_map_array for x in i]):
            return "Drew"

    def __check_move(self):
        weapon = self.__game_map_array[self.__current_move[0] - 1][
            self.__current_move[1] - 1
        ]
        if weapon == "":
            return True
        else:
            if weapon == self.__weapons[self.player_1]:
                print(
                    f"{'You' if self.__current_player == self.player_1 else self.player_1} Already Marked That Place !!!"
                )
                return False
            else:
                print(
                    f"{'You' if self.__current_player == self.player_2 else self.player_2} Already Marked That Place !!!"
                )
                return False

    def __use_weapon(self):
        self.__game_map_array[self.__current_move[0] - 1][
            self.__current_move[1] - 1
        ] = self.__weapons[self.__current_player]
        self.__move_count[self.__current_player] += 1

    def __take_move(self):
        while True:
            __move = input(f"{self.__current_player}'s move :- ")
            __move = [int(i) for i in __move.split(" ") if i.isnumeric()]
            if len(__move) >= 2 and all(
                [True if 0 < i <= self.__dimensions else False for i in __move[:2]]
            ):
                self.__current_move = tuple(__move[:2])
                if self.__check_move():
                    break
            else:
                print("Invalid Move !!!")

    def __switch_player(self):
        if self.__current_player == self.player_1:
            self.__current_player = self.player_2
        else:
            self.__current_player = self.player_1

    def get_move_count(self):
        return (self.__move_count[self.player_1], self.__move_count[self.player_2])

    def __generate_map(self, *shape: int) -> list[list[str]]:
        def array(axes):
            if not shape or shape[axes] <= 0:
                raise ValueError("length must be grater then Zero!!!")
            elif len(shape) == axes + 1:
                return list("" for _ in range(shape[axes]))
            elif len(shape) > axes:
                return list(array(axes + 1) for _ in range(shape[axes]))

        return array(0)  # type: ignore

    def __get_dim(self):
        while True:
            dim = input("Enter the game dimensions (>=3):- ")
            if dim.isnumeric():
                dim = int(dim)
            else:
                print("Enter right dimensions number !!!")
                continue
            if dim < 3:
                print("Enter right dimensions number !!!")
                continue
            return dim

    def __display(self):
        if not bool(self.__game_map):
            for array in self.__game_map_array:
                self.__game_map.rows.append(array)
        else:
            for array in zip(range(len(self.__game_map_array)), self.__game_map_array):
                self.__game_map.rows[array[0]] = array[1]

        system("cls")
        print(self.__game_map)

    def __get_players_name(self):
        return (input("Enter player 1 name :- "), input("Enter player 2 name :- "))


game = Tic_Tac_Toe()
game.run()
