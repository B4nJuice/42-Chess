from .abstract_pawn import AbstractPawn, PawnColor


class Bishop(AbstractPawn):
    def get_ascii(self) -> str:
        """Return 'B' for white bishops and 'b' for black bishops."""
        return "B" if self.color == PawnColor.WHITE else "b"
