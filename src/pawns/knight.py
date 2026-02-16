from .abstract_pawn import AbstractPawn, PawnColor


class Knight(AbstractPawn):
    def get_ascii(self) -> str:
        """Return 'H' for white knights and 'h' for black knights."""
        return "H" if self.color == PawnColor.WHITE else "h"
