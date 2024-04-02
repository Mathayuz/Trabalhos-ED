from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    valor: int
    prox: Lista


Lista = No | None


def ordena(lst: Lista) -> Lista:
    '''
    Ordena os elementos de *lst* em ordem não decrescente.

    Exemplos

    >>> arranjo(ordena(lista([5, 2, 4, 6, 1, 3])))
    [1, 2, 3, 4, 5, 6]

    Testes de propriedade
    A seguir, listas com tamanhos n = 0, 1, ..., 10,
    são geradas com os elementos 0, 1, ..., n. Para
    cada lista todas as suas permutações são usadas
    para testar o algoritmo de ordenação.
    >>> from itertools import permutations
    >>> for n in range(0, 11):
    ...     for p in permutations(range(n)):
    ...         lst = lista(list(p))
    ...         lst = ordena(lst)
    ...         assert lst == lista(list(range(n)))
    '''
    # Caso base: Se a lista estiver vazia ou conter apenas um elemento, está ordenada
    if lst is None or lst.prox is None:
        return lst
    
    # Dividir a lista ao meio
    esquerda, direita = divide(lst)
    
    # Conquistar recursivamente ordenando cada metade
    esquerda = ordena(esquerda)
    direita = ordena(direita)
    
    # Combinar as duas metades ordenadas
    return merge(esquerda, direita)

def num_itens(lst: Lista) -> int:
    '''
    Retorna o número de itens na lista.

    Exemplos
    
    >>> num_itens(lista([5, 2, 4, 6, 1, 3]))
    6
    >>> num_itens(lista([]))
    0
    '''
    if lst is None:
        return 0
    return 1 + num_itens(lst.prox)

def divide(lst: Lista) -> tuple[Lista, Lista]:
    '''
    Divide a lista em duas partes.

    Exemplos:

    >>> esquerda, direita = divide(lista([5, 2, 4, 6, 1, 3]))
    >>> arranjo(esquerda)
    [5, 2, 4]
    >>> arranjo(direita)
    [6, 1, 3]

    >>> esquerda, direita = divide(lista([2, 5, 8, 3, 6]))
    >>> arranjo(esquerda)
    [2, 5]
    >>> arranjo(direita)
    [8, 3, 6]
    '''
    # Encontrar o meio da lista
    n = num_itens(lst)
    meio = n // 2

    # Dividir a lista em duas partes
    aux_esquerda = lst
    direita = lst
    for _ in range(meio):
        direita = direita.prox # type: ignore
    for _ in range(meio - 1):
        aux_esquerda = aux_esquerda.prox # type: ignore
    aux_esquerda.prox = None # type: ignore
    esquerda = lst

    return esquerda, direita

    
def merge(esquerda: Lista, direita: Lista) -> Lista:
    '''
    Combina duas listas ordenadas.

    Exemplos:

    >>> arranjo(merge(lista([2, 5, 8]), lista([3, 6, 7])))
    [2, 3, 5, 6, 7, 8]
    >>> arranjo(merge(lista([2, 5, 8]), lista([3, 6])))
    [2, 3, 5, 6, 8]
    >>> arranjo(merge(lista([]), lista([3, 6])))
    [3, 6]
    >>> arranjo(merge(lista([2, 5, 8]), lista([])))
    [2, 5, 8]
    >>> arranjo(merge(lista([]), lista([])))
    []
    '''
    # Caso base: Se uma das listas é vazia, retorna a outra lista
    if esquerda is None:
        return direita
    elif direita is None:
        return esquerda
    
    # Comparar os elementos das duas listas e combinar em ordem
    if esquerda.valor <= direita.valor:
        resultado = esquerda
        resultado.prox = merge(esquerda.prox, direita)
    else:
        resultado = direita
        resultado.prox = merge(esquerda, direita.prox)
    
    return resultado


def lista(a: list[int]) -> Lista:
    '''
    Cria uma Lista com os elementos de *lst*.

    Exemplo

    >>> arranjo(lista([5, 1, 4]))
    [5, 1, 4]
    '''
    # cria um sentinela
    inicio = No(0, None)
    p = inicio
    for x in a:
        p.prox = No(x, None)
        p = p.prox
    # descarta o sentinela
    return inicio.prox


def arranjo(lst: Lista) -> list[int]:
    '''
    Cria um arranjo com os elementos de *lst*.
    '''
    a = []
    while lst is not None:
        a.append(lst.valor)
        lst = lst.prox
    return a
