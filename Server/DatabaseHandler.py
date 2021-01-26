# cmd structure -- script,amount,stage:
import Account
import mysql.connector

class DatabaseHandler:

    ip = ""
    username = ""
    password = ""
    db = None
    def __init__(self, IP, Username, Password):
        self.ip = IP
        self.username = Username
        self.password = Password
        self.db = self.connect(self.ip, self.username, self.password, "BotFarm")


    def connect(self, ip, username, password, database):
        db = mysql.connector.connect(
            host = ip,
            user = username,
            password = password,
            database = database
        )
        db.autocommit = True

        return db,db.cursor()

    def query(self, query):
        try:
            db, cursor = self.connect(self.ip, self.username, self.password, "BotFarm")
            cursor.execute(query)
            list = []
            for x in cursor:
                list += x
            # print(list)
            cursor.close()
            db.close()
            if len(list) == 0:
                return 1
            else:
                return list

        except mysql.connector.errors.ProgrammingError or mysql.connector.errors.Error as e:
            if e == mysql.connector.errors.ProgrammingError:
                print("Error: Invalid Query, Please Try Again.")
            else:
                print("Database Connection Dropped, Attempting To Reconnect.")
                self.db.ping(True,3,0)
            return 0


    def viewTables(self):
        return self.query("show tables;")

    def getTable(self, table_name):
        fieldCount = self.query(f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{table_name}';")[0]
        currentRow = []
        allRows = []
        query = self.query(f"SELECT * FROM {table_name}")
        # print(query)
        # l = len(list(query))

        # for i in range(0, l):
        #     currentRow.append((query[i]))
        #     if (i % fieldCount == 0 and i != 0) or i == l:
        #         print(currentRow)
        #         allRows.append(currentRow)
        #         currentRow = []
        return str(str(fieldCount) + ";" + str(query))

    def getAccountInfo(self, id):
        acc = self.query(f"SELECT * FROM Accounts WHERE id = '{id}'")
        return acc
        # Email = self.query("SELECT Email FROM Accounts WHERE Script = 'planks'")
        # Password = self.query("SELECT Password FROM Accounts WHERE Script = 'planks'")
        # Username = self.query("SELECT Username FROM Accounts WHERE Script = 'planks'")
        # Stage = self.query("SELECT Stage FROM Accounts WHERE Script = 'planks'")

    def getFarmAccount(self, script):
        # access db from here and store in Account object
        ID = self.query("SELECT ID FROM Accounts WHERE Script = 'planks'")
        Email = self.query("SELECT Email FROM Accounts WHERE Script = 'planks'")
        Password = self.query("SELECT Password FROM Accounts WHERE Script = 'planks'")
        Username = self.query("SELECT Username FROM Accounts WHERE Script = 'planks'")
        Stage = self.query("SELECT Stage FROM Accounts WHERE Script = 'planks'")
        Accounts = []

        for i in range(0, len(ID)):
            Accounts.append(Account.Account(ID[i],Email[i],Username[i],Password[i],script,Stage[i]))

        return Accounts

    def retrieveAccounts(self, script, amount):
        accounts = self.getFarmAccount(script)
        return accounts[:int(amount)]

    def addAccount(self, account):
        pass

    def removeAccount(self, account):
        pass

