from .abstract_pawn import AbstractPawn, PawnColor


class Queen(AbstractPawn):
    def get_ascii(self) -> str:
        """Return 'Q' for white queen and 'q' for black queen."""
        return "Q" if self.color == PawnColor.WHITE else "q"
