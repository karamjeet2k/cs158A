from socket import *

def connect_to_server():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('localhost', 12000))
    return client

def send_message(client, text):
    length = str(len(text)).zfill(2)
    client.send(length.encode())
    client.send(text.encode())

def receive_response(client):
    response = client.recv(64).decode()
    return response

def main():
    client = connect_to_server()
    text = input("Enter a message (max 99 letters): ")
    send_message(client, text)
    reply = receive_response(client)
    print("From Server:", reply)
    client.close()

if __name__ == "__main__":
    main()

