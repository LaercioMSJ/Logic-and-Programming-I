import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

#import generated UI file here
import Ui_TaxCalculator

class MyForm(QMainWindow, Ui_TaxCalculator.Ui_MainWindow):

        #DO NOT MODIFY THIS SECTION OF CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        #END DO NOT MODIFY

        #ADD SLOTS HERE
        #slot for detecting when the Exit menu item is clicked
        self.pushButtonCalculateTax.clicked.connect(self.calculateTax)



    #ADD SLOT FUNCTIONS HERE
    def calculateTax(self):
        self.inputOfSalaryAndDependents()
 


    #ADD ALL OTHER HELPER FUNCTIONS HERE
    def inputOfSalaryAndDependents(self):

        try:
            weeklySalary = float(self.lineEditSalary.text())
            dependents = int(self.lineEditDependents.text())
        except:
            QMessageBox.information(self, 'Invalid Data', 'Please, use only numbers in this field!', QMessageBox.Ok)
            self.lineEditSalary.clear()
            self.lineEditDependents.clear()
            return

        self.calculateAllValues(weeklySalary, dependents)

    
    def calculateAllValues(self, weeklySalary, dependents):
        provincialTaxRate = 0.06
        federalTaxRate = 0.25
        dependentsTaxRate = 0.02

        provincialTaxWithheld = weeklySalary * provincialTaxRate
        federalTaxWithheld = weeklySalary * federalTaxRate
        dependentDeduction = weeklySalary * (dependents * dependentsTaxRate)
        totalWithheld = (provincialTaxWithheld + federalTaxWithheld) - dependentDeduction
        totalTakeHomePay = weeklySalary - totalWithheld

        self.displayAllValues(provincialTaxWithheld, federalTaxWithheld, dependentDeduction, totalWithheld, totalTakeHomePay, dependents)


    def displayAllValues(self, provincialTaxWithheld, federalTaxWithheld, dependentDeduction, totalWithheld, totalTakeHomePay, dependents):
        self.labelProvincialTax.setText("Provincial Tax Withheld: ${0:.2f}".format(provincialTaxWithheld))
        self.labelFederalTax.setText("Federal Tax Withheld: ${0:.2f}".format(federalTaxWithheld))
        self.labelDependentDeduction.setText("Dependent Deduction for {0:.0f} dependents: ${1:.2f}".format(dependents, dependentDeduction))
        self.labelTotalWithheld.setText("Total Withheld: ${0:.2f}".format(totalWithheld))
        self.labelTotalTakeHomePay.setText("Total Take-Home Pay: ${0:.2f}".format(totalTakeHomePay))



#DO NOT MODIFY THIS SECTION OF CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
#END DO NOT MODIFY