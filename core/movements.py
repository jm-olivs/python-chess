from typing import Protocol

from core.types import Coordinate


class Movement(Protocol):
    @staticmethod
    def generate_coordinates() -> list[Coordinate]: ...


class Anywhere:
    """Created for debug purposes only."""

    @staticmethod
    def generate_coordinates() -> list[Coordinate]:
        return [Coordinate((x, y)) for x in range(8) for y in range(8)]
