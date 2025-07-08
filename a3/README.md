# CS158A Assignment 3 – Leader Election in an Asynchronous Ring

## information
Karamjeet Kaur  
San Jose State University  
CS158A - Summer 2025



## 📄 Description

This project implements a distributed leader election algorithm using an asynchronous non-anonymous ring network model. Each node is represented by a Python process using sockets, multithreading, and a UUID-based election protocol.

The goal is to elect a unique leader (node with the highest UUID) where:
- Only one leader is chosen (Uniqueness)
- All nodes agree on the same leader (Agreement)
- The election terminates (Termination)

---

## 🧾 Files Included in a3/Folder

myleprocess1.py # Process 1 (reads config1.txt)
myleprocess2.py # Process 2 (reads config2.txt)
myleprocess3.py # Process 3 (reads config3.txt)
config1.txt # IP & port config for process 1
config2.txt # IP & port config for process 2
config3.txt # IP & port config for process 3
log5001.txt # Log for process running on port 5001
log5002.txt # Log for process running on port 5002
log5003.txt # Log for process running on port 5003
README.md # This explanation file

---

## 🧪 How to Run the Program

> Open 3 terminal windows, one for each Python file. Run them 2–3 seconds apart.

### Example:
cmd
# Terminal 1
python myleprocess1.py

# Terminal 2 (after 2–3 seconds)
python myleprocess2.py

# Terminal 3 (after 2–3 seconds)
python myleprocess3.py
Once the leader election completes, each terminal should print something like:

 Leader is decided to d46fbc87-0db5-4152-a3f0-d27a2793925a
 Expected Output
Each log*.txt file should contain:

The process's UUID

Received and sent messages

Flag value (0 = election, 1 = leader found)

Comparison: greater / less / same
config1.txt
127.0.0.1,5001
127.0.0.1,5002
config2.txt
127.0.0.1,5002
127.0.0.1,5003
config3.txt
127.0.0.1,5003
127.0.0.1,5001
![image](https://github.com/user-attachments/assets/49886884-3595-4844-85c7-293d881461e6)




