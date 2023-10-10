import numpy as np
from os import system
from beautifultable import BeautifulTable
from platform import uname


class Chess:
    def __init__(self):
        self.__game_map = BeautifulTable()
        self.__game_map.set_style(BeautifulTable.STYLE_BOX_ROUNDED)  # type: ignore

        __commands = {"clear_screen": "cls" if uname().system == "Windows" else "clear"}
        system(__commands["clear_screen"])

        self.__game_map_array: list = []
        self.__whitePieces = {
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
        self.__blackPieces = {
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

        self.__whitePieces_location = {
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
        self.__blackPieces_location = {
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

        self.__player_1 = input("Enter player 1 name :- ")
        self.__player_2 = input("Enter player 2 name :- ")
        while 1:
            self.__player_1_color = input(
                f"{self.__player_1} enter you piece set ('w','b'):- "
            ).lower()
            if self.__player_1_color in ["w", "b"]:
                break

        self.__players = {
            self.__player_1: self.__whitePieces
            if self.__player_1_color == "w"  # type:ignore
            else self.__blackPieces,
            self.__player_2: self.__whitePieces
            if self.__player_1_color == "b"  # type:ignore
            else self.__blackPieces,
        }

    def run(self):
        self.__setup_game()
        self.__display()

    def __setup_game(self):
        self.__game_map_array = self.__generate_map(8, 8)
        self.__setup_map()

    def __setup_map(self):
        if not bool(self.__game_map):
            for row in self.__game_map_array:
                self.__game_map.rows.append(row)

    def insert_player_pieces(self):
        if self.__player_1_color == "w":
            ...
    
    def get_index(self):
        print(self.__players[self.__player_1])

    def __generate_map(self, *shape: int) -> list[list[str]]:
        def array(axes):
            if not shape or shape[axes] <= 0:
                raise ValueError("length must be grater then Zero!!!")
            elif len(shape) == axes + 1:
                return list("" for _ in range(shape[axes]))
            elif len(shape) > axes:
                return list(array(axes + 1) for _ in range(shape[axes]))

        return array(0)  # type: ignore

    def __display(self):
        print(self.__game_map)

    def get_players(self) -> None:
        print(self.__players.items())


game = Chess()
game.get_players()
game.run()
