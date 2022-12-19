import socket

HOST = 'localhost'
PORT = 1500
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

print("\n--- Bem-vindo ao Say Hello ---\n")

username = input('Username: ')
udp.sendto(username.encode(), dest)
codigo, servidor = udp.recvfrom(2048)
print(codigo.decode())
while (len(username) < 1) and (codigo.decode() == 'Este nome já está sendo utilizado'):
    print('Digite um username\n')
    username = input('Username: ')
    udp.sendto(username.encode(), dest)
    codigo, servidor = udp.recvfrom(2048)
    print(codigo.decode())

blockMutex = 0

while True:
    
    entrada = input("\nSH >>> ")
    entrada = entrada.split()
    comando = entrada[0].upper()
  
    if comando == "CREATE":
        enter_user = f'{entrada}+{username}+{blockMutex}'
        udp.sendto(enter_user.encode(), dest) # mandou a entrada
        quantInput, servidor = udp.recvfrom(2048) # recebeu a mend=sagem de input
        quantInput = input(quantInput.decode()) # fez o input
        udp.sendto(quantInput.encode(), dest) # mandou para o servidor
        codigo, servidor = udp.recvfrom(2048) #recebeu o resultado
        print(codigo.decode())
      
    elif comando == "DELETE":
        enter_user = f'{entrada}+{username}+{blockMutex}'
        udp.sendto(enter_user.encode(), dest)
        codigo, servidor = udp.recvfrom(2048)
        print(codigo.decode())
      
    elif comando == "JOIN":
        blockMutex = 1
        enter_user = f'{entrada}+{username}+{blockMutex}'
        udp.sendto(enter_user.encode(), dest)
        codigo, servidor = udp.recvfrom(2048)
        if codigo.decode() == '200 +OK':
            while True:
                msg = input()
                msg = msg.encode
                udp.send(msg)
      
    elif comando == "LEAVE":
        if len(entrada) != 1:
            print('\n400 -ERR este método não recebe parâmetros!')
            continue
        if blockMutex == 1:
            id_sala = None
            blockMutex = 0
            print('\n200 +OK')
        else:
            print('\n400 -ERR você não está em nenhum chat!')

    elif comando == 'CHATS':
        out, servidor = udp.recvfrom(2048)
        out = out.decode().split('!')
        if out[0] == '\n400 -ERR este método não recebe parâmetros!' or out[0] == '\n400 -ERR servidor ainda não possui chats!':
            print(f'\n{out[0]}')
        else:
            print(f'\n{out[0]}')
            print(out[1])

    # elif comando == "MEMBERS":
    #     if blockMutex == 0:
    #         codigo, servidor = udp.recvfrom(2048)
    #         print(codigo.decode())

    #     else:
    #         print('\n400 -ERR você deve estar em um chat para usar este parâmetro!')
      
    elif comando == "QUIT":
        if blockMutex == 0:
            break
        else:
            print('\,400 -ERR você só pode usar esse comando quando sair do chat atual!')

    else:
        print(f'''\nDigite um comando válido.
{'='*30}
CREATE → criar um chat
DELETE → deletar um chat
JOIN → entrar em um chat
LEAVE → sair de um chat
CHATS → imprime a árvore de chats
MEMBERS → imprime a lista de pessoas em cada chat
QUIT → encerra a conexão''')

print("\n--- Obrigado por ter usado Say Hello! ---\n")
