from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    '''Um nó em um encadeamento'''
    item: int
    prox: No | None

class Colecao:
    '''
    Uma coleção com a quantidade de figurinhas (enumeradas) total 
    de uma pessoa que possue algumas operações relacionadas
    a trocas de figurinhas entre pessoas.
    Exemplos
    >>> c = Colecao(5)
    >>> c.colecao_sem_repeticao()
    '[]'
    >>> c.colecao_com_repeticao()
    '[]'
    >>> c.insere(1)
    >>> c.insere(1)
    >>> c.insere(2)
    >>> c.insere(2)
    >>> c.insere(3)
    >>> c.insere(3)
    >>> c.insere(5)
    >>> c.colecao_sem_repeticao()
    '[1, 2, 3, 5]'
    >>> c.colecao_com_repeticao()
    '[1 (1), 2 (1), 3 (1)]'
    >>> c.remove(1)
    >>> c.remove(2)
    >>> c.remove(5)
    >>> c.colecao_sem_repeticao()
    '[1, 2, 3]'
    >>> c.colecao_com_repeticao()
    '[3 (1)]'
    '''
    inicio: No | None
    fim: No | None

    def __init__(self, ultima_figurinha: int) -> None:
        '''
        Cria uma nova coleção com capacidade para armazenar até a *ultima_figurinha*
        do álbum de figurinhas(desconsiderando as repetidas).
        '''
        self.ultima_figurinha = ultima_figurinha
        self.inicio = None
        self.fim = None

    def insere(self, figurinha: int):
        '''
        Insere a *figurinha* na coleção de maneira que possa haver figurinhas repetidas.
        Requer que a *figurinha* inserida faça parte do álbum.
        Exemplos
        >>> c = Colecao(10)
        >>> for i in range(1, 11):
        ...     c.insere(i)
        >>> for i in range(3, 8):
        ...     c.insere(i)
        >>> c.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'
        >>> c.colecao_com_repeticao()
        '[3 (1), 4 (1), 5 (1), 6 (1), 7 (1)]'
        >>> c.insere(0)
        Traceback (most recent call last):
        ...
        ValueError: figurinha não faz parte do álbum
        '''
        if figurinha < 1 or figurinha > self.ultima_figurinha:
            raise ValueError('figurinha não faz parte do álbum')
        if self.fim is None:
            self.inicio = No(figurinha, None)
            self.fim = self.inicio
        else:
            self.fim.prox = No(figurinha, None)
            self.fim = self.fim.prox
        ordena_no(self.inicio)

    def remove(self, figurinha: int):
        '''
        Remove a *figurinha* da coleção de maneira que possa haver figurinha repetidas.
        Requer que a *figurinha* removida faça parte do álbum.
        Requer que a *figurinha* removida esteja na coleção(podendo ser única ou repetida).
        Exemplos
        >>> c = Colecao(10)
        >>> c.colecao_sem_repeticao()
        '[]'
        >>> c.remove(3)
        Traceback (most recent call last):
        ...
        ValueError: figurinha não está na coleção
        >>> for i in range(1, 11):
        ...     c.insere(i)
        >>> c.insere(2)
        >>> c.insere(3)
        >>> c.insere(2)
        >>> c.remove(1)
        >>> c.remove(5)
        >>> c.colecao_sem_repeticao()
        '[2, 3, 4, 6, 7, 8, 9, 10]'
        >>> c.colecao_com_repeticao()
        '[2 (2), 3 (1)]'
        >>> c.remove(1)
        Traceback (most recent call last):
        ...
        ValueError: figurinha não está na coleção
        >>> c.remove(11)
        Traceback (most recent call last):
        ...
        ValueError: figurinha não faz parte do álbum
        '''
        if figurinha < 1 or figurinha > self.ultima_figurinha:
            raise ValueError('figurinha não faz parte do álbum')
        if not encontra_figurinha(self.inicio, figurinha):
            raise ValueError('figurinha não está na coleção')
        atual = self.inicio
        anterior = None
        while atual is not None:
            if atual.item == figurinha:
                if anterior is None:
                    self.inicio = atual.prox
                else:
                    anterior.prox = atual.prox
                if atual.prox is None:
                    self.fim = None
                break
            anterior = atual
            atual = atual.prox

    def colecao_sem_repeticao(self) -> str:
        '''
        Devolve uma lista com os elementos da coleção sem repetição.
        Exemplos
        >>> c = Colecao(5)
        >>> c.colecao_sem_repeticao()
        '[]'
        >>> c.insere(2)
        >>> for i in range(1, 6):
        ...     c.insere(i)
        >>> c.insere(1)
        >>> c.insere(2)
        >>> c.insere(3)
        >>> c.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5]'
        '''
        colecao = '['
        atual = self.inicio
        while atual is not None:
            while atual.prox is not None and atual.item == atual.prox.item:
                atual = atual.prox
            colecao += str(atual.item)
            if atual.prox is not None:
                colecao += ', '
            atual = atual.prox
        colecao += ']'
        return colecao

    def colecao_com_repeticao(self) -> str:
        '''
        Devolve uma lista com os elementos da coleção com repetição.
        Exemplos
        >>> c = Colecao(5)
        >>> c.colecao_com_repeticao()
        '[]'
        >>> c.insere(2)
        >>> for i in range(1, 6):
        ...     c.insere(i)
        >>> c.colecao_com_repeticao()
        '[2 (1)]'
        >>> c.insere(1)
        >>> c.insere(2)
        >>> c.insere(3)
        >>> c.colecao_com_repeticao()
        '[1 (1), 2 (2), 3 (1)]'
        '''
        repetidos = 0
        colecao = '['
        atual = self.inicio
        while atual is not None:
            while atual.prox is not None and atual.item == atual.prox.item:
                repetidos += 1
                atual = atual.prox
            if repetidos > 0:
                if len(colecao) > 1:
                    colecao += ', '
                colecao += str(atual.item) + ' (' + str(repetidos) + ')'
            repetidos = 0
            atual = atual.prox
        colecao += ']'
        return colecao

    def troca_maxima(self, outra: Colecao):
        '''
        Realiza a troca máxima entre *self* e *outra* coleção, de modo que apenas
        as figurinhas repetidas serão trocadas, e em ordem crescente.
        Requer que os álbuns sejam os mesmos(tamanhos iguais).
        Exemplos

        # Teste com coleção *c1* possuindo uma repetida que *c2* não tem,
        # *c2* possuindo 5 repetidas que *c1* não tem.
        # (apenas 1 deve ser trocada).
        # Além da troca de coleções vazias no começo.

        >>> c1 = Colecao(10)
        >>> c2 = Colecao(10)
        >>> c1.troca_maxima(c2)
        >>> c1.colecao_sem_repeticao()
        '[]'
        >>> c1.colecao_com_repeticao()
        '[]'
        >>> c2.colecao_sem_repeticao()
        '[]'
        >>> c2.colecao_com_repeticao()
        '[]'
        >>> for i in range(1, 3):
        ...     c1.insere(i)
        >>> c1.insere(1)
        >>> c1.insere(2)
        >>> c1.insere(2)
        >>> c1.insere(8)
        >>> for i in range(3, 8):
        ...     c2.insere(i)
        >>> c2.insere(1)
        >>> c2.insere(1)
        >>> c2.insere(3)
        >>> c2.insere(3)
        >>> c2.insere(5)
        >>> c2.insere(5)
        >>> c2.insere(6)
        >>> c1.colecao_sem_repeticao()
        '[1, 2, 8]'
        >>> c1.colecao_com_repeticao()
        '[1 (1), 2 (2)]'
        >>> c2.colecao_sem_repeticao()
        '[1, 3, 4, 5, 6, 7]'
        >>> c2.colecao_com_repeticao()
        '[1 (1), 3 (2), 5 (2), 6 (1)]'
        >>> c1.troca_maxima(c2)
        >>> c1.colecao_sem_repeticao()
        '[1, 2, 3, 8]'
        >>> c1.colecao_com_repeticao()
        '[1 (1), 2 (1)]'
        >>> c2.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7]'
        >>> c2.colecao_com_repeticao()
        '[1 (1), 3 (1), 5 (2), 6 (1)]'

        # Teste com coleção *c3* possuindo as mesmas repetidas que *c4*
        # (nada deve ser trocado).

        >>> c3 = Colecao(20)
        >>> c4 = Colecao(20)
        >>> for i in range(1, 8):
        ...     c3.insere(i)
        >>> c3.insere(1)
        >>> c3.insere(2)
        >>> c3.insere(2)
        >>> c3.insere(3)
        >>> c3.insere(4)
        >>> for i in range(1, 14):
        ...     c4.insere(i)
        >>> c4.insere(1)
        >>> c4.insere(2)
        >>> c4.insere(2)
        >>> c4.insere(3)
        >>> c4.insere(4)
        >>> c3.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7]'
        >>> c3.colecao_com_repeticao()
        '[1 (1), 2 (2), 3 (1), 4 (1)]'
        >>> c4.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]'
        >>> c4.colecao_com_repeticao()
        '[1 (1), 2 (2), 3 (1), 4 (1)]'
        >>> c3.troca_maxima(c4)
        >>> c3.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7]'
        >>> c3.colecao_com_repeticao()
        '[1 (1), 2 (2), 3 (1), 4 (1)]'
        >>> c4.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]'
        >>> c4.colecao_com_repeticao()
        '[1 (1), 2 (2), 3 (1), 4 (1)]'

        # Teste com coleção *c6* possuindo figurinhas repetidas que *c5* não tem,
        # porém possuindo as repetidas que *c5* tem(nada deve ser trocado).

        >>> c5 = Colecao(20)
        >>> c6 = Colecao(20)
        >>> for i in range(1, 8):
        ...     c5.insere(i)
        >>> c5.insere(1)
        >>> c5.insere(2)
        >>> c5.insere(2)
        >>> for i in range(1, 10):
        ...     c6.insere(i)
        >>> c6.insere(1)
        >>> c6.insere(2)
        >>> c6.insere(8)
        >>> c6.insere(9)
        >>> c5.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7]'
        >>> c5.colecao_com_repeticao()
        '[1 (1), 2 (2)]'
        >>> c6.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7, 8, 9]'
        >>> c6.colecao_com_repeticao()
        '[1 (1), 2 (1), 8 (1), 9 (1)]'
        >>> c5.troca_maxima(c6)
        >>> c5.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7]'
        >>> c5.colecao_com_repeticao()
        '[1 (1), 2 (2)]'
        >>> c6.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7, 8, 9]'
        >>> c6.colecao_com_repeticao()
        '[1 (1), 2 (1), 8 (1), 9 (1)]'

        # Teste com coleção *c7* possuindo apenas a figurinha 1(repetida 3 vezes)
        # e *c8* possuindo apenas a figurinha 2(repetida 1 vez)
        # (apenas 1 deve ser trocada).

        >>> c7 = Colecao(20)
        >>> c8 = Colecao(20)
        >>> c7.insere(1)
        >>> c7.insere(1)
        >>> c7.insere(1)
        >>> c7.insere(1)
        >>> c8.insere(2)
        >>> c8.insere(2)
        >>> c7.colecao_sem_repeticao()
        '[1]'
        >>> c7.colecao_com_repeticao()
        '[1 (3)]'
        >>> c8.colecao_sem_repeticao()
        '[2]'
        >>> c8.colecao_com_repeticao()
        '[2 (1)]'
        >>> c7.troca_maxima(c8)
        >>> c7.colecao_sem_repeticao()
        '[1, 2]'
        >>> c7.colecao_com_repeticao()
        '[1 (2)]'
        >>> c8.colecao_sem_repeticao()
        '[1, 2]'
        >>> c8.colecao_com_repeticao()
        '[]'

        # Teste com a coleção *c9* e *c10* não possuindo figurinhas repetidas
        # (nada deve ser trocado).

        >>> c9 = Colecao(20)
        >>> c10 = Colecao(20)
        >>> for i in range(1, 8):
        ...     c9.insere(i)
        >>> for i in range(1, 10):
        ...     c10.insere(i)
        >>> c9.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7]'
        >>> c9.colecao_com_repeticao()
        '[]'
        >>> c10.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7, 8, 9]'
        >>> c10.colecao_com_repeticao()
        '[]'
        >>> c9.troca_maxima(c10)
        >>> c9.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7]'
        >>> c9.colecao_com_repeticao()
        '[]'
        >>> c10.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7, 8, 9]'

        # Teste com coleção *c11* e *c12* possuindo figurinhas repetidas que o outro
        já possui(nada deve ser trocado).

        >>> c11 = Colecao(20)
        >>> c12 = Colecao(20)
        >>> for i in range(1, 8):
        ...     c11.insere(i)
        >>> c11.insere(1)
        >>> c11.insere(4)
        >>> for i in range(1, 10):
        ...     c12.insere(i)
        >>> c12.insere(1)
        >>> c12.insere(3)
        >>> c11.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7]'
        >>> c11.colecao_com_repeticao()
        '[1 (1), 4 (1)]'
        >>> c12.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7, 8, 9]'
        >>> c12.colecao_com_repeticao()
        '[1 (1), 3 (1)]'
        >>> c11.troca_maxima(c12)
        >>> c11.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7]'
        >>> c11.colecao_com_repeticao()
        '[1 (1), 4 (1)]'
        >>> c12.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7, 8, 9]'
        >>> c12.colecao_com_repeticao()
        '[1 (1), 3 (1)]'

        # Teste com coleção *c13* e *c14* possuindo 3 figurinhas disponíveis para troca

        >>> c13 = Colecao(20)
        >>> c14 = Colecao(20)
        >>> c13.insere(3)
        >>> c13.insere(2)
        >>> c13.insere(1)
        >>> c13.insere(2)        
        >>> c13.insere(5)
        >>> c13.insere(1)
        >>> c13.insere(5)
        >>> c14.insere(4)
        >>> c14.insere(8)
        >>> c14.insere(4)
        >>> c14.insere(3)
        >>> c14.insere(8)
        >>> c14.insere(7)
        >>> c14.insere(4)
        >>> c14.insere(6)
        >>> c14.insere(7)
        >>> c14.insere(6)
        >>> c13.colecao_sem_repeticao()
        '[1, 2, 3, 5]'
        >>> c13.colecao_com_repeticao()
        '[1 (1), 2 (1), 5 (1)]'
        >>> c14.colecao_sem_repeticao()
        '[3, 4, 6, 7, 8]'
        >>> c14.colecao_com_repeticao()
        '[4 (2), 6 (1), 7 (1), 8 (1)]'
        >>> c13.troca_maxima(c14)
        >>> c13.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7]'
        >>> c13.colecao_com_repeticao()
        '[]'
        >>> c14.colecao_sem_repeticao()
        '[1, 2, 3, 4, 5, 6, 7, 8]'
        >>> c14.colecao_com_repeticao()
        '[4 (1), 8 (1)]'

        # Teste com álbum *c3* sendo diferente do álbum *c2*
        # (*c3* é um álbum com 20 figurinhas e *c2* com 10 figurinhas)

        >>> c3.troca_maxima(c2)
        Traceback (most recent call last):
        ...
        ValueError: Álbuns diferentes
        '''
        if self.ultima_figurinha != outra.ultima_figurinha:
            raise ValueError('Álbuns diferentes')

        # Cria 2 encadeamentos para armazenar as figurinhas
        # que podem ser trocadas entre as coleções
        # (inicializados com None)
        trocaveis_self = None
        trocaveis_outra = None

        atual_self = self.inicio
        atual_outra = outra.inicio

        # Armazena as figurinhas repetidas de *self* em *trocaveis_self*
        while atual_self is not None:
            if atual_self.prox is not None and atual_self.item == atual_self.prox.item and \
            not encontra_figurinha(trocaveis_self, atual_self.item) and \
            not encontra_figurinha(outra.inicio, atual_self.item):
                    if trocaveis_self is None:
                        trocaveis_self = No(atual_self.item, None)
                    else:
                        q = trocaveis_self
                        while q.prox is not None:
                            q = q.prox
                        q.prox = No(atual_self.prox.item, None)
            atual_self = atual_self.prox

        # Armazena as figurinhas repetidas de *outra* em *trocaveis_outra*
        while atual_outra is not None:
            if atual_outra.prox is not None and atual_outra.item == atual_outra.prox.item and \
            not encontra_figurinha(trocaveis_outra, atual_outra.item) and \
            not encontra_figurinha(self.inicio, atual_outra.item):
                    if trocaveis_outra is None:
                        trocaveis_outra = No(atual_outra.item, None)
                    else:
                        p = trocaveis_outra
                        while p.prox is not None:
                            p = p.prox
                        p.prox = No(atual_outra.prox.item, None)
            atual_outra = atual_outra.prox

        # Troca as figurinhas repetidas de *self* com as figurinhas repetidas de *outra*
        while trocaveis_self is not None and trocaveis_outra is not None:
            self.remove(trocaveis_self.item)
            outra.remove(trocaveis_outra.item)
            self.insere(trocaveis_outra.item)
            outra.insere(trocaveis_self.item)
            trocaveis_self = trocaveis_self.prox
            trocaveis_outra = trocaveis_outra.prox

# Função auxiliar para ordenar um encadeamento
def ordena_no(p: No | None):
    '''
    Recebe um nó *p* e o ordena crescentemente
    Exemplos
    >>> p = No(5, No(3, No(2, No(2, No(1, None)))))
    >>> ordena_no(p)
    >>> p
    No(item=1, prox=No(item=2, prox=No(item=2, prox=No(item=3, prox=No(item=5, prox=None)))))
    '''
    q = p
    while q is not None:
        r = q.prox
        while r is not None:
            if r.item < q.item:
                q.item, r.item = r.item, q.item
            r = r.prox
        q = q.prox

# Função auxiliar para verificar a existência de uma figurinha em um encadeamento
def encontra_figurinha(p: No | None, figurinha: int) -> bool:
    '''
    Recebe um nó *p* e uma *figurinha* e devolve True se a figurinha está no nó
    e False caso contrário.
    Exemplos
    >>> p = No(1, No(2, No(3, No(4, No(5, None)))))
    >>> encontra_figurinha(p, 1)
    True
    >>> encontra_figurinha(p, 2)
    True
    >>> encontra_figurinha(p, 6)
    False
    '''
    while p is not None:
        if p.item == figurinha:
            return True
        p = p.prox
    return False
