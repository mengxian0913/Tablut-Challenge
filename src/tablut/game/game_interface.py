import asyncio

from tablut.common.enums.chess import CHESS
from tablut.common.enums.game_status import GAME_STATUS
from tablut.common.enums.player import ROLE
from tablut.common.enums.turn import TURN
from tablut.common.types.receive_state import ReceiveStateType
from tablut.cooked_tablut.cooked_tablut import CookedTablut
from tablut.game.depth_benchmark import DEPTH_BENCHMARK
from tablut.network.socket_client import SocketClient
from tablut.utils.logger import Logger
from tablut.utils.tools import Timer, Tools


class ChessGameInterface:
    KEEP_TIME_OUT = 3

    def __init__(
        self,
        role: ROLE,
        time_out: float,
        host: str,
        player_name: str = "Cooked",
    ) -> None:
        # Game Status
        self.__chess_board: list[list[CHESS]] = [
            [CHESS.EMPTY for _ in range(9)] for _ in range(9)
        ]
        self.__game_status: GAME_STATUS = GAME_STATUS.UNINITIALIZED

        # Assets
        self.__role: ROLE = role
        self.__player_name = player_name
        self.__time_out = time_out
        self.__timer = Timer(time_out - ChessGameInterface.KEEP_TIME_OUT)
        self.__server = SocketClient(role=self.__role, host=host)
        self.__cooked_tree = CookedTablut()
        self.logger = Logger(f"ChessGame_{player_name}")
        self.__max_depth: int = self.__calculate_optimal_depth(time_out)

    def __calculate_optimal_depth(self, time_out: float) -> int:
        """
        Calculate optimal search depth based on time budget using pre-computed benchmark table.

        Strategy:
        1. Calculate available time: time_out - KEEP_TIME_OUT (3s safety margin)
        2. Apply additional safety margin: 0.8x (20% buffer for network latency, etc)
        3. Find maximum depth where benchmark time < safe budget

        Args:
            time_out: Total time allocated in seconds

        Returns:
            Optimal max_depth for minimax search
        """
        available_time = time_out - ChessGameInterface.KEEP_TIME_OUT
        safe_budget = available_time * 0.8

        optimal_depth = 3  # Fallback minimum

        for depth in sorted(DEPTH_BENCHMARK.keys()):
            if DEPTH_BENCHMARK[depth] < safe_budget:
                optimal_depth = depth
            else:
                break

        self.logger.info(f"Calculated optimal depth: {optimal_depth}")
        return optimal_depth

    def __next_move(self) -> None:
        self.logger.info("Getting next move")

        try:
            self.__timer.reset()
            index_from, index_to = asyncio.run(self.__get_movement(self.__timer))
            move_from = Tools.pos_to_symbol(*index_from)
            move_to = Tools.pos_to_symbol(*index_to)
            self.__server.send_move(move_from, move_to, self.__role.value)
            self.logger.info(
                f"Sent move from {move_from} to {move_to} (took {self.__timer.elapsed():.2f}s)"
            )
        except Exception as e:
            self.logger.error(f"Failed to send move: {e}")

    def __update_chessboard(self, chess_board: list[list[CHESS]]) -> None:
        self.logger.info("Updating the chess board")
        self.__chess_board = chess_board

    async def __get_movement(
        self, timer: Timer
    ) -> tuple[tuple[int, int], tuple[int, int]]:
        try:
            movement = self.__cooked_tree.get_next_movement(
                self.__chess_board, self.__role, self.__max_depth
            )
            return (movement.from_node.row, movement.from_node.col), (
                movement.to_node.row,
                movement.to_node.col,
            )
        except:
            self.logger.error("Failed to get movement")
            raise RuntimeError("Failed to get movement")

    def __initialize(self) -> None:
        try:
            # Initialize the chess board or any other necessary setup
            self.logger.info("Initializing the chess board")
            self.__server.connect()
            self.__server.send_name(self.__player_name)

            self.__game_status = GAME_STATUS.INITIALIZED

            self.logger.info(
                f"Initialized game as {self.__role} with player name {self.__player_name}"
            )

        except Exception as e:
            self.logger.error(f"Initialization failed: {e}")

    def start_game(self) -> None:
        if self.__game_status == GAME_STATUS.UNINITIALIZED:
            self.__initialize()

        while (
            self.__game_status != GAME_STATUS.UNINITIALIZED
            and self.__game_status != GAME_STATUS.FINISHED
        ):
            self.logger.info(f"Current game status: {self.__game_status}")

            if self.__game_status == GAME_STATUS.PLAY:
                self.__next_move()

            server_response: ReceiveStateType = self.__server.receive_state()

            # Update the chess board
            self.__update_chessboard(server_response.board)

            # Update the game status
            if server_response.turn in [TURN.DRAW, TURN.WHITEWIN, TURN.BLACKWIN]:
                self.logger.info(f"Game ended with turn: {server_response.turn}")
                self.__game_status = GAME_STATUS.FINISHED
                continue

            # TURN and ROLE are different enums: compare their values.
            self.__game_status = (
                GAME_STATUS.PLAY
                if server_response.turn.value == self.__role.value
                else GAME_STATUS.WAIT
            )
