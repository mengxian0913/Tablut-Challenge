import time
from collections.abc import Callable

from tablut.common.enums.algorithm import GAME_STATUS
from tablut.common.enums.chess import CHESS
from tablut.common.enums.player import ROLE
from tablut.common.types.algorithm import (
    Best_Movement,
    Board,
    Node,
)


class SearchTimeout(Exception):
    """Raised inside the search when the deadline has passed."""


class CookedTree:
    def __init__(
        self,
    ) -> None:

        self.INF: int = 0x3F3F3F
        self.throne: Node = Node(4, 4)
        self.move_row: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, -5, -6, -7, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # fmt: skip # noqa: E501
        self.move_col: list[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, -5, -6, -7, -8]  # fmt: skip # noqa: E501

        # Depth fully searched by the last get_next_movement_in_time call.
        self.completed_depth: int = 0
        self._clock: Callable[[], float] = time.perf_counter
        self.__deadline: float | None = None

    def _get_alive_chess(
        self, chess_board: list[list[CHESS]], role: ROLE
    ) -> list[Node]:
        alive_chess: list[Node] = []
        for i, row in enumerate(chess_board):
            for j, cell in enumerate(row):
                if (
                    cell.value == role.value
                    or cell.value == CHESS.KING.value
                    and role == ROLE.WHITE
                ):
                    alive_chess.append(Node(i, j))
        return alive_chess

    def _get_heuristic(self, chess_board: list[list[CHESS]], role: ROLE) -> int:
        # TODO: Implement this in the subclass
        return -1

    def _get_game_status(
        self, chess_board: list[list[CHESS]], role: ROLE
    ) -> GAME_STATUS:
        # TODO: Implement this in the subclass
        return GAME_STATUS.ONGOING

    def _is_valid_movement(
        self, chess_board: list[list[CHESS]], from_node: Node, to_node: Node
    ) -> bool:
        # TODO: Implement this in the subclass
        return True

    def _get_captures(self, chess_board: Board, to_node: Node) -> list[Node]:
        """Cells captured by the piece that has just moved to ``to_node``."""
        # TODO: Implement this in the subclass
        return []

    def __make_move(
        self, chess_board: Board, from_node: Node, to_node: Node
    ) -> tuple[CHESS, CHESS, list[tuple[Node, CHESS]]]:
        """Apply a move and its captures in place.

        Return (moving piece, previous target cell, captured cells with their
        previous content) so that ``__undo_move`` can restore the board.
        """
        moving_piece: CHESS = chess_board[from_node.row][from_node.col]
        old_target: CHESS = chess_board[to_node.row][to_node.col]

        # The referee marks the throne as THRONE (not EMPTY) once it is vacated.
        chess_board[from_node.row][from_node.col] = (
            CHESS.THRONE if from_node == self.throne else CHESS.EMPTY
        )
        chess_board[to_node.row][to_node.col] = moving_piece

        captured: list[tuple[Node, CHESS]] = [
            (node, chess_board[node.row][node.col])
            for node in self._get_captures(chess_board, to_node)
        ]
        for node, _ in captured:
            chess_board[node.row][node.col] = (
                CHESS.THRONE if node == self.throne else CHESS.EMPTY
            )
        return moving_piece, old_target, captured

    def __undo_move(
        self,
        chess_board: Board,
        from_node: Node,
        to_node: Node,
        moving_piece: CHESS,
        old_target: CHESS,
        captured: list[tuple[Node, CHESS]],
    ) -> None:
        for node, piece in captured:
            chess_board[node.row][node.col] = piece
        chess_board[to_node.row][to_node.col] = old_target
        chess_board[from_node.row][from_node.col] = moving_piece

    def get_next_movement(
        self, chess_board: Board, role: ROLE, max_depth: int
    ) -> Best_Movement:

        alive_chess = self._get_alive_chess(chess_board, role)

        best_from: Node = Node(-1, -1)
        best_to: Node = Node(-1, -1)
        best_score: int = -self.INF if role == ROLE.WHITE else self.INF

        alpha = -self.INF
        beta = self.INF

        for node in alive_chess:
            for mv_row, mv_col in zip(self.move_row, self.move_col, strict=True):
                next_node: Node = Node(node.row + mv_row, node.col + mv_col)

                if not self._is_valid_movement(chess_board, node, next_node):
                    continue

                # Default to the first legal move so a forced loss still plays one.
                if best_from == Node(-1, -1):
                    best_from = node
                    best_to = next_node

                moving_piece, old_target, captured = self.__make_move(
                    chess_board, node, next_node
                )

                next_role = ROLE.BLACK if role == ROLE.WHITE else ROLE.WHITE

                score: int = self.__min_max_tree(
                    chess_board, max_depth, next_role, 1, alpha, beta
                )

                self.__undo_move(
                    chess_board, node, next_node, moving_piece, old_target, captured
                )

                if role == ROLE.WHITE:
                    if score > best_score:
                        best_score = score
                        best_from = node
                        best_to = next_node
                        alpha = max(alpha, best_score)
                else:
                    if score < best_score:
                        best_score = score
                        best_from = node
                        best_to = next_node
                        beta = min(beta, best_score)

        best_movement = Best_Movement(
            from_node=best_from,
            to_node=best_to,
            score=best_score,
        )

        return best_movement

    def get_next_movement_in_time(
        self, chess_board: Board, role: ROLE, time_limit: float, max_depth: int = 32
    ) -> Best_Movement:
        """Iterative deepening: search depth 1, 2, ... for at most ``time_limit``
        seconds and return the move of the last depth that was fully searched."""
        deadline = self._clock() + time_limit
        snapshot = [row[:] for row in chess_board]

        # Depth 1 runs without a deadline, so there is always a move to play.
        best = self.get_next_movement(chess_board, role, 1)
        self.completed_depth = 1

        for depth in range(2, max_depth + 1):
            # A forced win or loss (or no legal move) cannot be refined further.
            if abs(best.score) >= self.INF:
                break

            started = self._clock()
            self.__deadline = deadline
            try:
                best = self.get_next_movement(chess_board, role, depth)
            except SearchTimeout:
                # The search stopped half-way: put the moved pieces back.
                for row, saved in zip(chess_board, snapshot, strict=True):
                    row[:] = saved
                break
            finally:
                self.__deadline = None
            self.completed_depth = depth

            # The next depth is slower than this one: skip it if it cannot fit.
            now = self._clock()
            if now - started >= deadline - now:
                break

        return best

    def __min_max_tree(
        self,
        chess_board: Board,
        max_depth: int,
        role: ROLE,
        cur_depth: int,
        alpha: int,
        beta: int,
    ) -> int:

        if self.__deadline is not None and self._clock() >= self.__deadline:
            raise SearchTimeout

        game_status: GAME_STATUS = self._get_game_status(chess_board, role)
        if game_status == GAME_STATUS.WHITE_WIN:
            return self.INF
        if game_status == GAME_STATUS.BLACK_WIN:
            return -self.INF
        if game_status == GAME_STATUS.DRAW:
            return 0
        if cur_depth >= max_depth:
            return self._get_heuristic(chess_board, role)

        alive_chess: list[Node] = self._get_alive_chess(chess_board, role)

        best: int = -self.INF if role == ROLE.WHITE else self.INF

        for from_node in alive_chess:
            for mv_row, mv_col in zip(self.move_row, self.move_col, strict=True):
                next_node: Node = Node(from_node.row + mv_row, from_node.col + mv_col)
                if not self._is_valid_movement(chess_board, from_node, next_node):
                    continue

                moving_piece, old_target, captured = self.__make_move(
                    chess_board, from_node, next_node
                )

                next_role = ROLE.BLACK if role == ROLE.WHITE else ROLE.WHITE

                score: int = self.__min_max_tree(
                    chess_board, max_depth, next_role, cur_depth + 1, alpha, beta
                )

                self.__undo_move(
                    chess_board,
                    from_node,
                    next_node,
                    moving_piece,
                    old_target,
                    captured,
                )

                if role == ROLE.WHITE:
                    best = max(best, score)
                    alpha = max(alpha, best)
                    if best >= beta:
                        return best
                else:
                    best = min(best, score)
                    beta = min(beta, best)
                    if best <= alpha:
                        return best

        return best
