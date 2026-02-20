from ..pawns import (AbstractPawn,
                     PawnColor,
                     Pawn,
                     Bishop,
                     King,
                     Knight,
                     Queen,
                     Rook)
from typing import TextIO, Any
from io import StringIO

class Board():
    def __init__(self):
        self.board: list[list[AbstractPawn]] = []
        self.count_until_tie = 3
        self.move_history: list[str] = []
        self.group_move_history = []

        for y in range(8):
            self.board.append([])
            for x in range(8):
                self.board[y].append(None)

    def setup_board(self, board: TextIO) -> None:
        for y, line in enumerate(board.readlines()):
            for x in range(len(line.replace("\n", ""))):
                pawn: Any = None

                match line[x]:
                    case "p" | "P":
                        pawn = Pawn.create_pawn(PawnColor.WHITE if line[x].isupper() else PawnColor.BLACK)
                    case "b" | "B":
                        pawn = Bishop.create_pawn(PawnColor.WHITE if line[x].isupper() else PawnColor.BLACK)
                    case "k" | "K":
                        pawn = King.create_pawn(PawnColor.WHITE if line[x].isupper() else PawnColor.BLACK)
                    case "h" | "H":
                        pawn = Knight.create_pawn(PawnColor.WHITE if line[x].isupper() else PawnColor.BLACK)
                    case "q" | "Q":
                        pawn = Queen.create_pawn(PawnColor.WHITE if line[x].isupper() else PawnColor.BLACK)
                    case "r" | "R":
                        pawn = Rook.create_pawn(PawnColor.WHITE if line[x].isupper() else PawnColor.BLACK)

                self.board[y][x] = pawn

    def get_ascii_board(self) -> list[str]:
        ascii_board: list[str] = []
        for row in self.board:
            ascii_row = "".join(
                (p.get_ascii() if p is not None else ".") for p in row
            )
            ascii_board.append(ascii_row)

        return ascii_board

    def get_pos(self, pawn: AbstractPawn) -> str | None:
        for y, row in enumerate(self.board):
            for x, p in enumerate(row):
                if pawn == p:
                    return f"{'abcdefgh'[x]}{y+1}"
        return None

    def get_pawn(self, pos: str) -> AbstractPawn | None:
        x, y = self.pos_to_coords(pos)
        return self.board[y][x]

    def move(self, color: PawnColor, pos1: str = None, pos2: str = None) -> bool:
        x2, y2 = 0, 0
        try:
            if not pos1 or not pos2:
                return False

            if not self.get_pawn(pos1) or self.get_pawn(pos1).color != color:
                return False

            x1, y1 = self.pos_to_coords(pos1)
            x2, y2 = self.pos_to_coords(pos2)
        
            if isinstance(self.get_pawn(pos2), King):
                return False

            if not self.get_pawn(pos1).is_valid_move(self, pos1, pos2):
                return False

            if self.is_in_checkmate(color):
                return False

            test_board: Board = Board()
            test_board.setup_board(StringIO("\n".join(self.get_ascii_board())))
            test_board.board[y2][x2] = self.board[y1][x1]
            test_board.board[y1][x1] = None

            if test_board.is_in_check(color):
                return False

            pawn = self.board[y1][x1]

            if isinstance(pawn, King) and abs(x2 - x1) == 2:
                direction = 2 if x2 > x1 else -2

                rook_x_start = 7 if direction == 2 else 0
                rook_x_end = 5 if rook_x_start == 7 else 3

                self.board[y1][x1 + direction] = pawn
                self.board[y1][x1] = None

                rook = self.board[y1][rook_x_start]
                self.board[y1][rook_x_start] = None
                self.board[y1][rook_x_end] = rook

            else:
                self.board[y2][x2] = pawn
                self.board[y1][x1] = None

        except Exception as e:
            print(e)
            return False
        
        move_key = f"{pos1}{pos2}"
        self.move_history.append(move_key)
        self.group_move_history = [self.move_history[i:i+4] for i in range(0, len(self.move_history), 4)]

        if len(self.group_move_history[-4:]) >= 3:
            if self.group_move_history[-2][:len(self.group_move_history[-1])] == self.group_move_history[-1]:
                self.count_until_tie = 3 - self.group_move_history[-4:].count(self.group_move_history[-2])

        pawn: AbstractPawn = self.get_pawn(self.coords_to_pos((x2, y2)))

        if isinstance(pawn, King) or isinstance(pawn, Rook):
            pawn.has_moved = True

        return True

    @staticmethod
    def pos_to_coords(pos: str) -> tuple[int, int]:
        x: int = ord(pos[0]) - ord("a")
        y: int = int(pos[1]) - 1
        return (x, y)

    @staticmethod
    def coords_to_pos(coords: tuple[int, int]) -> str:
        x, y = coords
        return f"{'abcdefgh'[x]}{y+1}"

    def is_in_check(self, color: PawnColor) -> bool:
        """Return True if the king of `color` is under attack."""
        king_pos: str | None = None
        for y, row in enumerate(self.board):
            for x, p in enumerate(row):
                if p is None:
                    continue
                if isinstance(p, King) and p.color == color:
                    king_pos = f"{'abcdefgh'[x]}{y+1}"
                    break
            if king_pos is not None:
                break

        if king_pos is None:
            return False

        for y, row in enumerate(self.board):
            for x, p in enumerate(row):
                if p is None or p.color == color:
                    continue
                src = f"{'abcdefgh'[x]}{y+1}"
                try:
                    if p.is_valid_move(self, src, king_pos):
                        return True
                except Exception:
                    continue

        return False

    def is_in_checkmate(self, color: PawnColor) -> bool:
        """Return True if `color` is checkmated (in check and no escape)."""
        if not self.is_in_check(color):
            return False

        letters = 'abcdefgh'

        for y, row in enumerate(self.board):
            for x, p in enumerate(row):
                if p is None or p.color != color:
                    continue

                src = f"{letters[x]}{y+1}"

                for ry in range(8):
                    for rx in range(8):
                        dst = f"{letters[rx]}{ry+1}"
                        try:
                            if not p.is_valid_move(self, src, dst):
                                continue
                        except Exception:
                            continue

                        x1, y1 = self.pos_to_coords(src)
                        x2, y2 = self.pos_to_coords(dst)
                        src_piece = self.board[y1][x1]
                        dst_piece = self.board[y2][x2]

                        self.board[y2][x2] = src_piece
                        self.board[y1][x1] = None

                        still_in_check = self.is_in_check(color)

                        self.board[y1][x1] = src_piece
                        self.board[y2][x2] = dst_piece

                        if not still_in_check:
                            return False

        return True
    
if __name__ == "__main__":
    board = Board()
    with open("board.config", "r") as config:
        board.setup_board(config)
    print("\n".join(board.get_ascii_board()))

    print()
    print(board.move(PawnColor.BLACK, "e2", "e4"))
    print("\n".join(board.get_ascii_board()))
