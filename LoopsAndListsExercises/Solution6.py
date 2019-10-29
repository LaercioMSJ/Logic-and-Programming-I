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

    while chosenFloating.upper() !="DONE":
        x += 1
        chosenFloating = input("\nPlease, enter the " + str(x) + "° floating-point value (enter DONE if no more names): "))
        if chosenFloating.upper() != "DONE":
            setOfFloating.append (float(chosenFloating))


    uppercaseLetters = ""

    secondLetter = ""

    allVowelsReplaced = ""
    upperAllLetters = ""

    digitsInTheString = 0

    allVowelsInTheString = []
    vowels = "aeiouAEIOU"
    position = 0

    # PROCESS














    x = 0
    while (x < len(chosenString)):
        if chosenString[x] != chosenString[x].lower():
            uppercaseLetters += chosenString[x]

        x += 1


    b = True
    x = 0
    while (x < len(chosenString)):
        if (chosenString[x] == " "):
            b = True
        
        elif (x+1) < len(chosenString):
            if (chosenString[x] != " " and b == True and chosenString[x+1] != " "):
                secondLetter += chosenString[x+1]
                b = False
        
        x += 1


    x = 0
    while (x < len(chosenString)):
        upperAllLetters += chosenString[x].upper()

        if (upperAllLetters[x] == "A" or upperAllLetters[x] == "E" or upperAllLetters[x] == "I" or upperAllLetters[x] == "O" or upperAllLetters[x] == "U"):
            allVowelsReplaced += "_"

        else:
            allVowelsReplaced += (chosenString[x])
        
        x += 1


    x = 0
    while (x < len(chosenString)):
        if (chosenString[x] == "0" or chosenString[x] == "1" or chosenString[x] == "2" or chosenString[x] == "3" or chosenString[x] == "4" or \
        chosenString[x] == "5" or chosenString[x] == "6" or chosenString[x] == "7" or chosenString[x] == "8" or chosenString[x] == "9"):
            digitsInTheString += 1
        
        x += 1

    
    x = 0
    for char in chosenString:
        if char in vowels:
            position = x
            allVowelsInTheString.append (str(char) + " - " + str(position))

        x += 1


    # OUTPUT
    print("\nThe average of the values: " + str(averageOfTheValues))

    print("\nThe smallest of the values: " + str(smallestOfTheValues))

    print("\nThe largest of the values: " + str(largestOfTheValues))

    print("\nThe range, that is the difference between the smallest and largest: " + str(rangeOfTheValues))

    print("\nThe chosen floating values: " + str(setOfFloating))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()