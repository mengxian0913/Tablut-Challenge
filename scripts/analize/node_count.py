#!/usr/bin/env python3
"""Count the nodes visited by Alpha-Beta versus plain Minimax.

Both searches use the same rules, heuristic and root loop as the player, so the
only difference is pruning. Node counts do not depend on the machine, which is
why they are a better comparison than wall-clock time.

Usage:
    uv run scripts/analize/node_count.py [--max-alpha-beta 4] [--max-plain 3]
"""

import argparse
import time
from pathlib import Path

from tablut.common.enums.algorithm import GAME_STATUS
from tablut.common.enums.chess import CHESS
from tablut.common.enums.player import ROLE
from tablut.common.types.algorithm import Board, Node
from tablut.cooked_tablut.cooked_tablut import CookedTablut

ROOT = Path(__file__).resolve().parents[2]


class CountingTablut(CookedTablut):
    """CookedTablut that counts every node entered by the Alpha-Beta search."""

    def __init__(self) -> None:
        super().__init__()
        self.visited = 0

    def _get_game_status(self, chess_board: Board, role: ROLE) -> GAME_STATUS:
        # The Alpha-Beta search calls this exactly once per node it enters.
        self.visited += 1
        return super()._get_game_status(chess_board, role)


def opening_board() -> Board:
    """Standard Ashton opening, same position as scripts/benchmark_depth.py."""
    board: Board = [[CHESS.EMPTY for _ in range(9)] for _ in range(9)]
    for r, c in [(2, 4), (3, 4), (5, 4), (6, 4), (4, 2), (4, 3), (4, 5), (4, 6)]:
        board[r][c] = CHESS.WHITE
    for r, c in [
        (0, 3), (0, 4), (0, 5), (1, 4),
        (8, 3), (8, 4), (8, 5), (7, 4),
        (3, 0), (4, 0), (5, 0), (4, 1),
        (3, 8), (4, 8), (5, 8), (4, 7),
    ]:  # fmt: skip
        board[r][c] = CHESS.BLACK
    board[4][4] = CHESS.KING
    return board


def apply_move(tree: CookedTablut, board: Board, src: Node, dst: Node) -> Board:
    """Copy-based move, so the plain search needs no undo logic."""
    child = [row[:] for row in board]
    child[dst.row][dst.col] = child[src.row][src.col]
    child[src.row][src.col] = CHESS.THRONE if src == tree.throne else CHESS.EMPTY
    for cap in tree._get_captures(child, dst):
        child[cap.row][cap.col] = CHESS.THRONE if cap == tree.throne else CHESS.EMPTY
    return child


def plain_minimax(
    tree: CountingTablut, board: Board, role: ROLE, cur: int, max_depth: int
) -> int:
    """Minimax without pruning, mirroring CookedTree.__min_max_tree."""
    tree.visited += 1
    status = CookedTablut._get_game_status(tree, board, role)
    if status == GAME_STATUS.WHITE_WIN:
        return tree.INF
    if status == GAME_STATUS.BLACK_WIN:
        return -tree.INF
    if status == GAME_STATUS.DRAW:
        return 0
    if cur >= max_depth:
        return tree._get_heuristic(board, role)

    next_role = ROLE.BLACK if role == ROLE.WHITE else ROLE.WHITE
    best = -tree.INF if role == ROLE.WHITE else tree.INF
    for src in tree._get_alive_chess(board, role):
        for mv_row, mv_col in zip(tree.move_row, tree.move_col, strict=True):
            dst = Node(src.row + mv_row, src.col + mv_col)
            if not tree._is_valid_movement(board, src, dst):
                continue
            score = plain_minimax(
                tree, apply_move(tree, board, src, dst), next_role, cur + 1, max_depth
            )
            best = max(best, score) if role == ROLE.WHITE else min(best, score)
    return best


def plain_root(tree: CountingTablut, board: Board, depth: int) -> int:
    """Root score of a plain Minimax search for WHITE at the given depth."""
    best = -tree.INF
    for src in tree._get_alive_chess(board, ROLE.WHITE):
        for mv_row, mv_col in zip(tree.move_row, tree.move_col, strict=True):
            dst = Node(src.row + mv_row, src.col + mv_col)
            if not tree._is_valid_movement(board, src, dst):
                continue
            child = apply_move(tree, board, src, dst)
            score = plain_minimax(tree, child, ROLE.BLACK, 1, depth)
            best = max(best, score)
    return best


def run_alpha_beta(depth: int) -> tuple[int, int, float]:
    tree = CountingTablut()
    start = time.perf_counter()
    result = tree.get_next_movement(opening_board(), ROLE.WHITE, depth)
    return result.score, tree.visited, time.perf_counter() - start


def run_plain(depth: int) -> tuple[int, int, float]:
    tree = CountingTablut()
    start = time.perf_counter()
    score = plain_root(tree, opening_board(), depth)
    return score, tree.visited, time.perf_counter() - start


def plot(rows: list[tuple[int, int | None, int]], path: Path) -> None:
    """Save a log-scale chart of visited nodes per depth."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    depths = [depth for depth, _, _ in rows]
    plain = [(d, p) for d, p, _ in rows if p is not None]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(*zip(*plain, strict=True), marker="o", label="Plain Minimax")
    ax.plot(depths, [ab for _, _, ab in rows], marker="s", label="Alpha-Beta")
    ax.set_yscale("log")
    ax.set_xlabel("Search depth (plies)")
    ax.set_ylabel("Visited nodes (log scale)")
    ax.set_xticks(depths)
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=200)
    print(f"Chart written to {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-alpha-beta", type=int, default=4)
    parser.add_argument("--max-plain", type=int, default=3)
    parser.add_argument("--plot", type=Path, help="write a PNG chart to this path")
    args = parser.parse_args()

    print(f"Repository: {ROOT}")
    print(
        f"{'Depth':>5} | {'Plain nodes':>12} | {'Alpha-Beta nodes':>16} | "
        f"{'Reduction':>9} | {'Root score match':>16} | {'AB time (s)':>11}"
    )
    print("-" * 85)

    rows: list[tuple[int, int | None, int]] = []
    for depth in range(1, args.max_alpha_beta + 1):
        ab_score, ab_nodes, ab_time = run_alpha_beta(depth)
        if depth <= args.max_plain:
            plain_score, plain_nodes, _ = run_plain(depth)
            match = "yes" if plain_score == ab_score else "NO"
            reduction = f"{plain_nodes / ab_nodes:.1f}x"
            plain_text = f"{plain_nodes:,}"
            rows.append((depth, plain_nodes, ab_nodes))
        else:
            match, reduction, plain_text = "skipped", "-", "skipped"
            rows.append((depth, None, ab_nodes))
        print(
            f"{depth:>5} | {plain_text:>12} | {ab_nodes:>16,} | "
            f"{reduction:>9} | {match:>16} | {ab_time:>11.3f}"
        )

    if args.plot:
        plot(rows, args.plot)


if __name__ == "__main__":
    main()
