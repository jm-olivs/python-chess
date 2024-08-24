from os import environ

from core.pieces import Colors, DebugPiece
from game_manager import DebugGameManager, GameManager


def main():
    env = environ.get("ENV")
    game_manager = GameManager() if env != "dev" else DebugGameManager(DebugPiece(Colors.Black))
    game_manager.display_welcome_message()

    while True:
        command = input("Command: ")

        match command:
            case "1":
                game_manager.start()
            case "2":
                game_manager.exit()
            case command if "move" in command:
                game_manager.move()


if __name__ == "__main__":
    main()
