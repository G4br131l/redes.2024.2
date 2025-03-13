from socket import *
import time

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('O servidor está pronto')

try:
    while True:
        connectionSocket, addr = serverSocket.accept()

        sentence = connectionSocket.recv(1024000).decode()

        existe = sentence.find("mais")

        if existe != -1:
            sentence = sentence + " Lourival"
        else :
            sentence = sentence + " não sei"

        response = sentence.lower()

        connectionSocket.send(response.encode())
        connectionSocket.close()
        time.sleep(1)
except KeyboardInterrupt:
    print("Script interrompido pelo usuário.")
    # Adicione aqui qualquer código de limpeza necessário
    # ...
finally:
    print("Programa encerrado.")