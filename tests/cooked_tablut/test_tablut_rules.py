"""Rule tests for CookedTablut.

Expected results follow the referee's engine (GameAshtonTablut.java in
https://github.com/AGalassi/TablutCompetition), which decides the real games.
"""

import pytest
from tree_helpers import Pos, copy_board, make_board

from tablut.common.enums.algorithm import GAME_STATUS
from tablut.common.enums.chess import CHESS
from tablut.common.enums.player import ROLE
from tablut.common.types.algorithm import Node
from tablut.cooked_tablut.cooked_tablut import CookedTablut

W, B, K = CHESS.WHITE, CHESS.BLACK, CHESS.KING


def is_valid(pieces: dict[Pos, CHESS], start: Pos, target: Pos) -> bool:
    return CookedTablut()._is_valid_movement(
        make_board(pieces), Node(*start), Node(*target)
    )


def captures(pieces: dict[Pos, CHESS], moved_to: Pos) -> list[Pos]:
    """Captures made by the piece that has just arrived on ``moved_to``."""
    nodes = CookedTablut()._get_captures(make_board(pieces), Node(*moved_to))
    return sorted((node.row, node.col) for node in nodes)


# ------------------------------------------------------------- movement


@pytest.mark.parametrize("target", [(0, 6), (8, 6), (6, 0), (6, 8)])
def test_a_piece_can_slide_in_all_four_directions(target):
    assert is_valid({(6, 6): W}, (6, 6), target) is True


@pytest.mark.parametrize(
    ("blocker", "before", "beyond"),
    [
        ((3, 6), (4, 6), (2, 6)),  # moving up
        ((6, 3), (6, 4), (6, 2)),  # moving left
    ],
)
def test_a_piece_blocks_the_slide_towards_smaller_indexes(blocker, before, beyond):
    pieces = {(6, 6): W, blocker: B}

    assert is_valid(pieces, (6, 6), before) is True
    assert is_valid(pieces, (6, 6), blocker) is False
    assert is_valid(pieces, (6, 6), beyond) is False


def test_a_piece_outside_the_camps_cannot_cross_a_camp_cell():
    assert is_valid({(1, 2): W}, (1, 2), (1, 3)) is True
    assert is_valid({(1, 2): W}, (1, 2), (1, 6)) is False  # (1, 4) is a camp


def test_a_black_piece_can_move_inside_its_starting_camp():
    assert is_valid({(0, 3): B}, (0, 3), (0, 5)) is True


# ------------------------------------------------------ soldier captures


@pytest.mark.parametrize(
    ("pieces", "moved_to"),
    [
        ({(2, 2): W, (2, 3): B, (2, 4): W}, (2, 4)),
        ({(2, 2): B, (2, 3): W, (2, 4): B}, (2, 4)),
        ({(2, 2): K, (2, 3): B, (2, 4): W}, (2, 4)),  # the king is an anvil
        ({(2, 2): W, (2, 3): B, (2, 4): K}, (2, 4)),  # the king captures
    ],
)
def test_a_soldier_between_two_enemies_is_captured(pieces, moved_to):
    assert captures(pieces, moved_to) == [(2, 3)]


def test_moving_between_two_enemies_is_not_a_capture():
    pieces = {(2, 2): B, (2, 3): W, (2, 4): B}

    assert captures(pieces, (2, 3)) == []


def test_one_move_can_capture_in_several_directions():
    pieces = {
        (2, 6): W,
        (2, 5): B,
        (2, 4): W,
        (2, 7): B,
        (2, 8): W,
        (3, 6): B,
        (4, 6): W,
    }

    assert captures(pieces, (2, 6)) == [(2, 5), (2, 7), (3, 6)]


def test_no_capture_against_the_board_edge():
    """The cell behind the victim is off the board: the index must not wrap."""
    pieces = {(1, 6): B, (0, 6): W, (8, 6): B}

    assert captures(pieces, (1, 6)) == []


@pytest.mark.parametrize("castle", [CHESS.THRONE, K])
def test_the_castle_is_an_anvil_for_both_sides(castle):
    assert captures({(4, 2): B, (4, 3): W, (4, 4): castle}, (4, 2)) == [(4, 3)]
    assert captures({(2, 4): W, (3, 4): B, (4, 4): castle}, (2, 4)) == [(3, 4)]


def test_an_empty_camp_cell_is_an_anvil_for_both_sides():
    assert captures({(0, 1): B, (0, 2): W}, (0, 1)) == [(0, 2)]
    assert captures({(0, 1): W, (0, 2): B}, (0, 1)) == [(0, 2)]


@pytest.mark.parametrize(("moved_to", "victim"), [((2, 4), (1, 4)), ((4, 2), (4, 1))])
def test_white_cannot_capture_against_the_outer_camp_centers(moved_to, victim):
    assert captures({moved_to: W, victim: B}, moved_to) == []


# --------------------------------------------------------- king captures


def test_king_away_from_the_castle_is_captured_by_two_opposite_blacks():
    assert captures({(6, 6): K, (6, 5): B, (6, 7): B}, (6, 7)) == [(6, 6)]


def test_king_is_not_captured_by_blacks_on_adjacent_sides():
    assert captures({(6, 6): K, (5, 6): B, (6, 7): B}, (6, 7)) == []


def test_king_next_to_a_camp_is_captured_by_one_black():
    assert captures({(1, 3): K, (2, 3): B}, (2, 3)) == [(1, 3)]


@pytest.mark.parametrize(
    ("blacks", "expected"),
    [
        ([(3, 4), (5, 4), (4, 3), (4, 5)], [(4, 4)]),
        ([(3, 4), (5, 4), (4, 5)], []),
    ],
)
def test_king_in_the_castle_needs_four_blacks(blacks, expected):
    pieces = {(4, 4): K} | dict.fromkeys(blacks, B)

    assert captures(pieces, (4, 5)) == expected


@pytest.mark.parametrize(
    ("blacks", "expected"),
    [
        ([(2, 4), (3, 3), (3, 5)], [(3, 4)]),
        ([(3, 3), (3, 5)], []),  # a plain sandwich is not enough here
    ],
)
def test_king_next_to_the_castle_needs_three_blacks(blacks, expected):
    pieces = {(3, 4): K} | dict.fromkeys(blacks, B)

    assert captures(pieces, (3, 5)) == expected


# ------------------------------------------------------------ game status


def test_no_king_on_the_board_is_a_black_win():
    board = make_board({(1, 1): W, (7, 7): B})

    assert CookedTablut()._get_game_status(board, ROLE.WHITE) == GAME_STATUS.BLACK_WIN


@pytest.mark.parametrize(
    "blacks",
    [
        [(5, 5), (5, 7)],  # diagonal neighbours
        [(6, 5), (6, 7)],  # the king walked in between: not an active capture
    ],
)
def test_blacks_around_the_king_do_not_end_the_game_by_themselves(blacks):
    board = make_board({(6, 6): K, (1, 1): W} | dict.fromkeys(blacks, B))

    assert CookedTablut()._get_game_status(board, ROLE.WHITE) == GAME_STATUS.ONGOING


# ----------------------------------------------------------------- search


def test_black_plays_the_move_that_captures_the_king():
    tree = CookedTablut()
    board = make_board({(6, 6): K, (6, 5): B, (8, 7): B, (1, 1): W})
    original = copy_board(board)

    best = tree.get_next_movement(board, ROLE.BLACK, 2)

    assert (best.from_node, best.to_node) == (Node(8, 7), Node(6, 7))
    assert best.score == -tree.INF
    assert board == original


@pytest.mark.parametrize("role", [ROLE.WHITE, ROLE.BLACK])
def test_captures_made_during_the_search_are_undone(role):
    class CountingTablut(CookedTablut):
        captured = 0

        def _get_captures(self, chess_board, to_node):
            nodes = super()._get_captures(chess_board, to_node)
            self.captured += len(nodes)
            return nodes

    tree = CountingTablut()
    board = make_board(
        {
            (4, 4): K,
            (2, 2): W,
            (2, 3): B,
            (6, 4): W,
            (6, 6): B,
            (6, 2): W,
            (7, 3): B,
        }
    )
    original = copy_board(board)

    tree.get_next_movement(board, role, 3)

    assert tree.captured > 0
    assert board == original
