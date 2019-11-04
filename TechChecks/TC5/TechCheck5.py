###########################################
# Desc: Highest Common Divisor.
#
# Date: 01 November 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def getHighestCommonDivisor(value1, value2):

    listValues = [value1, value2]
    controller = min(listValues)

    while ((max(listValues) % controller != 0) or (min(listValues) % controller != 0)):
        controller -= 1

    return controller


def inValid (value):
    b = True
    while b == True:

        numberInteger = input("Enter the " + value + " number: ")
        if numberInteger.isnumeric():
            break
        else:
            print("ERROR! Enter a valid " + value + " number.")
    
    return numberInteger


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    tryAgain = "Y"

    while tryAgain == "Y":

        # INPUT
        firstNumber = int(inValid("first"))

        secondNumber = int(inValid("second"))

        # PROCESS
        highestCommonDivisor = getHighestCommonDivisor (firstNumber, secondNumber)
            
        # OUTPUT
        print("The Highest Common Divisor of {0} and {1} is {2}".format(firstNumber, secondNumber, highestCommonDivisor))

        b = True
        while b == True:

            tryAgain = input("\nWould you like to try again? (y/n) ").upper()

            if tryAgain == "Y" or tryAgain == "N":
                break
            else:
                print("ERROR! Enter a valid letter.")
    
    print("\nThank you for using the HCD program.")

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()