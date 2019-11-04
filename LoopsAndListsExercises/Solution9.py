###########################################
# Desc: Write a program that reads numbers and adds them to a
#  list if they aren’t already contained in the list.
#  When the list contains ten numbers, the program
#  displays the contents and quits.
#
# Date: 01 November 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.


    # INPUT
    listOfNumbers = []

    while 10 > len(listOfNumbers):
        inputedValue = input("\nPlease, enter a number: ")

        if inputedValue.isnumeric():

            valueCounter = listOfNumbers.count (int(inputedValue))

            if valueCounter == 0:
                listOfNumbers.append (int(inputedValue))


    # PROCESS

    # OUTPUT
    print("\nThe list contains ten different numbers: " + str(listOfNumbers))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()