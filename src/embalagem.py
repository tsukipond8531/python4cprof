from dataclasses import dataclass

@dataclass
class Envelope:
    comprimento: int
    largura: int

@dataclass
class Caixa:
    comprimento: int
    largura: int
    altura: int

@dataclass
class Rolo:
    comprimento: int
    diametro: int

'''Uma embalagem para envio nos correios.'''
Embalagem = Envelope | Caixa | Rolo

def dentro_limites(emb: Embalagem) -> bool:
    '''
    Produz True se *emb* está dentro dos limites, False caso contrário.

    Uma embalagem está dentro dos limites se suas medidas obedecem as seguintes
    restrições (em cm).

                     mínimo  máximo
    Envelope
        comprimento     16      60
        largura         11      60
    Caixa
        comprimento     15     100
        largura         10     100
        altura           1     100
    Rolo
        comprimento     18     100
        diametro         5      21

    Exemplos (alguns omitidos para diminuir o espaço)
    >>> dentro_limites(Envelope(20, 40))
    True
    >>> dentro_limites(Envelope(15, 40))
    False
    >>> dentro_limites(Caixa(30, 40, 80))
    True
    >>> dentro_limites(Caixa(30, 101, 80))
    False
    >>> dentro_limites(Rolo(50, 18))
    True
    >>> dentro_limites(Rolo(50, 4))
    False
    '''
    if isinstance(emb, Envelope):
        return 16 <= emb.comprimento <= 60 and \
               11 <= emb.largura <= 60
    elif isinstance(emb, Caixa):
        return 15 <= emb.comprimento <= 100 and \
               10 <= emb.largura <= 100 and \
                1 <= emb.altura <= 100
    elif isinstance(emb, Rolo):
        return 18 <= emb.comprimento <= 100 and \
                5 <= emb.diametro <= 21
