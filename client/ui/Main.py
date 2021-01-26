# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!
import os
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import socket

from PyQt5.QtWidgets import QMessageBox

import Account_Submission
import serverHandler
from AddBot import Ui_Add_Bot_Session


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1172, 415)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Database_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Database_Button.setGeometry(QtCore.QRect(20, 200, 101, 51))
        self.Database_Button.setObjectName("Database_Button")
        self.Session_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Session_Button.setGeometry(QtCore.QRect(20, 20, 101, 51))
        self.Session_Button.setAutoDefault(False)
        self.Session_Button.setDefault(False)
        self.Session_Button.setFlat(False)
        self.Session_Button.setObjectName("Session_Button")
        self.Analytics_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Analytics_Button.setGeometry(QtCore.QRect(20, 140, 101, 51))
        self.Analytics_Button.setObjectName("Analytics_Button")
        self.Notes_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Notes_Button.setGeometry(QtCore.QRect(20, 320, 101, 51))
        self.Notes_Button.setObjectName("Notes_Button")
        self.Scripts_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Scripts_Button.setGeometry(QtCore.QRect(20, 260, 101, 51))
        self.Scripts_Button.setObjectName("Scripts_Button")
        self.Accounts_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Accounts_Button.setGeometry(QtCore.QRect(20, 80, 101, 51))
        self.Accounts_Button.setDefault(False)
        self.Accounts_Button.setObjectName("Accounts_Button")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(130, 20, 1031, 351))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Session_Page = QtWidgets.QWidget()
        self.Session_Page.setObjectName("Session_Page")
        self.Session_Remove = QtWidgets.QPushButton(self.Session_Page)
        self.Session_Remove.setGeometry(QtCore.QRect(230, 310, 89, 31))
        self.Session_Remove.setObjectName("Session_Remove")
        self.Session_Confirm = QtWidgets.QPushButton(self.Session_Page)
        self.Session_Confirm.setGeometry(QtCore.QRect(910, 310, 89, 31))
        self.Session_Confirm.setObjectName("Session_Confirm")
        self.Session_Edit = QtWidgets.QPushButton(self.Session_Page)
        self.Session_Edit.setGeometry(QtCore.QRect(120, 310, 89, 31))
        self.Session_Edit.setObjectName("Session_Edit")
        self.Session_Table = QtWidgets.QTableWidget(self.Session_Page)
        self.Session_Table.setGeometry(QtCore.QRect(0, 0, 1001, 291))
        self.Session_Table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Session_Table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Session_Table.setColumnCount(8)
        self.Session_Table.setObjectName("Session_Table")
        self.Session_Table.setRowCount(0)
        self.Session_Add = QtWidgets.QPushButton(self.Session_Page)
        self.Session_Add.setGeometry(QtCore.QRect(10, 310, 89, 31))
        self.Session_Add.setObjectName("Session_Add")
        self.stackedWidget.addWidget(self.Session_Page)
        self.Accounts_Page = QtWidgets.QWidget()
        self.Accounts_Page.setObjectName("Accounts_Page")
        self.Accounts_Add = QtWidgets.QPushButton(self.Accounts_Page)
        self.Accounts_Add.setGeometry(QtCore.QRect(10, 310, 89, 41))
        self.Accounts_Add.setObjectName("Accounts_Add")
        self.Accounts_Edit = QtWidgets.QPushButton(self.Accounts_Page)
        self.Accounts_Edit.setGeometry(QtCore.QRect(120, 310, 89, 41))
        self.Accounts_Edit.setObjectName("Accounts_Edit")
        self.Accounts_Remove = QtWidgets.QPushButton(self.Accounts_Page)
        self.Accounts_Remove.setGeometry(QtCore.QRect(240, 310, 81, 41))
        self.Accounts_Remove.setObjectName("Accounts_Remove")
        self.Accounts_Confirm = QtWidgets.QPushButton(self.Accounts_Page)
        self.Accounts_Confirm.setGeometry(QtCore.QRect(910, 310, 89, 31))
        self.Accounts_Confirm.setObjectName("Accounts_Confirm")
        self.Accounts_Table = QtWidgets.QTableWidget(self.Accounts_Page)
        self.Accounts_Table.setGeometry(QtCore.QRect(0, 0, 1001, 291))
        self.Accounts_Table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Accounts_Table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Accounts_Table.setColumnCount(9)
        self.Accounts_Table.setObjectName("Accounts_Table")
        self.Accounts_Table.setRowCount(0)
        self.stackedWidget.addWidget(self.Accounts_Page)
        self.Analytics_Page = QtWidgets.QWidget()
        self.Analytics_Page.setObjectName("Analytics_Page")
        self.stackedWidget.addWidget(self.Analytics_Page)
        self.Database_Page = QtWidgets.QWidget()
        self.Database_Page.setObjectName("Database_Page")
        self.Database_Connect_Button = QtWidgets.QPushButton(self.Database_Page)
        self.Database_Connect_Button.setGeometry(QtCore.QRect(0, 310, 89, 31))
        self.Database_Connect_Button.setObjectName("Database_Connect_Button")
        self.Database_Connection_Status = QtWidgets.QLabel(self.Database_Page)
        self.Database_Connection_Status.setGeometry(QtCore.QRect(100, 310, 171, 31))
        self.Database_Connection_Status.setObjectName("Database_Connection_Status")
        self.SQL_Query_Label = QtWidgets.QLabel(self.Database_Page)
        self.SQL_Query_Label.setGeometry(QtCore.QRect(330, 310, 131, 31))
        self.SQL_Query_Label.setObjectName("SQL_Query_Label")
        self.SQL_Query_Button = QtWidgets.QPushButton(self.Database_Page)
        self.SQL_Query_Button.setGeometry(QtCore.QRect(920, 310, 89, 31))
        self.SQL_Query_Button.setObjectName("SQL_Query_Button")
        self.SQL_Query_Input = QtWidgets.QLineEdit(self.Database_Page)
        self.SQL_Query_Input.setGeometry(QtCore.QRect(470, 310, 421, 31))
        self.SQL_Query_Input.setObjectName("SQL_Query_Input")
        self.SQL_Query_Table = QtWidgets.QTableWidget(self.Database_Page)
        self.SQL_Query_Table.setGeometry(QtCore.QRect(0, 0, 1011, 301))
        self.SQL_Query_Table.setObjectName("SQL_Query_Table")
        self.stackedWidget.addWidget(self.Database_Page)
        self.Scripts_Page = QtWidgets.QWidget()
        self.Scripts_Page.setObjectName("Scripts_Page")
        self.stackedWidget.addWidget(self.Scripts_Page)
        self.Notes_Page = QtWidgets.QWidget()
        self.Notes_Page.setObjectName("Notes_Page")
        self.textBrowser = QtWidgets.QTextBrowser(self.Notes_Page)
        self.textBrowser.setGeometry(QtCore.QRect(30, 60, 271, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.Notes_Page)
        self.textBrowser_2.setGeometry(QtCore.QRect(370, 60, 271, 291))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.Notes_Page)
        self.textBrowser_3.setGeometry(QtCore.QRect(710, 60, 271, 291))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label = QtWidgets.QLabel(self.Notes_Page)
        self.label.setGeometry(QtCore.QRect(110, 20, 121, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Notes_Page)
        self.label_2.setGeometry(QtCore.QRect(420, 20, 161, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Notes_Page)
        self.label_3.setGeometry(QtCore.QRect(830, 20, 41, 31))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.Notes_Page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1172, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Database_Button.setText(_translate("MainWindow", "Database"))
        self.Session_Button.setStatusTip(_translate("MainWindow", "Displays information about the current session"))
        self.Session_Button.setText(_translate("MainWindow", "Session"))
        self.Analytics_Button.setText(_translate("MainWindow", "Analytics"))
        self.Notes_Button.setText(_translate("MainWindow", "Notes"))
        self.Scripts_Button.setText(_translate("MainWindow", "Scripts"))
        self.Accounts_Button.setText(_translate("MainWindow", "Accounts"))
        self.Session_Remove.setText(_translate("MainWindow", "Kill Bot"))
        self.Session_Confirm.setText(_translate("MainWindow", "Confirm"))
        self.Session_Edit.setText(_translate("MainWindow", "Edit Bot"))
        self.Session_Add.setText(_translate("MainWindow", "Add Bot"))
        self.Accounts_Add.setText(_translate("MainWindow", "Add \n"
                                                           " Account"))
        self.Accounts_Edit.setText(_translate("MainWindow", "Edit \n"
                                                            " Account"))
        self.Accounts_Remove.setText(_translate("MainWindow", "Remove \n"
                                                              " Account"))
        self.Accounts_Confirm.setText(_translate("MainWindow", "Confirm"))
        self.Database_Connect_Button.setText(_translate("MainWindow", "Connect"))
        self.Database_Connection_Status.setText(_translate("MainWindow", "Status: Not Connected"))
        self.SQL_Query_Label.setText(_translate("MainWindow", "Custom SQL Query:"))
        self.SQL_Query_Button.setText(_translate("MainWindow", "Execute"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Planned Features"))
        self.label_2.setText(_translate("MainWindow", "Current Features Notes"))
        self.label_3.setText(_translate("MainWindow", "Bugs"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))


class uiCode(Ui_MainWindow):

    sh = None
    connected = False

    def databaseQuery(self):
        print(1)
        self.stackedWidget.setCurrentWidget(self.Database_Page)
        print(2)

        print(3)
        if self.sh == None:
            self.sh = serverHandler.serverHandler("localhost", 8080)
        print(self.SQL_Query_Input.text())
        results = self.sh.getTable(self.SQL_Query_Input.text())

        # self.Session_Table.setHorizontalHeaderLabels(
        #     ("Session ID", "Username", "Script", "Current Action", "Gold Made", "Gold Muled", "PID", "Start Time"))

        self.SQL_Query_Table.setRowCount(0)
        self.SQL_Query_Table.setColumnCount(len(results[0]))
        header = self.SQL_Query_Table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        for i in range(1,len(results[0]) - 1):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        for i, item in enumerate(results):
            self.SQL_Query_Table.insertRow(i)
            for j, Property in enumerate(item):
                self.SQL_Query_Table.setItem(i, j, QtWidgets.QTableWidgetItem(Property))
        self.SQL_Query_Table.show()



    def connectToServer(self):
        if self.sh == None:
            self.sh = serverHandler.serverHandler("localhost",8080)

        status = self.sh.conenctToServer()

        if status == 0:
            self.connected = False
            self.Database_Connection_Status.setText("Failed to connect.")
        elif status == 1:
            self.connected = True
            self.Database_Connection_Status.setText("Connected Successfully.")
        elif status == 2:
            self.connected = True
            self.Database_Connection_Status.setText("Already Connected.")
        else:
            self.Database_Connection_Status.setText("Error.")

    def AddBotToSession(self):
        Add_Bot_Session = QtWidgets.QDialog()
        ui = Ui_Add_Bot_Session()
        ui.setupLogic(Add_Bot_Session)
        Add_Bot_Session.show()
        Add_Bot_Session.exec_()
        self.sessionsPage()

    def killBot(self, row):
        if self.sh == None:
            self.sh = serverHandler.serverHandler("localhost",8080)
        SessionID = self.sh.getSession()[row][0].strip()
        PID = self.sh.getSession()[row][6].strip()
        os.system(f"kill {PID}")
        self.sh.queryDB(f"DELETE FROM Session WHERE ID = '{SessionID}'")
        self.sessionsPage()


    def AddAccount(self):
        Account = QtWidgets.QDialog()
        ui = Account_Submission.Ui_Account()
        ui.setupUi(Account,self.sh)
        Account.show()
        Account.exec_()
        self.accountsPage()

    def removeAccount(self, row):
        if self.sh == None:
            self.sh = serverHandler.serverHandler("localhost",8080)
        AccountID = self.sh.getAccounts()[row][0].strip()
        self.sh.queryDB(f"DELETE FROM Account WHERE Account_ID = '{AccountID}'")
        self.accountsPage()

    def sessionsPage(self):
        self.stackedWidget.setCurrentWidget(self.Session_Page)
        header = self.Session_Table.horizontalHeader()


        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeToContents)
        if self.sh == None:
            self.sh = serverHandler.serverHandler("localhost", 8080)
        Session = self.sh.getSession()
        self.Session_Table.setHorizontalHeaderLabels(("ID", "Username", "Script", "Current Action",
                                                      "Gold Made", "Gold Muled", "PID", "Time Ran"))
        self.Session_Table.setRowCount(0)
        for i, Account in enumerate(Session[:-1]):
            self.Session_Table.insertRow(i)
            for j, Property in enumerate(Account):
                if j == 7:
                    millis = int(round(time.time() * 1000))
                    self.Session_Table.setItem(i, j, QtWidgets.QTableWidgetItem(str(int((millis - int(Property)) / 60000))))
                else:
                    self.Session_Table.setItem(i, j, QtWidgets.QTableWidgetItem(str(Property)))
        self.Session_Table.show()
    def accountsPage(self):
        header = self.Accounts_Table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        if self.sh == None:
            self.sh = serverHandler.serverHandler("localhost",8080)
        self.stackedWidget.setCurrentWidget(self.Accounts_Page)
        Accounts = self.sh.getAccounts()
        self.Accounts_Table.setHorizontalHeaderLabels(("ID","Email", "Password", "Username", "IP", "Port", "Script", "Running", "Banned"))
        self.Accounts_Table.setRowCount(0)
        for i, Account in enumerate(Accounts[:-1]):
            self.Accounts_Table.insertRow(i)
            for j, Property in enumerate(Account):
                self.Accounts_Table.setItem(i,j,QtWidgets.QTableWidgetItem(str(Property)))
        self.Accounts_Table.show()

    def setUpButtons(self):
        # self.tablesize()
        #setup main ui
        self.setupUi(self)
        self.sessionsPage()

        #Setup database tab
        self.Database_Button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Database_Page)
)
        self.SQL_Query_Button.clicked.connect(lambda: self.databaseQuery())
        self.Database_Connect_Button.clicked.connect(lambda: self.connectToServer())

        #Setup Session tab
        self.Session_Button.clicked.connect(lambda: self.sessionsPage())
        self.Session_Add.clicked.connect(lambda : self.AddBotToSession())
        self.Session_Remove.clicked.connect(lambda: self.killBot(self.Session_Table.currentRow()))
        #Setup Analytics tab
        self.Analytics_Button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Analytics_Page))

        #Setup Notes tab
        self.Notes_Button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Notes_Page))

        #Setup Scripts tab
        self.Scripts_Button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Scripts_Page))
        #Setup Accounts tab
        self.Accounts_Button.clicked.connect(lambda: self.accountsPage())
        self.Accounts_Add.clicked.connect(lambda: self.AddAccount())
        self.Accounts_Remove.clicked.connect(lambda: self.removeAccount(self.Accounts_Table.currentRow()))

    # def tablesize(self):
    #     header = self.Accounts_Table.horizontalHeader()
    #     header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    #     header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
    #     header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

    def showSession(self):
        pass
    def showDatabase(self):
        pass
    def showNotes(self):
        pass
    def showScripts(self):
        pass
    def showAnalytics(self):
        pass