import socket
import threading
from threading import Thread, Semaphore
from style import style
#from main import protocolo

HOST = 'localhost'
PORT = 1500
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

print("\n--- Bem-vindo ao Say Hello! ---\n")

def connect():
    try:
        cliente.connect(dest)
        print(f'{style.GREEN}• Conectado\n{style.RESET}')
    except:
        print(f'{style.RED}• Não foi possiível conectar-se{style.RESET}\n')
    username = 'username '
    username += input('username: ')
    while len(username) == 'username ':
        print(f'{style.RED}Digite um username{style.RESET}\n')
        username += input('username: ')
    cliente.sendall(username.encode())

    # msg = cliente.recv(2048).decode()
    # print(msg)

    # threading.Thread(target=msg_servidor, args=(cliente, )).start()
     

def entrada():
    while True:
        entrada = input('\nSH >>> ')
        cliente.sendall(entrada.encode())
        codigo, servidor = cliente.recvfrom(2048)
        print(codigo.decode())


def msg_servidor(cliente):
    while True:
        msg = cliente.recv(2048).decode()
        if msg != '':
            username = msg.split("->")[0]
            print(msg.split('->'))
            content = msg.split("->")[1]
        print(f"[{username}] {content}")

connect()
entrada()

# Receber = threading.Thread(target=, args=())
# Enviar = threading.Thread(target=, args=())
# while True:
    
#     entrada = input("\nSH >>> ")
#     entrada_split = entrada.split()
#     comando = entrada_split[0].upper()
#     parametro = ''
#     for i in entrada_split[1:]:
#         parametro += f'{i} '
#     enter_user = f'{entrada}+{username}'
#     cliente.sendto(enter_user.encode(), dest)

#     # protocolo(username, cliente)

#     if comando == "CREATE":
#         codigo, servidor = cliente.recvfrom(2048)
#         print(codigo.decode())
      
#     elif comando == "DELETE":
#         codigo, servidor = cliente.recvfrom(2048)
#         print(codigo.decode())
      
#     elif comando == "JOIN":
#         codigo, servidor = cliente.recvfrom(2048)
#         if codigo.decode() == '200 +OK':
#             while True:
#                 msg = input()
#                 msg = msg.encode
#                 cliente.send(msg)
      
#     elif comando == "LEAVE":
#         if len(entrada) != 1:
#             print('\n400 -ERR este método não recebe parâmetros!')
#             continue
#             id_sala = None
#             print('\n200 +OK')

#     elif comando == 'CHATS':
#         out, servidor = cliente.recvfrom(2048)
#         out = out.decode().split('!')
#         if out[0] == '\n400 -ERR este método não recebe parâmetros!' or out[0] == '\n400 -ERR servidor ainda não possui chats!':
#             print(f'\n{out[0]}')
#         else:
#             print(f'\n{out[0]}')
#             print(out[1])

#     # elif comando == "MEMBERS":
#     #     if blockMutex == 0:
#     #         codigo, servidor = cliente.recvfrom(2048)
#     #         print(codigo.decode())

#     #     else:
#     #         print('\n400 -ERR você deve estar em um chat para usar este parâmetro!')
      
#     elif comando == "QUIT":
#         break

#     else:
#         print(f'''\nDigite um comando válido.
# {'='*30}
# CREATE → criar um chat
# DELETE → deletar um chat
# JOIN → entrar em um chat
# LEAVE → sair de um chat
# CHATS → imprime a árvore de chats
# MEMBERS → imprime a lista de pessoas em cada chat
# QUIT → encerra a conexão''')

# print("\n--- Obrigado por ter usado Say Hello! ---\n")