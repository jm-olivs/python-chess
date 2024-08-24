import sys
from enum import Enum, auto

from core.board import Board, DebugBoard
from core.errors import InvalidMoveError
from core.pieces import Piece
from core.types import Coordinate


class GameStates(Enum):
    OnGoing = auto()
    Paused = auto()


class GameManager:
    state: GameStates | None = None
    board: Board

    def __init__(self) -> None:
        self.board = Board()

    def start(self) -> None:
        self.state = GameStates.OnGoing

    def pause(self) -> None:
        self.state = GameStates.Paused

    def exit(self) -> None:
        sys.exit(0)

    def move(self, piece: Piece, coordinate: Coordinate) -> None:
        self._validate_move(coordinate, piece.possible_coordinates)
        self.board.squares[coordinate] = piece
        piece.generate_possible_coordinates()

    @staticmethod
    def display_welcome_message() -> None:
        print("Welcome to Chess")
        print("Please select from the main menu")
        print("1: Start")
        print("2: Exit")

    @staticmethod
    def _validate_move(coordinate: Coordinate, possible_coordinates: list[Coordinate]) -> None:
        if not coordinate not in possible_coordinates:
            raise InvalidMoveError("Move is not allowed")


class DebugGameManager(GameManager):
    def __init__(self, piece: Piece) -> None:
        self.board = DebugBoard(piece)

    @staticmethod
    def display_welcome_message() -> None:
        print("Welcome to Chess (Running in debug mode)")
        print("Please select from the main menu")
        print("1: Start")
        print("2: Exit")
