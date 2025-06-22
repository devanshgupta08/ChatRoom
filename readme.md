
````markdown
# 🔐 Encrypted TCP Chat Application

A simple multi-client chat system built in Python using sockets and threading, with end-to-end encryption using the `cryptography` library. This project simulates a **TLS-like secure communication** channel over TCP/IP and allows multiple users to chat with real-time encrypted messaging.

---

## 📌 Features

- ✅ Multi-client chat support using **TCP socket programming**
- ✅ **Username-based message formatting**: `username: message`
- ✅ **AES symmetric encryption** with a pre-shared key using `cryptography` (simulating TLS)
- ✅ Real-time communication using **multithreading**
- ✅ Graceful disconnection with `quit` command

---

## 🧠 Technologies Used

- **Python 3**
- `socket` – for TCP/IP communication  
- `threading` – to handle multiple clients concurrently  
- `cryptography` – for AES-based encryption  
- Basic concepts of **networking**, **encryption**, and **secure message transmission**

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/encrypted-tcp-chat.git
cd encrypted-tcp-chat
````

### 2. Install dependencies

```bash
pip install cryptography
```

### 3. Run the Server

```bash
python server.py
```

### 4. Run the Client (in a new terminal)

```bash
python client.py
```

You can open multiple terminals and run `client.py` in each to simulate multiple users.

---

## 🔑 Encryption Key

A pre-generated symmetric AES key is stored in `crypto_utils.py`:

```python
KEY = b'YOUR_GENERATED_KEY_HERE'
```

> You can generate a new key using:

```python
from cryptography.fernet import Fernet
print(Fernet.generate_key())
```

Ensure the same key is shared across both client and server files.

---

## 💡 Sample Usage

```
Enter your username: Alice
Bob: Hi everyone!
Alice: Hello Bob!
```

Type `quit` to leave the chat.

---

## 📄 File Structure

```
.
├── server.py           # Chat server
├── client.py           # Chat client
└── crypto_utils.py     # AES encryption/decryption helper
```

---

## 🛡️ Learning Objectives

* Understand basics of **network protocols (TCP/IP)**
* Learn how to build **real-time encrypted communication systems**
* Apply **threading** for handling concurrency
* Simulate key concepts from **TLS, VPN, and firewall logic**

---

## ✍️ Author

**Devansh Gupta**
[Portfolio](https://portfolio-lilac-ten-82.vercel.app) | [GitHub](https://github.com/devanshgupta08) | [LinkedIn](https://www.linkedin.com/in/devansh-gupta-236bb7257)

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

```