from ..board import Board
from ..pawns import PawnColor
import copy
from typing import Protocol
from io import StringIO


class Algo(Protocol):
    def play(self, board: Board) -> tuple[str, str]:
        pass

    def set_color(self, color: PawnColor) -> None:
        pass


def start_game(algo1: Algo, algo2: Algo) -> PawnColor:
    board = Board()
    with open("board.config", "r") as board_config:
        board.setup_board(board_config)

    algo1.set_color(PawnColor.WHITE)
    algo2.set_color(PawnColor.BLACK)

    new_board: Board = Board()
    new_board.setup_board(StringIO("\n".join(board.get_ascii_board())))

    while True:
        for algo, color in [[algo1, PawnColor.WHITE], [algo2, PawnColor.BLACK]]:
            print(f"{color.value} to play:")
            print("\n".join(board.get_ascii_board()))
            while not board.move(color, *algo.play(new_board)):
                new_board = copy.deepcopy(board)
        
            checkmate: bool = {
                board.is_in_checkmate(PawnColor.WHITE): PawnColor.WHITE,
                board.is_in_checkmate(PawnColor.BLACK): PawnColor.BLACK,
            }.get(True)

            if board.count_until_tie == 0:
                return "tie: pat"

        if checkmate:
            return checkmate
