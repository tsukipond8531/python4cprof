def indice_maximo(valores: list[float]) -> int:
    '''
    Encontra o índice do valor máximo em *valores*.

    Caso o valor máximo ocorra em mais de um índice,
    o menor índice é devolvido.

    Requer que valores não seja vazio.

    Exemplos
    >>> indice_maximo([2, 1, 4, -2])
    2
    >>> indice_maximo([-1, -4, -1])
    0
    '''
    assert len(valores) != 0, "valores não pode ser vazio"
    imax = 0
    for i in range(1, len(valores)):
        if valores[imax] < valores[i]:
            imax = i
    return imax
