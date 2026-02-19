from .abstract_pawn import AbstractPawn, PawnColor


class Bishop(AbstractPawn):
    def get_ascii(self) -> str:
        """Return 'B' for white bishops and 'b' for black bishops."""
        return "B" if self.color == PawnColor.WHITE else "b"

    def is_valid_move(self, board, pos1: str, pos2: str) -> bool:
        """Bishop moves diagonally; path must be clear."""
        x1, y1 = board.pos_to_coords(pos1)
        x2, y2 = board.pos_to_coords(pos2)

        dx = x2 - x1
        dy = y2 - y1

        if abs(dx) != abs(dy):
            return False

        dest = board.get_pawn(pos2)
        if dest is not None and dest.color == self.color:
            return False

        steps = abs(dx)
        step_x = 1 if dx > 0 else -1
        step_y = 1 if dy > 0 else -1

        for s in range(1, steps):
            nx = x1 + s * step_x
            ny = y1 + s * step_y
            intermediate = f"{'abcdefgh'[nx]}{ny+1}"
            if board.get_pawn(intermediate) is not None:
                return False

        return True
