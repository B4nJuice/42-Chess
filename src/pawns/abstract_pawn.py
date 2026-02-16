from abc import ABC
from enum import Enum


class PawnColor(Enum):
    WHITE = "white"
    BLACK = "black"


class AbstractPawn(ABC):
    def __init__(self, color: PawnColor) -> None:
        self.color: PawnColor = color
