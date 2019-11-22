# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\W0433181\Desktop\Programming\Laercio_da_silva-1\PYQT Demos\UISamples\RadioButtons\RadioButtons.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 237)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButtonRed = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonRed.setGeometry(QtCore.QRect(20, 160, 82, 17))
        self.radioButtonRed.setChecked(True)
        self.radioButtonRed.setObjectName("radioButtonRed")
        self.radioButtonGreen = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonGreen.setGeometry(QtCore.QRect(20, 180, 82, 17))
        self.radioButtonGreen.setObjectName("radioButtonGreen")
        self.radioButtonBlue = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonBlue.setGeometry(QtCore.QRect(100, 180, 82, 17))
        self.radioButtonBlue.setObjectName("radioButtonBlue")
        self.radioButtonYellow = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonYellow.setGeometry(QtCore.QRect(100, 160, 82, 17))
        self.radioButtonYellow.setChecked(False)
        self.radioButtonYellow.setObjectName("radioButtonYellow")
        self.labelColor = QtWidgets.QLabel(self.centralwidget)
        self.labelColor.setGeometry(QtCore.QRect(10, 10, 151, 141))
        self.labelColor.setStyleSheet("background-color:red;")
        self.labelColor.setText("")
        self.labelColor.setObjectName("labelColor")
        self.radioButtonDarkGray = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonDarkGray.setGeometry(QtCore.QRect(180, 160, 82, 17))
        self.radioButtonDarkGray.setObjectName("radioButtonDarkGray")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Laercio M da Silva"))
        self.radioButtonRed.setText(_translate("MainWindow", "Red"))
        self.radioButtonGreen.setText(_translate("MainWindow", "Green"))
        self.radioButtonBlue.setText(_translate("MainWindow", "Blue"))
        self.radioButtonYellow.setText(_translate("MainWindow", "Yellow"))
        self.radioButtonDarkGray.setText(_translate("MainWindow", "Dark Gray"))
