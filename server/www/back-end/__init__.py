from . import cmds
from . import pid

def executeCommand(command):
    return cmds.executeCommand(command)

def launchBot(pidList, paramaters):
    return pid.launchBot(pidList, paramaters)
