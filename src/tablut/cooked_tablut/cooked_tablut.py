from tablut.common.enums.algorithm import GAME_STATUS
from tablut.common.enums.chess import CHESS
from tablut.common.enums.player import ROLE
from tablut.common.types.algorithm import Board, Node
from tablut.cooked_tree.cooked_tree import CookedTree

DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
CASTLE = (4, 4)
CAMP_CELLS = frozenset(
    {
        (0, 3), (0, 4), (0, 5), (1, 4),
        (8, 3), (8, 4), (8, 5), (7, 4),
        (3, 0), (4, 0), (5, 0), (4, 1),
        (3, 8), (4, 8), (5, 8), (4, 7),
    }
)  # fmt: skip
# The referee does not let White capture against these four camp cells.
CAMP_EDGE_CENTERS = frozenset({(0, 4), (8, 4), (4, 0), (4, 8)})


class CookedTablut(CookedTree):
    def dist(self, x, y, Node):
        x_dist = abs(x - Node.row)
        y_dist = abs(y - Node.col)
        distance = x_dist + y_dist
        return distance

    def _get_heuristic(self, chess_board: Board, role: ROLE) -> int:
        scores = []
        alive = super()._get_alive_chess(chess_board, role)
        for piece in alive:
            scores.append(self.get_score(piece, chess_board, role))
        heuristic = sum(scores)
        return heuristic

    def get_score(self, current_node: Node, chess_board: Board, role: ROLE):
        score = 0
        neighbor = None

        if role == ROLE.WHITE:
            if chess_board[current_node.row][current_node.col] == CHESS.KING:
                winning = [
                    Node(0, 1),
                    Node(0, 2),
                    Node(0, 6),
                    Node(0, 7),
                    Node(1, 0),
                    Node(2, 0),
                    Node(1, 8),
                    Node(2, 8),
                    Node(6, 0),
                    Node(7, 0),
                    Node(8, 1),
                    Node(8, 2),
                    Node(6, 8),
                    Node(7, 8),
                    Node(8, 6),
                    Node(8, 7),
                ]
                for winning_node in winning:
                    if (
                        current_node.row == winning_node.row
                        or current_node.col == winning_node.col
                    ) and self._is_valid_movement(
                        chess_board, current_node, winning_node
                    ):
                        score += 5

            for x in range(current_node.row - 1, current_node.row + 2):
                for y in range(current_node.col - 1, current_node.col + 2):
                    if x < 0 or x > 8 or y < 0 or y > 8:
                        continue
                    piece = chess_board[x][y]
                    if piece == CHESS.BLACK and self.dist(x, y, current_node) == 1:
                        score -= 1
                        neighbor = Node(x, y)
                    if score == -2:
                        break

            if score == -1 and neighbor != None:
                for x in range(neighbor.row - 1, neighbor.row + 2):
                    for y in range(neighbor.col - 1, neighbor.col + 2):
                        if x < 0 or x > 8 or y < 0 or y > 8:
                            continue
                        piece = chess_board[x][y]
                        if (
                            self.dist(x, y, neighbor) == 1
                            and piece == CHESS.WHITE
                            and (x == current_node.row or y == current_node.col)
                            and (Node(x, y) != current_node)
                        ):
                            score += 3

        # Black:
        else:
            for x in range(current_node.row - 1, current_node.row + 2):
                for y in range(current_node.col - 1, current_node.col + 2):
                    if x < 0 or x > 8 or y < 0 or y > 8:
                        continue
                    piece = chess_board[x][y]
                    if piece == CHESS.WHITE and self.dist(x, y, current_node) == 1:
                        score += 1
                    if score == 2:
                        break
            if score == 1 and neighbor != None:
                for x in range(neighbor.row - 1, neighbor.row + 2):
                    for y in range(neighbor.col - 1, neighbor.col + 2):
                        if x < 0 or x > 8 or y < 0 or y > 8:
                            continue
                        piece = chess_board[x][y]
                        if (
                            self.dist(x, y, neighbor) == 1
                            and piece == CHESS.WHITE
                            and (x == current_node.row or y == current_node.col)
                            and (Node(x, y) != neighbor)
                        ):
                            score -= 3
        return score

    # The same "state" of the game is reached twice: draw
    def _get_game_status(self, chess_board: Board, role: ROLE) -> GAME_STATUS:
        king: Node | None = None
        for x in range(0, 9):
            for y in range(0, 9):
                if chess_board[x][y] == CHESS.KING:
                    king = Node(x, y)
                    break
        # The king is removed from the board when it is captured.
        if king is None:
            return GAME_STATUS.BLACK_WIN
        winning = [
            Node(0, 1),
            Node(0, 2),
            Node(0, 6),
            Node(0, 7),
            Node(1, 0),
            Node(2, 0),
            Node(1, 8),
            Node(2, 8),
            Node(6, 0),
            Node(7, 0),
            Node(8, 1),
            Node(8, 2),
            Node(6, 8),
            Node(7, 8),
            Node(8, 6),
            Node(8, 7),
        ]
        if king in winning:
            return GAME_STATUS.WHITE_WIN

        check = False

        my_chess = super()._get_alive_chess(chess_board, role)

        for piece in my_chess:
            for x in range(9):
                if piece.row == x:
                    continue
                if self._is_valid_movement(chess_board, piece, Node(x, piece.col)):
                    check = True
                    break

            for y in range(9):
                if piece.col == y:
                    continue
                if self._is_valid_movement(chess_board, piece, Node(piece.row, y)):
                    check = True
                    break

        if not check and role == ROLE.WHITE:
            return GAME_STATUS.BLACK_WIN
        elif not check and role == ROLE.BLACK:
            return GAME_STATUS.WHITE_WIN

        return GAME_STATUS.ONGOING

    def _is_valid_movement(
        self, chess_board: Board, from_node: Node, to_node: Node
    ) -> bool:

        if from_node.row == to_node.row and from_node.col == to_node.col:
            return False

        if from_node.row != to_node.row and from_node.col != to_node.col:
            return False

        if to_node.row < 0 or to_node.row > 8 or to_node.col < 0 or to_node.col > 8:
            return False

        if (
            chess_board[from_node.row][from_node.col] != CHESS.KING
            and to_node.row == 4
            and to_node.col == 4
        ):
            return False

        # Every cell up to and including the target must be free. A piece that
        # does not start inside a camp cannot cross a camp cell either.
        step_row = (to_node.row > from_node.row) - (to_node.row < from_node.row)
        step_col = (to_node.col > from_node.col) - (to_node.col < from_node.col)
        from_camp = (from_node.row, from_node.col) in CAMP_CELLS
        row, col = from_node.row, from_node.col
        while (row, col) != (to_node.row, to_node.col):
            row, col = row + step_row, col + step_col
            if chess_board[row][col] != CHESS.EMPTY:
                return False
            if not from_camp and (row, col) in CAMP_CELLS:
                return False

        camps_left = [Node(0, 3), Node(0, 4), Node(0, 5), Node(1, 4)]
        camps_right = [Node(8, 3), Node(8, 4), Node(8, 5), Node(7, 4)]
        camps_low = [Node(3, 0), Node(4, 0), Node(5, 0), Node(4, 1)]
        camps_up = [Node(3, 8), Node(4, 8), Node(5, 8), Node(4, 7)]

        if to_node in camps_left and from_node not in camps_left:
            return False
        if to_node in camps_low and from_node not in camps_low:
            return False
        if to_node in camps_up and from_node not in camps_up:
            return False
        if to_node in camps_right and from_node not in camps_right:
            return False

        return True

    def _get_captures(self, chess_board: Board, to_node: Node) -> list[Node]:
        """Captures made by the piece that has just moved to ``to_node``.

        Mirrors the referee (GameAshtonTablut): a capture is always "active",
        so only the four neighbours of the moved piece can be captured.
        """
        mover = chess_board[to_node.row][to_node.col]
        captured: list[Node] = []

        for d_row, d_col in DIRECTIONS:
            row, col = to_node.row + d_row, to_node.col + d_col
            far = (row + d_row, col + d_col)
            if far[0] < 0 or far[0] > 8 or far[1] < 0 or far[1] > 8:
                continue
            victim = chess_board[row][col]
            anvil = chess_board[far[0]][far[1]]

            if mover == CHESS.BLACK:
                if victim == CHESS.KING:
                    if self._is_king_captured(chess_board, row, col, far):
                        captured.append(Node(row, col))
                elif victim == CHESS.WHITE and (
                    anvil == CHESS.BLACK or far in CAMP_CELLS or far == CASTLE
                ):
                    captured.append(Node(row, col))
            elif (
                mover in (CHESS.WHITE, CHESS.KING)
                and victim == CHESS.BLACK
                and (
                    anvil in (CHESS.WHITE, CHESS.KING, CHESS.THRONE)
                    or (far in CAMP_CELLS and far not in CAMP_EDGE_CENTERS)
                )
            ):
                captured.append(Node(row, col))

        return captured

    def _is_king_captured(
        self, chess_board: Board, row: int, col: int, far: tuple[int, int]
    ) -> bool:
        """King at (row, col), attacked by a black piece opposite to ``far``."""
        # In the castle or next to it: every side but the castle must be black.
        if abs(row - CASTLE[0]) + abs(col - CASTLE[1]) <= 1:
            return all(
                (row + d_row, col + d_col) == CASTLE
                or chess_board[row + d_row][col + d_col] == CHESS.BLACK
                for d_row, d_col in DIRECTIONS
            )
        return chess_board[far[0]][far[1]] == CHESS.BLACK or far in CAMP_CELLS
