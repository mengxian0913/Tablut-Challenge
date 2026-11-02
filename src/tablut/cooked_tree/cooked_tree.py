import random

from tablut.common.enums.algorithm import GAME_STATUS
from tablut.common.enums.chess import CHESS
from tablut.common.enums.player import ROLE
from tablut.common.types.algorithm import Best_Movement, Node


class CookedTree:
    def __init__(self) -> None:
        self.INF: int = 0x3F3F3F
        self.throne: Node = Node(4, 4)
        self.move_row: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, -5, -6, -7, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # fmt: skip # noqa: E501
        self.move_col: list[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, -5, -6, -7, -8]  # fmt: skip # noqa: E501

    def __get_alive_chess(
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

    def __get_heuristic(self, chess_board: list[list[CHESS]], role: ROLE) -> int:
        # TODO: Implement heuristic function
        return random.randint(-100, 100)

    def __get_game_status(
        self, chess_board: list[list[CHESS]], role: ROLE
    ) -> GAME_STATUS:
        # TODO: Implement this function
        return GAME_STATUS.ONGOING

    def __is_valid_movement(
        self, chess_board: list[list[CHESS]], from_node: Node, to_node: Node
    ) -> bool:
        # TODO: Implement this function
        return True

    def __make_move(
        self, chess_board: list[list[CHESS]], from_node: Node, to_node: Node
    ) -> tuple[CHESS, CHESS]:
        """Apply a move in place; return (moving piece, previous target cell)."""
        moving_piece: CHESS = chess_board[from_node.row][from_node.col]
        old_target: CHESS = chess_board[to_node.row][to_node.col]

        # The referee marks the throne as THRONE (not EMPTY) once it is vacated.
        chess_board[from_node.row][from_node.col] = (
            CHESS.THRONE if from_node == self.throne else CHESS.EMPTY
        )
        chess_board[to_node.row][to_node.col] = moving_piece
        return moving_piece, old_target

    def __undo_move(
        self,
        chess_board: list[list[CHESS]],
        from_node: Node,
        to_node: Node,
        moving_piece: CHESS,
        old_target: CHESS,
    ) -> None:
        chess_board[to_node.row][to_node.col] = old_target
        chess_board[from_node.row][from_node.col] = moving_piece

    def get_next_movement(
        self, chess_board: list[list[CHESS]], role: ROLE, max_depth: int
    ) -> Best_Movement:

        alive_chess = self.__get_alive_chess(chess_board, role)

        best_from: Node = Node(-1, -1)
        best_to: Node = Node(-1, -1)
        best_score: int = -self.INF if role == ROLE.WHITE else self.INF

        alpha = -self.INF
        beta = self.INF

        for node in alive_chess:
            for mv_row, mv_col in zip(self.move_row, self.move_col, strict=True):
                next_node: Node = Node(node.row + mv_row, node.col + mv_col)

                if not self.__is_valid_movement(chess_board, node, next_node):
                    continue

                # Default to the first legal move so a forced loss still plays one.
                if best_from == Node(-1, -1):
                    best_from = node
                    best_to = next_node

                moving_piece, old_target = self.__make_move(
                    chess_board, node, next_node
                )

                next_role = ROLE.BLACK if role == ROLE.WHITE else ROLE.WHITE

                score: int = self.__min_max_tree(
                    chess_board, max_depth, next_role, 1, alpha, beta
                )

                self.__undo_move(chess_board, node, next_node, moving_piece, old_target)

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

    def __min_max_tree(
        self,
        chess_board: list[list[CHESS]],
        max_depth: int,
        role: ROLE,
        cur_depth: int,
        alpha: int,
        beta: int,
    ) -> int:

        game_status: GAME_STATUS = self.__get_game_status(chess_board, role)
        if game_status == GAME_STATUS.WHITE_WIN:
            return self.INF
        if game_status == GAME_STATUS.BLACK_WIN:
            return -self.INF
        if game_status == GAME_STATUS.DRAW:
            return 0
        if cur_depth >= max_depth:
            return self.__get_heuristic(chess_board, role)

        alive_chess: list[Node] = self.__get_alive_chess(chess_board, role)

        best: int = -self.INF if role == ROLE.WHITE else self.INF

        for from_node in alive_chess:
            for mv_row, mv_col in zip(self.move_row, self.move_col, strict=True):
                next_node: Node = Node(from_node.row + mv_row, from_node.col + mv_col)
                if not self.__is_valid_movement(chess_board, from_node, next_node):
                    continue

                moving_piece, old_target = self.__make_move(
                    chess_board, from_node, next_node
                )

                next_role = ROLE.BLACK if role == ROLE.WHITE else ROLE.WHITE

                score: int = self.__min_max_tree(
                    chess_board, max_depth, next_role, cur_depth + 1, alpha, beta
                )

                self.__undo_move(
                    chess_board, from_node, next_node, moving_piece, old_target
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
