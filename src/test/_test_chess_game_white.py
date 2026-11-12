from tablut.common.enums.player import ROLE
from tablut.game.game_interface import ChessGameInterface

if __name__ == "__main__":
    game = ChessGameInterface(
        role=ROLE.WHITE, time_out=20.0, host="127.0.0.1", player_name="Cooked"
    )

    game.start_game()
