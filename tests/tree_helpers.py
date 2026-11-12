"""Shared helpers for the CookedTree tests.

The real Tablut rules are not implemented yet, so the search is tested against
small *fake* rules (rook-like moves, no captures). What is verified is that the
search is correct for ANY rule set, not that the Tablut rules are right.
"""

import random
from collections.abc import Callable

from tablut.common.enums.algorithm import GAME_STATUS
from tablut.common.enums.chess import CHESS
from tablut.common.enums.player import ROLE
from tablut.common.types.algorithm import Node
from tablut.cooked_tree.cooked_tree import Board, CookedTree

SIZE = 9
INF = CookedTree().INF
THRONE_POS = (4, 4)
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

type Pos = tuple[int, int]


def opponent(role: ROLE) -> ROLE:
    return ROLE.BLACK if role == ROLE.WHITE else ROLE.WHITE


# ---------------------------------------------------------------- boards


def empty_board() -> Board:
    board: Board = [[CHESS.EMPTY for _ in range(SIZE)] for _ in range(SIZE)]
    board[THRONE_POS[0]][THRONE_POS[1]] = CHESS.THRONE
    return board


def make_board(pieces: dict[Pos, CHESS]) -> Board:
    board = empty_board()
    for (row, col), piece in pieces.items():
        board[row][col] = piece
    return board


def copy_board(board: Board) -> Board:
    return [row[:] for row in board]


def random_board(seed: int, whites: int, blacks: int, king: bool = True) -> Board:
    """Reproducible board; the king may start on the (non-EMPTY) throne."""
    rng = random.Random(seed)
    cells = [(r, c) for r in range(SIZE) for c in range(SIZE)]
    rng.shuffle(cells)
    pieces: list[CHESS] = [CHESS.KING] if king else []
    pieces += [CHESS.WHITE] * whites + [CHESS.BLACK] * blacks
    return make_board(dict(zip(cells, pieces, strict=False)))


# ----------------------------------------------------------------- rules


def in_bounds(row: int, col: int) -> bool:
    return 0 <= row < SIZE and 0 <= col < SIZE


def passable(cell: CHESS) -> bool:
    return cell in (CHESS.EMPTY, CHESS.THRONE)


def rook_is_valid(board: Board, from_node: Node, to_node: Node) -> bool:
    """Fake rule: orthogonal slide over free cells, inside the board."""
    if not in_bounds(to_node.row, to_node.col):
        return False
    if (from_node.row != to_node.row) == (from_node.col != to_node.col):
        return False  # same cell, or not orthogonal
    d_row = (to_node.row > from_node.row) - (to_node.row < from_node.row)
    d_col = (to_node.col > from_node.col) - (to_node.col < from_node.col)
    row, col = from_node.row + d_row, from_node.col + d_col
    while True:
        if not passable(board[row][col]):
            return False
        if (row, col) == (to_node.row, to_node.col):
            return True
        row, col = row + d_row, col + d_col


def seeded_heuristic(seed: int = 0) -> Callable[[Board, ROLE], int]:
    """Deterministic, White-perspective, position-dependent (few ties)."""
    rng = random.Random(seed)
    table = {
        (r, c, p): rng.randint(-40, 40)
        for r in range(SIZE)
        for c in range(SIZE)
        for p in (CHESS.WHITE, CHESS.BLACK, CHESS.KING)
    }

    def heuristic(board: Board, role: ROLE) -> int:
        return sum(
            table[(r, c, cell)]
            for r, row in enumerate(board)
            for c, cell in enumerate(row)
            if cell in (CHESS.WHITE, CHESS.BLACK, CHESS.KING)
        )

    return heuristic


def constant_heuristic(value: int = 0) -> Callable[[Board, ROLE], int]:
    return lambda board, role: value


def always(status: GAME_STATUS) -> Callable[[Board, ROLE], GAME_STATUS]:
    return lambda board, role: status


def ongoing(board: Board, role: ROLE) -> GAME_STATUS:
    return GAME_STATUS.ONGOING


class FakeRulesTree(CookedTree):
    def __init__(
        self,
        heuristic: Callable[[Board, ROLE], int],
        game_status: Callable[[Board, ROLE], GAME_STATUS],
    ) -> None:
        super().__init__()
        self._heuristic_fn = heuristic
        self._game_status_fn = game_status

    def _get_heuristic(self, chess_board: Board, role: ROLE) -> int:
        return self._heuristic_fn(chess_board, role)

    def _get_game_status(self, chess_board: Board, role: ROLE) -> GAME_STATUS:
        return self._game_status_fn(chess_board, role)

    def _is_valid_movement(
        self, chess_board: Board, from_node: Node, to_node: Node
    ) -> bool:
        return rook_is_valid(chess_board, from_node, to_node)


def make_tree(
    heuristic: Callable[[Board, ROLE], int] | None = None,
    game_status: Callable[[Board, ROLE], GAME_STATUS] = ongoing,
) -> CookedTree:
    return FakeRulesTree(heuristic or seeded_heuristic(), game_status)


# ---------------------------------------------------------------- oracle


def pieces_of(board: Board, role: ROLE) -> list[Pos]:
    own = {CHESS.WHITE, CHESS.KING} if role == ROLE.WHITE else {CHESS.BLACK}
    return [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] in own]


def legal_moves(board: Board, role: ROLE) -> list[tuple[Pos, Pos]]:
    """Independent move generator: slides along the 4 directions."""
    moves: list[tuple[Pos, Pos]] = []
    for r, c in pieces_of(board, role):
        for d_row, d_col in DIRECTIONS:
            row, col = r + d_row, c + d_col
            while in_bounds(row, col) and passable(board[row][col]):
                moves.append(((r, c), (row, col)))
                row, col = row + d_row, col + d_col
    return moves


def play(board: Board, move: tuple[Pos, Pos]) -> Board:
    """Return a NEW board with the move applied (throne is kept as THRONE)."""
    (fr, fc), (tr, tc) = move
    new = copy_board(board)
    new[tr][tc] = board[fr][fc]
    new[fr][fc] = CHESS.THRONE if (fr, fc) == THRONE_POS else CHESS.EMPTY
    return new


def minimax_value(
    board: Board,
    role: ROLE,
    depth: int,
    max_depth: int,
    heuristic: Callable[[Board, ROLE], int],
    game_status: Callable[[Board, ROLE], GAME_STATUS],
) -> int:
    """Plain Minimax (NO pruning) with the same terminal/depth ordering."""
    status = game_status(board, role)
    if status == GAME_STATUS.WHITE_WIN:
        return INF
    if status == GAME_STATUS.BLACK_WIN:
        return -INF
    if status == GAME_STATUS.DRAW:
        return 0
    if depth >= max_depth:
        return heuristic(board, role)

    scores = [
        minimax_value(
            play(board, move),
            opponent(role),
            depth + 1,
            max_depth,
            heuristic,
            game_status,
        )
        for move in legal_moves(board, role)
    ]
    if not scores:
        return -INF if role == ROLE.WHITE else INF
    return max(scores) if role == ROLE.WHITE else min(scores)


def root_value(
    board: Board,
    role: ROLE,
    max_depth: int,
    heuristic: Callable[[Board, ROLE], int],
    game_status: Callable[[Board, ROLE], GAME_STATUS] = ongoing,
) -> int:
    """Value of the root position (the root itself is not checked for status)."""
    scores = [
        minimax_value(
            play(board, move), opponent(role), 1, max_depth, heuristic, game_status
        )
        for move in legal_moves(board, role)
    ]
    if not scores:
        return -INF if role == ROLE.WHITE else INF
    return max(scores) if role == ROLE.WHITE else min(scores)


def value_of_move(
    board: Board,
    role: ROLE,
    move: tuple[Pos, Pos],
    max_depth: int,
    heuristic: Callable[[Board, ROLE], int],
    game_status: Callable[[Board, ROLE], GAME_STATUS] = ongoing,
) -> int:
    return minimax_value(
        play(board, move), opponent(role), 1, max_depth, heuristic, game_status
    )


# ---------------------------------------------------------- introspection


def ordered_moves(board: Board, role: ROLE) -> list[tuple[Pos, Pos]]:
    """Moves in the SAME order CookedTree enumerates them (pieces row-major,
    then its displacement vectors). Needed to compare pruning step by step."""
    tree = CookedTree()
    moves: list[tuple[Pos, Pos]] = []
    for r, c in pieces_of(board, role):
        for d_row, d_col in zip(tree.move_row, tree.move_col, strict=True):
            if rook_is_valid(board, Node(r, c), Node(r + d_row, c + d_col)):
                moves.append(((r, c), (r + d_row, c + d_col)))
    return moves


def reference_alpha_beta(
    board: Board,
    role: ROLE,
    max_depth: int,
    heuristic: Callable[[Board, ROLE], int],
) -> tuple[int, tuple[Pos, Pos] | None, int]:
    """Textbook alpha-beta written independently of CookedTree (ongoing games
    only). Returns (score, best move, number of heuristic evaluations)."""
    evaluations = 0

    def node(b: Board, side: ROLE, depth: int, alpha: int, beta: int) -> int:
        nonlocal evaluations
        if depth >= max_depth:
            evaluations += 1
            return heuristic(b, side)
        white = side == ROLE.WHITE
        best = -INF if white else INF
        for move in ordered_moves(b, side):
            score = node(play(b, move), opponent(side), depth + 1, alpha, beta)
            if white:
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

    white = role == ROLE.WHITE
    best, best_move = (-INF if white else INF), None
    alpha, beta = -INF, INF
    for move in ordered_moves(board, role):
        score = node(play(board, move), opponent(role), 1, alpha, beta)
        if best_move is None or (score > best if white else score < best):
            best, best_move = score, move
            if white:
                alpha = max(alpha, best)
            else:
                beta = min(beta, best)
    return best, best_move, evaluations


def private(tree: CookedTree, name: str):
    """Access a double-underscore method. The mangling lives in ONE place, so a
    rename in the source only requires fixing this helper."""
    return getattr(tree, f"_CookedTree__{name}")


def as_pos(node: Node) -> Pos:
    return (node.row, node.col)
