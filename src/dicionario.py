from dataclasses import dataclass

@dataclass
class Item:
    '''Um par (chave, valor) em Dicionario.'''
    chave: str
    valor: int

@dataclass
class Dicionario:
    '''
    Um dicionario que associa strings com inteiros.

    Este dicionário mantém uma lista de pares (chave, valor) em uma lista. As
    adições são feitas no final da lista e as pesquisas são feitas de forma
    linear na lista.

    Este dicionário não suporta a remoção de items.
    '''
    items: list[Item]

def cria_dicionario() -> Dicionario:
    '''
    Cria um novo dicionário
    '''
    return Dicionario([])

def adiciona(dic: Dicionario, chave: str, valor: int) -> bool:
    '''
    Associa *chave* com *valor* em *dic* se ainda não existe valor associado
    com *chave*. Produz True se a associação foi criada, False caso contrário.

    Exemplos
    >>> dic = cria_dicionario()
    >>> adiciona(dic, 'Pedro', 24)
    True
    >>> adiciona(dic, 'Ana', 21)
    True
    >>> adiciona(dic, 'Pedro', 40)
    False
    '''
    if busca_chave(dic, chave) is None:
        dic.items.append(Item(chave, valor))
        return True
    else:
        return False

def busca_chave(dic: Dicionario, chave: str) -> None | int:
    '''
    Devolve o valor associado com *chave* em *dic*, ou None se *chave* não
    estiver em *dic*.

    Exemplos
    >>> dic = cria_dicionario()
    >>> adiciona(dic, 'verde', 10)
    True
    >>> adiciona(dic, 'amarelo', 20)
    True
    >>> busca_chave(dic, 'verde')
    10
    >>> busca_chave(dic, 'azul') is None
    True
    '''
    for item in dic.items:
        if item.chave == chave:
            return item.valor
    return None
