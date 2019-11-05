###########################################
# Desc: Design and write a program that removes all desired letters
#  from any user-entered sentence or phrase.
# Your solution should demonstrate an understanding of how to apply
#  list and looping concepts in a program that should:
#
# •	Take a sentence or phrase as input,
#
# •	Take a comma-separated list of letters to remove as input,
#
# •	Replace all occurrences of each target letter in the user-entered
#  sentence, regardless of case sensitivity, with an underscore (“_”)
#  character.
#
# •	Display the number of letters removed to the user,
#
# •	The program will keep asking the user to enter a new sentence until
#  the user enters the command ‘quit’.
# 
# Your solution must contain examples demonstrating your understanding
#  of appropriate use of functions and core assignment concepts
#  (loops and lists).
#
# Date: 03 November 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################


# This function selects only the letters to redact and returns a list with letters
def letterIdentifier(letters):
    
    # Declaration of listOfLetters list with empty
    listOfLetters = []

    # FOR loop is used to repeat each char in the stirng "letters"
    for char in letters:

        #if char != ",":  # This way the spaces entered by the user would also be redacted
        # isalpha() method is used to select only letters
        if char.isalpha():
            listOfLetters.append (char.upper())

    return listOfLetters


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.


    # INPUT
    # Declaration of enteredPhrase variable as a empty string
    enteredPhrase = ""

    # WHILE loop is used to keep the program repeating until QUIT is entered
    while enteredPhrase.upper() !="QUIT":

        # Declaration of variables and lists
        # Declaration of listLettersToRedact list with empty
        listLettersToRedact = []
        # Declaration of numberOfLettersRedacted variable with 0
        numberOfLettersRedacted = 0
        # Declaration of redactedPhrase variable as a empty string
        redactedPhrase = ""


        # Declaration of enteredPhrase variable with input of a string via keyboard
        enteredPhrase = str(input("\nType a phrase (or quit to exit program): "))

        # Checks if it was entered QUIT
        # If true the program skips to the next loop and the condition in the first WHILE ends the loop
        # If false the program continues to execute the lines below
        if enteredPhrase.upper() =="QUIT":
            continue

        # Declaration of lettersAndCommaToRedact variable with input of a string via keyboard
        lettersAndCommaToRedact = str(input("\nType a comma-separated list of letters to redact: "))


    # PROCESS
        # Call the letterIdentifier function to select only the letters to redact and returns a list with each letter
        #  and returns a list to listLettersToRedact
        listLettersToRedact = letterIdentifier(lettersAndCommaToRedact)

        # FOR loop is used to repeat each char in the stirng "enteredPhrase"
        for counter in range (len(enteredPhrase)):
            
            # IF is used to check if the CHAR is contained in the listLettersToRedact
            # If true "_" is added to string redactedPhrase and is added 1 to numberOfLettersRedacted
            # If false the CHAR is added to string redactedPhrase
            if enteredPhrase[counter].upper() in listLettersToRedact:

                numberOfLettersRedacted += 1
                redactedPhrase += "_"

            else:
                redactedPhrase += enteredPhrase[counter]


    # OUTPUT
        # Program shows on-screen the sentence contained within the quotation marks
        #  and the value contained in the variable numberOfLettersRedacted
        print("Number of letters redacted: " + str(numberOfLettersRedacted))
        # Program shows on-screen the sentence contained within the quotation marks
        #  and the string contained in the variable redactedPhrase
        print("Redacted phrase: " + redactedPhrase)


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()