def ordena(nomes: list[str]) -> list[str]:
    '''
    Cria uma nova lista com os mesmos elementos de nomes mas de forma ordenada.

    Exemplo
    >>> ordena(['Paulo', 'Ana', 'Maria', 'João'])
    ['Ana', 'João', 'Maria', 'Paulo']
    '''
    r = []
    for nome in nomes:
        r.append(nome)
        i = len(r) - 1
        # r[i] é o nome que foi inserido
        # troca r[i] com r[i - 1] até que ele fique na posição adequada
        while i > 0 and r[i - 1] > r[i]:
            ri = r[i]
            r[i] = r[i - 1]
            r[i - 1] = ri
            # Ou usando atribuição múltipla
            # r[i - 1], r[i] = r[i], r[i - 1]
            i = i - 1
    return r
