import socket, threading, sys

host = "127.0.0.1"
port = 15000



def receive_message(socket_input):
    while True:
        #print(f'\nreceive called in {socket_input.getsockname()}')
        try:
            message = socket_input.recv(1024).decode()
            if not message:
                break
            print(message)
            print()
        except:
            break


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f'connected to server, type \'exit\' to quit')
    print(f'Your name is: {client.getsockname()[1]}')
    print('---------------------------------------------')

    threading.Thread(target = receive_message, args = (client,), daemon = True).start()

    try:
         while True:
             message = input()
             client.send(message.encode())
             print()
             if message.lower() == 'exit': break
    finally:
        print('Disconnected from server')
        #client.close()



if __name__ == "__main__":
    main()
