# Esse import é necessário devido a autorreferência na definição de No
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    '''Um nó em uma lista encadeada.'''
    # O item armazenado no nó
    item: int
    # O próximo nó
    prox: None | No

class Lista:
    '''
    Uma lista ordenada de números.

    Essa implementação usa encadeamento de nós.
    '''
    primeiro: No | None

    def __init__(self):
        '''
        Cria uma nova lista.

        Exemplo
        >>> lst = Lista()
        >>> lst.para_list()
        []
        '''
        self.primeiro = None

    def insere_ordenado(self, item: int) -> bool:
        '''
        Insere *item* na lista de maneira que ela permaneça ordenada.

        Sempre produz True indicando que o item foi inserido.

        Exemplos
        >>> lst = Lista()
        >>> lst.insere_ordenado(2)
        True
        >>> lst.insere_ordenado(6)
        True
        >>> lst.insere_ordenado(4)
        True
        >>> lst.insere_ordenado(1)
        True
        >>> lst.para_list()
        [1, 2, 4, 6]
        '''
        # Procura a posição de inserção
        pred = None
        atual = self.primeiro
        while atual is not None and atual.item < item:
            pred = atual
            atual = atual.prox

        # Efetura a inserção
        if pred is None:
            # Não tem predecessor, então insere como primeiro
            self.primeiro = No(item, self.primeiro)
        else:
            # Insere item entre pred e atual
            # antes : pred -> atual
            # depois: pred -> novo -> atual
            pred.prox = No(item, pred.prox)
        return True

    def para_list(self) -> list[int]:
        '''
        Converte a lista para uma list do Python.

        Este método é útil para testar o funcionamento da lista.
        '''
        resultado = []
        atual = self.primeiro
        while atual is not None:
            resultado.append(atual.item)
            atual = atual.prox
        return resultado
