from .abstract_pawn import AbstractPawn, PawnColor


class Knight(AbstractPawn):
    def get_ascii(self) -> str:
        """Return 'H' for white knights and 'h' for black knights.

        Note: using 'h' as requested for the knight symbol.
        """
        return "H" if self.color == PawnColor.WHITE else "h"

    def is_valid_move(self, board, pos1: str, pos2: str) -> bool:
        """Knight moves in an L-shape (2,1) and can jump over pieces."""
        x1, y1 = board.pos_to_coords(pos1)
        x2, y2 = board.pos_to_coords(pos2)

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        if (dx, dy) not in ((1, 2), (2, 1)):
            return False

        dest = board.get_pawn(pos2)
        if dest is not None and dest.color == self.color:
            return False

        return True
