import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

#import generated UI file here
import Ui_RadioButtons

class MyForm(QMainWindow, Ui_RadioButtons.Ui_MainWindow):

        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        self.radioButtonRed.clicked.connect(self.radio_red_clicked)
        self.radioButtonBlue.clicked.connect(self.radio_blue_clicked)
        self.radioButtonGreen.clicked.connect(self.radio_green_clicked)
        self.radioButtonYellow.clicked.connect(self.radio_yellow_clicked)
        self.radioButtonDarkGray.clicked.connect(self.radio_darkGray_clicked)

    # ADD SLOT FUNCTIONS HERE
    def radio_red_clicked(self, enabled):
        if enabled:
            self.set_background("red")

    def radio_blue_clicked(self, enabled):
        if enabled:
            self.set_background("blue")

    def radio_green_clicked(self, enabled):
        if enabled:
            self.set_background("green")

    def radio_yellow_clicked(self, enabled):
        if enabled:
            self.set_background("yellow")
    
    def radio_darkGray_clicked(self, enabled):
        if enabled:
            self.set_background("darkgray")


    #ADD HELPER FUNCTIONS HERE

    def set_background(self, color):
        self.labelColor.setStyleSheet("background-color: {};".format(color))


# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY