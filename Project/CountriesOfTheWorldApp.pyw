###########################################
# Desc: PROG 1700 - Final Project (GUI)
#
# Date: 27 November 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################
#
# PSEUDOCODE:
# Open the Application
# Load the information contained in the countries.txt to a 2D list
# Show the names of all countries in the list object(GUI)
# By clicking on each country name, information regarding population,
#  area, density, percentage of world population should be shown on the screen
# Select unit of measure to show area (Miles or KMs)
# Select unit of measure to show density (Miles or KMs)
# Possibility to change the population of each country,
#  and click the update button to update the population contained in the 2D list
# Click save to save the information contained in the 2D list to the countries.txt file
# If user tries to close application without saving,
#  a message will be displayed on the screen asking if user wants to save changes
##
######################################################

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_CountriesOfTheWorld
import csv

#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_CountriesOfTheWorld.Ui_MainWindow):


    countries = []

    updateSaved = True


        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        self.actionLoad_Countries.triggered.connect(self.actionLoadCountries)

        self.listCountries.currentRowChanged.connect(self.countrySelectedFromList)

        self.pushButtonUpdate.clicked.connect(self.updateCountries)

        self.actionExit.triggered.connect(self.exitApplication)

        self.radioButtonSquare_Mile.clicked.connect(self.radioDensitySelection)
        self.radioButtonSquare_KM.clicked.connect(self.radioDensitySelection)





        self.labelTotal_Area_In.hide()
        self.labelPopulation.hide()
        self.pushButtonUpdate.hide()
        self.lineEditCountry_Population.hide()
        self.comboBoxTotal_Area_In.hide()
        self.groupBoxPopulation_Density.hide()
        self.labelPercentage_Of_World.hide()



        self.comboBoxTotal_Area_In.currentIndexChanged.connect(self.comboAreaSelection)

    def comboAreaSelection(self):

        milesToKmConstant = 1.60934

        selectedIndex = self.listCountries.currentRow()

        areaInMiles = float(self.countries[selectedIndex][2])

        if self.comboBoxTotal_Area_In.currentText() == "Sq. KMs":

            self.labelCountry_Area.setText("{0:,.1f}".format(areaInMiles * milesToKmConstant))

        elif self.comboBoxTotal_Area_In.currentText() == "Sq. Miles":
            self.labelCountry_Area.setText("{0:,.1f}".format(areaInMiles))

    
    def radioDensitySelection(self):

        milesToKmConstant = 1.60934

        selectedIndex = self.listCountries.currentRow()

        





    # ADD SLOT FUNCTIONS HERE
    def actionLoadCountries(self):
        self.loadCountriesFromFile()
        self.populateListWithCountries()


# Perguntar sobre essa função estar aqui e nao na no helper functions #
    def countrySelectedFromList(self, selectedIndex):#<- selectedIndex is the index of the item that was selected in the ui list
        
        # retrieve the appropriate data from the countries list which
        # contains the data that was loaded from the file
        countryName = self.countries[selectedIndex][0] #<- 0 is the name (the first value in the line)
        countryPopulation = int(self.countries[selectedIndex][1])  #<- 1 is the population (the second value in the line)
        countryArea = float(self.countries[selectedIndex][2])  #<- 2 is the area (the third value in the line)

        # set the values to the labels on the form
        self.labelCountry_Name.setText(countryName)
        self.lineEditCountry_Population.setText("{0:,}".format(countryPopulation))
        self.labelCountry_Area.setText("{0:,.1f}".format(countryArea))

        self.labelPopulation_Density.setText("{0:,.2f}".format(countryPopulation/countryArea))

        totalPopulationOfTheWorld = 0
        for i in range(len(self.countries)):
            totalPopulationOfTheWorld += int(self.countries[i][1])
        
        self.labelCountry_Percentage.setText("{0:.4f}%".format(countryPopulation*100/totalPopulationOfTheWorld))

        #set the label with the selected pixmap
        self.labelCountry_Flag.setPixmap(QPixmap("Project\\Files\\Flags\\" + countryName.replace(" ","_") + ".png"))


        self.labelTotal_Area_In.show()
        self.labelPopulation.show()
        self.pushButtonUpdate.show()
        self.lineEditCountry_Population.show()
        self.comboBoxTotal_Area_In.show()
        self.groupBoxPopulation_Density.show()
        self.labelPercentage_Of_World.show()


        self.comboAreaSelection()
        self.radioDensitySelection()

    

    def updateCountries(self):
        # determine the index of the currently selected country in the list
        selected_index = self.listCountries.currentRow()
        # update the data in memory (countries[]) with the values in the text boxes
        countryPopulation = self.lineEditCountry_Population.text()
        self.countries[selected_index][1] = countryPopulation.replace(",","")


        self.lineEditCountry_Population.setText("{0:,}".format(int(countryPopulation.replace(",",""))))
        # popup a message to the user to let them know that the data was updated
        QMessageBox.information(self,"Updated","Data has been updated in memory, but hasn\'t been updated in the file yet",QMessageBox.Ok)
        # toggle the updateSaved variable to False so that the program
        # prompts you to save to file when shutting down.
        self.updateSaved = False

        self.actionSave_To_File.setEnabled(True)



    def exitApplication(self):
        QApplication.closeAllWindows()






    #ADD HELPER FUNCTIONS HERE
    def loadCountriesFromFile(self):
        self.countries.clear()

        # open People.txt file with csv reader and read data into countries list.
        # You may have to adjust file path.
        with open("Project\\Files\\countries.txt", "r") as myFile:
            # load data into reader object
            fileData = csv.reader(myFile)
            # loop through each line in reader...each line is a list of values
            for row in fileData:
                # add each list to the countries list variable declared above
                self.countries.append(row)



    def populateListWithCountries(self):
        self.listCountries.clear()

        for country in self.countries:
            self.listCountries.addItem(country[0])



    def closeEvent(self, event):

        if self.updateSaved == False:

            msg = "Save changes to file before closing?"
            reply = QMessageBox.question(self, 'Save?',
                     msg, QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.saveChangesToFile()
                event.accept()



    def saveChangesToFile(self):
        # open the file for writing (w). Make sure it is the same location as the file you opened.
        with open("Project\\Files\\countries.txt", "w") as myFile:
            #loop through each list within the in-memory people list
            for country in self.countries: #<- refer to each list as person
                # join each value in the person list and write them with a line break
                myFile.write(",".join(country) + "\n")





# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY
