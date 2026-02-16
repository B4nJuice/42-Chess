from .abstract_pawn import AbstractPawn, PawnColor


class Rook(AbstractPawn):
    def get_ascii(self) -> str:
        """Return 'R' for white rooks and 'r' for black rooks."""
        return "R" if self.color == PawnColor.WHITE else "r"
