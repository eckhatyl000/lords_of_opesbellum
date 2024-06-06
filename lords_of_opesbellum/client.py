import socket
import threading

# Network setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            # Handle received messages
        except:
            print("An error occurred!")
            client.close()
            break

thread = threading.Thread(target=receive_messages)
thread.start()

def send_message(msg):
    client.send(msg.encode('utf-8'))