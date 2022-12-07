class ClassPreordem:
    def preordem(self, Node):
        if Node != None:
            print (f'{Node.data}, ', end='')
            self.preordem(Node.getLeftChild)
            self.preordem(Node.getRightChild)

class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None

    def __str__(self):
        return f'{self.carga}'


class ABB:
    def __init__(self, data='None'):
        self.__data = data
        self.__leftChild = None
        self.__rightChild = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, novo):
        self.__data = novo

    @property
    def getLeftChild(self):
        return self.__leftChild

    @getLeftChild.setter
    def insertLeft(self, novo):
        if self.__leftChild == None:
            self.__leftChild = novo

    @property
    def getRightChild(self):
        return self.__rightChild

    @getRightChild.setter
    def insertRight(self, novo):
        if self.__rightChild == None:
            self.__rightChild = novo
          
    def removeNo(self, chave:any)->any:
        if self.__raiz is None:
            return None
        if chave == self.__raiz.carga:
            if self.__raiz.esq is None and self.__raiz.dir is None:
                self.__raiz = None
                return None
            if self.__raiz.esq is None : 
                self.__raiz = self.__raiz.dir  
                return self.__raiz.carga
            elif self.__raiz.dir is None:
                self.__raiz = self.__raiz.esq
                return self.__raiz.carga             
        retorno = self.__removeNo(self.__raiz, chave)
        return retorno.carga
    
    # Dado um nó de uma BST e uma chave busca, este método
    # deleta o nó que contém a chave e devolve o novo nó raiz
    def __removeNo(self,node, chave):
        # Caso primário: não há raiz
        if node is None: 
            return None
  
        # Se a chave a ser deletada é menor do que a chave do nó raiz (da vez),
        # então a chave se encontra na subárvore esquerda
        if chave < node.carga:
            node.esq = self.__removeNo(node.esq,chave) 
  
        # Se a chave a ser deletada é maior do que a chave do nó raiz (da vez),
        # então a chave se encontra na subárvore esquerda
        elif(chave > node.carga):
            node.dir = self.__removeNo(node.dir, chave) 
  
        # Se a chave é igual à chave do nó raiz, então este é o nó 
        # a ser removido
        else:
            # (1) Nó com apenas 1 filho ou nenhum filho
            if node.esq is None : 
                temp = node.dir  
                node = None 
                return temp

            elif node.dir is None :
                temp = node.esq
                node = None
                return temp 
  
            # (2) Nó com dois filhos: obtem o sucessor inorder
            # (o menor nó da subárvore direita) 
            temp = self.__minValueNode(node.dir) 
  
            # copia o conteúdo do sucessor inorder para este nós
            node.carga = temp.carga
  
            # Deletao sucessor inorder
            node.dir = self.__removeNo(node.dir , temp.carga)

        return node

raiz = ABB('1')
raiz.insertLeft = ABB('2')
raiz.insertRight = ABB('3')

P1 = raiz.getLeftChild
P2 = raiz.getRightChild

P1.insertRight = ABB('4')

P2.insertLeft = ABB('5')
P2.insertRight = ABB('6')

arvore = ClassPreordem()
arvore.preordem(raiz)