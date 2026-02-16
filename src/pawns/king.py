from .abstract_pawn import AbstractPawn, PawnColor


class King(AbstractPawn):
    def get_ascii(self) -> str:
        """Return 'K' for white king and 'k' for black king."""
        return "K" if self.color == PawnColor.WHITE else "k"
