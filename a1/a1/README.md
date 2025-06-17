contact information: karamjeet.kaur@sjsu.edu

# Assignment 1
Variable-Length Message Client-Server
This project demonstrates a simple client-server communication using TCP sockets in Python. The client sends a message with a 2-digit length prefix, and the server reads the message, converts it to uppercase, and sends it back to the client.

## Features
Supports variable-length messages (up to 99 characters) Uses a 2-byte header to indicate the message length Capitalizes the message before sending back Built with Python’s socket module Easy to run and test in local environment

# Message Format
The first 2 characters of the message represent the length of the actual message.
The message itself follows immediately after the 2-digit length.
All characters are within the UTF-8 range: U+0000 to U+007F (i.e., basic ASCII).
Example:C:\Users\Checkout\Documents\cs158A>python myclient.py Input lowercase sentence: 05hello From Server: HELLO

# Usage Instructions
Start the server
cmd: python myvserver.py we should able see: Server is listening...

Start the client (in a new terminal)
python myvclient.py C:\Users\Checkout\Documents\cs158A> python myvclient.py Enter a message (max 99 letters): 17hi how are you ?karam From Server: 17HI HOW ARE YOU ?KARAM

Input lowercase sentence: 05hello From Server: HELLO

from server side like Connected from 127.0.0.1
msg_len: 5 processed: hello msg_len_sent: 5 Connection closed

Connected from 127.0.0.1 msg_len: 23 processed: 17hi how are you ?karam msg_len_sent: 23 Connection closed
