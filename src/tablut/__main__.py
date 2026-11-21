import sys

from tablut.common.enums.player import ROLE
from tablut.game.game_interface import ChessGameInterface


def main() -> None:
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <WHITE|BLACK> <timeout-seconds> <server-ip>")
        sys.exit(1)

    role = ROLE[sys.argv[1].upper()]
    timeout = float(sys.argv[2])
    host = sys.argv[3]

    game = ChessGameInterface(
        role=role, time_out=timeout, host=host, player_name="Cooked"
    )
    game.start_game()


if __name__ == "__main__":
    main()
