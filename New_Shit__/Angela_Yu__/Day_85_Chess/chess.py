############################################################## Made by Zero-Nico ##############################################################

from os import system
from beautifultable import BeautifulTable
from termcolor import colored
from platform import uname


commands = {"clear_screen": "cls" if uname().system == "Windows" else "clear"}


def clear():
    system(commands["clear_screen"])


class Player:
    def __init__(
        self,
        player_number: int,
        name: str = "",
        color: str = "",
        game_mode: int = 2,
    ) -> None:
        self.player_number = player_number
        self.name = name
        self.color = color
        self.color_list = [
            "black",
            "red",
            "green",
            "yellow",
            "blue",
            "magenta",
            "cyan",
            "white",
            "light_grey",
            "dark_grey",
            "light_red",
            "light_green",
            "light_yellow",
            "light_blue",
            "light_magenta",
            "light_cyan",
        ]
        self.game_mode = game_mode
        self.chess_pieces: dict = {}
        self.chess_pieces_locations: dict = {}
        self.dead_piece_locations: dict = {}
        self.moves = MoveSet(self.player_number, self)
        self.all_pieces_can: dict = {}
        self.all_enemy_piece_locations: dict = {}
        self.all_enemy_pieces_can: dict = {}
        self.got_check: bool = False
        self.got_check_mated: bool = False
        self.got_check_by: dict = {}
        self.can_only_counter_by: dict = {}
        self.pawn_power_up_row: int = 0
        self.upgradable_pawn: dict = {}
        self.pawn_upgrades: dict = {}

    def setup(self, invalid_name: dict = {}, remove_color: str = "") -> None:
        while True:
            self.name = (
                input(f"Enter player {self.player_number} name :- ").capitalize()
                if self.name == ""
                else self.name
            )
            if self.name == "#exit":
                exit()
            if len(self.name) == 0:
                print("Invalid name !!!")
                continue
            if self.name in invalid_name.values():
                for p_number, p_name in invalid_name.items():
                    if p_name == self.name:
                        print(f"Player {p_number} choose {self.name} first !!!")
                continue
            break

        if remove_color:
            self.color_list.remove(remove_color)
        print("Can choose color form :- ", self.color_list)
        while True:
            self.color = input(f"Enter Color :- ").lower()
            if self.color == "#exit":
                exit()
            if self.color in self.color_list:
                break
            print("Invalid Color !!!")

        self.__rearrange_pieces = (
            {
                1: self.__rearrange_player_1_pieces,
                2: self.__rearrange_player_2_pieces,
                3: self.__rearrange_player_3_pieces,
                4: self.__rearrange_player_4_pieces,
            }
            if self.game_mode == 4
            else {
                1: self.__rearrange_player_1_pieces,
                2: self.__rearrange_player_2_pieces,
            }
        )
        self.chess_pieces = self.__get_chess_pieces()
        self.chess_pieces_locations = self.__get_chess_pieces_location()
        self.__setup_player_pieces()
        self.__set_player_pieces_locations()
        if self.player_number == 1:
            self.pawn_power_up_row = 0
        elif self.player_number == 2:
            self.pawn_power_up_row = 7

        self.__update_pawn_upgrades()

        clear()

    def __get_chess_pieces(self) -> dict:
        chess_pieces = {
            "rook_1": colored("♜", self.color),
            "knight_1": colored("♞", self.color),
            "bishop_1": colored("♝", self.color),
            "queen": colored("♛", self.color),
            "king": colored("♚", self.color),
            "bishop_2": colored("♝", self.color),
            "knight_2": colored("♞", self.color),
            "rook_2": colored("♜", self.color),
            "pawn_1": colored("♟", self.color),
            "pawn_2": colored("♟", self.color),
            "pawn_3": colored("♟", self.color),
            "pawn_4": colored("♟", self.color),
            "pawn_5": colored("♟", self.color),
            "pawn_6": colored("♟", self.color),
            "pawn_7": colored("♟", self.color),
            "pawn_8": colored("♟", self.color),
        }
        return chess_pieces

    def __get_chess_pieces_location(self) -> dict:
        return {
            "rook_1": (),
            "knight_1": (),
            "bishop_1": (),
            "queen": (),
            "king": (),
            "bishop_2": (),
            "knight_2": (),
            "rook_2": (),
            "pawn_1": (),
            "pawn_2": (),
            "pawn_3": (),
            "pawn_4": (),
            "pawn_5": (),
            "pawn_6": (),
            "pawn_7": (),
            "pawn_8": (),
        }

    def __setup_player_pieces(self) -> None:
        self.chess_pieces = self.__rearrange_pieces[self.player_number](
            self.chess_pieces
        )
        self.chess_pieces_locations = self.__rearrange_pieces[self.player_number](
            self.chess_pieces_locations
        )

    def __rearrange_player_1_pieces(self, values) -> dict:
        return {
            name: pieces
            for name, pieces in list(values.items())[8:] + list(values.items())[:8]
        }

    def __rearrange_player_2_pieces(self, values) -> dict | None:
        if self.game_mode == 2:
            return {
                name: pieces
                for name, pieces in list(values.items())[:8][::-1]
                + list(values.items())[8:]
            }
        else:
            ...

    def __rearrange_player_3_pieces(self, values) -> None:
        ...

    def __rearrange_player_4_pieces(self, values) -> dict | None:
        ...

    def __set_player_pieces_locations(self) -> None:
        if self.player_number == 1:
            self.__set_locations(first_row=6, second_row=7)
        else:
            self.__set_locations(first_row=0, second_row=1)

    def __update_pawn_upgrades(self):
        self.pawn_upgrades: dict = {
            "rook": colored("♜", self.color),
            "knight": colored("♞", self.color),
            "bishop": colored("♝", self.color),
            "queen": colored("♛", self.color),
        }

    def __set_locations(self, first_row, second_row) -> None:
        self.chess_pieces_locations = {
            key: location
            for key, location in zip(
                self.chess_pieces_locations.keys(),
                [(first_row, position) for position in range(8)]
                + [(second_row, position) for position in range(8)],
            )
        }

    def get_selected_piece_moves(
        self, selected_piece_location, game_map_array, enemy_pieces_locations
    ) -> dict:
        return self.moves.get_moves(
            selected_piece_location, game_map_array, enemy_pieces_locations
        )

    def update_all_pieces_can(self, game_map_array):
        self.all_pieces_can = self.moves.get_all_pieces_moves(game_map_array)
        # print(f"{self.name} :- {self.all_pieces_can}")

    def get_piece_name(self, location):
        for piece_name, piece_location in self.chess_pieces_locations.items():
            if location == piece_location:
                return piece_name
        return None

    def got_killed(self, key: str | None = None) -> None:
        if key:
            self.dead_piece_locations[key] = self.chess_pieces_locations.pop(key)

    def can_pawn_power_up(self):
        all_pawns_locations = {
            piece_name: location
            for piece_name, location in self.chess_pieces_locations.items()
            if piece_name.split("_")[0] == "pawn"
        }
        for piece_name, location in all_pawns_locations.items():
            if location[0] == self.pawn_power_up_row:
                self.upgradable_pawn["name"] = piece_name
                self.upgradable_pawn["location"] = location
                return True
        return False

    def can_give_check(self, game_map_array):
        can_attack_king = self.moves.get_all_pieces_moves(
            game_map_array, {"king": self.all_enemy_piece_locations["king"]}
        )
        gave_check_by = {
            piece_name: piece_coordinates
            for piece_name, piece_coordinates in can_attack_king.items()
            if piece_coordinates["attack"]
        }

        check = False

        if any(gave_check_by):
            check = True

        return {
            "check": check,
            "gave_check_by": gave_check_by,
        }

    def update_values(self, checks):
        self.got_check = checks["check"]
        self.got_check_by = checks["gave_check_by"]

    def got_attack_ray_moves(self):
        return bool(self.moves.attack_ray)

    def reset_attack_ray_moves(self):
        self.moves.reset_attack_ray()

    def counter_check_by(self, game_map_array, checked_by_locations: dict, attack_ray):
        self.moves.update_attack_ray(attack_ray["move"])
        can_counter_check_by = self.moves.get_all_pieces_moves(
            game_map_array, checked_by_locations
        )

        if self.got_attack_ray_moves():
            can_counter_check_by = {
                piece_name: can
                for piece_name, can in can_counter_check_by.items()
                if can["move"] or can["attack"]
            }
        else:
            can_counter_check_by = {
                piece_name: can
                for piece_name, can in can_counter_check_by.items()
                if can["attack"]
            }
        for piece_name, moves in can_counter_check_by.items():
            self.can_only_counter_by[piece_name] = {
                "location": self.chess_pieces_locations[piece_name]
            } | moves

        return self.can_only_counter_by

    def reset_can_only_counter_by(self):
        self.can_only_counter_by = {}

    def check_for_check_mate(self):
        king_can = self.all_pieces_can["king"]
        if not (king_can["move"] or king_can["attack"]):
            if not self.can_only_counter_by:
                self.got_check_mated = True


class MoveSet:
    def __init__(self, player_number, player: Player) -> None:
        self.player_number: int = player_number
        self.player = player
        self.__move_map = {
            "rook": self.__get_rook_moves,
            "knight": self.__get_knight_moves,
            "bishop": self.__get_bishop_moves,
            "king": self.__get_king_moves,
            "queen": self.__get_queen_moves,
            "pawn": self.__get_pawn_moves,
        }
        self.__attack_ray_function_list = {
            "rook": self.__rook_attack_ray,
            "knight": self.__knight_attack_ray,
            "bishop": self.__bishop_attack_ray,
            "king": self.__king_attack_ray,
            "queen": self.__queen_attack_ray,
            "pawn": self.__pawn_attack_ray,
        }
        self.selected_piece_location: tuple = ()
        self.filtered_selected_piece_name: str
        self.game_map_array: list
        self.enemy_pieces_locations: dict
        self.__current_piece_can: dict = {"move": [], "attack": []}
        self.__skip: bool = False
        self.attack_ray: list = []

    def __get_rook_moves(self) -> dict:
        ranges = {
            key: [
                range(self.selected_piece_location[index] - 1, -1, -1),
                range(self.selected_piece_location[index] + 1, 8, 1),
            ]
            for index, key in enumerate(["v_ranges", "h_ranges"])
        }

        for range_set, coordinate_function in [
            (ranges["v_ranges"], self.__updated_y_coordinate),
            (ranges["h_ranges"], self.__updated_x_coordinate),
        ]:
            for _ran in range_set:
                for x in _ran:
                    if self.__check_coordinate(coordinate_function(x)):
                        self.__current_piece_can["move"].append(coordinate_function(x))
                    else:
                        attack = coordinate_function(x)
                        if self.__can_attack(attack):
                            self.__current_piece_can["attack"].append(attack)
                        break

        return self.__current_piece_can

    def __updated_y_coordinate(self, y) -> tuple:
        return (y, self.selected_piece_location[1])

    def __updated_x_coordinate(self, x) -> tuple:
        return (self.selected_piece_location[0], x)

    def __check_coordinate(self, coordinate):
        try:
            if (0 <= coordinate[0] < 8) and (0 <= coordinate[1] < 8):
                if self.filtered_selected_piece_name == "king":
                    values = self.player.all_enemy_pieces_can.values()
                    moves = set(sum([moves["move"] for moves in values], []))
                    return not (coordinate in moves) and (
                        self.game_map_array[coordinate[0]][coordinate[1]] == ""
                    )
                else:
                    if self.attack_ray:
                        return coordinate in self.attack_ray
                    else:
                        return self.game_map_array[coordinate[0]][coordinate[1]] == ""
            else:
                return False
        except:
            raise ValueError("Invalid Move passed in '__check_coordinate' !!!")

    def __get_knight_moves(self) -> dict:
        ranges = {
            key: [
                range(
                    self.selected_piece_location[index] - 1,
                    self.selected_piece_location[index] - 3,
                    -1,
                ),
                range(
                    self.selected_piece_location[index] + 1,
                    self.selected_piece_location[index] + 3,
                    1,
                ),
            ]
            for index, key in enumerate(["v_ranges", "h_ranges"])
        }

        for y in ranges["v_ranges"]:
            for x in ranges["h_ranges"]:
                for coordinate in zip(y, x[::-1]):
                    if self.__check_coordinate(coordinate):
                        self.__current_piece_can["move"].append(coordinate)
                    else:
                        attack = coordinate
                        if self.__can_attack(attack):
                            self.__current_piece_can["attack"].append(attack)

        return self.__current_piece_can

    def __get_bishop_moves(self) -> dict:
        ranges = {
            key: [
                range(self.selected_piece_location[index] - 1, -1, -1),
                range(self.selected_piece_location[index] + 1, 8, 1),
            ]
            for index, key in enumerate(["v_ranges", "h_ranges"])
        }

        for y in ranges["v_ranges"]:
            for x in ranges["h_ranges"]:
                for coordinate in zip(y, x):
                    if self.__check_coordinate(coordinate):
                        self.__current_piece_can["move"].append(coordinate)
                    else:
                        attack = coordinate
                        if self.__can_attack(attack):
                            self.__current_piece_can["attack"].append(attack)
                        break

        return self.__current_piece_can

    def __get_king_moves(self) -> dict:
        ranges = {
            key: [
                [self.selected_piece_location[index] - 1],
                [self.selected_piece_location[index] + 1],
            ]
            for index, key in enumerate(["v_ranges", "h_ranges"])
        }

        for range_set, coordinate_function in [
            (ranges["v_ranges"], self.__updated_y_coordinate),
            (ranges["h_ranges"], self.__updated_x_coordinate),
        ]:
            for _ran in range_set:
                for x in _ran:
                    if self.__check_coordinate(coordinate_function(x)):
                        self.__current_piece_can["move"].append(coordinate_function(x))
                    else:
                        attack = coordinate_function(x)
                        if self.__can_attack(attack):
                            self.__current_piece_can["attack"].append(attack)
                        break

        for y in ranges["v_ranges"]:
            for x in ranges["h_ranges"]:
                for coordinate in zip(y, x):
                    if self.__check_coordinate(coordinate):
                        self.__current_piece_can["move"].append(coordinate)
                    else:
                        attack = coordinate
                        if self.__can_attack(attack):
                            self.__current_piece_can["attack"].append(attack)
                        break

        return self.__current_piece_can

    def __get_queen_moves(self) -> dict:
        ranges = {
            key: [
                range(self.selected_piece_location[index] - 1, -1, -1),
                range(self.selected_piece_location[index] + 1, 8, 1),
            ]
            for index, key in enumerate(["v_ranges", "h_ranges"])
        }

        for range_set, coordinate_function in [
            (ranges["v_ranges"], self.__updated_y_coordinate),
            (ranges["h_ranges"], self.__updated_x_coordinate),
        ]:
            for _ran in range_set:
                for x in _ran:
                    if self.__check_coordinate(coordinate_function(x)):
                        self.__current_piece_can["move"].append(coordinate_function(x))
                    else:
                        attack = coordinate_function(x)
                        if self.__can_attack(attack):
                            self.__current_piece_can["attack"].append(attack)
                        break

        for y in ranges["v_ranges"]:
            for x in ranges["h_ranges"]:
                for coordinate in zip(y, x):
                    if self.__check_coordinate(coordinate):
                        self.__current_piece_can["move"].append(coordinate)
                    else:
                        attack = coordinate
                        if self.__can_attack(attack):
                            self.__current_piece_can["attack"].append(attack)
                        break

        return self.__current_piece_can

    def __get_pawn_moves(self) -> dict:
        if self.player_number == 1:
            self.__update_pawn_can_moves(6, "-")
            self.__update_pawn_attacks("-")
        else:
            self.__update_pawn_can_moves(1, "+")
            self.__update_pawn_attacks("+")
        return self.__current_piece_can

    def __update_pawn_can_moves(self, row: int, operation: str) -> None:
        forward_1 = self.__updated_y_coordinate(
            eval(f"self.selected_piece_location[0] {operation} 1")
        )
        if self.__check_coordinate(forward_1):
            self.__current_piece_can["move"].append(forward_1)

        if self.__can_pawn_move_2(row):
            forward_2 = self.__updated_y_coordinate(
                eval(f"self.selected_piece_location[0] {operation} 2")
            )
            if self.__check_coordinate(forward_2):
                self.__current_piece_can["move"].append(forward_2)

    def __can_pawn_move_2(self, row) -> bool:
        return self.selected_piece_location[0] == row

    def __update_pawn_attacks(self, operation) -> None:
        attacks = self.__pawn_attack_coordinates(operation)
        right_attacks = [attack for attack in attacks if self.__can_attack(attack)]
        self.__current_piece_can["attack"] += right_attacks

    def __pawn_attack_coordinates(self, operation) -> list:
        coordinates: list = []
        for opera in ["-", "+"]:
            coordinates.append(
                (
                    eval(f"self.selected_piece_location[0] {operation} 1"),
                    eval(f"self.selected_piece_location[1] {opera} 1"),
                )
            )
        return coordinates

    def __can_attack(self, attack_location) -> bool:
        if self.__is_enemy_piece(attack_location):
            return True
        return False

    def __is_enemy_piece(self, attack_location) -> bool:
        if attack_location in self.enemy_pieces_locations.values():
            return True
        return False

    def get_moves(
        self, selected_piece_location, game_map_array, enemy_pieces_locations
    ) -> dict:
        self.__reset__current_piece_can()
        self.__update_values(
            selected_piece_location, game_map_array, enemy_pieces_locations
        )
        return self.__move_map[self.filtered_selected_piece_name]()

    def __reset__current_piece_can(self):
        self.__current_piece_can = {"move": [], "attack": []}

    def __update_values(
        self,
        selected_piece_location: tuple,
        game_map_array: list,
        enemy_pieces_locations: dict = {},
    ) -> None:
        self.filtered_selected_piece_name = self.__get_filtered_piece_name(
            selected_piece_location
        )
        self.selected_piece_location = selected_piece_location
        self.game_map_array = game_map_array
        self.enemy_pieces_locations = (
            enemy_pieces_locations
            if enemy_pieces_locations
            else self.player.all_enemy_piece_locations
        )

    def __get_filtered_piece_name(self, piece_location: tuple):
        piece_name: str = ""
        for key, value in self.player.chess_pieces_locations.items():
            if piece_location == value:
                piece_name = key.split("_")[0]
        return piece_name

    def get_all_pieces_moves(
        self, game_map_array, enemy_pieces_locations: dict = {}
    ) -> dict:
        pieces_can = {}
        for piece_name, piece_location in self.player.chess_pieces_locations.items():
            pieces_can[piece_name] = self.get_moves(
                piece_location, game_map_array, enemy_pieces_locations
            )
            self.__reset__current_piece_can()

        return pieces_can

    def get_attack_ray(
        self, attack_ray_from_location, game_map_array, attack_ray_to_locations
    ):
        self.__reset__current_piece_can()
        self.__update_values(
            attack_ray_from_location, game_map_array, attack_ray_to_locations
        )
        return self.__attack_ray_function_list[self.filtered_selected_piece_name]()

    def __rook_attack_ray(self):
        ranges = {
            key: [
                range(self.selected_piece_location[index] - 1, -1, -1),
                range(self.selected_piece_location[index] + 1, 8, 1),
            ]
            for index, key in enumerate(["v_ranges", "h_ranges"])
        }

        for range_set, coordinate_function in [
            (ranges["v_ranges"], self.__updated_y_coordinate),
            (ranges["h_ranges"], self.__updated_x_coordinate),
        ]:
            for _ran in range_set:
                for x in _ran:
                    if not self.__skip:
                        if self.__check_coordinate(coordinate_function(x)):
                            self.__current_piece_can["move"].append(
                                coordinate_function(x)
                            )
                        else:
                            attack = coordinate_function(x)
                            if self.__can_attack(attack):
                                self.__current_piece_can["attack"].append(attack)
                                self.__skip = True
                                break
                    else:
                        break
                else:
                    if not self.__skip:
                        self.__reset__current_piece_can()

        self.__skip = False
        return self.__current_piece_can

    def __knight_attack_ray(self):
        return self.__current_piece_can

    def __bishop_attack_ray(self):
        ranges = {
            key: [
                range(self.selected_piece_location[index] - 1, -1, -1),
                range(self.selected_piece_location[index] + 1, 8, 1),
            ]
            for index, key in enumerate(["v_ranges", "h_ranges"])
        }

        for y in ranges["v_ranges"]:
            for x in ranges["h_ranges"]:
                for coordinate in zip(y, x):
                    if not self.__skip:
                        if self.__check_coordinate(coordinate):
                            self.__current_piece_can["move"].append(coordinate)
                        else:
                            attack = coordinate
                            if self.__can_attack(attack):
                                self.__current_piece_can["attack"].append(attack)
                                self.__skip = True
                                break
                    else:
                        break
                else:
                    if not self.__skip:
                        self.__reset__current_piece_can()
        self.__skip = False
        return self.__current_piece_can

    def __king_attack_ray(self):
        return self.__current_piece_can

    def __queen_attack_ray(self):
        ranges = {
            key: [
                range(self.selected_piece_location[index] - 1, -1, -1),
                range(self.selected_piece_location[index] + 1, 8, 1),
            ]
            for index, key in enumerate(["v_ranges", "h_ranges"])
        }

        for range_set, coordinate_function in [
            (ranges["v_ranges"], self.__updated_y_coordinate),
            (ranges["h_ranges"], self.__updated_x_coordinate),
        ]:
            for _ran in range_set:
                for x in _ran:
                    if not self.__skip:
                        if self.__check_coordinate(coordinate_function(x)):
                            self.__current_piece_can["move"].append(
                                coordinate_function(x)
                            )
                        else:
                            attack = coordinate_function(x)
                            if self.__can_attack(attack):
                                self.__current_piece_can["attack"].append(attack)
                                self.__skip = True
                                break
                    else:
                        break
                else:
                    if not self.__skip:
                        self.__reset__current_piece_can()
        self.__skip = False
        for y in ranges["v_ranges"]:
            for x in ranges["h_ranges"]:
                for coordinate in zip(y, x):
                    if not self.__skip:
                        if self.__check_coordinate(coordinate):
                            self.__current_piece_can["move"].append(coordinate)
                        else:
                            attack = coordinate
                            if self.__can_attack(attack):
                                self.__current_piece_can["attack"].append(attack)
                                self.__skip = True
                                break
                    else:
                        break
                else:
                    if not self.__skip:
                        self.__reset__current_piece_can()

        self.__skip = False
        return self.__current_piece_can

    def __pawn_attack_ray(self):
        return self.__current_piece_can

    def update_attack_ray(self, attack_ray: list):
        self.attack_ray = attack_ray

    def reset_attack_ray(self):
        self.attack_ray = []


class Chess:
    def __init__(self) -> None:
        clear()

        self.__game_display = BeautifulTable()
        self.__game_display.set_style(BeautifulTable.STYLE_BOX_ROUNDED)  # type: ignore
        self.__game_map_array = []
        self.__player_1 = Player(player_number=1, color="black")
        self.__player_2 = Player(
            player_number=2,
            color="white",
        )
        self.current_player = self.__player_1
        self.enemy_player = self.__player_2
        self.selected_piece_name: str | None
        self.selected_piece_can: dict = {}

        self.__selected_piece_location: tuple
        self.__move_to_location: tuple

    def run(self):
        self.__setup_game()
        while True:
            self.__update_players_moves_and_locations()
            self.__show_display()
            if self.current_player.got_check_by:
                print(f"⚔️  ⚔️  ⚔️    {self.enemy_player.name} Checked you. ⚔️  ⚔️  ⚔️")
                self.__defend_current_player_check()
                self.current_player.check_for_check_mate()

                if self.current_player.got_check_mated == True:
                    self.__show_display()
                    print(f"⭐  ⭐  ⭐  {self.enemy_player.name} Won  ⭐  ⭐  ⭐")
                    break

                self.__print_counter_pieces()

            self.__select_piece_location()
            self.__print_can()
            if input():
                continue
            if not self.__give_move_location():
                continue
            self.__make_move()

            if self.current_player.can_pawn_power_up():
                self.__upgrade_pawn()

            self.__reset_importent_values()
            self.__update_players_moves_and_locations()

            can_check = self.current_player.can_give_check(self.__game_map_array)
            self.enemy_player.update_values(can_check)

            self.__switch_player()

    def __setup_game(self) -> None:
        self.__game_map_array = self.__generate_map(8, 8)
        self.__player_1.setup()
        self.__player_2.setup(
            invalid_name={self.__player_1.player_number: self.__player_1.name},
            remove_color=self.__player_1.color,
        )
        self.__update_map()

    def __generate_map(self, *shape: int) -> list[list[str]]:
        def array(axes):
            if not shape or shape[axes] <= 0:
                raise ValueError("length must be grater then Zero!!!")
            elif len(shape) == axes + 1:
                return list("" for _ in range(shape[axes]))
            elif len(shape) > axes:
                return list(array(axes + 1) for _ in range(shape[axes]))

        return array(0)  # type: ignore

    def __update_map(self) -> None:
        self.__update_game_map_array(self.__player_1)
        self.__update_game_map_array(self.__player_2)
        self.__update_game_display()

    def __update_game_map_array(self, player: Player) -> None:
        for name, location in player.chess_pieces_locations.items():
            self.__game_map_array[location[0]][location[1]] = player.chess_pieces[name]

    def __update_game_display(self) -> None:
        if not bool(self.__game_display):
            for row in self.__game_map_array:
                self.__game_display.rows.append(row)
        else:
            for index, row in enumerate(self.__game_map_array):
                self.__game_display.rows[index] = row

    def __show_display(self) -> None:
        clear()
        print(self.__game_display)

    def __update_players_moves_and_locations(self):
        self.current_player.all_enemy_piece_locations = (
            self.enemy_player.chess_pieces_locations
        )
        self.enemy_player.update_all_pieces_can(self.__game_map_array)
        self.current_player.all_enemy_pieces_can = self.enemy_player.all_pieces_can
        self.current_player.update_all_pieces_can(self.__game_map_array)

    def __select_piece_location(self) -> None:
        while True:
            location = input(f"{self.current_player.name}, select your piece :- ")
            if location == "#exit":
                exit()
            location = self.__filter_coordinate(location)
            if filtered_location := self.__right_location(location):
                self.__selected_piece_location = filtered_location
                break

    def __filter_coordinate(self, move) -> list:
        _move = [int(m) - 1 for m in move.split(" ") if m.isnumeric()]
        if _move:
            return _move
        return []

    def __right_location(self, location) -> tuple:
        _move = [m for m in location if 0 <= m <= 7]
        if len(_move) >= 2:
            if self.current_player.got_check_by:
                counter_piece_locations = {
                    piece_name: values["location"]
                    for piece_name, values in self.current_player.can_only_counter_by.items()
                }
                if (
                    _move[0],
                    _move[1],
                ) in counter_piece_locations.values():
                    selected_location = (_move[0], _move[1])

                    self.__get_selected_piece_moves(selected_location)
                    if (
                        self.selected_piece_can["move"]
                        or self.selected_piece_can["attack"]
                    ):
                        return (_move[0], _move[1])
                    else:
                        print("This piece is currently immovable...")
                        return ()
                print("This piece is currently immovable...")
                return ()
            else:
                if (
                    _move[0],
                    _move[1],
                ) in self.current_player.chess_pieces_locations.values():
                    selected_location = (_move[0], _move[1])

                    self.__get_selected_piece_moves(selected_location)
                    if (
                        self.selected_piece_can["move"]
                        or self.selected_piece_can["attack"]
                    ):
                        return selected_location
                    else:
                        print("This piece is currently immovable...")
                        return ()

        print("Invalid Location !!!")
        return ()

    def __get_selected_piece_moves(self, selected_location):
        self.selected_piece_name = self.current_player.get_piece_name(selected_location)
        if self.current_player.got_check:
            self.selected_piece_can = self.current_player.can_only_counter_by[
                self.selected_piece_name
            ]
            self.selected_piece_can.pop("location")
        else:
            self.selected_piece_can = self.current_player.all_pieces_can[
                self.selected_piece_name
            ]

    def __print_can(self) -> None:
        readable = self.__readable_current_piece_can()
        if readable["move"]:
            print(f"Can Move:- {readable['move']}")
        if readable["attack"]:
            print(f"Can Attack:- {readable['attack']}")

    def __readable_current_piece_can(self) -> dict:
        readable: dict = {}
        coord_up_1 = lambda coord: (coord[0] + 1, coord[1] + 1)
        for items in self.selected_piece_can.items():
            readable[items[0]] = [coord_up_1(coord) for coord in items[1]]
        return readable

    def __give_move_location(self) -> bool:
        while True:
            move = input(f"{self.current_player.name}, enter your move :- ")
            if move == "#exit":
                exit()
            filtered_move = self.__filter_coordinate(move)
            right_move = self.__check_coordinate(filtered_move)
            if right_move:
                self.__move_to_location = right_move
                return True
            else:
                print("Invalid Move !!!")
                continue

    def __check_coordinate(self, move) -> tuple:
        if len(move) >= 2:
            move = tuple(move[:2])
            can = self.selected_piece_can["move"] + self.selected_piece_can["attack"]
            if move in can:
                return move
        return ()

    def __make_move(self) -> None:
        self.current_player.chess_pieces_locations[self.selected_piece_name] = (
            self.__move_to_location[0],
            self.__move_to_location[1],
        )
        self.__game_map_array[self.__selected_piece_location[0]][
            self.__selected_piece_location[1]
        ] = ""

        dead_piece_name = self.enemy_player.get_piece_name(self.__move_to_location)
        self.enemy_player.got_killed(key=dead_piece_name)
        self.__update_map()

    def __upgrade_pawn(self):
        upgrade_choice = ""
        print("\nChoose one of the following upgrades :-")
        for upgrade_name, upgrade in self.current_player.pawn_upgrades.items():
            print(f"{upgrade_name.capitalize()} - {upgrade}")

        while True:
            upgrade_choice = input("Enter your upgrade name :- ").lower()
            if upgrade_choice == "#exit":
                exit()
            if upgrade_choice in self.current_player.pawn_upgrades.keys():
                break
            print("Invalid upgrade choice !!!")

        similar_upgrade_pieces_count = sum(
            [
                1
                for piece_name, piece in self.current_player.chess_pieces.items()
                if piece_name.split("_")[0] == upgrade_choice
            ]
        )
        upgrade_choice_name = upgrade_choice + "_" + str(similar_upgrade_pieces_count)
        self.current_player.chess_pieces.pop(
            self.current_player.upgradable_pawn["name"]
        )
        self.current_player.chess_pieces[
            upgrade_choice_name
        ] = self.current_player.pawn_upgrades[upgrade_choice]
        self.current_player.chess_pieces_locations.pop(
            self.current_player.upgradable_pawn["name"]
        )
        self.current_player.chess_pieces_locations[
            upgrade_choice_name
        ] = self.current_player.upgradable_pawn["location"]

        self.__update_map()

    def __reset_importent_values(self):
        if self.current_player.got_attack_ray_moves():
            self.current_player.reset_attack_ray_moves()

        if self.current_player.got_check_by:
            self.current_player.reset_can_only_counter_by()

    def __defend_current_player_check(self):
        checked_by_locations: dict = {
            piece_name: self.enemy_player.chess_pieces_locations[piece_name]
            for piece_name in self.current_player.got_check_by.keys()
        }
        counter_by = self.current_player.counter_check_by(
            self.__game_map_array,
            checked_by_locations,
            self.enemy_player.moves.get_attack_ray(
                tuple(checked_by_locations.values())[0],
                self.__game_map_array,
                {"king": self.current_player.chess_pieces_locations["king"]},
            ),
        )
        return counter_by

    def __print_counter_pieces(self) -> None:
        counter_pieces_location = {
            piece_name: values["location"]
            for piece_name, values in self.current_player.can_only_counter_by.items()
        }
        print("Can counter by :-")
        for name, location in counter_pieces_location.items():
            print(f"\t {name} - {(location[0] + 1, location[1] + 1)}")

    def __switch_player(self) -> None:
        if self.current_player == self.__player_1:
            self.current_player = self.__player_2
            self.enemy_player = self.__player_1
        else:
            self.current_player = self.__player_1
            self.enemy_player = self.__player_2


game = Chess()
game.run()
