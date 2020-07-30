import client

class mule(client):
    def __init__(self, userName, isMember):
        super().__init__(pid,userName)
        self.isMember = isMember
        self.playerQueue = []
