from os import system
from beautifultable import BeautifulTable

# from prettytable import PrettyTable
from platform import uname


commands = {"clear_screen": "cls" if uname().system == "Windows" else "clear"}


def clear():
    system(commands["clear_screen"])


class Player:
    def __init__(self, player_number: int, name: str = "", color: str = "") -> None:
        self.player_number = player_number
        self.name = (
            input(f"Enter player {player_number} name :- ") if name == "" else name
        )
        while True:
            self.color = (
                input(f"Enter player {player_number} color ('w','b'):- ").lower()
                if color == ""
                else color
            )
            if self.color in ["w", "b"]:
                break
            print("Invalid color !!!")
        self.chess_pieces: dict = {}
        self.chess_pieces_locations: dict = {}
        self.pieces_death_locations: dict = {}
        self.moves = MoveSet(self.player_number, self)
        self.got_check_mated: bool = False  # TODO: check mate and Player response
        self.got_check: bool = False  # TODO: check and Player response
        clear()

    def update_check(self, checks):
        self.got_check = checks["check"]
        self.got_check_mated = checks["check_mate"]

    def can_give_check_mate(
        self, game_map_array, enemy_king_location, enemy_king_moves
    ):
        is_attacked = {
            piece_name: any(piece_attacks)
            for piece_name, piece_attacks in self.__get_all_pieces_attacks(
                game_map_array, enemy_king_location
            ).items()
        }
        king_attacked_by = [
            piece_name
            for piece_name, piece_attacks in is_attacked.items()
            if piece_attacks
        ]
        check = False
        check_mate = False

        if any(king_attacked_by):
            check = True
            if not (enemy_king_moves["moves"] and enemy_king_moves["attacks"]):
                check_mate = True

        return {"check": check, "check_mate": check_mate}

    def __get_all_pieces_attacks(self, game_map_array, enemy_king_location) -> dict:
        all_attacks = self.moves.get_all_pieces_attacks(
            self.chess_pieces_locations, game_map_array, enemy_king_location
        )
        print(all_attacks)
        return all_attacks

    def get_king_moves(self, game_map_array, enemy_pieces_locations):
        return self.moves.get_moves(
            self.chess_pieces_locations["king"], game_map_array, enemy_pieces_locations
        )

    def reset_moves(self) -> None:
        self.moves.reset()

    def setup(self) -> None:
        self.chess_pieces = self.__get_chess_pieces()
        self.chess_pieces_locations = self.__get_chess_pieces_location()
        self.__setup_player_1()
        self.__set_starting_pieces()

    def got_killed(self, key: str = "") -> None:
        if not key == "":
            self.pieces_death_locations[key] = self.chess_pieces_locations.pop(key)

    def get_selected_piece_moves(
        self, current_selected_location, game_map_array, enemy_pieces_locations
    ) -> dict:
        return self.moves.get_moves(
            current_selected_location, game_map_array, enemy_pieces_locations
        )

    def __setup_player_1(self) -> None:
        if self.player_number == 1:
            self.chess_pieces = self.__player_1_pieces_reset(self.chess_pieces)
            self.chess_pieces_locations = self.__player_1_pieces_reset(
                self.chess_pieces_locations
            )

    def __player_1_pieces_reset(self, values) -> dict:
        return {
            name: pieces
            for name, pieces in list(values.items())[8:] + list(values.items())[:8]
        }

    def __set_starting_pieces(self) -> None:
        if self.player_number == 1:
            self.__set_starting_pieces_locations(first_row=6, second_row=7)
        else:
            self.__set_starting_pieces_locations(first_row=0, second_row=1)

    def __set_starting_pieces_locations(self, first_row, second_row) -> None:
        self.chess_pieces_locations = {
            key: location
            for key, location in zip(
                self.chess_pieces_locations.keys(),
                [(first_row, position) for position in range(8)]
                + [(second_row, position) for position in range(8)],
            )
        }

    def __get_chess_pieces(self) -> dict:
        whitePieces = {
            "rook_1": "♖",
            "knight_1": "♘",
            "bishop_1": "♗",
            "queen": "♕",
            "king": "♔",
            "bishop_2": "♗",
            "knight_2": "♘",
            "rook_2": "♖",
            "pawn_1": "♙",
            "pawn_2": "♙",
            "pawn_3": "♙",
            "pawn_4": "♙",
            "pawn_5": "♙",
            "pawn_6": "♙",
            "pawn_7": "♙",
            "pawn_8": "♙",
        }
        blackPieces = {
            "rook_1": "♜",
            "knight_1": "♞",
            "bishop_1": "♝",
            "queen": "♛",
            "king": "♚",
            "bishop_2": "♝",
            "knight_2": "♞",
            "rook_2": "♜",
            "pawn_1": "♟",
            "pawn_2": "♟",
            "pawn_3": "♟",
            "pawn_4": "♟",
            "pawn_5": "♟",
            "pawn_6": "♟",
            "pawn_7": "♟",
            "pawn_8": "♟",
        }
        if self.color == "w":
            return whitePieces
        elif self.color == "b":
            return blackPieces
        else:
            raise ValueError("Invalid color")

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


class MoveSet:
    def __init__(self, player_number, player: Player) -> None:
        self.player_number: int = player_number
        self.player = player
        self.move_map = {
            "rook": self.__get_rook_moves,
            "knight": self.__get_knight_moves,
            "bishop": self.__get_bishop_moves,
            "king": self.__get_king_moves,
            "queen": self.__get_queen_moves,
            "pawn": self.__get_pawn_moves,
        }
        self.current_selected_location: tuple = ()
        self.current_piece_name: str
        self.game_map_array: list
        self.enemy_pieces_locations: dict
        self.__current_piece_can: dict = {"moves": [], "attacks": []}

    def reset(self):
        self.__current_piece_can = {"moves": [], "attacks": []}

    def get_all_pieces_attacks(
        self, chess_pieces_locations, game_map_array, enemy_pieces_locations
    ) -> dict:
        all_pieces_attacks = {}
        for piece_name, piece_location in chess_pieces_locations.items():
            all_pieces_attacks[piece_name] = self.get_moves(
                piece_location, game_map_array, enemy_pieces_locations
            )["attacks"]
            self.reset()

        return all_pieces_attacks

    def __get_rook_moves(self) -> dict:
        ranges = {
            key: [
                range(self.current_selected_location[index] - 1, -1, -1),
                range(self.current_selected_location[index] + 1, 8, 1),
            ]
            for index, key in enumerate(["v_ranges", "h_ranges"])
        }

        for range_set, coordinate_function in [
            (ranges["v_ranges"], self.__updated_y_coordinate),
            (ranges["h_ranges"], self.__updated_x_coordinate),
        ]:
            for _ran in range_set:
                for x in _ran:
                    if self.__right_move(coordinate_function(x)):
                        self.__current_piece_can["moves"].append(coordinate_function(x))
                    else:
                        attack = coordinate_function(x)
                        if self.__can_attack(attack):
                            self.__current_piece_can["attacks"].append(attack)
                        break

        return self.__current_piece_can

    def __can_attack(self, attack_location) -> bool:
        if self.__is_enemy_piece(attack_location):
            return True
        return False

    def __is_enemy_piece(self, attack_location) -> bool:
        # print(f"enemy :- {self.enemy_pieces_location}")
        if attack_location in self.enemy_pieces_locations.values():
            return True
        return False

    def __is_friendly_piece(self, attack_location):
        if attack_location in self.player.chess_pieces_locations.values():
            return True
        return False

    def __updated_y_coordinate(self, y) -> tuple:
        return (y, self.current_selected_location[1])

    def __updated_x_coordinate(self, x) -> tuple:
        return (self.current_selected_location[0], x)

    def __get_knight_moves(self) -> dict:
        ranges = {
            key: [
                range(
                    self.current_selected_location[index] - 1,
                    self.current_selected_location[index] - 3,
                    -1,
                ),
                range(
                    self.current_selected_location[index] + 1,
                    self.current_selected_location[index] + 3,
                    1,
                ),
            ]
            for index, key in enumerate(["v_ranges", "h_ranges"])
        }

        for y in ranges["v_ranges"]:
            for x in ranges["h_ranges"]:
                for coordinate in zip(y, x[::-1]):
                    if self.__right_move(coordinate):
                        self.__current_piece_can["moves"].append(coordinate)
                    else:
                        attack = coordinate
                        if self.__can_attack(attack):
                            self.__current_piece_can["attacks"].append(attack)

        return self.__current_piece_can

    def __get_bishop_moves(self) -> dict:
        ranges = {
            key: [
                range(self.current_selected_location[index] - 1, -1, -1),
                range(self.current_selected_location[index] + 1, 8, 1),
            ]
            for index, key in enumerate(["v_ranges", "h_ranges"])
        }

        for y in ranges["v_ranges"]:
            for x in ranges["h_ranges"]:
                for coordinate in zip(y, x):
                    if self.__right_move(coordinate):
                        self.__current_piece_can["moves"].append(coordinate)
                    else:
                        attack = coordinate
                        if self.__can_attack(attack):
                            self.__current_piece_can["attacks"].append(attack)
                        break

        return self.__current_piece_can

    def __get_king_moves(self) -> dict:
        ranges = {
            key: [
                [self.current_selected_location[index] - 1],
                [self.current_selected_location[index] + 1],
            ]
            for index, key in enumerate(["v_ranges", "h_ranges"])
        }

        for range_set, coordinate_function in [
            (ranges["v_ranges"], self.__updated_y_coordinate),
            (ranges["h_ranges"], self.__updated_x_coordinate),
        ]:
            for _ran in range_set:
                for x in _ran:
                    if self.__right_move(coordinate_function(x)):
                        self.__current_piece_can["moves"].append(coordinate_function(x))
                    else:
                        attack = coordinate_function(x)
                        if self.__can_attack(attack):
                            self.__current_piece_can["attacks"].append(attack)
                        break

        for y in ranges["v_ranges"]:
            for x in ranges["h_ranges"]:
                for coordinate in zip(y, x):
                    if self.__right_move(coordinate):
                        self.__current_piece_can["moves"].append(coordinate)
                    else:
                        attack = coordinate
                        if self.__can_attack(attack):
                            self.__current_piece_can["attacks"].append(attack)
                        break

        return self.__current_piece_can

    def __get_queen_moves(self) -> dict:
        ranges = {
            key: [
                range(self.current_selected_location[index] - 1, -1, -1),
                range(self.current_selected_location[index] + 1, 8, 1),
            ]
            for index, key in enumerate(["v_ranges", "h_ranges"])
        }

        for range_set, coordinate_function in [
            (ranges["v_ranges"], self.__updated_y_coordinate),
            (ranges["h_ranges"], self.__updated_x_coordinate),
        ]:
            for _ran in range_set:
                for x in _ran:
                    if self.__right_move(coordinate_function(x)):
                        self.__current_piece_can["moves"].append(coordinate_function(x))
                    else:
                        attack = coordinate_function(x)
                        if self.__can_attack(attack):
                            self.__current_piece_can["attacks"].append(attack)
                        break

        for y in ranges["v_ranges"]:
            for x in ranges["h_ranges"]:
                for coordinate in zip(y, x):
                    if self.__right_move(coordinate):
                        self.__current_piece_can["moves"].append(coordinate)
                    else:
                        attack = coordinate
                        if self.__can_attack(attack):
                            self.__current_piece_can["attacks"].append(attack)
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
            eval(f"self.current_selected_location[0] {operation} 1")
        )
        if self.__right_move(forward_1):
            self.__current_piece_can["moves"].append(forward_1)

        if self.__can_pawn_move_2(row):
            forward_2 = self.__updated_y_coordinate(
                eval(f"self.current_selected_location[0] {operation} 2")
            )
            if self.__right_move(forward_2):
                self.__current_piece_can["moves"].append(forward_2)

    def __can_pawn_move_2(self, row) -> bool:
        return self.current_selected_location[0] == row

    def __update_pawn_attacks(self, operation) -> None:
        attacks = self.__pawn_attack_coordinates(operation)
        # print(f"attacks = {attacks}")
        right_attacks = [attack for attack in attacks if self.__can_attack(attack)]
        self.__current_piece_can["attacks"] += right_attacks

    def __pawn_attack_coordinates(self, operation) -> list:
        coordinates: list = []
        for opera in ["-", "+"]:
            coordinates.append(
                (
                    eval(f"self.current_selected_location[0] {operation} 1"),
                    eval(f"self.current_selected_location[1] {opera} 1"),
                )
            )
        return coordinates

    def __right_move(self, moves) -> bool:
        try:
            if (0 <= moves[0] < 8) and (0 <= moves[1] < 8):
                return self.game_map_array[moves[0]][moves[1]] == ""
            else:
                return False
        except:
            # return False
            raise ValueError("Invalid move passed in '__right_move' !!!")

    def get_moves(
        self, current_selected_location, game_map_array, enemy_pieces_locations
    ) -> dict:
        self.__update_values(
            current_selected_location, game_map_array, enemy_pieces_locations
        )
        return self.move_map[self.current_piece_name]()

    def __update_values(
        self, current_selected_location, game_map_array, enemy_pieces_locations
    ) -> None:
        self.current_piece_name = self.get_piece_name_by_location(
            current_selected_location
        )
        self.current_selected_location = current_selected_location
        self.game_map_array = game_map_array
        self.enemy_pieces_locations = enemy_pieces_locations

    def get_piece_name_by_location(self, piece_location: tuple):
        piece_name: str = ""
        for key, value in self.player.chess_pieces_locations.items():
            if piece_location == value:
                piece_name = key.split("_")[0]
        return piece_name


class Chess:
    def __init__(self) -> None:
        clear()

        self.__game_display = BeautifulTable()
        self.__game_display.set_style(BeautifulTable.STYLE_BOX_ROUNDED)  # type: ignore
        self.__game_map_array: list = []
        self.__player_1 = Player(player_number=1)
        self.__player_2 = Player(
            player_number=2, color="b" if self.__player_1.color == "w" else "w"
        )
        self.current_player = self.__player_1
        self.enemy_player = self.__player_2
        self.__current_player_moves: dict
        self.__current_select_location: tuple
        self.__current_player_attack: tuple

    def run(self) -> None:
        self.__setup_game()
        while True:
            self.__display()
            self.__ask_select_location()
            self.__current_player_moves = self.current_player.get_selected_piece_moves(
                self.__current_select_location,
                self.__game_map_array,
                self.enemy_player.chess_pieces_locations,
            )

            self.__print_can()
            if input():
                continue

            if not (
                self.__current_player_moves["moves"]
                or self.__current_player_moves["attacks"]
            ):
                continue

            self.current_player.reset_moves()

            if not self.__ask_move_location():
                continue
            self.__make_move()

            can_check = self.current_player.can_give_check_mate(
                self.__game_map_array,
                {"king": self.enemy_player.chess_pieces_locations["king"]},
                self.enemy_player.get_king_moves(
                    self.__game_map_array, self.current_player.chess_pieces_locations
                ),
            )
            input()
            self.enemy_player.update_check(can_check)

            if self.enemy_player.got_check_mated == True:
                print(f"{self.current_player.name.capitalize()} Won")
                break

            self.__switch_player()

    def __print_can(self) -> None:
        readable = self.__readable_current_piece_can()
        print(f"Can Move:- {readable['moves'] if readable['moves'] else None}")
        print(f"Can Attack:- {readable['attacks'] if readable['attacks'] else None}")

    def __readable_current_piece_can(self) -> dict:
        readable: dict = {}
        coord_up_1 = lambda coord: (coord[0] + 1, coord[1] + 1)
        for items in self.__current_player_moves.items():
            readable[items[0]] = [coord_up_1(coord) for coord in items[1]]
        return readable

    def __ask_select_location(self) -> None:
        while True:
            location = input(
                f"{self.current_player.name.capitalize()}, select your piece :- "
            )
            location = self.__filter_coordinate(location)
            if filtered_location := self.__right_location(location):
                self.__current_select_location = filtered_location
                break
            print("Invalid location !!!")

    def __filter_coordinate(self, move) -> list:
        _move = [int(m) - 1 for m in move.split(" ") if m.isnumeric()]
        if _move:
            return _move
        return []

    def __right_location(self, location) -> tuple:
        _move = [m for m in location if 0 <= m <= 7]
        if len(_move) >= 2:
            if (
                _move[0],
                _move[1],
            ) in self.current_player.chess_pieces_locations.values():
                return (_move[0], _move[1])
        return ()

    def __ask_move_location(self) -> bool:
        while True:
            move = input(
                f"{self.current_player.name.capitalize()}, enter your move :- "
            )
            filtered_move = self.__filter_coordinate(move)
            right_move = self.__right_move(filtered_move)
            if right_move:
                self.__current_player_attack = right_move
                return True
            else:
                print("Invalid move!!!")
                continue

    def __right_move(self, moves) -> tuple:
        if len(moves) >= 2:
            move = tuple(moves[:2])
            can = (
                self.__current_player_moves["moves"]
                + self.__current_player_moves["attacks"]
            )
            if move in can:
                return move
        return ()

    def __make_move(self) -> None:
        enemy_killed_piece_name = ""
        for piece_name, location in self.current_player.chess_pieces_locations.items():
            if location == self.__current_select_location:
                self.current_player.chess_pieces_locations[piece_name] = (
                    self.__current_player_attack[0],
                    self.__current_player_attack[1],
                )
        self.__game_map_array[self.__current_select_location[0]][
            self.__current_select_location[1]
        ] = ""
        for piece_name, location in self.enemy_player.chess_pieces_locations.items():
            if location == self.__current_player_attack:
                enemy_killed_piece_name = piece_name
                break

        self.enemy_player.got_killed(key=enemy_killed_piece_name)
        self.__update_map()

    def __switch_player(self) -> None:
        if self.current_player == self.__player_1:
            self.current_player = self.__player_2
            self.enemy_player = self.__player_1
        else:
            self.current_player = self.__player_1
            self.enemy_player = self.__player_2

    def __setup_game(self) -> None:
        self.__game_map_array = self.__generate_map(8, 8)
        self.__player_1.setup()
        self.__player_2.setup()
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
            for row in enumerate(self.__game_map_array):
                self.__game_display.rows[row[0]] = row[1]

    def __display(self) -> None:
        clear()
        print(self.__game_display)

    def __get_players(self) -> None:
        print(self.__player_1.chess_pieces)
        print(self.__player_2.chess_pieces)
        print(self.__player_1.chess_pieces_locations)
        print(self.__player_2.chess_pieces_locations)


game = Chess()
game.run()
