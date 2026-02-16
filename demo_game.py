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
        "RHBQKBHR",  # rank1 - white major
        "PPPPPPPP",  # rank2 - white pawns
        "........",  # rank3
        "........",  # rank4
        "........",  # rank5
        "........",  # rank6
        "pppppppp",  # rank7 - black pawns
        "rhbqkbhr",  # rank8 - black major
    ])

    board.setup_board(StringIO(cfg))

    def show(msg: str = ""):
        if msg:
            print(msg)
        print("\n".join(board.get_ascii_board()))
        print()

    show("Initial position:")

    moves = [
        (PawnColor.BLACK, "e7", "e5"),
        (PawnColor.WHITE, "e2", "e4"),
        (PawnColor.BLACK, "g8", "f6"),
        (PawnColor.WHITE, "b1", "c3"),
        (PawnColor.BLACK, "f8", "c5"),
        (PawnColor.WHITE, "f1", "c4"),
        (PawnColor.BLACK, "b8", "c6"),
        (PawnColor.WHITE, "g1", "f3"),
        (PawnColor.BLACK, "a7", "a6"),
        (PawnColor.WHITE, "a2", "a3"),
        (PawnColor.BLACK, "h8", "g8"),
        (PawnColor.WHITE, "h1", "g1"),
        (PawnColor.BLACK, "d8", "e7"),
        (PawnColor.WHITE, "d1", "e2"),
    ]

    for i, (color, p1, p2) in enumerate(moves, start=1):
        ok = board.move(color, p1, p2)
        status = "OK" if ok else "ILLEGAL"
        show(f"Move {i}: {color.name} {p1}->{p2} -> {status}")


if __name__ == "__main__":
    main()
