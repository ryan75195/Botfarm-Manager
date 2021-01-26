import socket
import sys
import threading
from cmds import executeCommand
# cmds = sys.path.insert(0, 'cmds.py')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 6000))
sock.listen(1)
connections = []


def handler(c, a):
    if c not in connections:
        print("Connection from {} on port {}. ".format(a[0], a[1]))
    while True:
        length, msg = decode_messege(c, 5)
        msg = msg.replace("�",' ')
        print("[Client]: " + msg)
        response = str(interpretCommand(msg))
        if msg == "dc":
            c.send(encode(response))
            break
        print("[Server]: " + response)
        c.send(encode(response))
    c.close()

def encode(Message):
    length = len(Message)
    bits = len(str(length))
    msg = ("00000"[bits:] + str(length) + ":" + Message + '\n')
    # print(msg.encode("utf-8"))
    return msg.encode("utf-8")


def interpretCommand(command):

    if "," in command:
        return executeCommand(command)

    if command == "hello":
        return "hey"
    if command == "table":
        print("[Server] Updating Table")
        return("[Server] Updating Table")

    if command == "rm":
        print("[Server] Removing Entry")
        return("[Server] Removing Entry")

    if command == 'dc':
        print(f"[Server]: Disconnecting {a[0]} from server.")
        return(f"Disconnecting {a[0]} from server.")



def decode_messege(connection, startbytes):

        buffer = ""
        length = getMessageLen(connection,startbytes)
        remaining = length

        while remaining > 0:
            msg = str(connection.recv(remaining), encoding="utf-8", errors="replace")
            for i in msg:
                if remaining <= 0:
                    break
                elif i == ":":
                    continue
                # else:
                elif str.isalnum(i) or i == ',' or i == " " or i == "�":
                    buffer += i
                    remaining -= 1

            # print(i)
        messege = buffer
        return int(length), messege

def myrecv(connection, size):
    buffer = ''
    while size > 0:
        msg = connection.recv(1024).decode("utf-8")
        buffer += msg
        size -= len(msg)
    return buffer

while True:
    c, a = sock.accept()
    cThread = threading.Thread(target=handler, args=(c, a))
    cThread.daemon = True
    cThread.start()
    connections.append(c)