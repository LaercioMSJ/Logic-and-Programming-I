###########################################
# Desc: Write a while loop that prints:
# 
# All squares less than n. For example, if n is 100, print 0 1 4 9 16 25 36 49 64 81
# 
# All positive numbers that are divisible by 10 and less than n. For example, if n is 100, print 10 20 30 40 50 60 70 80 90
# 
# All powers of two less than n. For example, if n is 100, print 1 2 4 8 16 32 64
#
# Date: 27 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    chosenNumber = int(input("\nPlease, enter a number: "))

    squares = []
    divisibleBy10 = []
    powersOfTwo = []


    # PROCESS
    x=0
    while ((x * x) < chosenNumber):
        squares.append(x * x)
        x +=1


    x=1
    while ((10 * x) < chosenNumber):
        divisibleBy10.append(10 * x)
        x +=1


    x=0
    while ((2 ** x) < chosenNumber):
        powersOfTwo.append(2 ** x)
        x +=1


    # OUTPUT
    print("\nAll squares less than " + str(chosenNumber) + ": " + str(squares))

    print("\nAll positive numbers that are divisible by 10 and less than " + str(chosenNumber) + ": " + str(divisibleBy10))

    print("\nAll powers of two less than " + str(chosenNumber) + ": " + str(powersOfTwo))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()