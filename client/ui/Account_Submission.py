# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Account(object):
    def setupUi(self, Account, serverHandler):
        Account.setObjectName("Account")
        Account.resize(487, 247)
        self.Email_label = QtWidgets.QLabel(Account)
        self.Email_label.setGeometry(QtCore.QRect(20, 40, 67, 21))
        self.Email_label.setObjectName("Email_label")
        self.Email_input = QtWidgets.QLineEdit(Account)
        self.Email_input.setGeometry(QtCore.QRect(110, 40, 113, 25))
        self.Email_input.setObjectName("Email_input")
        self.Password_label = QtWidgets.QLabel(Account)
        self.Password_label.setGeometry(QtCore.QRect(270, 40, 71, 21))
        self.Password_label.setObjectName("Password_label")
        self.Password_input = QtWidgets.QLineEdit(Account)
        self.Password_input.setGeometry(QtCore.QRect(350, 40, 113, 25))
        self.Password_input.setObjectName("Password_input")
        self.Username_label = QtWidgets.QLabel(Account)
        self.Username_label.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.Username_label.setObjectName("Username_label")
        self.Username_input = QtWidgets.QLineEdit(Account)
        self.Username_input.setGeometry(QtCore.QRect(110, 80, 113, 25))
        self.Username_input.setObjectName("Username_input")
        self.Script_label = QtWidgets.QLabel(Account)
        self.Script_label.setGeometry(QtCore.QRect(270, 80, 51, 21))
        self.Script_label.setObjectName("Script_label")
        self.Script_input = QtWidgets.QLineEdit(Account)
        self.Script_input.setGeometry(QtCore.QRect(350, 80, 113, 25))
        self.Script_input.setObjectName("Script_input")
        self.IP_label = QtWidgets.QLabel(Account)
        self.IP_label.setGeometry(QtCore.QRect(20, 120, 67, 21))
        self.IP_label.setObjectName("IP_label")
        self.IP_input = QtWidgets.QLineEdit(Account)
        self.IP_input.setGeometry(QtCore.QRect(110, 120, 113, 25))
        self.IP_input.setObjectName("IP_input")
        self.Port_label = QtWidgets.QLabel(Account)
        self.Port_label.setGeometry(QtCore.QRect(270, 120, 81, 21))
        self.Port_label.setObjectName("Port_label")
        self.Port_input = QtWidgets.QLineEdit(Account)
        self.Port_input.setGeometry(QtCore.QRect(350, 120, 113, 25))
        self.Port_input.setObjectName("Port_input")
        self.Submit_Button = QtWidgets.QPushButton(Account)
        self.Submit_Button.setGeometry(QtCore.QRect(130, 180, 89, 25))
        self.Submit_Button.setObjectName("Submit_Button")
        self.Cancel_Button = QtWidgets.QPushButton(Account)
        self.Cancel_Button.setGeometry(QtCore.QRect(270, 180, 89, 25))
        self.Cancel_Button.setObjectName("Cancel_Button")

        self.retranslateUi(Account,serverHandler)
        QtCore.QMetaObject.connectSlotsByName(Account)

    def retranslateUi(self, Account, serverHandler):
        _translate = QtCore.QCoreApplication.translate
        Account.setWindowTitle(_translate("Account", "Account Information"))
        self.Email_label.setText(_translate("Account", "Email"))
        self.Password_label.setText(_translate("Account", "Password"))
        self.Username_label.setText(_translate("Account", "Username"))
        self.Script_label.setText(_translate("Account", "Script"))
        self.IP_label.setText(_translate("Account", "Proxy IP"))
        self.Port_label.setText(_translate("Account", "Proxy Port"))
        self.Submit_Button.setText(_translate("Account", "Submit"))
        self.Cancel_Button.setText(_translate("Account", "Cancel"))
        self.setupButtons(Account, serverHandler)

    def sendToDB(self,serverHandler, Account):
        email = self.Email_input.text().strip()
        password = self.Password_input.text().strip()
        username = self.Username_input.text().strip()
        ip = self.IP_input.text().strip()
        port = self.Port_input.text().strip()
        script = self.Script_input.text().strip()
        request = int(serverHandler.sendRequest(f"AddAccount,{email},{password},{username},{ip},{port},{script}"))
        if request == 1:
            print("Database updated successfully.")
        else:
            print("Database could not be updated at this time.")

        Account.close()

    def setupButtons(self, Account, serverHandler):

        self.Submit_Button.clicked.connect(lambda: self.sendToDB(serverHandler, Account))
        self.Cancel_Button.clicked.connect(lambda: Account.close())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Account = QtWidgets.QDialog()
    ui = Ui_Account()
    ui.setupUi(Account)
    Account.show()
    sys.exit(app.exec_())
