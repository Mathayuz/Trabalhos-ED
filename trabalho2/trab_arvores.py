from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    '''
    Um nó em uma árvore binária de busca (ABB).
    '''
    esq: Arvore
    val: int
    dir: Arvore

# Árvore binária de busca (ABB)
Arvore = No | None


# Função 1: Cria uma árvore binária de busca (ABB) a partir de uma lista de valores
def cria_ABB(valores: list[int]) -> Arvore:
    '''
    Cria e retorna a árvore binária de busca (ABB) que contém os valores
    do vetor *valores* que estão em ordem crescente.

    Exemplos:

    # Árvore vazia
    >>> cria_ABB([]) is None
    True

    # Árvore com um nó: ( 1 )
    >>> cria_ABB([1])
    No(esq=None, val=1, dir=None)

    # Árvore com dois nós: ( 1 ( 2 ))
    >>> cria_ABB([1, 2])
    No(esq=None, val=1, dir=No(esq=None, val=2, dir=None))

    # Árvore com três nós: (( 1 ) 2 ( 3 ))
    >>> cria_ABB([1, 2, 3])
    No(esq=No(esq=None, val=1, dir=None), val=2, dir=No(esq=None, val=3, dir=None))

    # Árvore com cinco nós: (( 1 ( 2 )) 3 ( 4 ( 5 )))
    >>> cria_ABB([1, 2, 3, 4, 5])
    No(esq=No(esq=None, val=1, dir=No(esq=None, val=2, dir=None)), val=3, dir=No(esq=None, val=4, dir=No(esq=None, val=5, dir=None)))

    # Árvore com seis nós: (( 1 ( 2 )) 3 (( 4 ) 5 ( 6 )))
    >>> cria_ABB([1, 2, 3, 4, 5, 6])
    No(esq=No(esq=None, val=1, dir=No(esq=None, val=2, dir=None)), val=3, dir=No(esq=No(esq=None, val=4, dir=None), val=5, dir=No(esq=None, val=6, dir=None)))
    '''
    # Retorna um Nó, onde o valor do nó é o valor do meio do vetor
    # e os filhos são as árvores criadas com os valores menores e maiores que o valor do meio
    if len(valores) == 0:
        return None
    inicio = 0
    fim = len(valores) - 1
    meio = (inicio + fim) // 2
    return No(cria_ABB(valores[:meio]), valores[meio], cria_ABB(valores[meio+1:]))


# Função 2: Verifica se duas ABBs têm os mesmos elementos
def ABB_mesmos_elementos(t: Arvore, r: Arvore) -> bool:
    '''
    Verifica e devolve True se as ABBs *t* e *r* têm os mesmos elementos,
    mesmo que as árvores não tenham a mesma estrutura (manténdo a propriedade de uma ABB)
    senão retorna False.

    Exemplos:

    # Árvores vazias
    >>> ABB_mesmos_elementos(None, None)
    True

    # Árvore *t* vazia e *r* não vazia
    >>> ABB_mesmos_elementos(None, No(None, 1, None))
    False

    # Árvore *t* não vazia e *r* vazia
    >>> ABB_mesmos_elementos(No(None, 1, None), None)
    False

    # Árvores com um nó e com o mesmo valor
    >>> ABB_mesmos_elementos(No(None, 1, None), No(None, 1, None))
    True

    # Árvores com um nó e com valores diferentes
    >>> ABB_mesmos_elementos(No(None, 1, None), No(None, 2, None))
    False

    # Árvore *t* com um nó e *r* com dois nós
    >>> ABB_mesmos_elementos(No(None, 1, None), No(None, 1, No(None, 2, None)))
    False

    # Árvore *t* com dois nós e *r* com um nó
    >>> ABB_mesmos_elementos(No(None, 1, No(None, 2, None)), No(None, 1, None))
    False

    # Árvores com três nós com os mesmos valores e mesma estrutura
    >>> ABB_mesmos_elementos(No(No(None, 1, None), 2, No(None, 3, None)), No(No(None, 1, None), 2, No(None, 3, None)))
    True

    # Árvores com três nós com os valores diferentes e mesma estrutura
    >>> ABB_mesmos_elementos(No(No(None, 1, None), 2, No(None, 3, None)), No(No(None, 1, None), 3, No(None, 4, None)))
    False

    # Árvores com três nós com os mesmos valores e estruturas diferentes
    >>> ABB_mesmos_elementos(No(No(None, 1, None), 2, No(None, 3, None)), No(None, 1, No(None, 2, No(None, 3, None))))
    True

    # Árvore *t* com três nós e *r* com quatro nós
    >>> ABB_mesmos_elementos(No(No(None, 1, None), 2, No(None, 3, None)), No(None, 1, No(None, 2, No(None, 3, No(None, 4, None)))))
    False

    # Árvore *t* com quatro nós e *r* com três nós
    >>> ABB_mesmos_elementos(No(No(None, 1, None), 2, No(None, 3, No(None, 4, None))), No(None, 1, No(None, 2, No(None, 3, None))))
    False
    '''
    # Se as duas árvores não são vazias, mas têm número de elementos diferentes, 
    # elas não têm os mesmos elementos
    # Se as duas árvores não são vazias e têm o mesmo número de elementos,
    # a função *ABB_mesmos_elementos_aux* verifica se todas as chaves de *t* estão em *r*
    assert verifica_ABB(t) and verifica_ABB(r)
    if num_elementos(t) != num_elementos(r):
        return False
    return ABB_mesmos_elementos_aux(t, r)

# Função auxiliar para verificar se duas ABBs têm os mesmos elementos
def ABB_mesmos_elementos_aux(t: Arvore, r: Arvore) -> bool:
    '''
    Verifica se as ABBs *t* e *r* têm os mesmos elementos,
    mesmo que as árvores não tenham a mesma estrutura (manténdo a propriedade de uma ABB)
    senão retorna False.
    Como essa função é apenas uma auxiliar da função *ABB_mesmos_elementos*,
    ela não possui exemplos, pois ela não leva em consideração todos os casos possíveis.
    Por isso os exemplos estão apenas na função principal *ABB_mesmos_elementos*.
    '''
    # Nesse caso a função *num_elementos* já foi chamada e sabemos que as árvores
    # têm o mesmo número de elementos.
    # Portanto, se *t* é vazia, *r* também é vazia e a função retorna True.
    # Senão, a função verifica se todos os elementos de *t* estão em *r*.
    # E as árvores *t* e *r*, na primeira chamada dessa função serão sempre Nós.
    if t is None:
        return True
    return busca_binaria(r, t.val) and ABB_mesmos_elementos_aux(t.esq, r) and ABB_mesmos_elementos_aux(t.dir, r)

# Função auxiliar para encontrar o número de elementos de uma árvore
def num_elementos(t: Arvore) -> int:
    '''
    Devolve o número de elementos da árvore *t*.
    Exemplos:
    >>> num_elementos(None)
    0
    >>> num_elementos(No(None, 1, None))
    1
    >>> num_elementos(No(No(None, 1, None), 2, No(None, 3, None)))
    3
    '''
    if t is None:
        return 0
    return 1 + num_elementos(t.esq) + num_elementos(t.dir)

# Função auxiliar que verifica se uma árvore é uma ABB
def verifica_ABB(t: Arvore) -> bool:
    '''
    Verifica se a árvore *t* é uma árvore binária de busca (ABB).
    Exemplos:
    >>> verifica_ABB(None)
    True
    >>> verifica_ABB(No(None, 1, None))
    True
    >>> verifica_ABB(No(No(None, 1, None), 2, No(None, 3, None)))
    True
    >>> verifica_ABB(No(No(None, 1, None), 2, No(None, 1, None)))
    False
    >>> verifica_ABB(No(No(None, 2, None), 1, No(None, 3, None)))
    False
    '''
    # Se a árvore é vazia, ela é uma ABB
    # Se a árvore é um nó, ela é uma ABB se as subárvores esquerda e direita são ABBs
    # e se o valor do nó é maior que o maior valor da subárvore esquerda e menor que o menor valor da subárvore direita
    if t is None:
        return True
    if t.esq is not None and maximo(t.esq) > t.val:
        return False
    if t.dir is not None and minimo(t.dir) < t.val:
        return False
    return verifica_ABB(t.esq) and verifica_ABB(t.dir)

# Função auxiliar para encontrar o maior valor de uma árvore
def maximo(t: No) -> int:
    '''
    Devolve o maior valor do nó *t*.
    Exemplos:
    >>> maximo(No(None, 1, None))
    1
    >>> maximo(No(No(None, 1, None), 2, No(None, 3, None)))
    3
    >>> maximo(No(No(None, 1, None), 2, No(None, 3, No(None, 4, None))))
    4
    '''
    if t.dir is None:
        return t.val
    return maximo(t.dir)

# Função auxiliar para encontrar o menor valor de uma árvore
def minimo(t: No) -> int:
    '''
    Devolve o menor valor do nó *t*.
    Exemplos:
    >>> minimo(No(None, 1, None))
    1
    >>> minimo(No(No(None, 1, None), 2, No(None, 3, None)))
    1
    >>> minimo(No(No(None, 2, None), 3, No(None, 4, No(None, 5, None))))
    2
    '''
    if t.esq is None:
        return t.val
    return minimo(t.esq)

# Função auxiliar para encontrar um elemento em uma árvore binária de busca
def busca_binaria(t: Arvore, x: int) -> bool:
    '''
    Verifica se o valor *x* está na árvore binária de busca *t*.
    Exemplos:
    >>> busca_binaria(None, 1)
    False
    >>> busca_binaria(No(None, 1, None), 1)
    True
    >>> busca_binaria(No(None, 1, None), 2)
    False
    >>> busca_binaria(No(No(None, 1, None), 2, No(None, 3, None)), 3)
    True
    >>> busca_binaria(No(No(None, 1, None), 2, No(None, 3, None)), 4)
    False
    '''
    if t is None:
        return False
    if t.val == x:
        return True
    if x < t.val:
        return busca_binaria(t.esq, x)
    return busca_binaria(t.dir, x)


# Função 3: Encontra todos os caminhos de tamanho máximo em uma árvore
def caminhos_TAMMAX(t: Arvore) -> list[list[int]]:
    r'''
    Devolve uma lista com todos os caminhos de tamanho máximo da árvore *t*, ou seja,
    uma lista com caminhos(listas) que contém os valores dos nós que pertencem ao caminho
    onde a altura + 1 da árvore é o tamanho do caminho.

    Exemplos:

    # Árvore vazia
    >>> caminhos_TAMMAX(None)
    []

    # Árvore com um nó: ( 1 )
    >>> caminhos_TAMMAX(No(None, 1, None))
    [[1]]

    # Árvore com dois nós: ( 1 ( 3 ))
    >>> caminhos_TAMMAX(No(None, 1, No(None, 3, None)))
    [[1, 3]]

    # Árvore com três nós: (( 1 ) 2 ( 3 ))
    >>> caminhos_TAMMAX(No(No(None, 1, None), 2, No(None, 3, None)))
    [[2, 1], [2, 3]]

    # Árvore com quatro nós: (( 1 ( 2 )) 3 ( 4 ))
    >>> caminhos_TAMMAX(No(No(None, 1, None), 2, No(None, 3, No(None, 4, None))))
    [[2, 3, 4]]

    # Árvore com sete nós: (( 1 ( 2 )) 4 (( 5 ) 6 ( 7 )))
    >>> caminhos_TAMMAX(No(No(No(None, 1, None), 2, No(None, 3, None)), 4, No(No(None, 5, None), 6, No(None, 7, None))))
    [[4, 2, 1], [4, 2, 3], [4, 6, 5], [4, 6, 7]]

    Teste com a seguinte árvore:
             2
           /   \
          8     3
         / \   / \
        3     7   5
       / \       /
          4     2

    >>> caminhos_TAMMAX(No(No(No(None, 3, No(None, 4, None)), 8, None), 2, No(No(None, 7, None), 3, No(No(None, 2, None), 5, None))))
    [[2, 8, 3, 4], [2, 3, 5, 2]]
    '''
    alt = altura(t)
    caminhos_t = caminhos(t)
    return [caminho for caminho in caminhos_t if len(caminho) == alt + 1]

# Função auxiliar para encontrar todos os caminhos de uma árvore
def caminhos(t: Arvore) -> list[list[int]]:
    r'''
    Devolve uma lista com todos os caminhos da árvore *t*.
    Exemplos:
    >>> caminhos(None)
    []
    >>> caminhos(No(None, 1, None))
    [[1]]
    >>> caminhos(No(No(None, 1, None), 2, No(None, 3, None)))
    [[2, 1], [2, 3]]
    >>> caminhos(No(No(No(None, 1, None), 2, No(None, 3, None)), 4, No(No(None, 5, None), 6, No(None, 7, None))))
    [[4, 2, 1], [4, 2, 3], [4, 6, 5], [4, 6, 7]]

    Teste com a seguinte árvore:
             2
           /   \
          8     3
         / \   / \
        3     7   5
       / \       /
          4     2
          
    >>> caminhos(No(No(No(None, 3, No(None, 4, None)), 8, None), 2, No(No(None, 7, None), 3, No(No(None, 2, None), 5, None))))
    [[2, 8, 3, 4], [2, 3, 7], [2, 3, 5, 2]]
    '''
    if t is None:
        return []
    if t.esq is None and t.dir is None:
        return [[t.val]]
    c = []
    caminhos_esq = caminhos(t.esq)
    caminhos_dir = caminhos(t.dir)
    for caminho in caminhos_esq + caminhos_dir:
        c += [[t.val] + caminho]
    return c

# Função auxiliar para encontrar a altura de uma árvore
def altura(t: Arvore) -> int:
    '''
    Devolve a altura da árvore *t*.
    Exemplos:
    >>> altura(None)
    -1
    >>> altura(No(None, 1, None))
    0
    >>> altura(No(No(None, 1, None), 2, No(None, 3, None)))
    1
    >>> altura(No(No(No(None, 1, None), 2, No(None, 3, None)), 4, None))
    2
    >>> altura(No(No(No(None, 3, No(None, 4, None)), 8, None), 2, No(No(None, 7, None), 3, No(No(None, 2, None), 5, None))))
    3
    '''
    if t is None:
        return -1
    return 1 + max(altura(t.esq), altura(t.dir))
