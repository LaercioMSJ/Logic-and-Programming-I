###########################################
# Desc: Calculate the total to charge for an order from an online store in Canada
# Ask user what country they are from and their order total
# If the user is from Canada, ask which province
# If the order is from outside Canada do not charge any taxes
# If the order was placed in Canada calculate tax based on the province
#   Alberta charge 5% General sales Tax (GST)
#   Ontario, New Brunswick, Nova Scotia charge 15% Harmonized sales tax
#   All other provinces charge 6% provincial sales tax + 5% GST tax (11% total tax)
# Tell the user the total with taxes for their order
#
# What do you need to test to ensure your code works correctly?
#   Someone who is from outside Canada (no tax)
#   Someone from Alberta, Canada (5% tax)
#   Someone from Ontario, NS, NB (15% tax)
#   Someone from Canada from a different province (e.g. Quebec) (11% tax)
#
# Date: 02 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    country = input("\nPlease, what country are you from? ").upper()

    if country == 'CANADA':
        province = input("Please, what province are you from? ").upper()
    
    orderTotal = float(input("Please, what is your order total? "))

    taxAlberta = 5
    taxOnNbNs = 15
    taxOtherProvinces = 11

    # PROCESS
    if country == 'CANADA':
        if province == 'ALBERTA':
            totalWithTaxes = (orderTotal * taxAlberta / 100) + orderTotal
            print("\nThe total with taxes for your order is ${0:.2f} and your tax is {1:.0f}%".format(totalWithTaxes, taxAlberta))

        elif province == ('ONTARIO' or 'NEW BRUNSWICK' or 'NOVA SCOTIA'):
            totalWithTaxes = (orderTotal * taxOnNbNs / 100) + orderTotal
            print("\nThe total with taxes for your order is ${0:.2f} and your tax is {1:.0f}%".format(totalWithTaxes, taxOnNbNs))

        else:
            totalWithTaxes = (orderTotal * taxOtherProvinces / 100) + orderTotal
            print("\nThe total with taxes for your order is ${0:.2f} and your tax is {1:.0f}%".format(totalWithTaxes, taxOtherProvinces))

    else:
        print("\nThe total for your order is ${0:.2f} and you do not have tax".format(orderTotal))

    # OUTPUT

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()