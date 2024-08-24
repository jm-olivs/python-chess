from core.pieces import Piece
from core.types import Coordinates


class Board:
    squares: dict[Coordinates, Piece | None]

    def __init__(self) -> None:
        # A chess board has a dimention of 8 x 8 (64 squares)
        self.squares = {Coordinates((x, y)): None for x in range(8) for y in range(8)}
