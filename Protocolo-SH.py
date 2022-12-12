import socket
from fila import Fila
from arvore import ArvoreBinaria
ABB = ArvoreBinaria()


# Parte do cliente
HOST = '10.0.4.73'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

# def login(entrada):
#   nome = input('user: ')
#   return nome
  
def join(nome, ABB):
    pass
    # sala = nome
    # valor = hash(sala)
    # pessoas = ABB.busca(valor).split()
    # limite = pessoas[1]
    
    # return ABB.busca(valor)

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

blockMutex = 0

while True:
    
    entrada = input("\nSH >>> ").split()
    # print()
    comando = entrada[0].upper()

    if comando == "LOGIN":
        if blockMutex == 0:
            if comando[1]:
                print('\nEste método não recebe parâmetros')
                continue
            # login(entrada)
            nome = input('user: ')
        else:
            print('Você só pode usar esse comando quando sair do chat')
      
    elif comando == "JOIN":
        blockMutex = 1
        print('entrou')
        # if join(entrada[1], ABB):
        #     print(f'Você entrou na sala "{entrada[1]}"')
        # else:
        #     print(f'Mil perdões, brotinho. Mas a sala "{entrada[1]}" não existe!')
            #Parametro pela metade

    elif comando == "LEAVE":
        if blockMutex == 1:
            blockMutex = 0
        else:
            pass
      
    elif comando == "CREATE":
        if blockMutex == 0:
            num = int(input('Limite de pessoas: '))
            print()
            pessoas = Fila(num)
            
            create(entrada, ABB, num)
            print(f'Sala "{entrada[1]}" criada com sucesso!')
        else:
            print('Você só pode usar esse comando quando sair do chat')
      
    elif comando == "DELETE":
        if blockMutex == 0:
            delete(entrada, ABB)
            print(f'Sala "{entrada[1]}" removida')
        else:
            print('Você só pode usar esse comando quando sair do chat')
      
    elif comando == "MSG":
        # mensagem()
        msg = ''
        for i in entrada[1:]:
            msg += f'{i} '
        # print(f'mensagem: {msg}')
        udp.sendto(msg.encode(), dest)
      
    elif comando == "QUIT":
        if blockMutex == 0:
            print('\nAté mais!')
            break
        else:
            print('Você só pode usar esse comando quando sair do chat')
      
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