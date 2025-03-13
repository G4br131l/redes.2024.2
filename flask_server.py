from flask import Flask, request, jsonify
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app)

# Function to send UDP request
def send_udp(message):
    host = '127.0.0.1'
    port = 12001

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(message.encode(), (host, port))
    data, _ = udp_socket.recvfrom(2048000)
    udp_socket.close()
    return data.decode()

# Function to send TCP request
def send_tcp(message):
    host = '127.0.0.1'
    port = 12000

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((host, port))
    tcp_socket.send(message.encode())
    data = tcp_socket.recv(1024)
    tcp_socket.close()
    return data.decode()

@app.route('/udp', methods=['POST'])
def handle_udp():
    print("REQUISIÇÃO UDP")
    message = request.json.get('message')
    print("MENSAGEM: " + message)
    response = send_udp(message)
    print("MENSAGEM TRANFORMADA: " + response)
    print("RESPOSTA ENVIADA!")
    return jsonify({'response': response})

@app.route('/tcp', methods=['POST'])
def handle_tcp():
    print("REQUISIÇÃO TCP")
    message = request.json.get('message')
    print("MENSAGEM: " + message)
    response = send_tcp(message)
    print("MENSAGEM TRANFORMADA: " + response)
    print("RESPOSTA ENVIADA!")
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5000)