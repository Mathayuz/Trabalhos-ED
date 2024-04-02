from __future__ import annotations
from ed import array

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
    colecao: array[int]
    # A coleção funciona de maneira que possui a quantidade de figurinhas
    # total de cada figurinha
    # (a figurinha 1 está na posição 0, a figurinha 2 na posição 1, etc.)

    def __init__(self, ultima_figurinha: int):
        '''
        Cria uma nova coleção com capacidade para armazenar a *ultima_figurinha*
        do álbum de figurinhas(desconsiderando as repetidas).
        '''
        self.colecao = array(ultima_figurinha, 0)


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
        if figurinha < 1 or figurinha > len(self.colecao):
            raise ValueError('figurinha não faz parte do álbum')
        self.colecao[figurinha-1] += 1


    def remove(self, figurinha: int):
        '''
        Remove a *figurinha* da coleção de maneira que possa haver figurinha repetidas.
        Requer que a *figurinha* removida faça parte do álbum.
        Requer que a *figurinha* removida esteja na coleção(podendo ser única ou repetida).
        Exemplos
        >>> c = Colecao(10)
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
        if figurinha < 1 or figurinha > len(self.colecao):
            raise ValueError('figurinha não faz parte do álbum')
        if self.colecao[figurinha-1] == 0:
            raise ValueError('figurinha não está na coleção')
        self.colecao[figurinha-1] -= 1


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
        for i in range(len(self.colecao)):
            if self.colecao[i] > 0:
                if len(colecao) > 1:
                    colecao += ', '
                colecao += str(i+1)
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
        colecao = '['
        for i in range(len(self.colecao)):
            if self.colecao[i] > 1:
                if len(colecao) > 1:
                    colecao += ', '
                colecao += str(i+1) + ' (' + str(self.colecao[i]-1) + ')'
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

        >>> c3.troca_maxima(c2)
        Traceback (most recent call last):
        ...
        ValueError: Álbuns diferentes
        '''
        if len(self.colecao) != len(outra.colecao):
            raise ValueError('Álbuns diferentes')

        # Cria 2 arrays para armazenar as figurinhas que podem ser trocadas entre as coleções
        trocaveis_self = array(len(outra.colecao), 0)
        trocaveis_outra = array(len(self.colecao), 0)

        i = 0 # Indice da figurinha - 1
        j = 0 # Indice para troca_self
        k = 0 # Indice para troca_outra

        # Adiciona aos arrays as figurinhas trocáveis de cada coleção
        while i < len(self.colecao):
            # Coleção *self* sem a figurinha *i+1* e coleção *outra* com a figurinha *i+1 repetida*
            if self.colecao[i] == 0 and outra.colecao[i] > 1:
                trocaveis_outra[j] = i + 1
                j += 1
            # Coleção *self* com a figurinha *i+1* e coleção *outra* sem a figurinha *i+1 repetida*
            if self.colecao[i] > 1 and outra.colecao[i] == 0:
                trocaveis_self[k] = i + 1
                k += 1
            i += 1

        figurinha = 0
        # Realiza a troca das figurinhas entre as coleções
        while trocaveis_self[figurinha] > 0 and trocaveis_outra[figurinha] > 0:
            self.insere(trocaveis_outra[figurinha])
            self.remove(trocaveis_self[figurinha])
            outra.insere(trocaveis_self[figurinha])            
            outra.remove(trocaveis_outra[figurinha])
            figurinha += 1
