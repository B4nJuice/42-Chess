from src.pawns import AbstractPawn


class Board():
    def __init__(self):
        self.board: list[list[AbstractPawn]]
