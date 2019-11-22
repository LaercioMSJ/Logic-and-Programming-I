import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap

#import generated UI file here
import Ui_DisplayImage

class MyForm(QMainWindow, Ui_DisplayImage.Ui_MainWindow):

        #DO NOT MODIFY THIS SECTION OF CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        #END DO NOT MODIFY

        #ADD SLOTS HERE
        #slot for detecting when the checkbox is checked or unchecked
        self.checkBoxDisplayImage.stateChanged.connect(self.checkbox_changed)


    #ADD SLOT FUNCTIONS HERE
    #function to execute when the checkbox slot is activated (checked or unchecked in UI)
    def checkbox_changed(self, value):
        self.toggle_image_display(value)


    #ADD ALL OTHER HELPER FUNCTIONS HERE
    def toggle_image_display(self, value):

        if value == 2: #checked
            # Change path if necessary...
            image = QPixmap("PYQT Demos\\UISamples\\DisplayImage\\images\\smiley.png")
        else: #unchecked
            image = QPixmap() #no image

        #set the label with the selected pixmap
        self.labelPicture.setPixmap(image)



#DO NOT MODIFY THIS SECTION OF CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
#END DO NOT MODIFY