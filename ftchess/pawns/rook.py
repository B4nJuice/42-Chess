from .abstract_pawn import AbstractPawn, PawnColor


class Rook(AbstractPawn):
    def get_ascii(self) -> str:
        """Return 'R' for white rooks and 'r' for black rooks."""
        return "R" if self.color == PawnColor.WHITE else "r"

    def is_valid_move(self, board, pos1: str, pos2: str) -> bool:
        """Rook moves any number of squares along a rank or file.

        Path must be clear and destination must be empty or occupied by an
        opponent piece.
        """
        # decode positions using board helper
        x1, y1 = board.pos_to_coords(pos1)
        x2, y2 = board.pos_to_coords(pos2)

        dx = x2 - x1
        dy = y2 - y1

        # must move along file or rank
        if not (dx == 0 or dy == 0):
            return False

        # destination can't have friendly piece
        dest = board.get_pawn(pos2)
        if dest is not None and dest.color == self.color:
            return False

        # check path
        steps = abs(dx) if dx != 0 else abs(dy)
        step_x = 0 if dx == 0 else (1 if dx > 0 else -1)
        step_y = 0 if dy == 0 else (1 if dy > 0 else -1)

        for s in range(1, steps):
            nx = x1 + s * step_x
            ny = y1 + s * step_y
            intermediate = f"{'abcdefgh'[nx]}{ny+1}"
            if board.get_pawn(intermediate) is not None:
                return False

        return True
