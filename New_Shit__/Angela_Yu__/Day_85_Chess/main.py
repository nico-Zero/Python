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
        self.color = (
            input(f"Enter player {player_number} color ('w','b'):- ").lower()
            if color == ""
            else color
        )
        self.chess_pieces: dict = {}
        self.chess_pieces_locations: dict = {}
        clear()

    def setup(self):
        self.chess_pieces = self.__get_chess_pieces()
        self.chess_pieces_locations = self.__get_chess_pieces_location()
        self.__setup_player_1()
        self.__set_starting_pieces()

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
    def __init__(self, player_number):
        self.player_number = player_number

    def give_rook_moves(self, current_location):
        ...

    def give_knight_moves(self, current_location):
        ...

    def give_bishop_moves(self, current_location):
        ...

    def give_king_moves(self, current_location):
        ...

    def give_queen_moves(self, current_location):
        ...

    def give_pawn_moves(self, current_location):
        ...

    def check_attack(self, attack_location):
        ...

    def check_pawn_attack(self, attack_location):
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
        self.current_select_location: tuple = ()
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

    def __can_move_piece(self):
        ...

    def __take_location(self):
        while True:
            location = input(f"{self.current_player.name} enter your move :- ")
            if filtered_location := self.__filter_str(location):
                self.current_select_location = filtered_location
                break
            print("Invalid location !!!")

    def __filter_str(self, move):
        _move = [int(m) for m in move.split(" ") if m.isnumeric()]
        _move = [m for m in _move if 0 < m <= 8]
        if len(_move) >= 2:
            if _move := self.__validate_location(tuple(_move[:2])):
                return _move
        return None

    def __validate_location(self, location):
        if (
            location[0] - 1,
            location[1] - 1,
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

    def get_players(self) -> None:
        print(self.player_1.chess_pieces)
        print(self.player_2.chess_pieces)
        print(self.player_1.chess_pieces_locations)
        print(self.player_2.chess_pieces_locations)


game = Chess()
game.run()
