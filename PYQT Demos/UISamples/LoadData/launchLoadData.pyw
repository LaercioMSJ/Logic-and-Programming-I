import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

#import generated UI file here
import Ui_LoadData
import csv

class MyForm(QMainWindow, Ui_LoadData.Ui_MainWindow):

    # declare a list variable that will hold all
    # of the people data loaded from file into memory
    people = []

        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        # slot for when the button is clicked
        self.pushLoadPeople.clicked.connect(self.push_load_people)
        # slot for when an item is selected in the list
        self.listPeople.currentRowChanged.connect(self.person_selected_from_list)


    # ADD SLOT FUNCTIONS HERE
    def push_load_people(self):
        self.load_people_from_file()
        self.populate_list_with_people()

    def person_selected_from_list(self, selected_index):#<- selected_index is the index of the item that was selected in the ui list
        self.display_person_data(selected_index)


    # ADD ALL OTHER HELPER FUNCTIONS HERE
    def load_people_from_file(self):
        self.people.clear()

        # open People.txt file with csv reader and read data into people list.
        # You may have to adjust file path.
        with open("PYQT Demos\\UISamples\\LoadData\\People.txt", "r") as myFile:
            # load data into reader object
            fileData = csv.reader(myFile)
            # loop through each line in reader...each line is a list of values
            for row in fileData:
                # add each list to the people list variable declared above
                self.people.append(row)


    def populate_list_with_people(self):
        self.listPeople.clear()

        for person in self.people:
            self.listPeople.addItem(person[0])


    def display_person_data(self, selected_index): #<- selected_index is the index of the item that was selected in the ui list

        # retrieve the appropriate data from the people list which
        # contains the data that was loaded from the file
        person_name = self.people[selected_index][0] #<- 0 is the name (the first value in the line)
        person_age = self.people[selected_index][1]  #<- 1 is the age (the second value in the line)

        # set the values to the labels on the form
        self.labelName.setText(person_name)
        self.labelAge.setText(person_age)

#DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
#END DO NOT MODIFY