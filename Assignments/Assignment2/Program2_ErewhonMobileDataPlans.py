###########################################
# Desc: Erewhon Mobile charges cellular customers a rate based on the total
#  amount of data used by a customer in the billing period. For simplicity,
#  customers are charge based on which range their total data usage falls
#  within. Note, it is not a cumulative charge; your program will figure
#  out which single range the usage falls into, then calculate the cost
#  based on that range’s cost. 
#
# Total Data Usage                      	 |  Rate of Charge 
# Up to and including 200Mb             	 |  $20.00 flat rate 
# Over 200Mb and up to and including 500Mb   |	$0.105 per Mb 
# Over 500Mb and up to and including 1Gb     |	$0.110 per Mb 
# Over 1Gb                                   |	$118.00 flat rate 
#
# Then, write a console application to input the customer’s usage in
#  mega/gigabytes and output the corresponding rate and charge.
# Your solution must contain examples demonstrating your understanding of
#  appropriate use of functions and core assignment concepts (decision structures).
#
# Date: 17 October 2019
#
# Author: Laercio M da Silva Junior - W0433181
###########################################


# This function multiplies two values and return the result
def multiplierFunction (value1, value2):
    return value1 * value2


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.


    # Show program title and use \n to have a space line
    print("\nErewhon Mobile Data Plans")


    # INPUT
    # Declaration of dataUsage variable with input of a float value via keyboard and used \n to have a space line
    dataUsage = float(input("\nEnter data usage (Mb): "))


    # Declaration of variables
    # Declaration of dataUsage_Rage variables with fixed values
    dataUsage_Rage1 = 200
    dataUsage_Rage2 = 500
    dataUsage_Rage3 = 1000
    
    # Declaration of rateOfCharge_FlatRate variables with fixed values
    rateOfCharge_FlatRate1 = 20.00
    rateOfCharge_FlatRate2 = 118.00

    # Declaration of rateOfCharge_PerMb variables with fixed values
    rateOfCharge_PerMb1 = 0.105
    rateOfCharge_PerMb2 = 0.110

    # Declaration of totalCharge variable with 0
    totalCharge = 0


    # PROCESS
    # Calculate totalCharge based on dataUsage, dataUsage_Rage and rateOfCharge_FlatRate or rateOfCharge_PerMb
    if dataUsage <= dataUsage_Rage1:
        totalCharge = rateOfCharge_FlatRate1

    elif dataUsage > dataUsage_Rage1 and dataUsage <= dataUsage_Rage2:
        totalCharge = multiplierFunction (rateOfCharge_PerMb1, dataUsage)

    elif dataUsage > dataUsage_Rage2 and dataUsage <= dataUsage_Rage3:
        totalCharge = multiplierFunction (rateOfCharge_PerMb2, dataUsage)

    elif dataUsage > dataUsage_Rage3:
        totalCharge = rateOfCharge_FlatRate2
        
    else:
        # Program shows on-screen the error message contained within the quotation marks if the dataUsage is incorrect
        print("\nThe data usage you entered is incorrect. Try again.")


    # OUTPUT
    # Program shows on-screen the sentence contained within the quotation marks and the value contained in the variable totalCharge.
    # The format method is used to return the formatted string and used \n to have a space line.
    print("\nTotal charge is ${0:.2f}".format(totalCharge))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()