def conta_no_intervalo(valores: list[int], min: int, max: int) -> int:
    '''Devolve a quantidade de items em valores que estão no intervalo [min, max].
    Exemplo
    >>> conta_no_intervalo([2, 5, 1, 4, 6, 8], 2, 6)
    4
    '''
    # poderia ser
    # quant: int = 0
    quant = 0
    for valor in valores:
        # poderia ser
        # min <= valor <= max
        if min <= valor and valor <= max:
            quant += 1
    return quant


def main():
    print('Este programa conta a quantidade de valores em um determinado intervalo.')
    s = input('Digite os valores separados por espaço: ')
    valores = []
    for valor in s.split():
        valores.append(int(valor))
    min = int(input('Digite o limite inferior do intervalo: '))
    max = int(input('Digite o limite superior do intervalo: '))

    print('Existe(m)', conta_no_intervalo(valores, min, max), 'valor(es) no intervalo.')


if __name__ == "__main__":
    main()
