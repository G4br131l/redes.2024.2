from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('O servidor está pronto')

while True:
    connectionSocket, addr = serverSocket.accept()

    if connectionSocket.recv(1024000).decode().find("mais") :
        sentence = connectionSocket.recv(1024000).decode() + " Lourival"
    else :
        sentence = connectionSocket.recv(1024000).decode() + " não sei"

    response = sentence.lower()

    connectionSocket.send(response.encode())
    connectionSocket.close()