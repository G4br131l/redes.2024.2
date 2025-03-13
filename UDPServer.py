from socket import *

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048000)

    message = message.decode() + " Lourival"

    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
