# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\w0404884\OneDrive - Nova Scotia Community College\Courses\PROG-1700 - Logic Prog\Week12\UISamples\DisplayImage\DisplayImage.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(262, 303)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelPicture = QtWidgets.QLabel(self.centralwidget)
        self.labelPicture.setGeometry(QtCore.QRect(20, 20, 221, 201))
        self.labelPicture.setText("")
        self.labelPicture.setObjectName("labelPicture")
        self.checkBoxDisplayImage = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxDisplayImage.setGeometry(QtCore.QRect(70, 240, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBoxDisplayImage.setFont(font)
        self.checkBoxDisplayImage.setTristate(False)
        self.checkBoxDisplayImage.setObjectName("checkBoxDisplayImage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 262, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Display Image Example"))
        self.checkBoxDisplayImage.setText(_translate("MainWindow", "Display Image"))

