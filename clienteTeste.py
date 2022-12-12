from time import sleep
import socket

HOST = '10.0.4.73'
PORT = 42000
servidor = (HOST, PORT)
udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

num = 0
print('== Cliente ==')
while True:
    print('enviando', num)
    udp.sendto(str(num).encode(), servidor)
    num += 1
    sleep(2)