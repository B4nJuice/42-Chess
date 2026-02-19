from .abstract_pawn import AbstractPawn, PawnColor


class Pawn(AbstractPawn):
    def get_ascii(self) -> str:
        """Return 'P' for white pawns and 'p' for black pawns."""
        return "P" if self.color == PawnColor.WHITE else "p"

    def is_valid_move(self, board, pos1: str, pos2: str) -> bool:
        ahead: int = 1 if self.color == PawnColor.WHITE else -1
        x1, y1 = board.pos_to_coords(pos1)
        x2, y2 = board.pos_to_coords(pos2)

        if x1 == x2 and y2 - y1 == ahead and board.get_pawn(pos2) is None:
            return True

        if abs(x2 - x1) == 1 and y2 - y1 == ahead and board.get_pawn(pos2) is not None and board.get_pawn(pos2).color != self.color:
            return True

        if y1 == (1 if self.color == PawnColor.WHITE else 6) and x1 == x2 and y2 - y1 == 2 * ahead and board.get_pawn(pos2) is None and board.get_pawn(f"{pos1[0]}{int(pos1[1]) + ahead}") is None:
            return True

        return False
