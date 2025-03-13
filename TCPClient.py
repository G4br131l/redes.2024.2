from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input('Entre com uma string: ')

clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024000)

print('Resposta do servidor: ', modifiedSentence.decode())

clientSocket.close()