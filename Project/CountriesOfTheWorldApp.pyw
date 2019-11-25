import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_CountriesOfTheWorld
import csv

#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_CountriesOfTheWorld.Ui_MainWindow):


    countries = []


        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        self.actionLoad_Countries.triggered.connect(self.actionLoadCountries)

        self.listCountries.currentRowChanged.connect(self.countrySelectedFromList)

        self.actionExit.triggered.connect(self.exitApplication)


    # ADD SLOT FUNCTIONS HERE
    def actionLoadCountries(self):
        self.loadCountriesFromFile()
        self.populateListWithCountries()



    def countrySelectedFromList(self, selectedIndex):#<- selectedIndex is the index of the item that was selected in the ui list
        
        # retrieve the appropriate data from the countries list which
        # contains the data that was loaded from the file
        countryName = self.countries[selectedIndex][0] #<- 0 is the name (the first value in the line)
        countryPopulation = self.countries[selectedIndex][1]  #<- 1 is the population (the second value in the line)
        countryArea = self.countries[selectedIndex][2]  #<- 2 is the area (the third value in the line)

        # set the values to the labels on the form
        self.labelCountry_Name.setText(countryName)
        self.lineEditCountry_Population.setText(countryPopulation)
        self.labelCountry_Area.setText(countryArea)



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


# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY
