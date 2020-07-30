# cmd structure -- script,amount,stage:
import os
import pid

process_id = 0

muleEmail = "bsdvarvvaav@gmail.com"
mulePass = "master75195"
muleUsername = "quuv"
activeAccounts = {}

def executeCommand(Command):
    global process_id
    Cmnd = int(Command[0])
    # for i in range(0,len(Command)):
    #     print(str(i) + ": " + Command[i])
    print(Command[0])
    if Cmnd == 1:
        cmd,name,location,world,isGiving = Command.split(",")
        # print("Name: " + name + ".")
        # print("Location: " + location + ".")
        # print("World: " + world + ".")
        # if isGiving == "true":
        #     print("Task: Recieving Gold.")
        # if isGiving == "false":
        #     print("Task: Giving Resources.")
        if process_id == 0:

            newName = "" + chr(34)
            for i in name:
                if i == " ":
                    newName += "\ "
                else:
                    newName += i
            newName += chr(34)
            print(newName)
            launchMule = f"java -jar ~/Applications/osbot.jar -login ryank645:master75195 -bot {muleEmail}:{mulePass}:0000 -script mule:" + f"{str(newName)}" + " -world " + "301"
            process_id = pid.launchBot(pid.getJavaPIDs(), launchMule)
            activeAccounts[muleUsername] = process_id
        return [muleUsername, process_id]

    if Cmnd == 2:
        cmd, userName = Command.split(",")
        os.system("kill " + str(activeAccounts[userName][0]))
        return "Killed Mule"