from enum import Enum, auto

class Cor(Enum):
    '''Rerpresenta a cor de um semáforo'''
    VERMELHO = auto()
    AMARELO = auto()
    VERDE = auto()

def proxima_cor(c: Cor) -> Cor:
    '''Determina a próxima cor de um semáforo que está na cor c.

    Exemplos
    >>> proxima_cor(Cor.VERMELHO).name
    'VERDE'
    '''
    if c == Cor.VERMELHO:
        return Cor.VERDE
    elif c == Cor.AMARELO:
        return Cor.VERMELHO
    elif c == Cor.VERDE:
        return Cor.AMARELO