def ordena_intercalacao(valores: list[int], inicio: int, fim: int):
    '''
    Ordena o subarranjo *valores[inicio:fim]* em ordem não decrescente.

    A ordenação é feita usando o algoritmo de intercalação.

    Requer que 0 <= inicio <= fim <= len(valores).

    Exemplos
    >>> valores = [3, 1, 6, 1, 2, 5, 3]
    >>> ordena_intercalacao(valores, 0, len(valores))
    >>> valores
    [1, 1, 2, 3, 3, 5, 6]
    '''
    assert 0 <= inicio <= fim <= len(valores)
    if fim > inicio + 1:
        m = (inicio + fim) // 2
        ordena_intercalacao(valores, inicio, m)
        ordena_intercalacao(valores, m, fim)
        intercala(valores, inicio, m, fim)

def intercala(valores: list[int], inicio: int, m: int, fim: int):
    '''
    Intercala os elementos dos subarranjos *valores[inicio:m]* e *valores[m:fim]*.

    Requer que 0 <= inicio < m < fim <= len(valores) e que os subarranjos
    valores[inicio:m] e valores[m:fim] estajam ordenados.

    Exemplo
    >>> valores = [1, 5, 2, 4, 1, 3, 5, 4, 6]
    >>> intercala(valores, 2, 4, 7)
    >>> valores
    [1, 5, 1, 2, 3, 4, 5, 4, 6]
    '''
    assert 0 <= inicio < m < fim <= len(valores)

    # Copia os elementos a direita de m para dir
    dir = []
    for i in range(inicio, m):
        dir.append(valores[i])

    # Copia os elementos a partir de m e a esquerda para esq
    esq = []
    for i in range(m, fim):
        esq.append(valores[i])

    i = 0
    j = 0
    k = inicio
    # Faz a intercação enquanto houver elementos em dir e esq
    while i < len(dir) and j < len(esq):
        if dir[i] < esq[j]:
            valores[k] = dir[i]
            i += 1
        else:
            valores[k] = esq[j]
            j += 1
        k += 1

    # Copia o resto de dir se houver
    while i < len(dir):
        valores[k] = dir[i]
        i += 1
        k += 1

    # Copia o resto de esq se houver
    while j < len(esq):
        valores[k] = esq[j]
        j += 1
        k += 1
