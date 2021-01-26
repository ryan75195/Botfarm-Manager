import os

class pid:
    def __init__(self):
        self.pidList = []

    OSBOT_PATH = "~/Applications/osbot.jar"
    OSBOT_USER = "ryank645"
    OSBOT_PASS = "master75195"

    def getJavaPIDs(self):
        return str(os.popen("pidof java").read()).replace("\n", '').split(" ")
        # return os.popen("pidof java")

    def launchBot(self, paramaters):
        self.pidList = self.getJavaPIDs()
        os.system(paramaters)
        self.newPidList = []
        while True:
            if self.getJavaPIDs() != self.pidList:
                self.newPidList = self.getJavaPIDs()
                break
        return [i for i in self.newPidList if i not in self.pidList]

    def killBot(self, pid):
        os.system("kill " + str(pid))
