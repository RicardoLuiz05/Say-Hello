import socket
from fila import Fila
from arvore import ArvoreBinaria
ABB = ArvoreBinaria()


# Parte do cliente
HOST = ''  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

# def login(entrada):
#   nome = input('user: ')
#   return nome
  
def join(entrada, ABB):
    sala = entrada[1]
    valor = hash(sala)
    pessoas = ABB.busca(valor).split()
    limite = pessoas[1]
    
    
    return ABB.busca(valor)

def create(entrada, ABB, num):
    nome = hash(entrada[1])
    pessoas = Fila(num)
    valor = [nome, num]
    ABB.creator(valor)

def delete(entrada, ABB):
    sala = entrada[1]
    valor = hash(sala)
    ABB.removeNo(valor)

# def mensagem():
#     msg = ''
#     for i in entrada[1:]:
#         msg += f'{i} '
#     print(f'mensagem: {msg}')
#     udp.sendto(msg, dest)


while True:
    
    entrada = input("\nSH >>> ").split()
    # print()
    comando = entrada[0].upper()

    if comando == "LOGIN":
        if comando[1]:
            print('\nEste método não recebe parâmetros')
            continue
        # login(entrada)
        nome = input('user: ')
        # class login:
        #     def __init__(self, nome):
        #         self.nome = nome
            
        #     def __str__(self):
        #         return f'{self.nome}'

        # usuario = login(nome)
      
    elif comando == "JOIN":
        if join(entrada, ABB):
            print(f'Você entrou na sala "{entrada[1]}"')
        else:
            print(f'Mil perdões, brotinho. Mas a sala "{entrada[1]}" não existe!')
            #Parametro pela metade

    elif comando == "LEAVE":
        pass
      
    elif comando == "CREATE":
        num = int(input('Limite de pessoas: '))
        print()
        pessoas = Fila(num)
        
        create(entrada, ABB, num)
        print(f'Sala "{entrada[1]}" criada com sucesso!')
      
    elif comando == "DELETE":
        delete(entrada, ABB)
        print(f'Sala "{entrada[1]}" removida')
      
    elif comando == "MSG":
        # mensagem()
        msg = ''
        for i in entrada[1:]:
            msg += f'{i} '
        # print(f'mensagem: {msg}')
        udp.sendto(msg.encode(), dest)
      
    elif comando == "QUIT":
        print('\nAté mais!')
        break
      
    else:
        print(f'''\nDigite um comando válido.
{'='*30}
LOGIN → definir seu username
JOIN → entrar em um chat
LEAVE → sair de um chat
CREATE → criar um chat
DELETE → deletar um chat
MSG → mandar mensagem no chat
QUIT → encerrar conexão''')

print("\n--- Obrigado por ter usado Say Hello ---\n")