###########################################
# Desc: Write programs that read a line of input as a string and print:
# 
# Only the uppercase letters in the string.
# Every second letter of the string.
# The string, with all vowels replaced by an underscore.
# The number of digits in the string.
# The positions of all vowels in the string.
#
# Date: 28 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    chosenString = str(input("\nPlease, enter a string: "))
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
        if (chosenString[x].isnumeric()):
            digitsInTheString += 1
        
        x += 1
    # x = 0
    # while (x < len(chosenString)):
    #     if (chosenString[x] == "0" or chosenString[x] == "1" or chosenString[x] == "2" or chosenString[x] == "3" or chosenString[x] == "4" or \
    #     chosenString[x] == "5" or chosenString[x] == "6" or chosenString[x] == "7" or chosenString[x] == "8" or chosenString[x] == "9"):
    #         digitsInTheString += 1
        
    #     x += 1

    
    x = 0
    for char in chosenString:
        if char in vowels:
            position = x
            allVowelsInTheString.append (str(char) + " - " + str(position))

        x += 1


    # OUTPUT
    print("\nOnly the uppercase letters in the string: " + str(uppercaseLetters))

    print("\nEvery second letter of the string: " + str(secondLetter))

    print("\nThe string, with all vowels replaced by an underscore: " + str(allVowelsReplaced))

    print("\nThe number of digits in the string: " + str(digitsInTheString))

    print("\nThe positions of all vowels in the string: " + str(allVowelsInTheString))

    print("\nThe chosen string: " + str(chosenString))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()