import sys
from src.gman import Gman


def get_command_and_arguments(line):
    line = line.split()
    return line[0], line[1:]


def main():
    file_path = sys.argv[1]
    f = open(file_path, "r")

    for line in f.readlines():
        command, arguments = get_command_and_arguments(line)

        if command == "SOURCE":
            sourceX, sourceY, sourcedir = arguments
            gman = Gman.init(sourceX, sourceY, sourcedir)
        elif command == "DESTINATION":
            destinationX, destinationY = arguments
            gman.move(destinationX, destinationY)
        elif command == "PRINT_POWER":
            gman.print_power()


if __name__ == "__main__":
    main()
