# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\w0404884\OneDrive - Nova Scotia Community College\Courses\PROG-1700 - Logic Prog\Week12\UISamples\SaveData\SaveData.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(295, 274)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listPeople = QtWidgets.QListWidget(self.centralwidget)
        self.listPeople.setGeometry(QtCore.QRect(20, 40, 121, 192))
        self.listPeople.setObjectName("listPeople")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButtonUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(180, 150, 91, 23))
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 93, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 123, 31, 16))
        self.label_3.setObjectName("label_3")
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(180, 90, 91, 20))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditAge = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditAge.setGeometry(QtCore.QRect(180, 120, 91, 20))
        self.lineEditAge.setObjectName("lineEditAge")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 295, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_to_File = QtWidgets.QAction(MainWindow)
        self.actionSave_to_File.setObjectName("actionSave_to_File")
        self.menuFile.addAction(self.actionSave_to_File)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Save Data Example"))
        self.label.setText(_translate("MainWindow", "People"))
        self.pushButtonUpdate.setText(_translate("MainWindow", "Update"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Age"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSave_to_File.setText(_translate("MainWindow", "Save to File"))

