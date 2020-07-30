import queue
import cmds

class client:


    def __init__(self, Email, Password, userName, socket):
        self.socket = socket
        self.pid = -1
        self.Email = Email
        self.Password = Password
        self.userName = userName
        self.commands = queue.Queue()
        self.muleQueuePositon = None

    def getPID(self):
        return self.pid

    def setPID(self, pid):
        self.pid = pid

    # def getUserName(self):
    #     return self.userName
    #
    # def setUserName(self, username):
    #     self.userName = username

    def ExecuteCommand(self):
        success = False
        if cmds.executeCommand(self.command.get()):
            success = True
        return success

    def AddCommand(self, cmd):
        self.commands.put(cmd)

    def getMuleQueuePosition(self):
        return self.muleQueuePositon

    def setMuleQueuePosition(self, position):
        self.muleQueuePositon = position
