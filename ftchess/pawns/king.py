from .abstract_pawn import AbstractPawn, PawnColor


class King(AbstractPawn):
    def get_ascii(self) -> str:
        """Return 'K' for white king and 'k' for black king."""
        return "K" if self.color == PawnColor.WHITE else "k"

    def is_valid_move(self, board, pos1: str, pos2: str) -> bool:
        """King moves one square any direction. Castling not handled."""
        x1, y1 = board.pos_to_coords(pos1)
        x2, y2 = board.pos_to_coords(pos2)

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        if max(dx, dy) != 1:
            return False

        dest = board.get_pawn(pos2)
        if dest is not None and dest.color == self.color:
            return False

        return True
