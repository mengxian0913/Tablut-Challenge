from pydantic import BaseModel as Model


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
