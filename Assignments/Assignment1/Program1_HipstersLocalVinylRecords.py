###########################################
# Desc: Program 1 – Hipster's Local Vinyl Records.
#
# Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.
# Delivery is charged at a rate of $15 per kilometer. 
#
# All purchases are subject to a 14% sales tax. 
#
# Because this store loves retro technology, you have been asked to develop a console
# application solution that will enable the company’s retail staff to calculate receipts.
# Begin by designing your solution to this problem in pseudocode, which will be submitted
# along with the program. The program user must be able to input the customer's name,
# the number of kilometers distance, and the cost of any records purchased.
# Once the input is provided, the program will display the customer's name and
# three calculated costs: delivery cost, records cost (plus tax) and total cost, as shown below.
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################
#
# PSEUDOCODE:
# Request customer name
# Request the distance in kilometers for delivery
# Request the cost of records purchased
# Calculate delivery cost (the delivery distance in kilometers multiplied by the delivery rate)
# Calculate purchase cost (the cost of records purchased multiplied by the sale rate)
# Calculate total purchase cost (the purchase cost plus delivery cost)
# Show on screen the customer name
# Show on screen the delivery cost
# Show on screen the purchase cost
# Show on screen the total purchase cost
#
######################################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # Show program title and use \n to have a space line
    print("\nHipster's Local Vinyl Records - Customer Order Details")


    # INPUT
    # Declaration of customerName variable with input of a string via keyboard and used \n to have a space line
    customerName = input("\nEnter the customer's name: ")

    # Declaration of deliveryDistance variable with input of a float value via keyboard
    deliveryDistance = float(input("Enter the distance in kilometers for delivery: "))

    # Declaration of recordsCost variable with input of a float value via keyboard
    recordsCost = float(input("Enter the cost of records purchased: "))
    
    # Declaration of fixed rate variables
    deliveryRate = 15
    salesTax = 0.14


    # PROCESS
    # Delivery cost calculation
    # Where the delivery distance in kilometers multiplied by the delivery rate results in the desired value
    deliveryCost = deliveryDistance * deliveryRate

    # Purchase cost calculation
    # Where the cost of records purchased multiplied by the sale rate results in the desired value
    purchaseCost = (recordsCost * salesTax) + recordsCost

    # Total purchase cost calculation
    # Where the purchase cost plus delivery cost results in the desired value
    totalCost = purchaseCost + deliveryCost


    # OUTPUT
    # Program shows on-screen sentence contained within quotation marks and concatenates with the string contained in the variable customerName
    # It used \n to have a space line
    print("\nPurchase summary for " + customerName.title())

    # Program shows on-screen the sentence contained within the quotation marks and the value contained in the variable deliveryCost.
    # The format method is used to return the formatted string.
    print("Delivery Cost: ${0:.2f}".format(deliveryCost))

    # Program shows on-screen the sentence contained within the quotation marks and the value contained in the variable purchaseCost.
    # The format method is used to return the formatted string.
    print("Purchase Cost: ${0:.2f}".format(purchaseCost))
    
    # Program shows on-screen the sentence contained within the quotation marks and the value contained in the variable totalCost.
    # The format method is used to return the formatted string.
    print("Total Cost   : ${0:.2f}".format(totalCost))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()