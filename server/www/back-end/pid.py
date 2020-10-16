import os

OSBOT_PATH = "~/Applications/osbot.jar"
OSBOT_USER = ""
OSBOT_PASS = ""
def getJavaPIDs():
    return str(os.popen("pidof java").read()).replace("\n", '').split(" ")
    # return os.popen("pidof java")

def launchBot(pidList, paramaters):
    os.system(paramaters)
    newPidList = []
    while True:
        if getJavaPIDs() != pidList:
            newPidList = getJavaPIDs()
            break
    return [i for i in newPidList if i not in pidList]

def killBot(pid):
    os.system("kill " + str(pid))
