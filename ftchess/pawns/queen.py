from .abstract_pawn import AbstractPawn, PawnColor


class Queen(AbstractPawn):
    def get_ascii(self) -> str:
        """Return 'Q' for white queen and 'q' for black queen."""
        return "Q" if self.color == PawnColor.WHITE else "q"

    def is_valid_move(self, board, pos1: str, pos2: str) -> bool:
        """Queen moves like rook or bishop (combined)."""
        # decode
        x1, y1 = board.pos_to_coords(pos1)
        x2, y2 = board.pos_to_coords(pos2)

        dx = x2 - x1
        dy = y2 - y1

        # not moving
        if dx == 0 and dy == 0:
            return False

        # destination friendly?
        dest = board.get_pawn(pos2)
        if dest is not None and dest.color == self.color:
            return False

        # determine if straight or diagonal
        if dx == 0 or dy == 0:
            steps = abs(dx) if dx != 0 else abs(dy)
            step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
            step_y = 0 if dy == 0 else (1 if dy > 0 else -1)
        elif abs(dx) == abs(dy):
            steps = abs(dx)
            step_x = 1 if dx > 0 else -1
            step_y = 1 if dy > 0 else -1
        else:
            return False

        for s in range(1, steps):
            nx = x1 + s * step_x
            ny = y1 + s * step_y
            intermediate = f"{'abcdefgh'[nx]}{ny+1}"
            if board.get_pawn(intermediate) is not None:
                return False

        return True
