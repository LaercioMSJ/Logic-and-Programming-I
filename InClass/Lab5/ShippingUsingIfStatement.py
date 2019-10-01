###########################################
# Desc: Calculate shipping charges for a shopper
# Ask the user to enter the amount for their total purchase
# If their total is under $50 add $10, otherwise shipping is free
# Tell the user their final total including shipping costs and format the number so it looks like a monetary value
# Don’t forget to test your solution with 
# a value > 50
# a value < 50
# a value of exactly 50
#
# Date: 01 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.


    # INPUT
    # Declaration of totalPurchase variable with input of a float value via keyboard
    totalPurchase = float(input("Please, enter the amount of your total purchase: "))

    # Declaration of shipping variable
    shipping = float(10)


    # PROCESS
    # If statement
    if totalPurchase < 50:
        finalTotal = totalPurchase + shipping
        print("Including ${1:.2f} shipping costs for your purchase.".format(finalTotal,shipping))
    else:
        finalTotal = totalPurchase
        print("Not included shipping cost for your purchase.")


    # OUTPUT
    # Program shows on-screen the sentence contained within the quotation marks and the value contained in the variable finalTotal.
    # The format method is used to return the formatted string.
    print("Your final total is ${0:.2f}.".format(finalTotal))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()