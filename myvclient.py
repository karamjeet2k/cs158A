
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 12000))

# Ask  to  user for  the message
text = input("Enter a message (max 99 letters): ")
length = str(len(text)).zfill(2)  # Making sure it's 2 digits, like '05'

# Send length + message
client.send(length.encode())
client.send(text.encode())

# Receive and show response
reply = client.recv(64).decode()
print("From Server:", reply)

client.close()
