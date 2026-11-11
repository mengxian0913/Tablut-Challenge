# Candidate Score Function:
from tablut.common.enums.chess import CHESS
from tablut.common.enums.player import ROLE
from tablut.common.types.algorithm import Node

type Board = list[list[CHESS]]

INF: int = 0x3F3F3F

# We could penalise the loss of pieces but giving score a -10 to begin with for each piece lost.


"""
1. Define the rule of getting point for each role of their pieces on the board.
2. Define the score for each situation of based on the rule.
"""


def dist(x, y, Node):
    x_dist = abs(x - Node.row)
    y_dist = abs(y - Node.col)
    distance = x_dist + y_dist
    return distance


def is_valid_movement(chess_board: list[list[CHESS]], from_node: Node, to_node: Node):
    pass


def get_score(current_node: Node, chess_board: Board, role: ROLE):
    score = 0
    neighbor = None

    if role == ROLE.WHITE:
        if chess_board[current_node.row][current_node.col] == CHESS.KING and (
            is_valid_movement(chess_board, current_node, Node(current_node.row, 9))
            or is_valid_movement(chess_board, current_node, Node(current_node.row, -9))
            or is_valid_movement(chess_board, current_node, Node(9, current_node.col))
            or is_valid_movement(chess_board, current_node, Node(-9, current_node.col))
        ):
            score += 5  # random value

        for x in range(9):
            for y in range(9):
                piece = chess_board[x][y]
                if piece == CHESS.BLACK and dist(x, y, current_node) == 1:
                    score -= 1
                    neighbor = Node(x, y)
                if score == -2:
                    break
        if score == -1:
            for x in range(9):
                for y in range(9):
                    if (
                        dist(x, y, neighbor) == 1
                        and chess_board[x][y] == CHESS.WHITE
                        and (x == current_node.row or y == current_node.col)
                        and (Node(x, y) != current_node)
                    ):
                        score += 3

    else:
        for x in range(9):
            for y in range(9):
                piece = chess_board[x][y]
                if piece == CHESS.WHITE and dist(x, y, current_node) == 1:
                    score += 1
                if score == 2:
                    break
        if score == 1:
            for x in range(9):
                for y in range(9):
                    if (
                        dist(x, y, neighbor) == 1
                        and chess_board[x][y] == CHESS.WHITE
                        and (x == current_node.row or y == current_node.col)
                        and (Node(x, y) != current_node)
                    ):
                        score -= 3
    return score
