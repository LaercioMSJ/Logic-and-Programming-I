###########################################
# Desc: Tech Check 2 - Tax Withheld Calculator.
#
# Author: Laercio.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    print("Tax Withheld Calculator")

    # Input
    # weeklySalary = 1000
    weeklySalary = input("\nPlease enter the full amount of your weekly salary: ")
    # dependents = 2
    dependents = input("How many dependents do you have? ")
    provincialTaxRate = 0.06
    federalTaxRate = 0.25
    dependentsTaxRate = 0.02

    # Process
    provincialTaxWithheld = float(weeklySalary) * float(provincialTaxRate)
    federalTaxWithheld = float(weeklySalary) * float(federalTaxRate)
    dependentDeduction = float(weeklySalary) * (int(dependents) * float(dependentsTaxRate))
    totalWithheld = (provincialTaxWithheld + federalTaxWithheld) - dependentDeduction
    totalTakeHomePay = float(weeklySalary) - totalWithheld

    # Output
    #print("{0:.2f}".format(provincialTaxWithheld))
    print("\nProvincial Tax Withheld: ${0:.2f}".format(provincialTaxWithheld))
    #print("{0:.2f}".format(federalTaxWithheld))
    print("Federal Tax Withheld: ${0:.2f}".format(federalTaxWithheld))
    #print("{0:.0f} {1:.2f}".format(int(dependents), dependentDeduction))
    print("Dependent Deduction for {0:.0f} dependents: ${1:.2f}".format(int(dependents), dependentDeduction))
    #print("{0:.2f}".format(totalWithheld))
    print("Total Withheld: ${0:.2f}".format(totalWithheld))
    #print("{0:.2f}".format(totalTakeHomePay))
    print("Total Take-Home Pay: ${0:.2f}".format(totalTakeHomePay))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()