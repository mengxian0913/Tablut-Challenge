"""White-box tests: they target the internal structure of CookedTree.

IDs (WB-xx) are referenced by docs/test_cases/test_strategy.md.
Double-underscore methods are reached through ``private`` (tree_helpers), so a
rename in the source only needs one fix in the helper.
"""

import pytest
from tree_helpers import (
    SIZE,
    THRONE_POS,
    always,
    as_pos,
    constant_heuristic,
    copy_board,
    legal_moves,
    make_board,
    make_tree,
    private,
    random_board,
    reference_alpha_beta,
    rook_is_valid,
    root_value,
    seeded_heuristic,
)

from tablut.common.enums.algorithm import GAME_STATUS
from tablut.common.enums.chess import CHESS
from tablut.common.enums.player import ROLE
from tablut.common.types.algorithm import Node
from tablut.cooked_tree.cooked_tree import CookedTree

pytestmark = pytest.mark.whitebox


# --------------------------------------------- WB-01 move vector table


def test_wb01_move_vectors_cover_every_rook_displacement_once():
    tree = CookedTree()
    vectors = list(zip(tree.move_row, tree.move_col, strict=True))

    expected = {(sign * step, 0) for step in range(1, SIZE) for sign in (1, -1)} | {
        (0, sign * step) for step in range(1, SIZE) for sign in (1, -1)
    }
    assert len(vectors) == 4 * (SIZE - 1)
    assert set(vectors) == expected  # all of them ...
    assert len(set(vectors)) == len(vectors)  # ... and no duplicates


# ----------------------------------------------- WB-02 alive pieces


def test_wb02_white_includes_king_and_is_row_major():
    board = make_board(
        {
            (7, 1): CHESS.WHITE,
            (4, 4): CHESS.KING,
            (2, 6): CHESS.WHITE,
            (0, 0): CHESS.BLACK,
        }
    )

    alive = CookedTree()._get_alive_chess(board, ROLE.WHITE)

    assert [as_pos(n) for n in alive] == [(2, 6), (4, 4), (7, 1)]


def test_wb02_black_only_black_pieces():
    board = make_board({(7, 1): CHESS.WHITE, (4, 4): CHESS.KING, (0, 0): CHESS.BLACK})

    alive = CookedTree()._get_alive_chess(board, ROLE.BLACK)

    assert [as_pos(n) for n in alive] == [(0, 0)]


@pytest.mark.parametrize("role", [ROLE.WHITE, ROLE.BLACK])
def test_wb02_no_pieces_means_empty_list(role):
    alive = CookedTree()._get_alive_chess(make_board({}), role)

    assert alive == []  # the empty THRONE cell is not a piece


# ------------------------------------------ WB-03..06 make / undo move


def test_wb03_make_move_moves_the_piece():
    board = make_board({(2, 2): CHESS.WHITE})
    tree = CookedTree()

    piece, old, captured = private(tree, "make_move")(board, Node(2, 2), Node(2, 7))

    assert (piece, old, captured) == (CHESS.WHITE, CHESS.EMPTY, [])
    assert board[2][2] == CHESS.EMPTY
    assert board[2][7] == CHESS.WHITE


def test_wb04_leaving_the_throne_leaves_a_throne_cell():
    board = make_board({THRONE_POS: CHESS.KING})
    tree = CookedTree()

    private(tree, "make_move")(board, Node(*THRONE_POS), Node(4, 6))

    assert board[THRONE_POS[0]][THRONE_POS[1]] == CHESS.THRONE
    assert board[4][6] == CHESS.KING


def test_wb04_leaving_a_normal_cell_leaves_it_empty():
    board = make_board({(1, 1): CHESS.BLACK})

    private(CookedTree(), "make_move")(board, Node(1, 1), Node(1, 2))

    assert board[1][1] == CHESS.EMPTY


@pytest.mark.parametrize(
    "target_piece", [CHESS.EMPTY, CHESS.THRONE, CHESS.BLACK, CHESS.WHITE]
)
def test_wb05_undo_restores_whatever_was_on_the_target(target_piece):
    """The target is restored to its ORIGINAL content, not forced to EMPTY
    (it matters for the throne)."""
    board = make_board({(0, 0): CHESS.KING})
    board[0][5] = target_piece
    original = copy_board(board)
    tree = CookedTree()

    piece, old, captured = private(tree, "make_move")(board, Node(0, 0), Node(0, 5))
    private(tree, "undo_move")(board, Node(0, 0), Node(0, 5), piece, old, captured)

    assert board == original


def test_wb05_captured_pieces_are_removed_and_restored_by_undo():
    """A captured king on the throne leaves a THRONE cell, like a vacated one."""

    class CapturingTree(CookedTree):
        def _get_captures(self, chess_board, to_node):
            return [Node(2, 3), Node(*THRONE_POS)]

    board = make_board(
        {(2, 0): CHESS.BLACK, (2, 3): CHESS.WHITE, THRONE_POS: CHESS.KING}
    )
    original = copy_board(board)
    tree = CapturingTree()

    piece, old, captured = private(tree, "make_move")(board, Node(2, 0), Node(2, 2))

    assert captured == [(Node(2, 3), CHESS.WHITE), (Node(*THRONE_POS), CHESS.KING)]
    assert board[2][3] == CHESS.EMPTY
    assert board[THRONE_POS[0]][THRONE_POS[1]] == CHESS.THRONE

    private(tree, "undo_move")(board, Node(2, 0), Node(2, 2), piece, old, captured)
    assert board == original


def test_wb06_king_returning_to_the_throne_round_trip():
    board = make_board({(4, 6): CHESS.KING})
    original = copy_board(board)
    tree = CookedTree()

    piece, old, captured = private(tree, "make_move")(
        board, Node(4, 6), Node(*THRONE_POS)
    )
    assert board[4][4] == CHESS.KING and board[4][6] == CHESS.EMPTY
    assert old == CHESS.THRONE

    private(tree, "undo_move")(
        board, Node(4, 6), Node(*THRONE_POS), piece, old, captured
    )
    assert board == original


# ------------------------------------------- WB-07/08 rule injection


def test_wb07_default_rules_are_the_placeholder_implementations():
    """Placeholders: update this test when the real rules are implemented."""
    tree = CookedTree()
    board = make_board({})

    assert tree._get_game_status(board, ROLE.WHITE) == GAME_STATUS.ONGOING
    assert tree._is_valid_movement(board, Node(0, 0), Node(0, 1)) is True
    assert tree._get_captures(board, Node(0, 1)) == []
    assert all(-100 <= tree._get_heuristic(board, ROLE.WHITE) <= 100 for _ in range(50))


def test_wb08_injected_rules_replace_the_defaults():
    board = make_board({(3, 3): CHESS.WHITE})
    tree = make_tree(constant_heuristic(1), always(GAME_STATUS.DRAW))

    assert tree._get_heuristic(board, ROLE.WHITE) == 1
    assert tree._get_game_status(board, ROLE.WHITE) == GAME_STATUS.DRAW
    assert tree._is_valid_movement(board, Node(3, 3), Node(3, 4)) is True
    assert tree._is_valid_movement(board, Node(3, 3), Node(4, 4)) is False


# ------------------------------------- WB-09/10 evaluation order & roles


def test_wb09_heuristic_runs_only_on_ongoing_leaves():
    """Terminal status wins over the depth cut-off: the heuristic must not be
    consulted for a node that is already decided."""
    calls = []

    def spy(board, role):
        calls.append(1)
        return 0

    board = make_board({(4, 3): CHESS.KING})
    tree = make_tree(spy, always(GAME_STATUS.DRAW))

    tree.get_next_movement(board, ROLE.WHITE, 3)

    assert calls == []


def test_wb10_status_is_called_with_the_side_to_move():
    seen = []

    def spy(board, role):
        seen.append(role)
        return GAME_STATUS.ONGOING

    board = make_board({(0, 0): CHESS.KING, (8, 8): CHESS.BLACK})
    tree = make_tree(constant_heuristic(0), spy)

    tree.get_next_movement(board, ROLE.WHITE, 2)

    assert set(seen) == {ROLE.BLACK, ROLE.WHITE}
    assert seen[0] == ROLE.BLACK  # first evaluated node: opponent to move


def test_wb10_heuristic_receives_the_side_to_move_at_the_leaves():
    seen = []

    def spy(board, role):
        seen.append(role)
        return 0

    board = make_board({(0, 0): CHESS.KING, (8, 8): CHESS.BLACK})

    make_tree(spy).get_next_movement(board, ROLE.WHITE, 1)
    assert set(seen) == {ROLE.BLACK}  # depth 1: it is black's turn

    seen.clear()
    make_tree(spy).get_next_movement(board, ROLE.WHITE, 2)
    assert set(seen) == {ROLE.WHITE}  # depth 2: back to white


# -------------------------------------------------- WB-11 pruning


class CountingHeuristic:
    def __init__(self, inner):
        self.inner = inner
        self.calls = 0

    def __call__(self, board, role):
        self.calls += 1
        return self.inner(board, role)


def unpruned_leaf_count(board, role, depth, heuristic):
    counter = CountingHeuristic(heuristic)
    root_value(board, role, depth, counter)
    return counter.calls


@pytest.mark.parametrize("role", [ROLE.WHITE, ROLE.BLACK], ids=lambda r: r.name)
@pytest.mark.parametrize("seed", range(4))
def test_wb11_alpha_beta_really_prunes(role, seed):
    """Same answer as Minimax, but with strictly fewer leaf evaluations."""
    board = random_board(seed, 1, 2)
    base = seeded_heuristic(seed)
    counted = CountingHeuristic(base)
    tree = make_tree(counted)

    result = tree.get_next_movement(copy_board(board), role, 3)

    assert result.score == root_value(board, role, 3, base)
    assert counted.calls < unpruned_leaf_count(board, role, 3, base)


@pytest.mark.parametrize("role", [ROLE.WHITE, ROLE.BLACK], ids=lambda r: r.name)
def test_wb11_cut_off_on_equality_with_flat_evaluation(role):
    """With every leaf equal, `best >= beta` / `best <= alpha` (equality) must
    cut: a strict comparison would visit far more leaves."""
    board = random_board(9, 1, 2)
    counted = CountingHeuristic(constant_heuristic(0))
    tree = make_tree(counted)

    result = tree.get_next_movement(copy_board(board), role, 3)

    assert result.score == 0
    flat_leaves = unpruned_leaf_count(board, role, 3, constant_heuristic(0))
    assert counted.calls * 5 < flat_leaves


# ----------------------------------- WB-15 pruning == reference alpha-beta


@pytest.mark.parametrize("role", [ROLE.WHITE, ROLE.BLACK], ids=lambda r: r.name)
@pytest.mark.parametrize("depth", [2, 3])
@pytest.mark.parametrize("seed", range(4))
def test_wb15_same_pruning_as_a_textbook_alpha_beta(seed, depth, role):
    """The tree must take exactly the same decisions AND evaluate exactly the
    same leaves as an independent textbook alpha-beta that uses the same move
    order. This catches 'correct but slower' regressions (a missing window
    update, a `>` instead of `>=`, ...) that a result comparison cannot see.
    It is expected to be updated when move ordering is introduced."""
    board = random_board(seed, 1, 2)
    base = seeded_heuristic(seed)
    counted = CountingHeuristic(base)

    result = make_tree(counted).get_next_movement(copy_board(board), role, depth)

    score, move, evaluations = reference_alpha_beta(board, role, depth, base)
    assert result.score == score
    assert (as_pos(result.from_node), as_pos(result.to_node)) == move
    assert counted.calls == evaluations


# ---------------------------------------------- WB-12 tie-breaking


def test_wb12_ties_keep_the_first_move_in_enumeration_order():
    """CHARACTERIZATION: with every score equal the FIRST legal move wins.
    Enumeration order: pieces row-major, then vectors (rows down, rows up,
    cols right, cols left). Expected to change if move ordering is added."""
    board = make_board({(2, 2): CHESS.WHITE, (6, 6): CHESS.BLACK})
    tree = make_tree(constant_heuristic(0))

    white = tree.get_next_movement(copy_board(board), ROLE.WHITE, 1)
    black = tree.get_next_movement(copy_board(board), ROLE.BLACK, 1)

    assert (as_pos(white.from_node), as_pos(white.to_node)) == ((2, 2), (3, 2))
    assert (as_pos(black.from_node), as_pos(black.to_node)) == ((6, 6), (7, 6))


def test_wb12_a_later_strictly_better_move_replaces_the_default():
    board = make_board({(2, 2): CHESS.WHITE})

    def prefers_row_8(board, role):
        return 1 if board[8][2] == CHESS.WHITE else 0

    result = make_tree(prefers_row_8).get_next_movement(board, ROLE.WHITE, 1)

    assert as_pos(result.to_node) == (8, 2)
    assert result.score == 1


# ------------------------------------------------ WB-13 depth limits


@pytest.mark.parametrize("role", [ROLE.WHITE, ROLE.BLACK], ids=lambda r: r.name)
def test_wb13_depth_zero_behaves_like_depth_one(role):
    """CHARACTERIZATION: the root already plays one move, so a limit of 0 or 1
    both evaluate right after it."""
    board = random_board(4, 2, 2)
    heuristic = seeded_heuristic(4)
    tree = make_tree(heuristic)

    zero = tree.get_next_movement(copy_board(board), role, 0)
    one = tree.get_next_movement(copy_board(board), role, 1)

    assert zero == one


# ------------------------------------------ WB-14 oracle self-check


@pytest.mark.parametrize("role", [ROLE.WHITE, ROLE.BLACK], ids=lambda r: r.name)
@pytest.mark.parametrize("seed", range(3))
def test_wb14_oracle_move_generator_agrees_with_the_fake_rule(seed, role):
    """Guard the guard: the independent move generator used by the oracle must
    produce exactly the moves the rook rule accepts for the tree's vectors."""
    board = random_board(seed, 2, 3)
    tree = CookedTree()
    alive = tree._get_alive_chess(board, role)

    by_rule = {
        (as_pos(piece), (piece.row + d_row, piece.col + d_col))
        for piece in alive
        for d_row, d_col in zip(tree.move_row, tree.move_col, strict=True)
        if rook_is_valid(board, piece, Node(piece.row + d_row, piece.col + d_col))
    }

    assert set(legal_moves(board, role)) == by_rule


def test_wb13_default_heuristic_returns_an_int():
    """The base class heuristic is a placeholder that still returns an int."""
    tree = CookedTree()
    board = make_board({(3, 3): CHESS.WHITE, (5, 5): CHESS.BLACK})

    result = tree._get_heuristic(board, ROLE.WHITE)

    assert isinstance(result, int)
