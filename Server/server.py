import socket, threading, pickle
import SocketHandler
import struct

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        # print ("New connection added: ", clientAddress)

    def encode(self,Message):
        # if Message == None:
        #     Message == "No Message"
        length = len(str(Message))
        bits = len(str(length))
        msg = ("00000"[bits:] + str(length) + ":" + str(Message) + '\n')
        # print(msg.encode("utf-8"))
        return msg.encode("utf-8")



    def my_encoder(self, my_string):
        for i in my_string:
            try:
                yield chr(i)
            except UnicodeDecodeError:
                yield " "  # or another whietespaces


    def recvall(self, sock):
        BUFF_SIZE = 4096  # 4 KiB
        data = b''
        while True:
            part = sock.recv(BUFF_SIZE)
            data += part
            # print(data)
            if '\n' in ''.join(self.my_encoder(data)):
                # print("Message recieved: " + data.decode() )
                # either 0 or end of data
                break
        return data

    def run(self):
        print ("Connection from : ", clientAddress)
        accountPIDs = {}
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        while True:
            # print(accountPIDs)
            data = self.recvall(self.csocket)
            # print("data" + data)
            msg = str(data,encoding="utf-8", errors='replace').replace("�"," ")
            print("msg" + msg)
            if msg=='bye':
              break
            ret = SocketHandler.processRequest(msg)
            print("ret" + str(ret))
            self.csocket.send((str(ret) + '\n').encode("utf-8"))

        print ("Farmer on IP ", clientAddress , " disconnected...")

LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
