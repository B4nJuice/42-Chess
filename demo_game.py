#!/usr/bin/env python3
"""Small demo game that moves several pieces for each side and prints the
board after each move. Uses the project's board and pawns modules.

Note: this project uses an inverted rank numbering where the first line fed to
Board.setup_board is rank '1' (top). We build the initial config accordingly.
"""
from io import StringIO


def main() -> None:
    import sys

    sys.path.insert(0, "./src")

    from src.board.board import Board
    from src.pawns import PawnColor

    board = Board()

    # initial config: rank1 at top, rank8 at bottom
    cfg = "\n".join([
        "rhbqkbhr",  # rank1 - black major
        "pppppppp",  # rank2 - black pawns
        "........",  # rank3
        "........",  # rank4
        "........",  # rank5
        "........",  # rank6
        "PPPPPPPP",  # rank7 - white pawns
        "RHBQKBHR",  # rank8 - white major
    ])

    board.setup_board(StringIO(cfg))

    def show(msg: str = ""):
        if msg:
            print(msg)
        print("\n".join(board.get_ascii_board()))
        print()

    show("Initial position:")

    moves = [
        (PawnColor.WHITE, "e7", "e5"),
        (PawnColor.BLACK, "e2", "e4"),
        (PawnColor.WHITE, "g8", "f6"),
        (PawnColor.BLACK, "b1", "c3"),
        (PawnColor.WHITE, "f8", "c5"),
        (PawnColor.BLACK, "f1", "c4"),
        (PawnColor.WHITE, "b8", "c6"),
        (PawnColor.BLACK, "g1", "f3"),
        (PawnColor.WHITE, "a7", "a6"),
        (PawnColor.BLACK, "a2", "a3"),
        (PawnColor.WHITE, "h8", "g8"),
        (PawnColor.BLACK, "h1", "g1"),
        (PawnColor.WHITE, "d8", "e7"),
        (PawnColor.BLACK, "d1", "e2"),
    ]

    for i, (color, p1, p2) in enumerate(moves, start=1):
        ok = board.move(color, p1, p2)
        status = "OK" if ok else "ILLEGAL"
        show(f"Move {i}: {color.name} {p1}->{p2} -> {status}")


if __name__ == "__main__":
    main()
