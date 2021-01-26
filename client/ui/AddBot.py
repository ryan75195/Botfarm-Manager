# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddBot.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from serverHandler import serverHandler


class base(object):


    def setupUi(self, Add_Bot_Session):
        Add_Bot_Session.setObjectName("Add_Bot_Session")
        Add_Bot_Session.resize(363, 254)
        self.Script_Tesxt = QtWidgets.QLabel(Add_Bot_Session)
        self.Script_Tesxt.setGeometry(QtCore.QRect(60, 50, 67, 31))
        self.Script_Tesxt.setObjectName("Script_Tesxt")
        self.label_2 = QtWidgets.QLabel(Add_Bot_Session)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 67, 31))
        self.label_2.setObjectName("label_2")
        self.Select_Script = QtWidgets.QComboBox(Add_Bot_Session)
        self.Select_Script.setGeometry(QtCore.QRect(120, 50, 171, 31))
        self.Select_Script.setObjectName("Select_Script")
        self.Select_Account = QtWidgets.QComboBox(Add_Bot_Session)
        self.Select_Account.setGeometry(QtCore.QRect(120, 100, 171, 31))
        self.Select_Account.setObjectName("Select_Account")
        self.Confirm_Add = QtWidgets.QPushButton(Add_Bot_Session)
        self.Confirm_Add.setGeometry(QtCore.QRect(90, 170, 81, 25))
        self.Confirm_Add.setObjectName("Confirm_Add")
        self.Cancel_Add = QtWidgets.QPushButton(Add_Bot_Session)
        self.Cancel_Add.setGeometry(QtCore.QRect(200, 170, 89, 25))
        self.Cancel_Add.setObjectName("Cancel_Add")

        self.retranslateUi(Add_Bot_Session)
        QtCore.QMetaObject.connectSlotsByName(Add_Bot_Session)

    def retranslateUi(self, Add_Bot_Session):
        _translate = QtCore.QCoreApplication.translate
        Add_Bot_Session.setWindowTitle(_translate("Add_Bot_Session", "Dialog"))
        self.Script_Tesxt.setText(_translate("Add_Bot_Session", "Script:"))
        self.label_2.setText(_translate("Add_Bot_Session", "Account:"))
        self.Confirm_Add.setText(_translate("Add_Bot_Session", "Confirm"))
        self.Cancel_Add.setText(_translate("Add_Bot_Session", "Cancel"))

class Ui_Add_Bot_Session(base):

    def __init__(self):
        self.OSBOTusername = "ryank645"
        self.OSBOTpassword = "master75195"

    def setupLogic(self, Add_Bot_Session):
        sh = serverHandler("localhost",8080)
        Accounts = sh.getAccounts()
        self.setupUi(Add_Bot_Session)
        self.Select_Script.addItems(["Puro Puro","Tutorial","Mule", "None"])
        Emails = {}
        for idx, account in enumerate(Accounts):
            Emails[idx] = account[1] if account != [] else -1
        print(Emails)
        self.Select_Account.addItems([x for x in Emails.values() if x != -1])
        print(Accounts)

        self.Cancel_Add.clicked.connect(lambda: Add_Bot_Session.close())
        self.Confirm_Add.clicked.connect(lambda: self.addSession(
            Accounts[[x for x in Emails.keys() if str(Emails[x]).strip() == self.Select_Account.currentText().replace(" ", "")][0]],
                                         self.Select_Script.currentText(),sh, Add_Bot_Session))


    def addSession(self, Account, Script, sh, Add_Bot_Session):
        print(Account)
        import time
        from pid import pid as p
        global OSBotusername
        global OSBOTpassword
        millis = int(round(time.time() * 1000))
        scriptName, params, world, noRandoms = self.getParams(Script,Account)

        print(Account[5].strip())
        if scriptName == "-1":

            if int(Account[5].strip()) == -1:
                launchBot = f"java -jar ~/Applications/OSBot.jar -login ryank645:master75195 -bot {Account[1].strip()}:{Account[2].strip()}:0000 " \
                            f" -world {str(world)} -allow lowcpu "
            else:
                launchBot = f"java -jar ~/Applications/OSBot.jar -login ryank645:master75195 -bot {Account[1].strip()}:{Account[2].strip()}:0000 " \
                            f" -world {str(world)} -allow lowcpu " \
                            f"-proxy {Account[4].strip()}:{Account[5].strip()}:4oBdKR:qJ1bH5"
        else:
            if int(Account[5].strip()) == -1:
                launchBot = f"java -jar ~/Applications/OSBot.jar -login {self.OSBOTusername}:{self.OSBOTpassword} -bot {Account[1].strip()}:{Account[2].strip()}:0000 " \
                            f"-script {scriptName}:{params} -world {str(world)} -allow {noRandoms}lowcpu "

            else:
                launchBot = f"java -jar ~/Applications/OSBot.jar -login {self.OSBOTusername}:{self.OSBOTpassword} -bot {Account[1].strip()}:{Account[2].strip()}:0000 " \
                            f"-script {scriptName}:{params} -world {str(world)} -allow {noRandoms}lowcpu " \
                            f"-proxy {Account[4].strip()}:{Account[5].strip()}:4oBdKR:qJ1bH5"
        print(launchBot)
        pid = p().launchBot(launchBot)[0]
        sh.queryDB("INSERT INTO Session (ID, Username, Script, StartTime, PID)"
                   f" VALUES ('{Account[0].strip()}','{Account[3].strip()}','{Script}','{millis}', '{pid}');")
        Add_Bot_Session.close()
        # print(self.Select_Account.currentText())

    def getParams(self, Script, Account):
        if Script == "Puro Puro":
            return "PuroPuro",f"{Account[1].strip()}#{Account[2].strip()}",302,"norandoms,"
        if Script == "Tutorial":
            return "TutorialIsland",f"{Account[1].strip()}#{Account[2].strip()}",301,""
        if Script == "None":
            return "-1","-1",301,""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add_Bot_Session = QtWidgets.QDialog()
    ui = Ui_Add_Bot_Session()
    ui.setupUi(Add_Bot_Session)
    Add_Bot_Session.show()
    sys.exit(app.exec_())
