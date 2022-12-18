import socket
# from fila import Fila
from arvore import ABB
arvore = ABB()

HOST = 'localhost'
PORT = 1500
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

print("\n--- Bem-vindo ao Say Hello ---\n")

username = input('Username: ')
while len(username) < 1:
    print('Digite um username\n')
    username = input('Username: ')

blockMutex = 0

while True:
    
    entrada = input("\nSH >>> ")
    enter_user = f'{entrada}+{username}'
    udp.sendto(enter_user.encode(), dest)
    entrada = entrada.split()
    comando = entrada[0].upper()
  
    if comando == "CREATE":
        codigo_create, servidor = udp.recvfrom(2048)
        print(codigo_create.decode())
      
    elif comando == "DELETE":
        codigo_create, servidor = udp.recvfrom(2048)
        print(codigo_create.decode())
      
    elif comando == "JOIN":
        sala = ''
        for i in entrada[1:]:
            sala += f'{i} ' 
        if arvore.busca(hash(sala)):
            print('\n200 +OK')
            id_sala = hash(sala)
            blockMutex = 1
        else:
            print('\n400 -ERR chat não existente')

    elif comando == "LEAVE":
        if len(entrada) != 1:
            print('\n400 -ERR este método não recebe parâmetros')
            continue
        if blockMutex == 1:
            id_sala = None
            blockMutex = 0
            print('\n200 +OK')
        else:
            print('\n400 -ERR você não está em nenhum chat')
      
    elif comando == "MSG":
        msg = ''
        for i in entrada[1:]:
            msg += f'{i} '
        udp.sendto(msg.encode(), dest)

    elif comando == 'CHATS':
        if len(entrada) != 1:
            print('\n400 -ERR este método não recebe parâmetros')
            continue
        if arvore.raiz == None:
            print('\n400 -ERR servidor ainda não possui chats')
            continue
        print()
        print('200 +OK\n')
        arvore.preordem()
      
    elif comando == "QUIT":
        if blockMutex == 0:
            break
        else:
            print('\,400 -ERR você só pode usar esse comando quando sair do chat')

    else:
        print(f'''\nDigite um comando válido.
{'='*30}
CREATE → criar um chat
DELETE → deletar um chat
JOIN → entrar em um chat
LEAVE → sair de um chat
MSG → mandar mensagem no chat
CHATS → imprime a árvore de chats
MEMBERS → imprime a fila de pessoas em cada chat
QUIT → encerrar conexão''')

print("\n--- Obrigado por ter usado Say Hello ---\n")