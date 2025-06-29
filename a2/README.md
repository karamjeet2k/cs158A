# Assignment 2 – Multi-Client Chat Application (CS158A)

This project demonstrates a multi-client chat system using Python's socket and threading modules. The server handles multiple clients simultaneously, and each client can send and receive messages in real time.

---

## 📁 Files in a2 directory

- mychatserver.py – the chat server that listens for and handles multiple clients
- mychatclient.py – the client application that connects to the server
- README.md – instructions for running the programs with sample output

---

## ▶️ How to Run the Programs

### 💻 Step 1: Run the Server

Open **one terminal** and navigate to the a2 directory. Then run:

cmd
python mychatserver.py
you should able to see
server listening at 127.0.0.1:15000
New connection from ('127.0.0.1', 52677)
52677: hi
52677: how are you doing
running the client
python mychatclient.py
connected to server, type 'exit' to quit
Your name is: 52677
---------------------------------------------
hi

how are you doing

exit
Disconnected from server
![image](https://github.com/user-attachments/assets/a9e72bf2-bf9e-4645-8147-5a9362a219e5)



