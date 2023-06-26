def sinal(n: int) -> str:
    '''Devolve o sinal de n.

    Exemplos
    >>> sinal(3)
    'positivo'
    >>> sinal(0)
    'neutro'
    >>> sinal(-1)
    'negativo'
    '''
    if n > 0:
        return 'positivo'
    else:
        if n < 0:
            return 'negativo'
        else:
            return 'neutro'
    # ou usando o elif
    # if n > 0:
    #    return 'positivo'
    # elif n < 0:
    #     return 'negativo'
    # else:
    #     return 'neutro'
