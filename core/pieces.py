from abc import ABC
from enum import Enum
from typing import ClassVar

from core.movements import Anywhere, Movement
from core.types import Coordinate


class Colors(str, Enum):
    White = "white"
    Black = "black"


class Piece(ABC):
    name: ClassVar[str]
    movement: ClassVar[Movement]
    _count: ClassVar[int] = 0
    id: str
    color: Colors
    possible_coordinates: list[Coordinate]

    def __init__(self, color: Colors) -> None:
        snake_case_name = self.name.replace(" ", "_").lower()
        self.id = f"{snake_case_name}_{color.value}_{self._count}"
        self.color = color
        Piece._count += 1

        self.generate_possible_coordinates()

    def generate_possible_coordinates(self) -> None:
        self.possible_coordinates = self.movement.generate_coordinates()

    def __repr__(self) -> str:
        return self.id


class DebugPiece(Piece):
    """A piece that can move anywhere."""

    name = "Debug Piece"
    movement = Anywhere
