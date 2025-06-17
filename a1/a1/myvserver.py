
from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 12000))
server.listen(1)
print("Server is listening...")

while True:
    conn, addr = server.accept()
    print("Connected from", addr[0])

    # Getting the message length for the first 2 bytes)
    length = int(conn.recv(2).decode())
    print("msg_len:", length)

    # Getting  the actual message
    message = ""
    while len(message) < length:
        message += conn.recv(64).decode()

    print("processed:", message)
    print("msg_len_sent:", len(message))

    # Send back capitalized message
    conn.send(message.upper().encode())

    conn.close()
    print("Connection closed\n")

