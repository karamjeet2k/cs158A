from socket import *

serverPort = 12000  # Port number

serverSocket = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket

# This empty string means the server will listen on all available interfaces
serverSocket.bind(('', serverPort))  # Bind the socket to the 
serverSocket.listen(1)
# accept
cnSocket, addr = serverSocket.accept()  # Accept a connection from a client

# receive
sentence = cnSocket.recv(64).decode()  # Receive a sentence from the client

# process
modifiedSentence = sentence.upper()  # Convert the sentence to uppercase
# send
cnSocket.send(modifiedSentence.encode())  # Send the modified sentence back to the client

# close
cnSocket.close()        # Close the connection with the client
serverSocket.close()    # Close the server socket
