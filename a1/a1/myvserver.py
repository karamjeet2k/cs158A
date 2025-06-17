
from socket import *

def start_server():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('localhost', 12000))
    server.listen(1)
    print("Server is listening...")
    return server

def handle_client(conn):
    length = int(conn.recv(2).decode())
    print("msg_len:", length)
    
    message = ""
    while len(message) < length:
        message += conn.recv(64).decode()

    print("processed:", message)
    print("msg_len_sent:", len(message))

    conn.send(message.upper().encode())
    conn.close()
    print("Connection closed\n")

def main():
    server = start_server()
    while True:
        conn, addr = server.accept()
        print("Connected from", addr[0])
        handle_client(conn)

if __name__ == "__main__":
    main()


