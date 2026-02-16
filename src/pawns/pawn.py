from .abstract_pawn import AbstractPawn, PawnColor


class Pawn(AbstractPawn):
    def get_ascii(self) -> str:
        """Return 'P' for white pawns and 'p' for black pawns."""
        return "P" if self.color == PawnColor.WHITE else "p"
