from tablut.common.enums.algorithm import GAME_STATUS
from tablut.common.enums.player import ROLE
from tablut.common.types.algorithm import Board, Node
from tablut.cooked_tree.cooked_tree import CookedTree


class CookedTablut(CookedTree):
    def _get_heuristic(self, chess_board: Board, role: ROLE) -> int:
        # TODO: Implement this in the subclass
        return -1

    def _get_game_status(self, chess_board: Board, role: ROLE) -> GAME_STATUS:
        # TODO: Implement this in the subclass
        return GAME_STATUS.ONGOING

    def _is_valid_movement(
        self, chess_board: Board, from_node: Node, to_node: Node
    ) -> bool:
        # TODO: Implement this in the subclass
        return True
