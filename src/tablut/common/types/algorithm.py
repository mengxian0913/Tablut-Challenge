from __future__ import annotations

from collections.abc import Callable

from pydantic import BaseModel as Model

from tablut.common.enums.algorithm import GAME_STATUS
from tablut.common.enums.chess import CHESS
from tablut.common.enums.player import ROLE

type Board = list[list[CHESS]]
type HeuristicFn = Callable[[Board, ROLE], int]
type GameStatusFn = Callable[[Board, ROLE], GAME_STATUS]
type IsValidMovementFn = Callable[[Board, Node, Node], bool]


class Node(Model):
    row: int
    col: int

    def __init__(self, row: int, col: int) -> None:
        super().__init__(row=row, col=col)

    model_config = {"frozen": True}


class Best_Next_Movement(Model):
    next_node: Node
    score: int

    def __init__(self, next_node: Node, score: int) -> None:
        super().__init__(next_node=next_node, score=score)


class Best_Movement(Model):
    from_node: Node
    to_node: Node
    score: int

    def __init__(self, from_node: Node, to_node: Node, score: int) -> None:
        super().__init__(from_node=from_node, to_node=to_node, score=score)
