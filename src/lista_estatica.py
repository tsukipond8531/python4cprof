from dataclasses import dataclass

@dataclass
class No:
    '''Um nó em uma lista encadeada.'''
    # O item armazenado no nó
    item: int
    # O índice do próximo nó no encademento
    prox: None | int

@dataclass
class Lista:
    '''Uma lista encadeada com tamanho máximo fixo.

    Os nós são alocados quando a lista é criada e a quantidade de nós não é
    alterada. O campo prox de cada nó é utilizado para indicar o próximo nó da
    lista (iniciando com primeiro), se o nó está na lista, ou o próximo nó
    livre (iniciando com disponivel), se o nó não está na lista. Se o nó está
    disponível, o campo item não armazena nenhum valor válido.
    '''
    # Os nós pré-alocados
    nos: list[No]
    # O índice em nos do primeiro nó da lista ou None se a lista está vazia
    primeiro: None | int
    # O índice em nos do primeiro nó disponível ou None se não existe nenhum
    disponivel: None | int
    # O número de itens na lista
    num_itens: int

def cria_lista(n: int) -> Lista:
    '''Cria uma nova lista com tamanho máximo n.

    Requer que n > 0.

    Exemplo
    >>> lst = cria_lista(3)
    >>> to_list(lst)
    []
    '''
    assert n > 0
    # Faz o encadeamento dos disponíveis, começando com 0
    nos = []
    for i in range(n):
        nos.append(No(0, i + 1))
    # O último nó não tem um próximo
    nos[n - 1].prox = None
    return Lista(nos, None, 0, 0)

def insere_ordenado(lst: Lista, item: int) -> bool:
    '''Insere item em lst de maneira que lst permaneça ordenada.

    Produz True se existia espaço em lst e item foi inserido, False caso contrário.

    Requer que lst esteja ordenada.

    Exemplos
    >>> lst = cria_lista(4)
    >>> insere_ordenado(lst, 2)
    True
    >>> insere_ordenado(lst, 6)
    True
    >>> insere_ordenado(lst, 4)
    True
    >>> insere_ordenado(lst, 1)
    True
    >>> # Não tem mais espaço
    >>> insere_ordenado(lst, 7)
    False
    >>> to_list(lst)
    [1, 2, 4, 6]
    '''
    if lst.disponivel is None:
        return False

    # Usa o primeiro nó disponível
    novo = lst.disponivel
    lst.disponivel = lst.nos[novo].prox
    lst.nos[novo].item = item

    # Procura a posição de inserção
    pred = None
    atual = lst.primeiro
    while atual is not None and lst.nos[atual].item < item:
        pred = atual
        atual = lst.nos[atual].prox

    # Efetura a inserção
    if pred is None:
        # Não tem predecessor, então insere como primeiro da lst
        lst.nos[novo].prox = lst.primeiro
        lst.primeiro = novo
    else:
        # Insere novo entre pred e atual
        # antes : pred -> atual
        # depois: pred -> novo -> atual
        lst.nos[pred].prox = novo
        lst.nos[novo].prox = atual

    lst.num_itens += 1
    return True

def to_list(lst: Lista) -> list[int]:
    '''Converte lst para uma list do Python.'''
    resultado = []
    atual = lst.primeiro
    while atual is not None:
        resultado.append(lst.nos[atual].item)
        atual = lst.nos[atual].prox
    return resultado
