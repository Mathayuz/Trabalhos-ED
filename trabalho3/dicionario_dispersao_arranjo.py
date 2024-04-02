from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Item:
    '''
    Associacao entre chave e valor.
    '''
    chave: str
    valor: int

class Dicionario:
    '''
    Uma coleção de chaves únicas associadas com valores.

    Exemplos:

    >>> d = Dicionario()
    >>> d.num_itens()
    0
    >>> d.associa('Jorge', 25)
    >>> d.associa('Bia', 40)
    >>> d.num_itens()
    2
    >>> d.get('Jorge')
    25
    >>> d.get('Bia')
    40
    >>> d.get('Andre') is None
    True
    >>> d.associa('Bia', 50)
    >>> d.get('Bia')
    50
    >>> d.remove('Jorge')
    >>> d.get('Jorge') is None
    True
    >>> d.remove('Ana')
    >>> d.num_itens()
    1

    Testes

    O teste a seguir cria uma lista com uma permutação dos números de 0 a 99 e
    cria um dicionário adicionando cada número (string) como chave associada
    com o próprio número.

    Em seguida, para cada número da lista o get é executado para verificar se a
    associação está correta. Depois a associação é removida e todas as outras
    associações são verificadas.

    >>> import random
    >>> lst = list(range(100))
    >>> random.shuffle(lst)
    >>> d = Dicionario()
    >>> # Faz associação
    >>> for valor in lst:
    ...     d.associa(str(valor), valor)
    >>> for i in range(len(lst)):
    ...     # Associação original
    ...     assert d.get(str(i)) == i
    ...     # Modifica a associação e verifica
    ...     d.associa(str(i), 2 * i)
    ...     assert d.get(str(i)) == 2 * i
    ...     # Remove a associação e verifica
    ...     d.remove(str(i))
    ...     assert d.get(str(i)) is None
    ...     # As associações que não foram removidas permanecem as mesmas?
    ...     for j in range(i + 1, len(lst)):
    ...         assert d.get(str(j)) == j
    '''
    tabela: list[list[Item]]
    numero_elem: int

    def __init__(self) -> None:
        '''
        Cria um novo dicionário vazio.
        '''
        self.tabela = [[] for _ in range(10)]
        self.numero_elem = 0

    def _mapeia(self, chave: str) -> int:
        '''
        Devolve o índice da *chave* na tabela de dispersão.
        O mapeamento é feito usando o resto da função hash da chave dividida pelo tamanho da tabela.
        '''
        return hash(chave) % len(self.tabela)

    def num_itens(self) -> int:
        '''
        Devolve a quantidade de chaves no dicionário.
        '''
        return self.numero_elem
    
    def get(self, chave: str) -> int | None:
        '''
        Devolve o valor associado com *chave* no dicionário ou None se a chave
        não está no dicionário.
        '''
        i = self._mapeia(chave)
        if self.tabela[i] != []:
            for assoc in self.tabela[i]:
                if assoc.chave == chave:
                    return assoc.valor
        return None

    def associa(self, chave: str, valor: int):
        '''
        Associa a *chave* com o *valor* no dicionário. Se *chave* já está
        associada com um valor, ele é sustituído por *valor*.
        '''
        i = self._mapeia(chave)
        for j in self.tabela[i]:
            if j.chave == chave:
                j.valor = valor
                return # Garante que a chave não será adicionada novamente
        self.numero_elem += 1
        self.tabela[i].append(Item(chave, valor))
        self._redispersiona()

    def remove(self, chave: str):
        '''
        Remove a *chave* e o valor associado com ela do dicionário. Não faz
        nada se a *chave* não está no dicionário.
        '''
        i = self._mapeia(chave)
        j = 0
        while j < len(self.tabela[i]):
            if self.tabela[i][j].chave == chave:
                self.tabela[i].pop(j)
                self.numero_elem -= 1
                self._redispersiona()
                return
            j += 1

    def _fator_carga(self) -> float:
        '''
        Devolve o fator de carga da tabela de dispersão.
        '''
        return self.numero_elem / len(self.tabela)

    def _redispersiona(self):
        '''
        Redispersiona a tabela de dispersão. Caso a tabela atual tenha
        um fator de carga > 10, a tabela é redispersionada para o dobro do tamanho atual.
        Caso o fator de carga seja < 5 e o len(self.tabela > 10),
        a tabela é redispersionada para a metade do tamanho atual.

        Testes

        Os testes a seguir cria um dicionário e assim, associa e remove chaves
        para verificar se a redispersão está funcionando corretamente.
        
        >>> d = Dicionario()
        >>> assert len(d.tabela) == 10

        >>> for i in range(150):
        ...     d.associa(str(i), i)
        >>> assert len(d.tabela) == 20

        >>> for i in range(150, 201):
        ...     d.associa(str(i), i)
        >>> assert len(d.tabela) == 40

        >>> for i in range(150, 201):
        ...     d.remove(str(i))
        >>> assert len(d.tabela) == 20

        >>> for i in range(50, 150):
        ...     d.remove(str(i))
        >>> assert len(d.tabela) == 10
        '''
        if self._fator_carga() <= 10 and self._fator_carga() >= 5:
            return # Não precisa redispersar
        elif self._fator_carga() < 5 and len(self.tabela) > 10:
            nova_tabela = [[] for _ in range(len(self.tabela) // 2)]
        else: # self._fator_carga() > 10
            nova_tabela = [[] for _ in range(len(self.tabela) * 2)]
        for lista in self.tabela:
            for item in lista:
                i = hash(item.chave) % len(nova_tabela)
                nova_tabela[i].append(item)
        self.tabela = nova_tabela
    