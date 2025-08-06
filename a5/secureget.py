import socket
import ssl

# Step 1: Define target host and port
hostname = 'www.google.com'
port = 443  # HTTPS port

# Step 2: Create TCP socket and wrap it with SSL
context = ssl.create_default_context()
sock = socket.create_connection((hostname, port))
ssock = context.wrap_socket(sock, server_hostname=hostname)

# Step 3: Send HTTP GET request for root path
request = f"GET / HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"
ssock.sendall(request.encode())

# Step 4: Receive full HTTP response
response = b""
while True:
    data = ssock.recv(4096)
    if not data:
        break
    response += data

# Step 5: Close the secure socket
ssock.close()

# Step 6: Separate HTTP headers from HTML content
try:
    header, html = response.split(b'\r\n\r\n', 1)
except ValueError:
    html = response  # fallback: save everything if split fails

# Step 7: Save only the HTML part to file
with open("response.html", "wb") as f:
    f.write(html)

print(" Clean HTML content saved to response.html")

