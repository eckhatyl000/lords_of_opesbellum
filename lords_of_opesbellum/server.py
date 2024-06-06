import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen()

clients = []

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if not msg:
                break
            broadcast(msg, client)
        except:
            clients.remove(client)
            break

def broadcast(msg, current_client):
    for client in clients:
        if client != current_client:
            client.send(msg.encode('utf-8'))

while True:
    client, addr = server.accept()
    clients.append(client)
    print(f'Connected to {addr}')
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()