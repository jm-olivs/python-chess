from game_manager import GameManager


def main():
    game_manager = GameManager()

    print("Welcome to Chess")
    print("Please select from the main menu")
    print("1: Start")
    print("2: Exit")

    while True:
        command = input("Command: ")

        match command:
            case "1":
                game_manager.start()
            case "2":
                game_manager.exit()


if __name__ == "__main__":
    main()
