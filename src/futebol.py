from dataclasses import dataclass

@dataclass
class Desempenho:
    '''O desempenho de um time em um campeonato de futebol'''
    # O nome do time
    time: str
    # Pontos (3 por vitória e 1 por empate)
    pontos: int
    # Saldo de gols (gols pro - gols contra)
    saldo: int

def atualiza_desempenho(d: Desempenho, gols_pro: int, gols_contra: int):
    '''Atualiza o desempenho d considerando o resultado gols_pro x gols_contra.

    Exemplos
    >>> d = Desempenho('Maringá', 0, 0)
    >>> # Vitória
    >>> atualiza_desempenho(d, 5, 1)
    >>> d
    Desempenho(time='Maringá', pontos=3, saldo=4)
    >>> # Empate
    >>> atualiza_desempenho(d, 2, 2)
    >>> d
    Desempenho(time='Maringá', pontos=4, saldo=4)
    >>> # Derrota
    >>> atualiza_desempenho(d, 0, 3)
    >>> d
    Desempenho(time='Maringá', pontos=4, saldo=1)
    '''
    d.saldo = d.saldo + gols_pro - gols_contra

    if gols_pro > gols_contra:
        d.pontos = d.pontos + 3
    elif gols_pro == gols_contra:
        d.pontos = d.pontos + 1
