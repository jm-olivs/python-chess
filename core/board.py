from core.pieces import Piece
from core.types import Coordinate


class Board:
    squares: dict[Coordinate, Piece | None]

    def __init__(self) -> None:
        # A chess board has a dimention of 8 x 8 (64 squares)
        self.squares = {Coordinate((x, y)): None for x in range(8) for y in range(8)}


class DebugBoard(Board):
    """Board for development purposes"""

    def __init__(self, piece: Piece) -> None:
        # A chess board has a dimention of 8 x 8 (64 squares)
        self.squares = {Coordinate((x, y)): None for x in range(8) for y in range(8)}

        self.squares[Coordinate((0, 0))] = piece
