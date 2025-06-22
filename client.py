import socket
import threading
from crypto_utils import encrypt_message, decrypt_message

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            encrypted_msg = client.recv(4096)
            msg = decrypt_message(encrypted_msg)
            print(msg)
        except:
            break

def send_messages():
    while True:
        msg = input()
        client.send(encrypt_message(msg))
        if msg.lower() == "quit":
            break


prompt = decrypt_message(client.recv(1024))
print(prompt)
username = input()
client.send(encrypt_message(username))

threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
