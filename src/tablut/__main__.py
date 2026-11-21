import sys

from tablut.common.enums.player import ROLE
from tablut.game.game_interface import ChessGameInterface


<<<<<<< HEAD
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
=======
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
>>>>>>> 307566e64c7d3573651ce0ccc28808e7b3c167bf
