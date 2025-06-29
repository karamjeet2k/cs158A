import socket
import threading

host = '127.0.0.1'
port = 15000

# empty dictionary to store clients
# Key: socket: port
clients = {}

def broadcast(sender, message):
    keys = list(clients.keys())
    for client in keys:
        if client == sender:
            continue
        try:
            client.send(message.encode())
        except socket.error as er:
            print(er)
            remove_client(client)

def handle_client(client, addr):
    clients[client] = addr[1]  # this will be the port number
    print(f"New connection from {addr}")

    while True:
        message = client.recv(1024).decode()
        print(f'{addr[1]}: {message}')
        if (not message) or message.lower() == 'exit':
            break
        broadcast(client, f"{addr[1]}: {message}")
    
    # clean up when disconnected
    remove_client(client)
    print(f"client: {addr} is now closed")
    client.close()

def remove_client(client):
    if client in clients:
        del clients[client]

def start_server():
    # create a socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f'server listening at {host}:{port}')

    while True:
        client, addr = server.accept()
        # for each client, we create a thread
        threading.Thread(target=handle_client, args=(client, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()
