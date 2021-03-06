###########################################
# # Desc: When passengers check in at the airline counter, they are allowed a maximum luggage weight of 50 lbs.
# If luggage exceeds the weight limit, a $25 surcharge is applied.
# Write a program to allow passengers to enter the total weight of their luggage and calculate whether to apply a surcharge.
# Your program should display a message indicating whether a surcharge is required, or not.
#
# Date: 04 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    luggageWeight = float(input("\nPlease, enter the total weight of their luggage: "))
    maxWeight = 50
    surcharge = 25
    message = ""

    # PROCESS
    if luggageWeight > maxWeight:
        message = "\nYour luggage has exceeded the weight limit. A ${:.2f} surcharge will apply.".format(surcharge)
    else:
        message = "\nYour luggage has not exceeded the weight limit. Surcharge is not required."

    # OUTPUT
    print(message)

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()