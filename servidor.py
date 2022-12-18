import socket
from arvore import ABB
arvore = ABB()

HOST = 'localhost'
PORT = 1500
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

print(f"{' '*10}Acorde! \n-- Say Hello está no ar! --\n\n")

blockMutex = 0

while True:
  
    enter_user, cliente = udp.recvfrom(2048)
    enter_user = enter_user.decode().split('+')
    entrada = enter_user[0].split()
    comando = entrada[0].upper()
    usuario = enter_user[1]
  
    if comando == 'CREATE':
        nome = ''
        for i in entrada[1:]:
            nome += f'{i} '
        if blockMutex == 0:
            arvore.inserir(nome)
            print(f'{usuario} criou o chat: {nome}\n')
            codigo = '200 +OK sala criada com sucesso'
        else:
            codigo = '\n400 -ERR você só pode usar esse comando quando sair do chat'
        udp.sendto(codigo.encode(), cliente)

    elif comando == 'DELETE':
        nome = ''
        for i in entrada[1:]:
            nome += f'{i} '
        if blockMutex == 0:
            valor = hash(nome)
            arvore.remover(valor)
            print(f'{usuario} removeu o chat: {nome}\n')
            codigo = '200 +OK sala removida com sucesso'
        else:
            codigo = '\n400 -ERR você só pode usar esse comando quando sair do chat'
        udp.sendto(codigo.encode(), cliente)

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