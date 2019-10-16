###########################################
# Desc: Enter application description here.
#
# Author: Enter name here.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.
    sku_one = "ABC123"
    sku_two = "ABC456"
    sku_three = "ABC789"

    # Input
    print("Welcome to my provincial tax calculator.")
    print("-" * 50)

    # Process
    sku_one_total = calculateTaxForOneSKU(sku_one)
    sku_two_total = calculateTaxForOneSKU(sku_two)
    sku_three_total = calculateTaxForOneSKU(sku_three)
    average = (sku_one_total + sku_two_total + sku_two_total) / 3

    # Output
    print()
    printSKU(sku_one, sku_one_total)
    printSKU(sku_two, sku_two_total)
    printSKU(sku_three, sku_three_total)
    print()
    print("-" * 50)
    print()
    print("Average tax is ${:.2f}".format(average))

def printSKU(skuCode, total):
    print("Your order total for SKU {0} is: ${1:.2f}".format(skuCode, total))

def calculateTaxForOneSKU(skuCode):
    taxRate_AB = 0.05
    taxRate_ON_NS_NB = 0.15
    taxRate_Other = 0.11

    orderTotal = float(input("Please enter your order total for {}: $".format(skuCode)))
    country = input("Please enter your country: ").lower()

    if country == "canada":
        #Calculate provincial taxes based on province chosen
        province = input("Please enter your province: ").lower()

        taxRate = 0

        if province == "alberta":
            #Tax rate is 5%
            taxRate = taxRate_AB
        elif (province == "ontario") or (province == "nova scotia") \
                or (province == "new brunswick"):
            #Tax rate is 15%
            taxRate = taxRate_ON_NS_NB
        else:
            #Tax rate is 11%
            #Note: Any non-province value will incorrectly end up here
            taxRate = taxRate_Other

        #Do the math calculation
        finalTaxAmount = orderTotal * taxRate

        #Display amount of tax to user
        print("Your tax total amount is: ${:.2f}".format(finalTaxAmount))

        #Re-assign the value including tax back into the original orderTotal variable
        orderTotal = finalTaxAmount + orderTotal

    else: # <-- We started with having an if-else, but removed it after we determined it wasn't needed,
            #based on how we decided to structure our program logic
        #Add no tax if it's any other country
        print("No sales tax.")
    print()
    return orderTotal
    

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()