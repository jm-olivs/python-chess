import sys
from enum import Enum, auto


class GameStates(Enum):
    OnGoing = auto()
    Paused = auto()


class GameManager:
    state: GameStates | None = None

    def start(self) -> None:
        self.state = GameStates.OnGoing

    def pause(self) -> None:
        self.state = GameStates.Paused

    def exit(self) -> None:
        sys.exit(0)
