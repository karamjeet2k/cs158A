import socket
import threading
import time
import uuid
import json

# Message class to serialize/deserialize JSON
class Message:
    def __init__(self, uuid, flag):
        self.uuid = str(uuid)  # always store as string for JSON
        self.flag = flag       # 0 = election, 1 = leader found

    def to_json(self):
        return json.dumps(self.__dict__) + "\n"

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Message(uuid.UUID(data['uuid']), data['flag'])


# === Load configuration from appropriate config file ===
# IMPORTANT: Change config1.txt to config2.txt or config3.txt for other processes
with open("config3.txt", "r") as f:
    lines = f.read().splitlines()
    my_ip, my_port = lines[0].split(",")
    neighbor_ip, neighbor_port = lines[1].split(",")

my_port = int(my_port)
neighbor_port = int(neighbor_port)

# === Initialization ===
my_uuid = uuid.uuid4()
leader_id = None
state_flag = 0  # 0: in election, 1: leader decided
log_file = f"log{my_port}.txt"

# Clear the log file at the start
open(log_file, 'w').close()

def log(message):
    with open(log_file, 'a') as f:
        f.write(message + "\n")
    print(message)


# === Server thread: receive messages ===
def server_thread():
    global state_flag, leader_id

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((my_ip, my_port))
    server.listen(1)
    conn, addr = server.accept()

    while True:
        data = b""
        while not data.endswith(b"\n"):
            chunk = conn.recv(1024)
            if not chunk:
                return
            data += chunk

        msg = Message.from_json(data.decode())
        incoming_uuid = msg.uuid
        flag = msg.flag

        comparison = "greater" if incoming_uuid > str(my_uuid) else ("less" if incoming_uuid < str(my_uuid) else "same")

        if state_flag == 0:
            if flag == 0:
                if incoming_uuid > str(my_uuid):
                    log(f"Received: uuid={incoming_uuid}, flag={flag}, {comparison}, 0")
                    send(Message(incoming_uuid, 0))
                    log(f"Sent: uuid={incoming_uuid}, flag=0")

                elif incoming_uuid == str(my_uuid):
                    log(f"Received: uuid={incoming_uuid}, flag={flag}, {comparison}, 0 — my own UUID back")
                    leader_id = str(my_uuid)
                    state_flag = 1
                    send(Message(leader_id, 1))
                    log(f"Sent: uuid={leader_id}, flag=1")

                else:
                    log(f"Received: uuid={incoming_uuid}, flag={flag}, {comparison}, 0 - ignored")

            elif flag == 1:
                state_flag = 1
                leader_id = incoming_uuid
                log(f"Received: uuid={incoming_uuid}, flag=1, {comparison}, 1 | Leader is {leader_id}")
                if incoming_uuid != str(my_uuid):
                    send(Message(incoming_uuid, 1))
                    log(f"Sent: uuid={incoming_uuid}, flag=1")

        elif state_flag == 1:
            log(f"Received: uuid={incoming_uuid}, flag={flag}, {comparison}, 1 | Leader is {leader_id}")


# === Client function to send messages ===
def send(message):
    try:
        client.sendall(message.to_json().encode())
    except:
        log("Client send failed.")


# === Main Code ===
log(f"My UUID: {my_uuid}")

# Start server in a separate thread
threading.Thread(target=server_thread, daemon=True).start()

# Setup client connection (retry until neighbor is ready)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False
while not connected:
    try:
        client.connect((neighbor_ip, neighbor_port))
        connected = True
    except:
        time.sleep(1)

# Wait to ensure all servers are ready
time.sleep(5)

# Send initial election message
initial_msg = Message(my_uuid, 0)
send(initial_msg)
log(f"Sent: uuid={my_uuid}, flag=0")

# Wait until leader is decided
while state_flag == 0:
    time.sleep(1)

# Final log once leader is known
log(f"Leader is decided to {leader_id}.")
