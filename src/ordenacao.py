def ordena_insercao(valores: list[int]):
    '''
    Ordena valores em ordem não decrescente usando o
    algoritmo de ordenação por inserção.

    Exemplos
    >>> valores = [3, 1, 6, 1, 2, 5, 3]
    >>> ordena_insercao(valores)
    >>> valores
    [1, 1, 2, 3, 3, 5, 6]
    '''
    for j in range(1, len(valores)):
        i = j
        while i > 0 and valores[i] < valores[i - 1]:
            valores[i], valores[i - 1] = valores[i - 1], valores[i]
            i -= 1


def ordena_intercalacao(valores: list[int], inicio: int, fim: int):
    '''
    Ordena o subarranjo valores[inicio:fim] em ordem não decrescente usando o
    algoritmo de ordenação por intercalação.

    Exemplos
    >>> valores = [3, 1, 6, 1, 2, 5, 3]
    >>> ordena_intercalacao(valores, 0, len(valores))
    >>> valores
    [1, 1, 2, 3, 3, 5, 6]
    '''
    if fim > inicio + 1:
        m = (inicio + fim) // 2
        ordena_intercalacao(valores, inicio, m)
        ordena_intercalacao(valores, m, fim)
        intercala(valores, inicio, m, fim)


def intercala(valores: list[int], inicio: int, m: int, fim: int):
    '''
    Intervacala os elementos dos subarranjos valores[inicio:m] e
    valores[m:fim].

    Requer que inicio < m < fim e que os subarranjos valores[inicio:m] e
    valores[m:fim] estajam ordenados.

    Exemplo
    >>> valores = [1, 5, 2, 4, 1, 3, 5, 4, 6]
    >>> intercala(valores, 2, 4, 7)
    >>> valores
    [1, 5, 1, 2, 3, 4, 5, 4, 6]
    '''
    # copia os elementos a direita de m para dir
    dir = []
    for i in range(inicio, m):
        dir.append(valores[i])

    # copia os elementos a esqueda de m para dir
    esq = []
    for i in range(m, fim):
        esq.append(valores[i])

    i = 0
    j = 0
    k = inicio
    # faz a intercação até enquanto houver elementos em dir e esq
    while i < len(dir) and j < len(esq):
        if dir[i] < esq[j]:
            valores[k] = dir[i]
            i += 1
        else:
            valores[k] = esq[j]
            j += 1
        k += 1

    # copia os resto de dir se houver
    while i < len(dir):
        valores[k] = dir[i]
        i += 1
        k += 1

    # copia os resto de esq se houver
    while j < len(esq):
        valores[k] = esq[j]
        j += 1
        k += 1
