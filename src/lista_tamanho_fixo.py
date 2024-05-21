from dataclasses import dataclass

@dataclass
class No:
    '''Um nó em uma lista encadeada.'''
    # O item armazenado no nó
    item: int
    # O índice do próximo nó no encademento
    prox: None | int

class Lista:
    '''
    Uma lista ordenada de números.

    A implementação é feita com um encadeamento de tamanho máximo fixo.

    Os nós são alocados quando a lista é criada e a quantidade de nós não é
    alterada. O campo prox de cada nó é utilizado para indicar o próximo nó da
    lista (se o nó está na lista), ou o próximo nó livre (se o nó não está na
    lista). Se o nó está disponível, o campo item não armazena nenhum valor
    válido.
    '''
    # Os nós pré-alocados
    nos: list[No]
    # O índice em nos do primeiro nó da lista ou None se a lista está vazia
    primeiro: None | int
    # O índice em nos do primeiro nó disponível ou None se não existe nenhum
    disponivel: None | int
    # O número de itens na lista
    num_itens: int

    def __init__(self, n: int):
        '''
        Cria uma nova lista com tamanho máximo *n*.

        Requer que n > 0.

        Exemplo
        >>> lst = Lista(3)
        >>> lst.para_list()
        []
        '''
        assert n > 0
        self.nos = []
        self.primeiro = None
        self.disponivel = 0
        self.num_itens = 0
        # Faz o encadeamento dos disponíveis, começando com 0
        for i in range(n):
            self.nos.append(No(0, i + 1))
        # O último nó não tem um próximo
        self.nos[n - 1].prox = None

    def insere_ordenado(self, item: int) -> bool:
        '''
        Insere *item* na lista de maneira que ela permaneça ordenada.

        Produz True se existia espaço na lista e *item* foi inserido, False caso contrário.

        Exemplos
        >>> lst = Lista(4)
        >>> lst.insere_ordenado(2)
        True
        >>> lst.insere_ordenado(6)
        True
        >>> lst.insere_ordenado(4)
        True
        >>> lst.insere_ordenado(1)
        True
        >>> # Não tem mais espaço
        >>> lst.insere_ordenado(7)
        False
        >>> lst.para_list()
        [1, 2, 4, 6]
        '''
        if self.disponivel is None:
            return False

        # Usa o primeiro nó disponível
        novo = self.disponivel
        self.disponivel = self.nos[novo].prox
        self.nos[novo].item = item

        # Procura a posição de inserção
        pred = None
        atual = self.primeiro
        while atual is not None and self.nos[atual].item < item:
            pred = atual
            atual = self.nos[atual].prox

        # Efetura a inserção
        if pred is None:
            # Não tem predecessor, então insere como primeiro da self
            self.nos[novo].prox = self.primeiro
            self.primeiro = novo
        else:
            # Insere novo entre pred e atual
            # antes : pred -> atual
            # depois: pred -> novo -> atual
            self.nos[pred].prox = novo
            self.nos[novo].prox = atual

        self.num_itens += 1
        return True

    def para_list(self) -> list[int]:
        '''
        Converte a lista para uma list do Python.

        Este método é útil para testar o funcionamento da lista.
        '''
        resultado = []
        atual = self.primeiro
        while atual is not None:
            resultado.append(self.nos[atual].item)
            atual = self.nos[atual].prox
        return resultado
