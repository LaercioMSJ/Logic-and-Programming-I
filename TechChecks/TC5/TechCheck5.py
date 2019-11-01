###########################################
# Desc: Highest Common Divisor.
#
# Date: 01 November 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def getHighestCommonDivisor(value1, value2):

    listValues = [value1, value2]

    lowestValue = int(min(listValues))
    highestValue = int(max(listValues))
    controller = lowestValue

    while ((highestValue % controller != 0) or (lowestValue % controller != 0)):
        controller -= 1

    return controller


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    tryAgain = "y"

    while tryAgain == "y":

        # INPUT
        b = True

        while b == True:
            
            firstNumber = input("\nEnter the first number: ")
            if firstNumber.isnumeric():
                break
            else:
                print("ERROR! Enter a valid first number.")
                b = True
                continue

        while b == True:

            secondNumber = input("\nEnter the second number: ")
            if secondNumber.isnumeric():
                break
            else:
                print("ERROR! Enter a valid second number.")
                b = True
                continue

        # PROCESS
        highestCommonDivisor = getHighestCommonDivisor (firstNumber, secondNumber)
            
        # OUTPUT
        print("The Highest Common Divisor of {0:.0f} and {1:.0f} is {2:.0f}".format(int(firstNumber), int(secondNumber), int(highestCommonDivisor)))

        tryAgain = input("\nWould you like to try again? (y/n) ")
    
    print("\nThank you for using the HCD program.")

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()