import sys
from enum import Enum, auto

from core.board import Board


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
