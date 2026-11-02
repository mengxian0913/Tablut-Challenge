"""Black-box tests: only the public API (CookedTree.get_next_movement) is used.

IDs (BB-xx) are referenced by docs/test_cases/test_strategy.md.
"""

import pytest
from tree_helpers import (
    INF,
    always,
    as_pos,
    constant_heuristic,
    copy_board,
    legal_moves,
    make_board,
    make_tree,
    random_board,
    root_value,
    seeded_heuristic,
    value_of_move,
)

from tablut.common.enums.algorithm import GAME_STATUS
from tablut.common.enums.chess import CHESS
from tablut.common.enums.player import ROLE
from tablut.common.types.algorithm import Node

pytestmark = pytest.mark.blackbox

ROLES = [ROLE.WHITE, ROLE.BLACK]

# (whites, blacks, depth, seeds). The depth-3 boards have few pieces so the
# un-pruned oracle stays fast enough to run on every commit.
DIFFERENTIAL_CASES = [
    (2, 3, 1, range(12)),
    (2, 3, 2, range(12)),
    (1, 1, 3, range(5)),
]


def differential_params():
    return [
        pytest.param(
            role, seed, whites, blacks, depth, id=f"{role.name}-d{depth}-seed{seed}"
        )
        for whites, blacks, depth, seeds in DIFFERENTIAL_CASES
        for role in ROLES
        for seed in seeds
    ]


# ------------------------------------------- BB-01..03 differential testing


@pytest.mark.parametrize("role, seed, whites, blacks, depth", differential_params())
def test_bb01_to_bb03_matches_unpruned_minimax(role, seed, whites, blacks, depth):
    """BB-01 score == plain Minimax, BB-02 chosen move is legal and worth that
    score, BB-03 the caller's board is left untouched."""
    board = random_board(seed, whites, blacks)
    original = copy_board(board)
    heuristic = seeded_heuristic(seed)
    tree = make_tree(heuristic)

    result = tree.get_next_movement(board, role, depth)

    assert board == original, "the input board was modified"
    assert result.score == root_value(original, role, depth, heuristic)
    move = (as_pos(result.from_node), as_pos(result.to_node))
    assert move in legal_moves(original, role), "illegal move returned"
    assert value_of_move(original, role, move, depth, heuristic) == result.score
    assert -INF <= result.score <= INF


# ------------------------------------------------- BB-04 greedy depth 1


def column_heuristic(board, role):
    """White-perspective: white pieces like high columns, black likes low."""
    total = 0
    for row in board:
        for col, cell in enumerate(row):
            if cell in (CHESS.WHITE, CHESS.KING):
                total += col
            elif cell == CHESS.BLACK:
                total -= col
    return total


def test_bb04_white_depth1_maximises_heuristic():
    board = make_board({(2, 0): CHESS.WHITE, (6, 3): CHESS.BLACK})
    tree = make_tree(column_heuristic)

    result = tree.get_next_movement(board, ROLE.WHITE, 1)

    assert (as_pos(result.from_node), as_pos(result.to_node)) == ((2, 0), (2, 8))
    # white moves 0 -> 8 columns while black stays on column 3
    assert result.score == 8 - 3


def test_bb04_black_depth1_minimises_heuristic():
    board = make_board({(2, 0): CHESS.WHITE, (6, 3): CHESS.BLACK})
    tree = make_tree(column_heuristic)

    result = tree.get_next_movement(board, ROLE.BLACK, 1)

    assert (as_pos(result.from_node), as_pos(result.to_node)) == ((6, 3), (6, 8))
    assert result.score == 0 - 8


# ------------------------------------------- BB-05..07 tactical scenarios


def king_on_edge_wins(board, role):
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == CHESS.KING and (r in (0, 8) or c in (0, 8)):
                return GAME_STATUS.WHITE_WIN
    return GAME_STATUS.ONGOING


def test_bb05_white_takes_immediate_win():
    board = make_board({(4, 3): CHESS.KING})
    tree = make_tree(constant_heuristic(0), king_on_edge_wins)

    result = tree.get_next_movement(board, ROLE.WHITE, 1)

    assert result.score == INF
    assert as_pos(result.from_node) == (4, 3)
    assert result.to_node.row in (0, 8) or result.to_node.col in (0, 8)


def test_bb05_win_is_seen_even_at_the_depth_limit():
    """The terminal check must come before the depth cut-off (depth 1 here)."""
    board = make_board({(4, 3): CHESS.KING})
    tree = make_tree(constant_heuristic(-999), king_on_edge_wins)

    assert tree.get_next_movement(board, ROLE.WHITE, 1).score == INF


def king_on_top_row_wins(board, role):
    return GAME_STATUS.WHITE_WIN if CHESS.KING in board[0] else GAME_STATUS.ONGOING


def test_bb06_black_blocks_the_only_escape():
    """King (3,3) threatens to reach row 0 through column 3. Black has a
    single piece and exactly one move (to (0,3)) stops it."""
    board = make_board({(3, 3): CHESS.KING, (0, 0): CHESS.BLACK})
    tree = make_tree(constant_heuristic(0), king_on_top_row_wins)

    result = tree.get_next_movement(board, ROLE.BLACK, 2)

    assert (as_pos(result.from_node), as_pos(result.to_node)) == ((0, 0), (0, 3))
    assert result.score == 0  # no forced win for white any more


def black_reaches_corner_wins(board, role):
    return GAME_STATUS.BLACK_WIN if board[8][8] == CHESS.BLACK else GAME_STATUS.ONGOING


def test_bb07_white_blocks_black_threat():
    """Black (8,0) would slide to the winning cell (8,8). Only the white
    soldier (7,5) can interpose, by moving to (8,5)."""
    board = make_board({(0, 0): CHESS.KING, (7, 5): CHESS.WHITE, (8, 0): CHESS.BLACK})
    tree = make_tree(constant_heuristic(0), black_reaches_corner_wins)

    result = tree.get_next_movement(board, ROLE.WHITE, 2)

    assert (as_pos(result.from_node), as_pos(result.to_node)) == ((7, 5), (8, 5))
    assert result.score == 0


def test_bb07_depth1_does_not_see_the_threat():
    """Search depth matters: with depth 1 white cannot know it must block."""
    board = make_board({(0, 0): CHESS.KING, (7, 5): CHESS.WHITE, (8, 0): CHESS.BLACK})
    tree = make_tree(constant_heuristic(0), black_reaches_corner_wins)

    assert tree.get_next_movement(board, ROLE.WHITE, 1).score == 0
    assert tree.get_next_movement(board, ROLE.WHITE, 2).score == 0
    # but if white cannot block, depth 2 reveals the loss
    unblockable = make_board({(0, 0): CHESS.KING, (8, 0): CHESS.BLACK})
    assert tree.get_next_movement(unblockable, ROLE.WHITE, 2).score == -INF


# --------------------------------------------- BB-08 terminal statuses


TERMINAL_CASES = [
    (GAME_STATUS.WHITE_WIN, INF),
    (GAME_STATUS.BLACK_WIN, -INF),
    (GAME_STATUS.DRAW, 0),
]


@pytest.mark.parametrize("role", ROLES, ids=lambda r: r.name)
@pytest.mark.parametrize(
    "status, expected", TERMINAL_CASES, ids=lambda v: getattr(v, "name", str(v))
)
def test_bb08_terminal_status_scores(role, status, expected):
    """Even when every continuation is already decided (so the player is
    forced to lose, win or draw) a LEGAL move must still be returned."""
    board = random_board(3, 2, 3)
    tree = make_tree(constant_heuristic(7), always(status))

    result = tree.get_next_movement(board, role, 3)

    assert result.score == expected
    move = (as_pos(result.from_node), as_pos(result.to_node))
    assert move in legal_moves(board, role)


# ------------------------------------------------ BB-09 no legal moves


NO_MOVE_CASES = [
    pytest.param(
        ROLE.WHITE,
        {(0, 0): CHESS.KING, (0, 1): CHESS.BLACK, (1, 0): CHESS.BLACK},
        -INF,
        id="white-boxed-in",
    ),
    pytest.param(
        ROLE.BLACK,
        {(0, 0): CHESS.BLACK, (0, 1): CHESS.WHITE, (1, 0): CHESS.WHITE},
        INF,
        id="black-boxed-in",
    ),
    pytest.param(ROLE.WHITE, {}, -INF, id="white-has-no-pieces"),
    pytest.param(ROLE.BLACK, {}, INF, id="black-has-no-pieces"),
]


@pytest.mark.parametrize("role, pieces, expected_score", NO_MOVE_CASES)
def test_bb09_no_legal_move_returns_sentinel(role, pieces, expected_score):
    """A side that cannot move loses; the root reports it with the (-1,-1)
    sentinel and the worst score for that side."""
    result = make_tree().get_next_movement(make_board(pieces), role, 2)

    assert result.from_node == Node(-1, -1)
    assert result.to_node == Node(-1, -1)
    assert result.score == expected_score


# ------------------------------------------------ BB-10 determinism


def test_bb10_deterministic_and_no_state_leaks_between_calls():
    board_a = random_board(1, 2, 2)
    board_b = random_board(2, 2, 2)
    tree = make_tree(seeded_heuristic(5))

    first = tree.get_next_movement(copy_board(board_a), ROLE.WHITE, 2)
    tree.get_next_movement(copy_board(board_b), ROLE.BLACK, 2)
    second = tree.get_next_movement(copy_board(board_a), ROLE.WHITE, 2)

    assert first == second


# ------------------------------------------------ BB-11 piece ownership


def test_bb11_white_can_move_a_lone_king():
    board = make_board({(4, 4): CHESS.KING, (0, 0): CHESS.BLACK})

    result = make_tree().get_next_movement(board, ROLE.WHITE, 1)

    assert as_pos(result.from_node) == (4, 4)


@pytest.mark.parametrize("seed", range(6))
def test_bb11_each_side_only_moves_its_own_pieces(seed):
    board = random_board(seed, 2, 3)
    tree = make_tree(seeded_heuristic(seed))

    white = tree.get_next_movement(copy_board(board), ROLE.WHITE, 1)
    black = tree.get_next_movement(copy_board(board), ROLE.BLACK, 1)

    assert board[white.from_node.row][white.from_node.col] in (
        CHESS.WHITE,
        CHESS.KING,
    )
    assert board[black.from_node.row][black.from_node.col] == CHESS.BLACK


# ------------------------------------------- BB-12 longest slides (8 cells)

# (start, target, white_bystander): the white piece sits where it can neither
# block the black slide nor reach the target, so black's 8-cell slide decides.
EXTREME_SLIDES = [
    pytest.param((0, 0), (8, 0), (0, 5), id="down-8"),
    pytest.param((8, 0), (0, 0), (8, 5), id="up-8"),
    pytest.param((0, 0), (0, 8), (5, 0), id="right-8"),
    pytest.param((0, 8), (0, 0), (5, 8), id="left-8"),
]


@pytest.mark.parametrize("start, target, bystander", EXTREME_SLIDES)
def test_bb12_root_considers_the_longest_slide_in_every_direction(
    start, target, bystander
):
    board = make_board({start: CHESS.WHITE})

    def likes_target(b, role):
        return 1 if b[target[0]][target[1]] == CHESS.WHITE else 0

    result = make_tree(likes_target).get_next_movement(board, ROLE.WHITE, 1)

    assert (as_pos(result.from_node), as_pos(result.to_node)) == (start, target)
    assert result.score == 1


@pytest.mark.parametrize("start, target, bystander", EXTREME_SLIDES)
def test_bb12_deeper_nodes_consider_the_longest_slide_too(start, target, bystander):
    """Black's reply (a deeper node, not the root) must also see the 8-cell
    slide: it is the only way to reach the target and score -1."""
    board = make_board({bystander: CHESS.WHITE, start: CHESS.BLACK})

    def black_likes_target(b, role):
        return -1 if b[target[0]][target[1]] == CHESS.BLACK else 0

    result = make_tree(black_likes_target).get_next_movement(board, ROLE.WHITE, 2)

    assert result.score == -1
