class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class No:
    def __init__(self, user):
        self.__user = user
        self.__prox = None

    @property
    def user(self):
        return self.__user

    @property
    def prox(self):
        return self.__prox

    # @property
    # def chat(self):
    #     return self.__chat

    @user.setter
    def user(self, novo_user:str):
        self.__user = novo_user

    @prox.setter
    def prox(self, novo_prox:str):
        self.__prox = novo_prox

    # @chat.setter
    # def chat(self, chat):
    #     self.__chat = chat

    def __str__(self):
        return str(self.user)


class Lista:
    def __init__(self):
        self.__cabeca = None
        self.__tamanho = 0

    @property
    def cabeca(self):
        return self.__cabeca

    @property
    def tamanho(self):
        return self.__tamanho

    @cabeca.setter
    def cabeca(self, n_cabeca):
        self.__cabeca = n_cabeca

    @tamanho.setter
    def tamanho(self, n_tamanho):
        self.__tamanho = n_tamanho

    def insere_no_inicio(self, id):
        novo_no = No(id)
        novo_no.prox = self.cabeca
        self.cabeca = novo_no
        self.tamanho += 1

    def inserir(self, no_anterior, user):
        novo_no = No(user)
        novo_no.prox = no_anterior.prox
        no_anterior.prox = novo_no
        self.tamanho += 1

    def buscar(self, valor):
        cursor = self.cabeca
        while cursor and (cursor.user != valor):
            cursor = cursor.prox
        return cursor

    def remover(self, valor):
        if self.cabeca.user == valor:
            self.cabeca = self.cabeca.prox
        else:
            anterior = None
            cursor = self.cabeca
            while cursor and (cursor.user != valor):
                anterior = cursor
                cursor = cursor.prox
            if cursor:
                anterior.prox = cursor.prox
            else:
                anterior.prox = None
        self.tamanho -= 1

    def __str__(self) -> str:
        cursor = self.cabeca
        str = ''
        while cursor:
            str += f'• {cursor.user}\n'
            cursor = cursor.prox
        return str

# l = Lista()
# l.insere_no_inicio(10000)
# l.inserir(l.cabeca, 50)
# l.inserir(l.cabeca, 100)
# print(l)