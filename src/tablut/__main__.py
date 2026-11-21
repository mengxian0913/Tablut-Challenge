import sys

from tablut.common.enums.player import ROLE
from tablut.game.game_interface import ChessGameInterface


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("Usage: python -m tablut <WHITE|BLACK> <timeout> <server-ip>")
        return 1

    role_arg, timeout_arg, host = argv
    role = ROLE(role_arg.upper())
    timeout = float(timeout_arg)

    ChessGameInterface(role=role, time_out=timeout, host=host).start_game()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
