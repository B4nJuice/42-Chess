from abc import ABC, abstractmethod
from enum import Enum


class PawnColor(Enum):
    WHITE = "white"
    BLACK = "black"


class AbstractPawn(ABC):
    def __init__(self, color: PawnColor) -> None:
        self.color: PawnColor = color

    @classmethod
    def create_pawn(cls, color: PawnColor) -> 'AbstractPawn':
        return cls(color)

    @abstractmethod
    def get_ascii(self) -> str:
        pass
