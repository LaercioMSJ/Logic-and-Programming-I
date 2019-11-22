import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

#import generated UI file here
import Ui_MessageBoxes

class MyForm(QMainWindow, Ui_MessageBoxes.Ui_MainWindow):

        #DO NOT MODIFY THIS SECTION OF CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        #END DO NOT MODIFY

        #ADD SLOTS HERE
        #slot for detecting when the Exit menu item is clicked
        self.actionExit.triggered.connect(self.exit_application)
        self.actionShow_Message.triggered.connect(self.show_message_box)


    #ADD SLOT FUNCTIONS HERE
    #function to execute when the checkbox slot is activated (checked or unchecked in UI)
    def show_message_box(self):
        QMessageBox.information(self, 'Hi', 'Have a nice day!', QMessageBox.Ok)


    def exit_application(self):
        QApplication.closeAllWindows()


    #ADD ALL OTHER HELPER FUNCTIONS HERE
    def closeEvent(self, event):

        quit_msg = "Are you sure you want to exit?"
        reply = QMessageBox.question(self, 'Exit?',
                 quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



#DO NOT MODIFY THIS SECTION OF CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
#END DO NOT MODIFY