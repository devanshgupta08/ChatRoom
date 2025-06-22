from cryptography.fernet import Fernet

# Pre-shared encryption key (use Fernet.generate_key() to create a new one)
KEY = b'2VljKXYN9qNAbz9P2dT4Xn3ml7tCegQCRia2CBtFV5k='

cipher = Fernet(KEY)

def encrypt_message(message: str) -> bytes:
    return cipher.encrypt(message.encode('utf-8'))

def decrypt_message(token: bytes) -> str:
    return cipher.decrypt(token).decode('utf-8')
