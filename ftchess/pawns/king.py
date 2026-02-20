from .abstract_pawn import AbstractPawn, PawnColor
from .rook import Rook
import copy


class King(AbstractPawn):
    def __init__(self, color: PawnColor) -> None:
        self.has_moved = False
        super().__init__(color)

    def get_ascii(self) -> str:
        """Return 'K' for white king and 'k' for black king."""
        return "K" if self.color == PawnColor.WHITE else "k"

    def _can_castle(self, board, pos1: str, pos2: str) -> bool:
        if self.has_moved:
            return False

        if board.is_in_check(self.color):
            return False

        x1, y1 = board.pos_to_coords(pos1)
        x2, _ = board.pos_to_coords(pos2)

        direction = 1 if x2 > x1 else -1

        rook_pos = board.coords_to_pos((7 if direction == 1 else 0, y1))
        rook = board.get_pawn(rook_pos)

        if rook is None:
            return False

        if not isinstance(rook, Rook):
            return False

        if rook.color != self.color or rook.has_moved:
            return False

        rook_x = 7 if direction == 1 else 0

        for x in range(x1 + direction, rook_x, direction):
            intermediate = board.coords_to_pos((x, y1))
            if board.get_pawn(intermediate) is not None:
                return False

        new_board = copy.deepcopy(board)
        for step in range(1, 3 if direction == -1 else 2):
            pos2 = new_board.coords_to_pos((x1 + step * direction, y1))
            if not new_board.move(self.color, pos1, pos2):
                return False
            pos1 = pos2

        return True

    def is_valid_move(self, board, pos1: str, pos2: str) -> bool:
        """King moves one square any direction. Castling not handled."""
        x1, y1 = board.pos_to_coords(pos1)
        x2, y2 = board.pos_to_coords(pos2)

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        if dy == 0 and abs(dx) == 2:
            return self._can_castle(board, pos1, pos2)

        if max(dx, dy) != 1:
            return False

        dest = board.get_pawn(pos2)
        if dest is not None and dest.color == self.color:
            return False

        return True
