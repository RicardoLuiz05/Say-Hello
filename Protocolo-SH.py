import cliente

def login(tokens):
    usuario = tokens[1]
    senha = tokens[2]

# def password():
#     pass

def create():
    pass

def delete():
    pass

def join():
    pass

def chat():
    pass


while True:
    
    tokens = input("\nSH>>>").upper().split()
    print()
    command = tokens[0]

    if command == "LOGIN":
        login = login(tokens)
    # if command == "PASS":
    #     pass
    elif command == "CREATE":
        pass    
    elif command == "DELETE":
        pass
    elif command == "JOIN":
        pass
    elif command == "CHAT":
        pass
    elif command == "QUIT":
        break
    else:
        print("Digite um comando válido.")

print("\n---Encerramento do programa---")