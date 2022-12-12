import threading
from time import sleep
import socket

HOST = '10.0.4.73'
PORT = 42000
servidor = (HOST, PORT)
udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp.bind(servidor)

print('== Servidor ==')


def receber():
    while True:
        msg, cliente = udp.recvfrom(1024)
        print('cliente', cliente, 'enviou:', msg.decode())


t_recebimento = threading.Thread(target=receber)
t_recebimento.start()

while True:
    sleep(3)
    print('server')