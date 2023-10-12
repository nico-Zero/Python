from os import system
from beautifultable import BeautifulTable
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
        self.moves = MoveSet(self.player_number, self)
        clear()

    def setup(self):
        self.chess_pieces = self.__get_chess_pieces()
        self.chess_pieces_locations = self.__get_chess_pieces_location()
        self.__setup_player_1()
        self.__set_starting_pieces()

    def selected_piece_moves(self, current_location, game_map_array):
        return self.moves.get_moves(current_location, game_map_array)

    def __setup_player_1(self):
        if self.player_number == 1:
            self.chess_pieces = self.__player_1_pieces_reset(self.chess_pieces)
            self.chess_pieces_locations = self.__player_1_pieces_reset(
                self.chess_pieces_locations
            )

    def __player_1_pieces_reset(self, values):
        return {
            name: pieces
            for name, pieces in list(values.items())[8:] + list(values.items())[:8]
        }

    def __set_starting_pieces(self):
        if self.player_number == 1:
            self.__set_starting_pieces_locations(first_row=6, second_row=7)
        else:
            self.__set_starting_pieces_locations(first_row=0, second_row=1)

    def __set_starting_pieces_locations(self, first_row, second_row):
        self.chess_pieces_locations = {
            key: location
            for key, location in zip(
                self.chess_pieces_locations.keys(),
                [(first_row, position) for position in range(8)]
                + [(second_row, position) for position in range(8)],
            )
        }

    def __get_chess_pieces(self):
        whitePieces = {
            "rook_1": "♖",
            "knight_1": "♘",
            "bishop_1": "♗",
            "king": "♔",
            "queen": "♕",
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
            "king": "♚",
            "queen": "♛",
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

    def __get_chess_pieces_location(self):
        return {
            "rook_1": (),
            "knight_1": (),
            "bishop_1": (),
            "king": (),
            "queen": (),
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
    def __init__(self, player_number, player: Player):
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
        self.current_location: tuple = ()
        self.current_piece: str = ""
        self.game_map_array: list = []
        self.current_piece_can: dict = {"moves": [], "attacks": []}

    def __update_y(self, y):
        return (y, self.current_location[1])

    def __update_x(self, x):
        return (self.current_location[0], x)

    def __get_rook_moves(self):
        h_ranges = [
            range(self.current_location[1], 0),
            range(self.current_location[1], 8),
        ]
        v_ranges = [
            range(self.current_location[0], 0),
            range(self.current_location[0], 8),
        ]

        for coordinate_functions in [self.__update_y, self.__update_x]:
            for _ran in [v_ranges, h_ranges]:
                for x in _ran:
                    if self.__right_move([coordinate_functions(x)]):
                        self.current_piece_can["moves"].append(coordinate_functions(x))
                    else:
                        self.current_piece_can["attacks"].append(
                            coordinate_functions(x)
                        )
                        break
        return self.current_piece_can

    def __get_knight_moves(self):
        ...

    def __get_bishop_moves(self):
        ...

    def __get_king_moves(self):
        ...

    def __get_queen_moves(self):
        ...

    def __get_pawn_moves(self):
        if self.player_number == 1:
            self.__update_pawn_can_moves(6, "-")
            self.__update_pawn_attacks("-")
        else:
            self.__update_pawn_can_moves(1, "+")
            self.__update_pawn_attacks("+")
        return self.current_piece_can

    def __update_pawn_can_moves(self, row: int, operation: str):
        forward_1 = self.__update_y(eval(f"self.current_location[0] {operation} 1"))
        if self.__can_pawn_move_2(row):
            forward_2 = self.__update_y(eval(f"self.current_location[0] {operation} 2"))
        if self.__right_move(forward_1):
            self.current_piece_can["moves"].append(forward_1)
            if self.__can_pawn_move_2(row):
                if self.__right_move(forward_2):  # type:ignore
                    self.current_piece_can["moves"].append(forward_2)  # type:ignore

    def __can_pawn_move_2(self, row):
        return self.current_location[0] == row

    def __update_pawn_attacks(self, operation):
        attacks = self.__pawn_attack_coordinates(operation)
        right_attacks = [attack for attack in attacks if self.__right_move(attack)]
        self.current_piece_can["attacks"] += right_attacks

    def __pawn_attack_coordinates(self, operation):
        coordinates: list = []
        for opera in ["-", "+"]:
            coordinates.append(
                (
                    eval(f"self.current_location[0] {operation} 1"),
                    eval(f"self.current_location[1] {opera} 1"),
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
            raise ValueError("Invalid move passed in '__right_move' !!!")

    def get_moves(self, current_location, game_map_array):
        self.__update_values(current_location, game_map_array)
        print(self.current_piece)
        return self.move_map[self.current_piece]()

    def __update_values(self, current_location, game_map_array):
        for key, value in self.player.chess_pieces_locations.items():
            if current_location == value:
                self.current_piece = key.split("_")[0]
        self.current_location = current_location
        self.game_map_array = game_map_array

    def check_attack(self, attack_location):
        ...


class Chess:
    def __init__(self):
        clear()

        self.__game_map = BeautifulTable()
        self.__game_map.set_style(BeautifulTable.STYLE_BOX_ROUNDED)  # type: ignore
        self.__game_map_array: list = []
        self.player_1 = Player(player_number=1)
        self.player_2 = Player(
            player_number=2, color="b" if self.player_1.color == "w" else "w"
        )
        self.current_player = self.player_1
        self.__current_select_location: tuple = ()
        self.current_move: tuple = ()

    def __switch_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def run(self):
        self.__setup_game()
        while True:
            self.__display()
            self.__take_location()
            self.__update_game_map()
            moves = self.current_player.selected_piece_moves(
                self.__current_select_location, self.__game_map_array
            )
            print(moves)
            break

    def __take_location(self):
        while True:
            location = input(f"{self.current_player.name} enter your move :- ")
            if filtered_location := self.__filter_str(location):
                self.__current_select_location = filtered_location
                break
            print("Invalid location !!!")

    def __filter_str(self, move):
        _move = [int(m) - 1 for m in move.split(" ") if m.isnumeric()]
        _move = [m for m in _move if 0 <= m <= 7]
        if len(_move) >= 2:
            if _move := self.__validate_location(tuple(_move[:2])):
                return _move
        return None

    def __validate_location(self, location):
        if (
            location[0],
            location[1],
        ) in self.current_player.chess_pieces_locations.values():
            return location
        else:
            return None

    def __setup_game(self):
        self.__game_map_array = self.__generate_map(8, 8)
        self.player_1.setup()
        self.player_2.setup()
        self.__setup_map()

    def __generate_map(self, *shape: int) -> list[list[str]]:
        def array(axes):
            if not shape or shape[axes] <= 0:
                raise ValueError("length must be grater then Zero!!!")
            elif len(shape) == axes + 1:
                return list("" for _ in range(shape[axes]))
            elif len(shape) > axes:
                return list(array(axes + 1) for _ in range(shape[axes]))

        return array(0)  # type: ignore

    def __setup_map(self):
        self.__update_game_map_array(self.player_1)
        self.__update_game_map_array(self.player_2)
        self.__update_game_map()

    def __update_game_map_array(self, player: Player):
        for name, location in player.chess_pieces_locations.items():
            self.__game_map_array[location[0]][location[1]] = player.chess_pieces[name]

    def __update_game_map(self):
        if not bool(self.__game_map):
            for row in self.__game_map_array:
                self.__game_map.rows.append(row)
        else:
            for row in zip(range(len(self.__game_map_array)), self.__game_map_array):
                self.__game_map.rows[row[0]] = row[1]

    def __display(self):
        clear()
        print(self.__game_map)

    def __get_players(self) -> None:
        print(self.player_1.chess_pieces)
        print(self.player_2.chess_pieces)
        print(self.player_1.chess_pieces_locations)
        print(self.player_2.chess_pieces_locations)


game = Chess()
game.run()
