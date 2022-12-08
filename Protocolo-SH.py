import socket
from arvore import ArvoreBinaria
import getpass
ABB = ArvoreBinaria()

HOST = ''  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor está
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

def login(tokens):
    # usuario = tokens[1]
    # senha = tokens[2
  pass

def join(tokens, ABB):
    sala = tokens[1]
    valor = hash(sala)
    return ABB.busca(valor)

def create(tokens, ABB):
    nome = tokens[1]
    valor = hash(nome)
    ABB.add(valor)
    return True

def delete(tokens, ABB):
    sala = tokens[1]
    valor = hash(sala)
    ABB.removeNo(valor)

def mensagem():
    pass


while True:
    
    tokens = input("\nSH >>> ").split()
    print()
    command = tokens[0].upper()

    if command == "LOGIN":
        usuario = input('user: ')
        senha = getpass.getpass("senha: ")
        # login = login(tokens)
      
    elif command == "JOIN":
       if join(tokens, ABB):
         print('Você entrou na sala')
       else:
         print(f'Sinto muito, meu nobre. Mas a sala "{tokens[1]}" não existe!')
         #Parametro pela metade
      
    elif command == "CREATE":
      if create(tokens, ABB):
        print(f'Sala "{tokens[1]}" criada com sucesso!')
      
      
    elif command == "DELETE":
        delete(tokens, ABB)
        print(f'Sala "{tokens[1]}" removida')
      
    elif command == "MSG":
        msg = ''
        for i in tokens[1:]:
            msg += f'{i} '
        print(f'mensagem: {msg}')
        udp.sendto(msg.encode(), dest)
        
      
    elif command == "QUIT":
        print('Até mais </3')
        break
      
    else:
        print(f'''Digite um comando válido.
{'='*30}
LOGIN → entrar na sua conta
JOIN → entrar em um chat
CREATE → criar um chat
DELETE → deletar um chat
MSG → mandar mensagem no chat
QUIT → encerrar conexão''')

print("\n---Obrigado por ter usado Say Hello---")