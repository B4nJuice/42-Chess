from ..pawns import (AbstractPawn,
                     PawnColor,
                     Pawn,
                     Bishop,
                     King,
                     Knight,
                     Queen,
                     Rook)
from typing import TextIO, Any


class Board():
    def __init__(self):
        self.board: list[list[AbstractPawn]] = []

        for y in range(8):
            self.board.append([])
            for x in range(8):
                self.board[y].append(None)

    def setup_board(self, board: TextIO) -> None:
        for y, line in enumerate(board.readlines()):
            for x in range(len(line := line.strip())):
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
        x: int = int(pos[0], 16) - 10
        y: int = int(pos[1]) - 1

        return self.board[y][x]

    def move(self, pos1, pos2) -> None:
        x1: int = int(pos1[0], 16) - 10
        y1: int = int(pos1[1]) - 1

        x2: int = int(pos2[0], 16) - 10
        y2: int = int(pos2[1]) - 1

        self.board[y2][x2] = self.board[y1][x1]
        self.board[y1][x1] = None


if __name__ == "__main__":
    board = Board()
    with open("board.config", "r") as config:
        board.setup_board(config)
    print("\n".join(board.get_ascii_board()))
    board.move("e2", "e4")
    print("\n".join(board.get_ascii_board()))
