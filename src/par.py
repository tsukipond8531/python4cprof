def par(n: int) -> bool:
    '''
    Produz True se *n* é par, isto é, *n* é múltiplo de 2. False caso contrário.

    Exemplos
    >>> par(10)
    True
    >>> par(3)
    False
    >>> par(0)
    True
    '''
    return n % 2 == 0
