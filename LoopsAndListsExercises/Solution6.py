###########################################
# Desc: Write a program that reads a set of floating-point\
#  values. Ask the user to enter the values, then print:
# 
# The average of the values
# The smallest of the values
# The largest of the values
# The range, that is the difference between the smallest and largest
#
# Date: 29 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.


    # INPUT
    setOfFloating = []
    chosenFloating = " "

    x = 0
    while chosenFloating.upper() !="DONE":
        x += 1
        chosenFloating = input("\nPlease, enter the " + str(x) + "° floating-point value (enter DONE if no more names): ")
        if chosenFloating.upper() != "DONE":
            for char in chosenFloating:
                if char in "1234567890.":
                    b = True
                else:
                    continue

            setOfFloating.append (float(chosenFloating))


    averageOfTheValues = 0.0
    sumOfTheValues = 0.0

    smallestOfTheValues = 0.0

    largestOfTheValues = 0.0

    rangeOfTheValues = 0.0

    # PROCESS
    x = 0
    while (x < len(setOfFloating)):
        sumOfTheValues += setOfFloating[x]
        x += 1

    averageOfTheValues = sumOfTheValues/len(setOfFloating)


    # OUTPUT
    print("\nThe average of the values: " + str(averageOfTheValues))

    print("\nThe smallest of the values: " + str(smallestOfTheValues))

    print("\nThe largest of the values: " + str(largestOfTheValues))

    print("\nThe range, that is the difference between the smallest and largest: " + str(rangeOfTheValues))

    print("\nThe chosen floating values: " + str(setOfFloating))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()