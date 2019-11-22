import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_MessageBoxDemo

#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_MessageBoxDemo.Ui_MainWindow):

        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        self.pushButtonMessageBox.clicked.connect(self.pushButtonMessageBox_Clicked)


    # ADD SLOT FUNCTIONS HERE. Format: WidgetName_Event
    def pushButtonMessageBox_Clicked(self):
        # Call helper function
        self.displayMessageBox()


    #ADD HELPER FUNCTIONS HERE
    def displayMessageBox(self):
        QMessageBox.warning(self, "Message Box Title", \
                                "Here is a message box text!", \
                                QMessageBox.Ok)



# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY
