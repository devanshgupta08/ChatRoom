import socket
import threading
from crypto_utils import encrypt_message, decrypt_message

HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = {}

def handle_client(client):
    while True:
        try:
            encrypted_msg = client.recv(4096)
            msg = decrypt_message(encrypted_msg)

            if msg.lower() == "quit":
                break

            full_msg = f"{usernames[client]}: {msg}"
            print(full_msg)
            broadcast(encrypt_message(full_msg), client)

        except:
            break

    clients.remove(client)
    broadcast(encrypt_message(f"{usernames[client]} has left the chat."), client)
    del usernames[client]
    client.close()

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def receive_connections():
    print(f"Encrypted Chat Server running on {HOST}:{PORT}")
    while True:
        client, _ = server.accept()
        client.send(encrypt_message("Enter your username: "))
        username = decrypt_message(client.recv(1024))
        usernames[client] = username
        clients.append(client)
        print(f"{username} connected.")
        broadcast(encrypt_message(f"{username} has joined the chat."), client)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()
