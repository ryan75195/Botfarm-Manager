import socket
import threading
import commands


currentPlayerTrading = None

def processRequest(request):
    # print("Processing Request")
    len, msg = decode_messege(5, request)
    location, request = msg.split(',')[:2]
    args = msg.split(',')[2:]
    print("[CLIENT] " + str(request))

    if location == "Manager":
        response = managerRequest(request, args)
        return response

    elif location == "Mule":
        response = muleRequest(request, args)
        print("Response: " + str(response))
        return response

    elif location == "Puro":
        response = puroRequest(request, args)
        print("Response: " + str(response))
        return response

    else:
        return "invalid request"


def muleRequest(Request, args):
    if Request == "startmule":
        global currentPlayerTrading

        playerName, isRecieving, amount = args

        # print(playerName)

        if playerName == "done":
            currentPlayerTrading = None
            print("[SERVER] Mule is now available.")
        elif currentPlayerTrading is None:
            print("[SERVER] Mule is meeting with " + playerName + ".")
            currentPlayerTrading = playerName
            if isRecieving == "1":
                commands.muleNoDB(playerName, amount)
            else:
                commands.muleNoDB(playerName)
            return 1
        elif currentPlayerTrading == playerName:
            print("[SERVER] Request already being processed.")
            return 1
        else:
            print("[SERVER] Mule is busy. Try again soon.")
            return 0


    elif Request == "getmulepid":
        print("[SERVER] Mule PID is " + str(commands.getMulePID()) + ".")
        return str(commands.getMulePID())
    elif Request == "kill":
        pid = args[0]
        commands.killBot(pid)
        print(f"[SERVER] Successfully Killed Mule.")


def managerRequest(Request, args):
    # print(str(Request) + str(args))
    if Request == "connect":
        return 1
    if Request == "AddAccount":
        email = args[0]
        password = args[1]
        username = args[2]
        ip = args[3]
        port = args[4]
        script = args[5]

        argList = args
        for i in range(0,len(argList)):
            if argList[i] == "":
                if i == 4:
                    argList[i] = -1
                else:
                    argList[i] = "null"

        print(args[0],args[1],args[2],args[3],args[4],args[5])
        success = commands.addAccount(args[0],args[1],args[2],args[3],args[4],args[5])
        return success
    if Request == "getAccounts":
        return commands.getAccounts()
    if Request == "QueryDB":
        query = ''
        for i in args:
            # print(i)
            query += i + ","
        # print(query[:-1]+";")
        return commands.QueryDB(query[:-1]+";")
    if Request == "getSession":
        return commands.getSession()
    if Request == "ViewTable":
        return commands.db.getTable(args[0])

def puroRequest(Request, args):
    if Request == "getworld":
        print("[SERVER] Last portal spotted on world " + str(commands.getRingWorld()) + ".")
        return commands.getRingWorld()
    if Request == "setworld":
        # print(f"pppants: {args}")
        world = args[0]
        commands.setRingWorld(world)
        print(f"[SERVER] Database updated to world {commands.getRingWorld()}.")
        return "Database updated successfully."
        # return f"Database updated to world {commands.getRingWorld()}."
    if Request == "getmulepid" or Request == "startmule" or Request == "kill":
        return muleRequest(Request, args)
    if Request == "UpdateSession":
        print(args)
        hasUsername = False
        for i in range(len(commands.getAccounts())):
            if commands.getAccounts()[i] == args[3]:
                # print(f"Account, {commands.getAccounts()[i-3]}; Args, {args[3]}")
                hasUsername = True
                break
            # print("No need to update name. already set.")
        if not hasUsername:
            # print("Updating username in db")
            # print(f"UPDATE Account SET Username = '{args[3].strip()}' WHERE Email = '{args[4].strip()}';")
            commands.QueryDB(f"UPDATE Account SET Username = '{args[3].strip()}' WHERE Email = '{args[4].strip()}';")
        # print(f"UPDATE Session SET CurrentAction = '{args[0].strip()}', GoldMade = '{args[1].strip()}', GoldMuled = '{args[2].strip()}' WHERE Username = '{args[3].strip()}'")
        commands.QueryDB(f"UPDATE Session SET CurrentAction = '{args[0].strip()}', GoldMade = '{args[1].strip()}', GoldMuled = '{args[2].strip()}' WHERE Username = '{args[3].strip()}'")
        return "Set"




def decode_messege(startbytes, msg):
    buffer = ""
    # length = getMessageLen(connection, startbytes)
    # remaining = length

    # while remaining > 0:
        # msg = str(connection.recv(remaining), encoding="utf-8", errors="replace")

    for i in msg:
        # if remaining <= 0:
        #     break
        # el

        if i == ":":
            buffer = ""
            continue
        # else:
        elif str.isalnum(i) or i == ',' or i == " " or i == "�" or i == "_" or i == "(" or i == ")" or \
                i == "'" or i == "*" or i == "-" or i == "." or i =="@" or i == "=" or i == "":
            buffer += i
        # elif i == "":
        #     buffer += ' '
            # remaining -= 1

        # print(i)
    messege = buffer
    # print(f"Decoded: {messege}")
    return len(messege), messege

def getMessageLen(connection, startbytes):
    remaining = startbytes
    buffer = ""
    while remaining > 0:
        msg = connection.recv(startbytes).decode("utf-8")
        for i in msg:
            if i == ":" or remaining <= 0:
                break
            elif str(i).isnumeric():
                buffer += str(i)
                remaining -= 1
    length = int(buffer)
    return length