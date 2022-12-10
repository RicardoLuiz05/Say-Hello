class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
      
class Fila:
    def __init__(self, tamanho):
        self.__frente = 0
        self.__final  = -1
        self.__tamanho = tamanho
        self.__ocupados = 0
        self.__dados = [None for i in range(tamanho)]

    def estaVazia(self) -> bool:
        return self.__ocupados == 0

    def estaCheia(self)->bool:
        return self.__ocupados == self.__tamanho


    def tamanho(self)->int:
        return self.__ocupados

    def __len__(self)->int:
        return self.__ocupados

    def elemento(self, posicao:int) -> any:
        try:
            assert posicao > 0 and posicao <= self.__ocupados
            inicio = self.__frente
            for i in range(posicao-1):

                inicio = (inicio + 1) % self.__tamanho

            return self.__dados[inicio]
        except AssertionError:
            raise FilaException(f'Posicao inválida para a fila atual com {self.__ocupados} elementos')
    
    def busca(self, chave:any)->int:
        inicio = self.__frente
        count = 0
        for i in range(self.__ocupados):
            count += 1
            if self.__dados[inicio] == chave:
                return count

            inicio = (inicio + 1) % self.__tamanho

        raise FilaException(f'A chave {chave} não está na Fila.')


    def enfileira(self, conteudo:any):
        if self.estaCheia():
            raise FilaException(f'Fila cheia. Não é possivel a inserção')

        self.__final = (self.__final + 1) % self.__tamanho
        self.__dados[self.__final] = conteudo
        self.__ocupados += 1

    def desenfileira(self)->any:
        if self.estaVazia():
            raise FilaException(f'Fila vazia. Não é possivel a remocao')

        carga = self.__dados[self.__frente]
        self.__frente = (self.__frente + 1) % self.__tamanho
        self.__ocupados -= 1


    def __str__(self):
        s = '[ '

        inicio = self.__frente
        for i in range(self.__ocupados):
            s += f'{self.__dados[inicio]} '
            inicio = (inicio + 1) % self.__ocupados

        s += ']'
        return s


    def esvazia(self):
        self.__ocupados = 0
        self.__frente = 0
        self.__final = -1
        '''
        while(not self.estaVazia()):
            self.desenfileira()
        '''