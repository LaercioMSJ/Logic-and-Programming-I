###########################################
# Desc: Enter application description here.
#
# Author: Enter name here.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.
    displayIntro()
    # Input
    hotelCost = 100
    airfareCost = 200
    baggageCost = 300

    # Process
    hotelTaxTotal = applyTax(hotelCost)
    airfareTaxTotal = applyTax(airfareCost)
    baggageTaxTotal = applyTax(baggageCost)
    grandTaxTotal = hotelTaxTotal + airfareTaxTotal + baggageTaxTotal

    # Output
    print("Total tax is ${:.2f}".format(grandTaxTotal))
    
# Display Introduction Text
def displayIntro():
    print("Welcome to my tax calculator!")

# Tax Calculation. Returns 15% of the value to tax parameter.
def applyTax(valueToTax):
    taxRate = 0.15
    value = valueToTax * taxRate
    return value

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()