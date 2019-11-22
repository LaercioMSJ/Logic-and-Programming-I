# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\w0404884\OneDrive - Nova Scotia Community College\Courses\PROG-1700 - Logic Prog\Week12\UISamples\LoadData\LoadData.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(278, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listPeople = QtWidgets.QListWidget(self.centralwidget)
        self.listPeople.setGeometry(QtCore.QRect(20, 40, 111, 192))
        self.listPeople.setObjectName("listPeople")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushLoadPeople = QtWidgets.QPushButton(self.centralwidget)
        self.pushLoadPeople.setGeometry(QtCore.QRect(20, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushLoadPeople.setFont(font)
        self.pushLoadPeople.setObjectName("pushLoadPeople")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 70, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(148, 90, 21, 16))
        self.label_3.setObjectName("label_3")
        self.labelName = QtWidgets.QLabel(self.centralwidget)
        self.labelName.setGeometry(QtCore.QRect(180, 70, 81, 16))
        self.labelName.setText("")
        self.labelName.setObjectName("labelName")
        self.labelAge = QtWidgets.QLabel(self.centralwidget)
        self.labelAge.setGeometry(QtCore.QRect(180, 90, 61, 16))
        self.labelAge.setText("")
        self.labelAge.setObjectName("labelAge")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 278, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Load Data Example"))
        self.label.setText(_translate("MainWindow", "People"))
        self.pushLoadPeople.setText(_translate("MainWindow", "Load People"))
        self.label_2.setText(_translate("MainWindow", "Name:"))
        self.label_3.setText(_translate("MainWindow", "Age:"))

