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
    totalPurchase = float(input("Please, enter the amount of your total purchase: "))
    shipping = float(10)

    # PROCESS
    if totalPurchase < 50:
        finalTotal = totalPurchase + shipping
        print("Your final total is ${0:.2f} including ${1:.2f} shipping costs.".format(finalTotal,shipping))
    else:
        finalTotal = totalPurchase
        print("Your final total is ${0:.2f}. Not included shipping cost for your purchase.".format(finalTotal))

    # OUTPUT
    print("Have a nice day.")

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()