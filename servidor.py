import socket

HOST = ''  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

print('Servidor no ar...')
while True:
    msg, cliente = udp.recvfrom(1024)  # quantidade de bytes que espera receber
    print('Recebi de ', cliente, msg.decode()) # decode = de bytes para string
udp.close()