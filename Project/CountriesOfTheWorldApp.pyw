###########################################
# Desc: PROG 1700 - Final Project (GUI)
#
# Date: 09 December 2019
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
#
######################################################

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_CountriesOfTheWorld
import csv

#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_CountriesOfTheWorld.Ui_MainWindow):

    # Declaration of countries list with empty which will receive all data from all countries
    countries = []
    # Declaration of updateSaved variable boolean type that helps verify if the file needs to be saved
    updateSaved = True


        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        # When the user clicks on the "Load Countries" tab the program executes this line
        self.actionLoad_Countries.triggered.connect(self.actionLoadCountries)

        # When the user clicks on a country in the list the program executes this line
        self.listCountries.currentRowChanged.connect(self.countrySelectedFromList)

        # When the user clicks on the "Update Population" button the program executes this line
        self.pushButtonUpdate.clicked.connect(self.updateCountries)

        # When the user selects an area unit of measure the program executes this line
        self.comboBoxTotal_Area_In.currentIndexChanged.connect(self.comboAreaSelection)

        # When the user clicks on an area unit of measure for density, the program executes this line
        self.radioButtonSquare_Mile.toggled.connect(self.radioDensitySelection)
        self.radioButtonSquare_KM.toggled.connect(self.radioDensitySelection)

        # When the user clicks on the "Save To File" tab the program executes this line
        self.actionSave_To_File.triggered.connect(self.userWantsToSave)

        # When the user clicks on the "Exit" tab the program executes this line
        self.actionExit.triggered.connect(self.exitApplication)
        
        # Calls function that hides almost all items
        self.hideAllFields()



    # ADD SLOT FUNCTIONS HERE
    # Function executed when clicked on the "Load Countries" tab
    def actionLoadCountries(self):
        # Calls the function that loads the country information contained in countries.txt to "countries" list
        self.loadCountriesFromFile()
        # Calls the function that adds countries names to the List Object
        self.populateListWithCountries()
        # Calls function that hides almost all items when the user clicks on the "Load Countries" tab again after the program is already started and used
        self.hideAllFields()

    
    # Function executed when clicked on a country in the list
    def countrySelectedFromList(self, selectedIndex):#<- SelectedIndex is the index of the item that was selected in the ui list
        # Retrieves the name from the selected country and add to countryName variable
        countryName = self.countries[selectedIndex][0] #<- 0 is the name (the first value in the line)

        # Set the values to the labels on the form
        self.labelCountry_Name.setText(countryName)

        # Calls the function that shows the image of the flag of the selected country
        self.displayCountryFlag(countryName)

        # Calls the function that shows the population of the selected country
        self.showPopulation(selectedIndex)

        # Calls the function that checks the unit of measure of the area that is selected, converts if necessary and displays the area of the selected country
        self.comboAreaSelection()

        # Calls the function that checks the unit of measure of the area that is selected, converts if necessary and displays the population density of the selected country
        self.radioDensitySelection()

        # Calls the function that calculates the percentage of the world population that the selected country has
        self.percentageOfWorldPopulation(selectedIndex)

        # Calls function that shows almost all items
        self.showAllFields()


    # Function executed when clicked on the "Update Population" button
    def updateCountries(self):
        # Determine the index of the currently selected country in the list
        selectedIndex = self.listCountries.currentRow()

        # Checks if user entered population value is an integer
        try:
            countryPopulation = int(self.lineEditCountry_Population.text().replace(",",""))
        except:
            # If the entered value is not an integer, an error message is displayed on the screen
            QMessageBox.information(self, 'Invalid', 'Data is invalid so not updated in memory.', QMessageBox.Ok)
            self.showPopulation(selectedIndex)
            return

        # Update the data in memory with the user entered population value
        self.countries[selectedIndex][1] = str(countryPopulation)

        # Calls function that displays updated and correctly formatted population value
        self.showPopulation(selectedIndex)

        # Popup a message to the user to let them know that the data was updated
        QMessageBox.information(self, "Updated", "Data has been updated in memory, but hasn\'t been updated in the file yet.", QMessageBox.Ok)
        
        # Toggle the updateSaved variable to False so that the program prompts you to save to file when shutting down.
        self.updateSaved = False

        # Calls the functions below to update the calculated values based on the country's population.
        # Calls the function that checks the unit of measure of the area that is selected, converts if necessary and displays the population density of the selected country
        self.radioDensitySelection()
        # Calls the function that calculates the percentage of the world population that the selected country has
        self.percentageOfWorldPopulation(selectedIndex)

        # Enables "Save To File" tab and disables "Load Countries" tab so that user can save changes
        self.actionSave_To_File.setEnabled(True)
        self.actionLoad_Countries.setEnabled(False)


    # Function executed when selected an area unit of measure
    def comboAreaSelection(self):
        # Constant to convert miles to kms
        milesToKmConstant = 1.60934

        # Determine the index of the currently selected country in the list
        selectedIndex = self.listCountries.currentRow()

        # Retrieves the area in miles from the selected country and add to areaInMiles variable
        areaInMiles = float(self.countries[selectedIndex][2])

        # Check if comboBoxTotal_Area_In is selected in the "Sq. KMs" option
        if self.comboBoxTotal_Area_In.currentText() == "Sq. KMs":
            # If comboBoxTotal_Area_In is selected in the "Sq. KMs" option, calculates area in KMs and displays value in labelCountry_Area
            self.labelCountry_Area.setText("{0:,.1f}".format(areaInMiles * milesToKmConstant))

        # Check if comboBoxTotal_Area_In is selected in the "Sq. Miles" option
        elif self.comboBoxTotal_Area_In.currentText() == "Sq. Miles":
            # If comboBoxTotal_Area_In is selected in the "Sq. Miles" option, displays area in Miles in labelCountry_Area
            self.labelCountry_Area.setText("{0:,.1f}".format(areaInMiles))

    
    # Function executed when clicked on an area unit of measure for density
    def radioDensitySelection(self):
        # Constant to convert miles to kms
        milesToKmConstant = 1.60934

        # Determine the index of the currently selected country in the list
        selectedIndex = self.listCountries.currentRow()

        # Retrieves the population from the selected country and add to countryPopulation variable
        countryPopulation = int(self.countries[selectedIndex][1])  #<- 1 is the population (the second value in the line)

        # Retrieves the area in miles from the selected country and add to areaInMiles variable
        areaInMiles = float(self.countries[selectedIndex][2])  #<- 2 is the area (the third value in the line)

        # Check if radioButtonSquare_Mile is selected
        if self.radioButtonSquare_Mile.isChecked() == True:
            # If radioButtonSquare_Mile is selected, calculates density in miles and displays value in labelPopulation_Density
            density = countryPopulation/areaInMiles
            self.labelPopulation_Density.setText("{0:,.2f}".format(density))

        # Check if radioButtonSquare_KM is selected
        elif self.radioButtonSquare_KM.isChecked() == True:
            # If radioButtonSquare_KM is selected, calculates density in KMs and displays value in labelPopulation_Density
            density = countryPopulation/(areaInMiles * milesToKmConstant)
            self.labelPopulation_Density.setText("{0:,.2f}".format(density))


    # Function executed when clicked on the "Save To File" tab
    def userWantsToSave(self):
        # Enables "Load Countries" tab and disables "Save To File" tab so the user cannot save again until they make new changes
        self.actionSave_To_File.setEnabled(False)
        self.actionLoad_Countries.setEnabled(True)
        # Calls the function that saves changes to countries.txt
        self.saveChangesToFile()


    # Function executed when clicked on the "Exit" tab
    def exitApplication(self):
        # When the user clicks on the "Exit" tab the program is closed
        QApplication.closeAllWindows()



    #ADD HELPER FUNCTIONS HERE
    # Function that loads the country information contained in countries.txt to "countries" list
    def loadCountriesFromFile(self):
        # Clears all list data
        self.countries.clear()
        # Variable used to check if the file is empty
        i = 0

        # Checks if the file exists and is in the correct location
        try:
            # Open countries.txt file with csv reader and read data into countries list.
            with open("Project\\Files\\countries.txt", "r") as myFile:

                # Loads data into reader object
                fileData = csv.reader(myFile)
                # loop through each line in reader...each line is a list of values
                for row in fileData:
                    # add each list to the countries list variable declared above
                    self.countries.append(row)
                    i += 1

        # If the file does not exist or is in the wrong location, an error message is displayed on the screen
        except:
            QMessageBox.information(self, 'File Not Found', 'Please confirm that the countries.txt file is in the Project\Files folders!', QMessageBox.Ok)
            return

        # Checks if the file is empty
        if i == 0:
            # popup a message to the user to let them know that the file is empty
            QMessageBox.information(self, "Empty File", "countries.txt file is empty!", QMessageBox.Ok)

        # Calls the function that checks if the data contained in the countries.txt file is in the correct format
        self.dataValidation()


    # Function that checks if the data contained in the countries.txt file is in the correct format
    def dataValidation(self):

        # Checks if the data contained in the countries.txt file is in the correct format
        try:
            for row in range (len(self.countries)):
                str(self.countries[row][0])
                int(self.countries[row][1])
                float(self.countries[row][2])

        # If the data contained in the countries.txt file is in the wrong format, an error message is displayed on the screen
        except:
            QMessageBox.information(self, 'Non-standard file', 'The contents of the file must be organized in the format "country, population, area". In which country contains letters, the population contains integers and the area contains floating numbers.', QMessageBox.Ok)
            self.countries.clear()
            return
        

    # Function that adds countries names to the List Object
    def populateListWithCountries(self):
        self.listCountries.clear()

        for country in self.countries:
            self.listCountries.addItem(country[0])


    # Function that shows the image of the flag of the selected country 
    def displayCountryFlag(self, nameOfTtheCountry):
        # Sets the labelCountry_Flag with the selected pixmap
        self.labelCountry_Flag.setPixmap(QPixmap("Project\\Files\\Flags\\" + nameOfTtheCountry.replace(" ","_") + ".png"))


    # Function that shows the population of the selected country
    def showPopulation(self, selectedIndex):
        # Retrieves the population from the selected country and add to countryPopulation variable
        countryPopulation = int(self.countries[selectedIndex][1])  #<- 1 is the population (the second value in the line)
        self.lineEditCountry_Population.setText("{0:,}".format(countryPopulation))


    # Function that calculates the percentage of the world population that the selected country has
    def percentageOfWorldPopulation(self, selectedIndex):
        # Retrieves the population from the selected country and add to population variable
        population = int(self.countries[selectedIndex][1]) #<- 1 is the population (the second value in the line)

        # Declaration of totalPopulationOfTheWorld variable of integer type with 0
        totalPopulationOfTheWorld = 0

        # loop to sum the population of all countries
        for i in range(len(self.countries)):
            totalPopulationOfTheWorld += int(self.countries[i][1])

        # Calculate to find out the percentage of the world population that the selected country has
        percentage = (population * 100) / totalPopulationOfTheWorld
        
        # Sets the labelCountry_Percentage with the result
        self.labelCountry_Percentage.setText("{0:.4f}%".format(percentage))


    # Function that hides almost all items
    def hideAllFields(self):
        self.labelCountry_Name.hide()
        self.labelCountry_Flag.hide()
        self.labelPopulation.hide()
        self.pushButtonUpdate.hide()
        self.lineEditCountry_Population.hide()
        self.labelTotal_Area_In.hide()
        self.comboBoxTotal_Area_In.hide()
        self.labelCountry_Area.hide()
        self.groupBoxPopulation_Density.hide()
        self.labelPercentage_Of_World.hide()
        self.labelCountry_Percentage.hide()


    # Function that shows almost all items
    def showAllFields(self):
        self.labelCountry_Name.show()
        self.labelCountry_Flag.show()
        self.labelPopulation.show()
        self.lineEditCountry_Population.show()
        self.pushButtonUpdate.show()
        self.labelTotal_Area_In.show()
        self.comboBoxTotal_Area_In.show()
        self.labelCountry_Area.show()
        self.groupBoxPopulation_Density.show()
        self.labelPercentage_Of_World.show()
        self.labelCountry_Percentage.show()


    # Function that identified any attempt to close the application
    def closeEvent(self, event):
        # Checks if the "Update Population" button has been clicked and not yet saved the changes
        if self.updateSaved == False:

            # If the "Update Population" button has been clicked and not yet saved the changes, application asks the user if they want to save changes
            reply = QMessageBox.question(self, "Save?", "Save changes to file before closing?", QMessageBox.Yes, QMessageBox.No)

            # If user clicks "Yes", calls the function that saves the changes to the countries.txt
            if reply == QMessageBox.Yes:
                self.userWantsToSave()
                event.accept()


    # Function that saves changes to countries.txt
    def saveChangesToFile(self):
        # Checks if the file exists and is in the correct location
        try:
            # open the file for writing (w). Make sure it is the same location as the file you opened.
            with open("Project\\Files\\countries.txt", "w") as myFile:
                #loop through each list within the in-memory country list
                for country in self.countries: #<- refer to each list as person
                    # join each value in the country list and write them with a line break
                    myFile.write(",".join(country) + "\n")
            
            # Changes the value in the updateSaved variable so that the user can close the application without receiving a message asking to save the changes again
            self.updateSaved = True

        # If the file does not exist or is in the wrong location, an error message is displayed on the screen
        except:
            QMessageBox.information(self, 'File Not Found', 'Please confirm that the countries.txt file is in the Project\Files folders!', QMessageBox.Ok)
            return

        # Popup a message to the user to let them know that the data was saved
        QMessageBox.information(self, "Saved", "Country data has been saved to file.", QMessageBox.Ok)



# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY
