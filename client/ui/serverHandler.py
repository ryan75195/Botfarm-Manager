import socket

class serverHandler():

    ip = ""
    port = -1

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.isConnected = False
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, self.port))

    def conenctToServer(self):
        if not self.isConnected:
            print("Connecting")
            self.s.connect((self.ip, self.port))
            msg = self.sendRequest("connect")
            if int(msg) == int("1"):
                self.isConnected = True
                return 1
            else:
                return 0
        else:
            return 2

    def isConnected(self):
        pass

    def sendRequest(self,Message):
        print(Message)
        self.s.send(("Manager," + Message + "\n").encode())
        data = b""
        while True:
            # print(data)
            data += self.s.recv(5)
            if "\n" in data.decode("utf-8"):
                msg = data.decode("utf-8")
                break
        return msg

    def getTable(self, TableName):
        rowlen, response = self.sendRequest("ViewTable,"+TableName).split(";")
        print(response)
        responseStripped = response.translate({ord(i): '' for i in '[' + "'" + ']' + '\n'}).split(',')
        # print(rowlen + ":" + str(responseStripped))
        Table = []
        Row = []
        # counter = 0
        done = False
        while not done:
            for i in range(0, int(rowlen)):
                try:
                    Row.append(responseStripped[i])
                except:
                    done = True
            if Row != []:
                Table.append(Row)
            # print(Row)
            Row = []
            responseStripped = responseStripped[int(rowlen):]
        #
        for i in Table:
            print(i)
        print(" ")
        print(Table)


        return Table

    def queryDB(self, query):
        response = self.sendRequest("QueryDB,"+query).split(";")
        print(response)
        return response

    def getAccounts(self):
        AccountsUnformatted = self.sendRequest("getAccounts").translate({ord(i): '' for i in '[' + "'" + ']' + '\n'}).split(',')
        AccountsFormatted = []
        Account = []
        done = False
        while not done:
            for i in range(0,9):
                try:
                   Account.append(AccountsUnformatted[i])
                except:
                    done = True
            AccountsFormatted.append(Account)
            Account = []
            AccountsUnformatted = AccountsUnformatted[9:]

        return AccountsFormatted

    def getSession(self):
        SessionUnformatted = self.sendRequest("getSession").translate({ord(i): '' for i in '[' + "'" + ']' + '\n'}).split(',')
        SessionFormatted = []
        Session = []
        done = False
        while not done:
            for i in range(0, 8):
                try:
                    Session.append(SessionUnformatted[i])
                except:
                    done = True

            SessionFormatted.append(Session)
            Session = []
            SessionUnformatted = SessionUnformatted[8:]

        return SessionFormatted
