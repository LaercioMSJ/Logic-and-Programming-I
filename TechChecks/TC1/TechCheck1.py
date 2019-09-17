###########################################
# Desc: .
#
# Author: Laercio.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # Input
    bill = input("Please enter your original bill amount: ")
    #bill = 85
    tax = 0.15
    tip = 0.20

    # Process
    tax_result = float(bill) * float(tax)
    tip_result = float(bill) * float(tip)
    total = float(bill) + float(tax_result) + float(tip_result)

    # Output
    print("Your original bill amount is: " + str(bill))
    print("Your tax is: " + str(round(tax_result, 2)))
    print("Your tip is: " + str(round(tip_result, 2)))
    print("Your total is: " + str(round(total, 2)))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()