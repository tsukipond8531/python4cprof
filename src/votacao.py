from dataclasses import dataclass
from enum import StrEnum, auto

class Cor(StrEnum):
    VERDE = auto()
    AZUL = auto()
    VERMELHO = auto()

@dataclass
class Totalizacao:
    verde: int
    azul: int
    vermelho: int
