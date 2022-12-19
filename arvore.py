class No:
    def __init__(self, nome):
        self.__id = hash(nome)
        self.__nome = nome
        self.__esq = None
        self.__dir = None

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def esq(self):
        return self.__esq

    @property
    def dir(self):
        return self.__dir

    @id.setter
    def id(self, novo_id:int):
        self.__id = novo_id

    @nome.setter
    def nome(self, novo_nome:str):
        self.__nome = novo_nome

    @esq.setter
    def esq(self, nova_esq):
        self.__esq = nova_esq

    @dir.setter
    def dir(self, nova_dir):
        self.__dir = nova_dir

    def __str__(self):
        return f'{self.nome}'


class ABB:
    def __init__(self, raiz=None):
        if raiz is None:
            self.__raiz = None
        else:
            self.__raiz = self.inserir_dado(raiz)

    @property
    def raiz(self) -> object:
        return self.__raiz

    def esta_vazia(self) -> bool:
        return self.__raiz == None

    def inserir(self, nome):
        if self.esta_vazia():
            self.__raiz = No(nome)
        else:
            self.__inserir(nome, self.raiz)

    def __inserir(self, nome, no):
        id = hash(nome)
        if id < no.id:
            if no.esq != None:
                self.__inserir(nome, no.esq)
            else:
                no.esq = No(nome)
        else:
            if no.dir != None:
                self.__inserir(nome, no.dir)
            else:
                no.dir = No(nome)

    def busca(self, id: int) -> any:
        return self.__busca(id, self.__raiz)

    def __busca(self, id, no: No) -> any:
        if no is None:
            return False
        if (id == no.id):
            return True
        elif (id < no.id and no.esq != None):
            return self.__busca(id, no.esq)
        elif (id > no.id and no.dir != None):
            return self.__busca(id, no.dir)
        else:
            return False

    def buscaList(self, id: int) -> any:
        return self.__buscaList(id, self.__raiz)
                                             
    def __buscaList(self, id, no: No) -> any:
        if no is None:
            return False
        if (id == no.id):
            return no.lista
        elif (id < no.id and no.esq != None):
            return self.__buscaList(id, no.esq)
        elif (id > no.id and no.dir != None):
            return self.__buscaList(id, no.dir)
        else:
            return False

    def remover(self, id):
        if self.__raiz is None:
            return None
        if id == self.__raiz.id:
            if self.__raiz.esq is None and self.__raiz.dir is None:
                self.__raiz = None
                return None
            if self.__raiz.esq is None : 
                self.__raiz = self.__raiz.dir  
                return self.__raiz.id
            elif self.__raiz.dir is None:
                self.__raiz = self.__raiz.esq
                return self.__raiz.id
        retorno = self.__remover(self.__raiz, id)
        return retorno.id

    def __remover(self, no, id):
        if no is None: 
            return None
        if id < no.id:
            no.esq = self.__remover(no.esq, id) 
        elif(id > no.id):
            no.dir = self.__remover(no.dir, id) 
        
    def preordem(self):
        return self.__preordem(self.__raiz)

    def __preordem(self, no):
        res = []
        if no:
            res.append(no.nome)
            res = res + self.__preordem(no.esq)
            res = res + self.__preordem(no.dir)
        return res
