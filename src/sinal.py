def sinal(n: int) -> str:
    '''Devolve o sinal de n, isto é, 1 se n > 0, -1 se n < 1, 0 caso contrário.

    Exemplos
    >>> sinal(3)
    1
    >>> sinal(0)
    0
    >>> sinal(-4)
    -1
    '''
    if n > 0:
        return 1
    else:
        if n < 0:
            return -1
        else:
            return 0
    # Ou usando o elif
    # if n > 0:
    #     return 1
    # elif n < 0:
    #     return -1
    # else:
    #     return 0
