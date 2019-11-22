import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

#import generated UI file here
import Ui_SaveData
import csv

class MyForm(QMainWindow, Ui_SaveData.Ui_MainWindow):

    # declare a list variable that will hold all
    # of the people data loaded from file into memory
    people = []

    # if the user updates values in the list this value should be toggled
    # to true...so that when they exit, they can be prompted to save their updates to the file
    # before the application closes
    unsaved_changes = False

        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        # slot for when the button is clicked
        self.pushButtonUpdate.clicked.connect(self.update_people)
        # slot for when an item is selected in the list
        self.listPeople.currentRowChanged.connect(self.person_selected_from_list)
        # slot for when the Exit command in the menu is clicked
        self.actionExit.triggered.connect(self.exit_program)
        # slot for when the Save to File command in the menu is clicked
        self.actionSave_to_File.triggered.connect(self.save_action_clicked)

        # setup form by automatically loading data from file and filling UI list
        # when the form starts up
        self.load_people_from_file()
        self.populate_list_with_people()

    # ADD SLOT FUNCTIONS HERE
    def person_selected_from_list(self, selected_index):#<- selected_index is the index of the item that was selected in the ui list
        #get the appropriate data from the people[] list and
        #fill the textboxes with each value
        self.display_person_data(selected_index)

    def update_people(self):
        # determine the index of the currently selected person in the list
        selected_index = self.listPeople.currentRow()
        # update the data in memory (people[]) with the values in the text boxes
        self.people[selected_index][0] = self.lineEditName.text() #<- .text() gets the current value from the textbox
        self.people[selected_index][1] = self.lineEditAge.text()
        # reload the list in case the name was changed...we want the change to be reflected in the UI list
        self.populate_list_with_people()
        # popup a message to the user to let them know that the data was updated
        QMessageBox.information(self,
                                'Updated',
                                'Data has been updated in memory, but hasn''t been updated in the file yet',
                                QMessageBox.Ok)
        # toggle the unsaved_changes variable to True so that the program
        # prompts you to save to file when shutting down.
        self.unsaved_changes = True

    def exit_program(self):
        QApplication.closeAllWindows()

    def save_action_clicked(self):
        # call the save_changes_to_file helper function which does the heavy lifting
        self.save_changes_to_file()
        # popup a message to the user confirming that the changes were saved to the file
        QMessageBox.information(self, 'Saved', 'Changes were saved to the file', QMessageBox.Ok)
        # toggle the unsaved_changes variable back to False because we no longer have any unsaved changes
        self.unsaved_changes = False


    # ADD ALL OTHER HELPER FUNCTIONS HERE
    def load_people_from_file(self):
        self.people.clear()

        # open People.txt file with csv reader and read data into people list
        # You may have to adjust the path.
        with open("PYQT Demos\\UISamples\\SaveData\People.txt", "r") as myFile:
            # load data into reader object
            fileData = csv.reader(myFile)
            # loop through each line in reader...each line is a list of values
            for row in fileData:
                # add each list to the people list variable declared above
                self.people.append(row)


    def populate_list_with_people(self):
        self.listPeople.clear()
        # load the list with the names of the people in the people[] list
        # that was loaded from the text file
        for person in self.people:
            self.listPeople.addItem(person[0])


    def display_person_data(self, selected_index): #<- selected_index is the index of the item
                                                   # that was selected in the ui list
                                                   # for example if the first person in the list was
                                                   # selected then the selected_index value would be 0

        # retrieve the appropriate data from the people list which
        # contains the data that was loaded from the file
        person_name = self.people[selected_index][0] #<- 0 is the name (the first value in the line)
        person_age = self.people[selected_index][1]  #<- 1 is the age (the second value in the line)

        # set the values to the labels on the form
        self.lineEditName.setText(person_name)
        self.lineEditAge.setText(person_age)

    def closeEvent(self, event):

        if self.unsaved_changes == True:

            msg = "Save changes to file before closing?"
            reply = QMessageBox.question(self, 'Save?',
                     msg, QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.save_changes_to_file()
                event.accept()

    def save_changes_to_file(self):
        # open the file for writing (w). Make sure it is the same location as the file you opened.
        with open("PYQT Demos\\UISamples\\SaveData\People.txt", "w") as myFile:
            #loop through each list within the in-memory people list
            for person in self.people: #<- refer to each list as person
                # join each value in the person list and write them with a line break
                myFile.write(",".join(person) + "\n")



# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY