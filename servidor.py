import threading
import socket
from arvore import ABB
from lista import Lista

arvore = ABB()
lista = Lista()
lista.insere_no_inicio('Pessoas online\n')
# sala = threading.Semaphore(1)

HOST = 'localhost'
PORT = 1500
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    RESET = '\033[0m'

print(f"{' '*10}Acorde! \n-- Say Hello está no ar! --\n\n")

blockMutex = 0

while True:

    usuario, cliente = udp.recvfrom(2048)
    usuario = usuario.decode()
    if lista.buscar(usuario):
        codigo = 'Este nome já está sendo utilizado'
    else:
        lista.inserir(lista.cabeca, usuario)
        codigo = f'{style.BLUE}• Conectando no Protocolo{style.RESET}'
    udp.sendto(codigo.encode(), cliente)


    enter_user, cliente = udp.recvfrom(2048)
    enter_user = enter_user.decode().split('+')
    entrada = enter_user[0].split()
    comando = entrada[0].upper()
    usuario = enter_user[1]
    blockMutex = enter_user[2]


    if comando == 'CREATE':
        if blockMutex == 0:
            quantInput = 'Quantidade máxima de pessoas no chat: '
            udp.sendto(quantInput.encode(), cliente)
            quantInput, cliente = udp.recvfrom(2048)
            try:
                quantInput = int(quantInput.decode())
            except:
                codigo = f'{style.RED}400 -ERR quantidade deve ser um número inteiro{style.RESET}'
                udp.sendto(codigo.encode(), cliente)
                continue
            nome = ''
            for i in entrada[1:-1]:
                nome += f'{i} '
            if arvore.busca(hash(nome)):
                codigo = f'{style.RED}400 -ERR chat já existente!{style.RESET}'
            else:
                arvore.inserir(nome)
                print(f'{style.BLUE}{usuario} criou o chat: {nome}\n{style.RESET}')
                codigo = f'{style.GREEN}200 +OK sala criada com sucesso!{style.RESET}'
        else:
            codigo = f'{style.RED}\n400 -ERR você só pode usar esse comando quando sair do chat atual!{style.RESET}'
        udp.sendto(codigo.encode(), cliente)


    elif comando == 'DELETE':
        if len(entrada) == 1:
            codigo = f'{style.RED}400 -ERR este método recebe parâmetros!{style.RESET}'
        else:
            nome = ''
            for i in entrada[1:]:
                nome += f'{i} '
            if blockMutex == 0:
                if arvore.busca(hash(nome)):
                    arvore.remover(hash(nome))
                    print(f'{style.BLUE}{usuario} removeu o chat: {nome}\n{style.RESET}')
                    codigo = f'{style.GREEN}200 +OK sala removida com sucesso!{style.RESET}'
                else:
                    codigo = f'{style.RED}400 -ERR este chat não existe!{style.RESET}'
            else:
                codigo = f'{style.RED}\n400 -ERR você só pode usar esse comando quando sair do chat!{style.RESET}'
        udp.sendto(codigo.encode(), cliente)


    elif comando == "JOIN":
        if len(entrada) == 1:
            codigo = f'{style.RED}400 -ERR este método recebe parâmetros!{style.RESET}'
        else:
            nome = ''
            for i in entrada[1:]:
                nome += f'{i} '
            if arvore.busca(hash(nome)):
                lista.remover(usuario)
                lista.inserir(lista.cabeca, usuario, hash(nome))
                codigo = f'{style.GREEN}200 +OK{style.RESET}'
            else:
                codigo = f'{style.RED}400 -ERR esta sala não existe!{style.RESET}'
        udp.sendto(codigo.encode(), cliente)
        msg = udp.recv(4096)
        msg = f'{usuario}: {msg.decode()}'
        cursor = lista.cabeca
        while cursor:
            if cursor.chat == hash(nome):
                udp.send(msg.encode())
            cursor = cursor.prox

    elif comando == 'CHATS':
        if len(entrada) != 1:
            codigo = f'{style.RED}\n400 -ERR este método não recebe parâmetros!{style.RESET}'
        elif arvore.raiz == None:
            codigo = f'{style.RED}\n400 -ERR servidor ainda não possui chats!{style.RESET}'
        codigo = f'{style.GREEN}200 +OK\n{style.RESET}'
        preordem = ''
        for i in (arvore.preordem()):
            preordem += f'• {i}\n'
        out = f'{codigo}!{preordem}'
        udp.sendto(out.encode(), cliente)


    # elif comando == 'MEMBERS':
    #     if blockMutex == 0:
    #         if len(entrada) == 1:
    #             codigo = '400 -ERR este método recebe parâmetros!'
    #         else:
    #             nome = ''
    #             for i in entrada[1:]:
    #                 nome += f'{i} '
    #             arvore.busca(hash(nome))
    #     else:
    #         codigo = '\n400 -ERR você só pode usar esse comando quando sair do chat!'
    #     udp.sendto(codigo.encode(), cliente)
