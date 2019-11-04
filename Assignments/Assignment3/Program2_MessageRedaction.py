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

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    enteredPhrase = ""

    while enteredPhrase.upper() !="QUIT":

        listLettersToRedact = []
        numberOfLettersRedacted = 0
        redactedPhrase = ""

        enteredPhrase = input("\nType a phrase (or quit to exit program): ")

        if enteredPhrase.upper() =="QUIT":
            continue

        lettersToRedact = input("\nType a comma-separated list of letters to redact: ")


    # PROCESS

        for char in lettersToRedact:

            #if char != ",":
            if char.isalpha():
                listLettersToRedact.append (char.upper())


        x = 0
        while x < len(enteredPhrase):
                
            if enteredPhrase[x].upper() in listLettersToRedact:

                numberOfLettersRedacted += 1
                redactedPhrase += "_"

            else:
                redactedPhrase += enteredPhrase[x]

            x += 1


    # OUTPUT
        print("Number of letters redacted: " + str(numberOfLettersRedacted))
        print("Redacted phrase: " + redactedPhrase)


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()