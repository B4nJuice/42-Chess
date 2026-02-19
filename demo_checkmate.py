#!/usr/bin/env python3
"""Demo script to test check and checkmate detection.

Creates a few handcrafted positions and prints whether the given color
is in check or checkmate.
"""
from __future__ import annotations

import sys

sys.path.insert(0, "./ftchess")

from src.board.board import Board
from src.pawns import (
    PawnColor,
    King,
    Queen,
    Rook,
    Bishop,
    Knight,
    Pawn,
)


def place(board: Board, pos: str, piece: object | None) -> None:
    x, y = board.pos_to_coords(pos)
    board.board[y][x] = piece


def empty_board() -> Board:
    b = Board()
    # clear everything
    for y in range(8):
        for x in range(8):
            b.board[y][x] = None
    return b


def show_board(b: Board) -> None:
    print("\n".join(b.get_ascii_board()))


def test_simple_check() -> None:
    print("== Simple check test ==")
    b = empty_board()
    # black king on e5, white rook on e1 -> black in check
    place(b, "e5", King(PawnColor.BLACK))
    place(b, "e1", Rook(PawnColor.WHITE))
    show_board(b)
    print("Black in check:", b.is_in_check(PawnColor.BLACK))
    print("Black in mate:", b.is_in_checkmate(PawnColor.BLACK))
    print()


def test_scholars_mate() -> None:
    print("== Scholar's mate (white mates black) ==")
    b = empty_board()
    # set up scholar's mate final position (approximate):
    # black king on e8, white queen on f7 delivering mate, bishop helps
    place(b, "f8", King(PawnColor.BLACK))
    place(b, "f7", Queen(PawnColor.WHITE))
    place(b, "c4", Bishop(PawnColor.WHITE))
    # add a couple of white pawns to mimic realistic coverage
    place(b, "e2", Pawn(PawnColor.WHITE))
    place(b, "f2", Pawn(PawnColor.WHITE))
    show_board(b)
    print("Black in check:", b.is_in_check(PawnColor.BLACK))
    print("Black in mate:", b.is_in_checkmate(PawnColor.BLACK))
    print()


def test_no_check() -> None:
    print("== No check test ==")
    b = empty_board()
    place(b, "e8", King(PawnColor.BLACK))
    place(b, "e1", King(PawnColor.WHITE))
    place(b, "a1", Rook(PawnColor.WHITE))
    show_board(b)
    print("Black in check:", b.is_in_check(PawnColor.BLACK))
    print("White in check:", b.is_in_check(PawnColor.WHITE))
    print()


def main() -> None:
    test_simple_check()
    test_scholars_mate()
    test_no_check()


if __name__ == "__main__":
    main()
