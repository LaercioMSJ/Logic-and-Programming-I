###########################################
# Desc: Write a program that will allow the user to enter two numbers
# The program will print the results of four calculations:
# The result of adding the two user-entered numbers
# The result of subtracting the two user-entered numbers
# The result of multiplying the two user-entered numbers
# The result of dividing the two user-entered numbers
# All of the mathematical operations must be written in four separate functions.
#
# Date: 09 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    firtNumber = float(input("\nPlease, enter the first number: "))
    secondNumber = float(input("Please, enter the second number: "))

    # PROCESS

    def adding(value1, value2):
        return value1 + value2

    def subtracting(value1, value2):
        return value1 - value2

    def multiplying(value1, value2):
        return value1 * value2

    def dividing(value1, value2):
        return value1 / value2


    # OUTPUT
    print("\nAdding: {0:.2f}, subtracting: {1:.2f}, multiplying: {2:.2f}, dividing: {3:.2f}".format\
        (adding(firtNumber, secondNumber), subtracting(firtNumber, secondNumber), multiplying(firtNumber, secondNumber), dividing(firtNumber, secondNumber)))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()