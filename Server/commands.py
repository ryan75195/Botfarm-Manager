# cmd structure -- script,amount,stage:
import os
import pid
import DatabaseHandler
import script
import datetime
# import server

process_id = 0

muleEmail = ""
mulePass = ""
muleUsername = ""
db = DatabaseHandler.DatabaseHandler("localhost", "root", "fejfe3-ximmef-fUqfuq") # ip, username, pass
mulePID = -1
pid = pid.pid()

def getDateAndTime():
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y, %H:%M:%S").split(",")
    return dt_string



def muleStatus():
    request =  db.query("Select Current_Action From Session")
    if request == "Busy":
        return "Mule is busy with another farmer right now, Please try again later.",1
    if request == "Ready":
        return "Mule is available, starting.", 2
    if request == "Waiting":
        return "Mule is waiting in designated area.", 3
    if request == "Trading":
        return "Mule is currently trading player.", 4
    if request == "Complete":
        return "Trade complete.", 5


def muleNoDB(PlayerName, amount = None):
    global mulePID
    email = ""
    password = ""
    world = "398"
    PlayerName = PlayerName.replace(" ", "~")
    print(f"Name: {PlayerName}, Amount: {amount}")
    if amount == None:
        print("Giving")
        launchMule = f"java -jar ~/Applications/OSBot.jar -login ryank645:master75195 -bot {email}:{password}:0000 -script mule:" + f"{str(PlayerName)}#0" + " -world " + world
    else:
        print("Recieving")
        launchMule = f"java -jar ~/Applications/OSBot.jar -login ryank645:master75195 -bot {email}:{password}:0000 -script mule:" + f"{str(PlayerName)}#{amount}" + " -world " + world

    mulePID = pid.launchBot(launchMule)

def getMulePID():
    if type(mulePID) is list:
        return mulePID[0]
    else:
        return mulePID

def startMule(processID, Command):
    cmd, name, location, world, isGiving = Command.split(",")

    mule = db.retrieveAccounts("mule",1)
    if processID == 0:

        newName = "" + chr(34)
        for i in name:
            if i == " ":
                newName += "\ "
            else:
                newName += i
        newName += chr(34)
        # print(newName)
        launchMule = f"java -jar ~/Applications/OSBot.jar -login ryank645:master75195 -bot {mule.email}:{mule.password}:0000 -script mule:" + f"{str(newName)}" + " -world " + world
        process_id = pid.launchBot(pid.getJavaPIDs(), launchMule)
        db.query(f"DELETE FROM Session WHERE Bot_ID = {mule.id};")
        db.query(f"INSERT INTO Session(Bot_ID,World,Start_Time,Current_Action,Date,PID)Values("
                 f"{mule.id}, {world}, {getDateAndTime()[0]}, 'logging in',{getDateAndTime()[1]}, {process_id});")
    return str(muleUsername)



def killBot(pid):
    # cmd, PID = Command.split(",")
    os.system("kill " + str(pid))
    global mulePID
    mulePID = -1
    return f"Killed {pid}"

# def startBot(id):
#     # cmd, Script, Amount = Command.split(",")
#     # if (Script == "planks"):
#     #     Script = script.script("planks", 0, None)
#     accounts = db.getAccountInfo(id)
#     # print(accounts)
#     # accountPIDs = {}
#
#     # print(f"Starting account: {accounts}")
#     p = pid.pid()
#     processID = p.launchBot(f"java -jar ~/Applications/OSBot.jar -login ryank645:master75195 -bot {account.email}:{account.password}:0000 -script {Script.name}:null -world 305")[0]
#     # print(f"{account.id},{account.world},{processID}")
#     db.query(f"DELETE FROM Session WHERE Bot_ID = {account.id};")
#     db.query(f"INSERT INTO Session (Bot_ID,Wealth_Generated,World,Start_Time,Current_Action,Runs_Completed,Date,End_Time,PID) VALUES ('{account.id}', '0', '301', '{getDateAndTime()[0]}', 'logging in', '0', '{getDateAndTime()[1]}', '-1', '{processID}');")
#     # db.query(f"INSERT INTO Session (Bot_ID) Values ('1')")
#     # accountPIDs[account.id] = processID
#     return f"{Amount} {Script.name} bots have been successfully started."

def QueryDB(Query):
    # print(Query[0])
    return db.query(Query)

def getAccounts():
    Accounts = db.query("SELECT * FROM Account")
    # print(Accounts)
    return Accounts

def getSession():
    Session = db.query("SELECT * FROM Session")
    # print(Session)
    return Session

def addAccount(email,password,username,ip,port,script):
    query = f"INSERT INTO Account (Email, Password, Username, IP, Port, Script) VALUES ('{email}','{password}','{username}','{ip}','{port}','{script}');"
    # print(query)
    success = db.query(query)
    if success == 1:
        # print("Account successfully added.")
        return 1
    else:
        print("Failure.")
        return 0

def setRingWorld(World):
    try:
        db.query(f"UPDATE JAR_GENERATOR SET World = '{str(World)}' WHERE ID = 1")
        return str(getRingWorld())
    except:
        return -2 # Server is busy

def getRingWorld():
    try:
        currentWorld = db.query("SELECT World FROM JAR_GENERATOR WHERE ID = '1'")
        return currentWorld[0]
    except:
        return -2 # Server is busy



# def execute(Command):
#     global process_id
#     Cmnd = int(Command[0]) if Command[0].isdigit() else -1
#     # for i in range(0,len(Command)):
#     #     print(str(i) + ": " + Command[i])
#     print(Cmnd)
#     if Cmnd == 1 and len(Command.split(",")) == 5: #Mule Request
#         return muling(process_id,Command)
#     elif Cmnd == 2 and len(Command.split(",")) == 2: # Kill Bot
#         return killBot(Command)
#     elif Cmnd == 3 and len(Command.split(",")) == 3: # Start Bot
#         return startBot(Command)
#     elif Cmnd == 4: #Database Query
#         return database(Command)
#     elif Cmnd == 5: #ring world
#         return ringworld(Command)
#     else:
#         return "Invalid command."

