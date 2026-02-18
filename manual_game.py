from src.board import Board
from src.pawns import PawnColor
from src.player import start_game


class ManualAlgo():
    def play(self, board: Board):
        return input().split()
    
    def set_color(self, color: PawnColor) -> None:
        self.color = color


if __name__ == "__main__":
    winner = start_game(ManualAlgo(), ManualAlgo())
    print(f"{winner.value} wins!")    