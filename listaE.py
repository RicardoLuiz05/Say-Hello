class NodoLista:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class ListaEncadeada:
    def __init__(self, max:int):
        self.tamanho = 0
        self.max = max
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def inserir(self, novo_dado) -> any:
      if self.max > self.tamanho:
        novo_nodo = NodoLista(novo_dado)
        novo_nodo.proximo = lista.cabeca
        lista.cabeca = novo_nodo
        self.tamanho += 1
        return self.tamanho
        
      return 'O chat está cheio!!'

    def remover(self, valor):
      assert self.cabeca, "A lista está vazia!"
  
      if self.cabeca.dado == valor:
          self.cabeca = self.cabeca.proximo
        
      else:
          anterior = None
          corrente = self.cabeca
        
          while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo

          if corrente:
              anterior.proximo = corrente.proximo
            
          else:
              anterior.proximo = None
          self.tamanho -= 1
          return self.tamanho

lista = ListaEncadeada(5)
print("Lista vazia:", lista)

lista.inserir(5)
print("Lista contém um único elemento:", lista)
input()
lista.inserir(3)
print("Inserindo um novo elemento:", lista)
input()
lista.inserir(10)
print("Inserindo um novo elemento:", lista)
input()
lista.inserir(10)
print("Inserindo um novo elemento:", lista)
input()
lista.inserir(60)
print("Inserindo um novo elemento:", lista)
input()
print(lista.inserir(90))
input()

lista.remover(3)
print("\nRemovendo um novo elemento:", lista)
input()
lista.inserir(90)
print("Inserindo um novo elemento:", lista)