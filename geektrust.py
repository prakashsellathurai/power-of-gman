import sys
from src.gman import GManGame


def get_cmd_and_args(line):
    line = line.split()
    return line[0], line[1:]


def main():
    file_path = sys.argv[1]

    f = open(file_path, "r")

    gmangame = GManGame()

    for line in f.readlines():
        cmd, args = get_cmd_and_args(line)

        if cmd == "SOURCE":
            game.init_player(args[0], args[1], args[2])
        elif cmd == "DESTINATION":
            game.move_player_to(args[0], args[1])
        elif cmd == "PRINT_POWER":
            print("POWER", game.calculate_power())


if __name__ == "__main__":
    main()
