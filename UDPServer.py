from socket import *
import time 

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

try:
    while True:
        message, clientAddress = serverSocket.recvfrom(2048000)

        message = message.decode()

        if "Lourival" in message:
            message = message + " claro que não"
        else :
            message = message + " talvez"

        modifiedMessage = message.upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        time.sleep(1)
except KeyboardInterrupt:
    print("Script interrompido pelo usuário.")
    # Adicione aqui qualquer código de limpeza necessário
    # ...
finally:
    print("Programa encerrado.")