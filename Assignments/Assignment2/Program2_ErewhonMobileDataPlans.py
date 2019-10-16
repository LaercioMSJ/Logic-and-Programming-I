###########################################
# Desc: .
#
# Date: XX October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.


    def multiplierFunction(value1, value2):
        return value1 * value2


    # Show program title and use \n to have a space line
    print("\nErewhon Mobile Data Plans")



    # INPUT
    # Declaration of dataUsage variable with input of a float value via keyboard and used \n to have a space line
    dataUsage = float(input("\nEnter data usage (Mb): "))


    dataUsage_Rage1 = 200
    dataUsage_Rage2 = 500
    dataUsage_Rage3 = 1000


    rateOfCharge_FlatRate1 = 20.00
    rateOfCharge_FlatRate2 = 118.00


    rateOfCharge_PerMb1 = 0.105
    rateOfCharge_PerMb2 = 0.110


    # PROCESS

    if dataUsage <= dataUsage_Rage1:
        totalCharge = rateOfCharge_FlatRate1

    elif dataUsage > dataUsage_Rage1 and dataUsage <= dataUsage_Rage2:
        totalCharge = multiplierFunction(rateOfCharge_PerMb1, dataUsage)

    elif dataUsage > dataUsage_Rage2 and dataUsage <= dataUsage_Rage3:
        totalCharge = multiplierFunction(rateOfCharge_PerMb2, dataUsage)

    elif dataUsage > dataUsage_Rage3:
        totalCharge = rateOfCharge_FlatRate2



    # OUTPUT
    # Program shows on-screen the sentence contained within the quotation marks and the value contained in the variable totalCharge.
    # The format method is used to return the formatted string and used \n to have a space line.
    print("\nTotal charge is ${0:.2f}".format(totalCharge))





#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()