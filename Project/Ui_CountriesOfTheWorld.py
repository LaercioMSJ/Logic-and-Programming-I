# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\LaercioMSJ\Desktop\NSCC\Logic and Programming I\Laercio_da_silva\Project\CountriesOfTheWorld.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 661)
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAccessibleName("")
        self.centralwidget.setAccessibleDescription("")
        self.centralwidget.setObjectName("centralwidget")
        self.listCountries = QtWidgets.QListWidget(self.centralwidget)
        self.listCountries.setGeometry(QtCore.QRect(25, 40, 271, 551))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listCountries.setFont(font)
        self.listCountries.setObjectName("listCountries")
        self.labelChoose_A_Country = QtWidgets.QLabel(self.centralwidget)
        self.labelChoose_A_Country.setGeometry(QtCore.QRect(30, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelChoose_A_Country.setFont(font)
        self.labelChoose_A_Country.setObjectName("labelChoose_A_Country")
        self.labelCountry_Name = QtWidgets.QLabel(self.centralwidget)
        self.labelCountry_Name.setGeometry(QtCore.QRect(320, 40, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelCountry_Name.setFont(font)
        self.labelCountry_Name.setText("")
        self.labelCountry_Name.setObjectName("labelCountry_Name")
        self.labelPopulation = QtWidgets.QLabel(self.centralwidget)
        self.labelPopulation.setEnabled(True)
        self.labelPopulation.setGeometry(QtCore.QRect(320, 290, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPopulation.setFont(font)
        self.labelPopulation.setObjectName("labelPopulation")
        self.labelTotal_Area_In = QtWidgets.QLabel(self.centralwidget)
        self.labelTotal_Area_In.setEnabled(True)
        self.labelTotal_Area_In.setGeometry(QtCore.QRect(320, 400, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelTotal_Area_In.setFont(font)
        self.labelTotal_Area_In.setObjectName("labelTotal_Area_In")
        self.labelCountry_Area = QtWidgets.QLabel(self.centralwidget)
        self.labelCountry_Area.setGeometry(QtCore.QRect(530, 400, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelCountry_Area.setFont(font)
        self.labelCountry_Area.setText("")
        self.labelCountry_Area.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCountry_Area.setObjectName("labelCountry_Area")
        self.labelCountry_Flag = QtWidgets.QLabel(self.centralwidget)
        self.labelCountry_Flag.setGeometry(QtCore.QRect(330, 80, 331, 171))
        self.labelCountry_Flag.setText("")
        self.labelCountry_Flag.setObjectName("labelCountry_Flag")
        self.labelPercentage_Of_World = QtWidgets.QLabel(self.centralwidget)
        self.labelPercentage_Of_World.setEnabled(True)
        self.labelPercentage_Of_World.setGeometry(QtCore.QRect(320, 550, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPercentage_Of_World.setFont(font)
        self.labelPercentage_Of_World.setObjectName("labelPercentage_Of_World")
        self.labelCountry_Percentage = QtWidgets.QLabel(self.centralwidget)
        self.labelCountry_Percentage.setGeometry(QtCore.QRect(550, 550, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelCountry_Percentage.setFont(font)
        self.labelCountry_Percentage.setText("")
        self.labelCountry_Percentage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelCountry_Percentage.setObjectName("labelCountry_Percentage")
        self.pushButtonUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonUpdate.setEnabled(True)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(510, 320, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonUpdate.setFont(font)
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.lineEditCountry_Population = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCountry_Population.setEnabled(True)
        self.lineEditCountry_Population.setGeometry(QtCore.QRect(410, 290, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditCountry_Population.setFont(font)
        self.lineEditCountry_Population.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEditCountry_Population.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditCountry_Population.setInputMask("")
        self.lineEditCountry_Population.setObjectName("lineEditCountry_Population")
        self.groupBoxPopulation_Density = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxPopulation_Density.setEnabled(True)
        self.groupBoxPopulation_Density.setGeometry(QtCore.QRect(320, 440, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBoxPopulation_Density.setFont(font)
        self.groupBoxPopulation_Density.setFlat(False)
        self.groupBoxPopulation_Density.setCheckable(False)
        self.groupBoxPopulation_Density.setObjectName("groupBoxPopulation_Density")
        self.radioButtonSquare_Mile = QtWidgets.QRadioButton(self.groupBoxPopulation_Density)
        self.radioButtonSquare_Mile.setEnabled(True)
        self.radioButtonSquare_Mile.setGeometry(QtCore.QRect(10, 30, 141, 17))
        self.radioButtonSquare_Mile.setTabletTracking(False)
        self.radioButtonSquare_Mile.setChecked(True)
        self.radioButtonSquare_Mile.setObjectName("radioButtonSquare_Mile")
        self.radioButtonSquare_KM = QtWidgets.QRadioButton(self.groupBoxPopulation_Density)
        self.radioButtonSquare_KM.setGeometry(QtCore.QRect(10, 50, 131, 17))
        self.radioButtonSquare_KM.setObjectName("radioButtonSquare_KM")
        self.labelPopulation_Density = QtWidgets.QLabel(self.groupBoxPopulation_Density)
        self.labelPopulation_Density.setGeometry(QtCore.QRect(240, 40, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPopulation_Density.setFont(font)
        self.labelPopulation_Density.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelPopulation_Density.setText("")
        self.labelPopulation_Density.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelPopulation_Density.setObjectName("labelPopulation_Density")
        self.comboBoxTotal_Area_In = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxTotal_Area_In.setEnabled(True)
        self.comboBoxTotal_Area_In.setGeometry(QtCore.QRect(420, 400, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxTotal_Area_In.setFont(font)
        self.comboBoxTotal_Area_In.setEditable(False)
        self.comboBoxTotal_Area_In.setObjectName("comboBoxTotal_Area_In")
        self.comboBoxTotal_Area_In.addItem("")
        self.comboBoxTotal_Area_In.addItem("")
        self.listCountries.raise_()
        self.labelChoose_A_Country.raise_()
        self.labelCountry_Area.raise_()
        self.labelTotal_Area_In.raise_()
        self.labelCountry_Name.raise_()
        self.labelCountry_Flag.raise_()
        self.labelPopulation.raise_()
        self.labelPercentage_Of_World.raise_()
        self.labelCountry_Percentage.raise_()
        self.pushButtonUpdate.raise_()
        self.lineEditCountry_Population.raise_()
        self.groupBoxPopulation_Density.raise_()
        self.comboBoxTotal_Area_In.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Countries = QtWidgets.QAction(MainWindow)
        self.actionLoad_Countries.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionLoad_Countries.setFont(font)
        self.actionLoad_Countries.setObjectName("actionLoad_Countries")
        self.actionSave_To_File = QtWidgets.QAction(MainWindow)
        self.actionSave_To_File.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionSave_To_File.setFont(font)
        self.actionSave_To_File.setObjectName("actionSave_To_File")
        self.actionExit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionLoad_Countries)
        self.menuFile.addAction(self.actionSave_To_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Countries of the World"))
        self.labelChoose_A_Country.setText(_translate("MainWindow", "Choose a country from the list:"))
        self.labelPopulation.setText(_translate("MainWindow", "Population:"))
        self.labelTotal_Area_In.setText(_translate("MainWindow", "Total Area in"))
        self.labelPercentage_Of_World.setText(_translate("MainWindow", "Percentage of World Population:"))
        self.pushButtonUpdate.setText(_translate("MainWindow", "Update Population"))
        self.groupBoxPopulation_Density.setTitle(_translate("MainWindow", "Population Density"))
        self.radioButtonSquare_Mile.setText(_translate("MainWindow", "Per Square Mile"))
        self.radioButtonSquare_KM.setText(_translate("MainWindow", "Per Square KM"))
        self.comboBoxTotal_Area_In.setCurrentText(_translate("MainWindow", "Sq. Miles"))
        self.comboBoxTotal_Area_In.setItemText(0, _translate("MainWindow", "Sq. Miles"))
        self.comboBoxTotal_Area_In.setItemText(1, _translate("MainWindow", "Sq. KMs"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_Countries.setText(_translate("MainWindow", "Load Countries"))
        self.actionSave_To_File.setText(_translate("MainWindow", "Save To File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
