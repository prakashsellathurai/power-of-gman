import sys
from src.game import Game


def get_command_and_arguments(line):
    line = line.split()
    return line[0], line[1:]


def main():
    file_path = sys.argv[1]
    f = open(file_path, "r")

    source_x = 0
    source_y = 0
    sourcedir = ""
    destination_x = 0
    destination_y = 0

    for line in f.readlines():
        command, arguments = get_command_and_arguments(line)

        if command == "SOURCE":
            source_x, source_y, sourcedir = arguments
        elif command == "DESTINATION":
            destination_x, destination_y = arguments
        elif command == "PRINT_POWER":
            game = Game.initialize(source_x, source_y, sourcedir)
            game.move(destination_x, destination_y)
            game.print_power()


if __name__ == "__main__":
    main()
