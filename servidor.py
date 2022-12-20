import socket
import threading
from threading import Thread, Semaphore
import time
from arvore import ABB
from lista import Lista
from style import style

HOST = 'localhost'
PORT = 1500
limite = 50
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

arvore = ABB()
lista = Lista()
lista.insere_no_inicio('Pessoas online\n')
semaforoA = Semaphore(1)
semaforoL = Semaphore(1)

print(f"{' '*2}Sorria e Acene! \n--- Say Hello! ---\n\n")

def protocolo(address, cliente, entrada):
    while True:
        # entrada, address = udp.recvfrom(2048)
        # entrada = str(entrada)
        # entrada = entrada[2:-1]
        # # entrada, cliente = udp.recvfrom(2048)
        # # entrada = entrada.decode()
        # try:
        #     entrada = entrada.split()
        # except:
        #     pass
        # comando = entrada[0].upper()
        entrada = str(entrada)
        entrada = entrada.split()
        comando = entrada[0].upper()
    
        if comando == 'CREATE':
            entrada = entrada[1:]
            nome = ''
            for i in entrada:
                nome += f'{i} '
            if arvore.busca(hash(nome)):
                codigo = f'{style.RED}400 -ERR chat já existente!{style.RESET}'
            else:
                semaforoA.acquire()
                arvore.inserir(nome)
                semaforoA.release()
                time.sleep(0.5)
                print(f'{style.BLUE}{cliente} criou o chat: {nome}\n{style.RESET}')
                codigo = f'{style.GREEN}200 +OK sala criada com sucesso!{style.RESET}'
            udp.sendto(codigo.encode(), address)
            # print('B')
    
    
        elif comando == 'DELETE':
            if len(entrada) == 1:
                codigo = f'{style.RED}400 -ERR este método recebe parâmetros!{style.RESET}'
            else:
                nome = ''
                for i in entrada[1:]:
                    nome += f'{i} '
                if arvore.busca(hash(nome)):
                    semaforoA.acquire()
                    arvore.remover(hash(nome))
                    semaforoA.release()
                    print(f'{style.BLUE}{cliente} removeu o chat: {nome}\n{style.RESET}')
                    time.sleep(1)
                    codigo = f'{style.GREEN}200 +OK sala removida com sucesso!{style.RESET}'
                else:
                    codigo = f'{style.RED}400 -ERR este chat não existe!{style.RESET}'
            udp.sendto(codigo.encode(), cliente)
    
    
        elif comando == "JOIN":
            if len(entrada) == 1:
                codigo = f'{style.RED}400 -ERR este método recebe parâmetros!{style.RESET}'
            else:
                nome = ''
                for i in entrada[1:]:
                    nome += f'{i} '
                if arvore.busca(hash(nome)):
                    semaforoL.acquire()
                    lista.remover(cliente)
                    lista.inserir(lista.cabeca, cliente)
                    semaforoL.release()
                    time.sleep(1)
                    codigo = f'{style.GREEN}200 +OK{style.RESET}'
                else:
                    codigo = f'{style.RED}400 -ERR esta sala não existe!{style.RESET}'
            udp.sendto(codigo.encode(), cliente)
            msg = udp.recv(4096)
            msg = f'{cliente}: {msg.decode()}'
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

        # print('b')
    
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

def mensagem_unicast(cliente, msg):
    udp.sendto(msg.encode(), cliente)

def mensagem_broadcast(msg):
    for user in lista:
        mensagem_unicast(user, msg)

def adm_cliente(address, cliente):
    lista.inserir(lista.cabeca, address)
    cliente = str(cliente)
    cliente = cliente[2:-1]
    clienteN = cliente.split()
    if clienteN[0] == 'username':
        username = clienteN[1]
        print(f'{style.BLUE}Cliente {username} conectado{style.RESET}\n')
    # threading.Thread(target=protocolo, args=(address, username, cliente, )).start()
    print('a')
    protocolo(address, username, cliente)


def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        servidor.bind((HOST, PORT))
    except:
        pass
    while True:
        cliente, address = udp.recvfrom(2048)
        threading.Thread(target=adm_cliente, args=(address, cliente, )).start()
        # thread = threading.Thread(target=adm_cliente, args=(cliente, ))
        # thread.start()


if __name__ == '__main__':
    main()