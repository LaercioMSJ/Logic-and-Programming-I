###########################################
# Desc: Design and write a program that reads the text from a
#  provided text file into a list, displays the text on-screen,
#  makes some alterations to the text and outputs the changed
#  text to the screen, then saves the altered text as a new file.
# 
# Begin by designing your solution to this problem in pseudocode,
#  which will be submitted along with the program. Your solution
#  should demonstrate an understanding of how to apply file I/O,
#  list and looping concepts. Your program will read all the text
#  contained in a file (provided) into a list and output the
#  unchanged text content to the console. Your program should then
#  make the following alterations:
# 
# •	Add a line number (starting with line number 1) to the beginning
#  of each line of text in the file.
# •	Any line of text that is longer than twenty characters should
#  be converted to all lowercase letters.
# •	Any line 20 or less characters long should be converted to all
#  uppercase letters.
# •	Your program should randomly select a line in the text and OMIT
#  it from any output.
# 
# Once all text alterations are complete, output the altered text
#  to the console, and finish by saving the altered text to a new
#  text file. Every time the program is run it should pick a different
#  random line of text and you can assume the file doesn’t contain
#  any commas. Although a text file is provided, your finished program
#  should work with any text-based file, not just the original A-Team text.
# 
# Your solution must contain examples demonstrating your understanding
#  of appropriate use of functions and core assignment concepts
#  (file I/O, 2-d lists).
#
# Date: 17 November 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################
#
# PSEUDOCODE:
# Open the ateam_Original.txt file and save in originalText
# Count number of characters in each line of text
# If greater than 20, make all characters lowercase
# If less than or equal to 20 make all characters uppercase
# Add the line number at the beginning of each sentence
# Select one of the sentences to be taken from the text
# Show the original text on screen
# Show the altered text on screen
# Save the altered text to a new text file
#
######################################################

import random

# This function changes all letters of a sentence to uppercase or lowercase, based on the number of characters in the sentence,
#  and randomly selects one of the sentences to be taken from the text and returns the full text after making these changes
def textAlterer (text):

    # Declaration of variables and lists
    newText = []
    lineOfText = ""
    lineNumber = 1
    charPerLine = 0
    charLineLimit = 20

    # FOR loop is used to repeat each char of the text
    for char in text:

        # If char is different from line break (\n), char is added to lineOfText, and incremented by 1 the charPerLine
        if char != "\n":
            lineOfText += char
            charPerLine += 1

        # If char equals line break (\n) and charPerLine is greater than 20, lineOfText is added to newText using lowercase together with line number
        # Incremented by 1 the lineNumber, charPerLine becames 0 again, and lineOfText becames empty again
        elif (charPerLine > charLineLimit and char == "\n"):
            newText.append (str(lineNumber) + ": " + lineOfText.lower())
            lineNumber += 1
            charPerLine = 0
            lineOfText = ""

        # If char equals line break (\n) and charPerLine is smaller than 20 or equals 20, lineOfText is added to newText using uppercase together with line number
        # Incremented by 1 the lineNumber, charPerLine becames 0 again, and lineOfText becames empty again
        elif (charPerLine <= charLineLimit and char == "\n"):
            newText.append (str(lineNumber) + ": " + lineOfText.upper())
            lineNumber += 1
            charPerLine = 0
            lineOfText = ""

    # An entire line of text becomes empty using the random.randint
    newText [random.randint (0, len(newText) - 1)] = ""

    # Returns the full text after making all changes
    return newText



def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.


    # INPUT
    # Open the ateam_Original.txt file with original text and save in originalText
    fileName = "Assignments\\Assignment4\\ateam_Original.txt"
    accessMode = "r"

    with open(fileName, accessMode) as originalFile:
        
        originalText = (originalFile.read() + "\n")


    # PROCESS
    # Call the textAlterer function to make changes to the originalText, and return it to alteredText
    alteredText = textAlterer (originalText)


    # OUTPUT
    # Program shows on-screen the sentence contained within the quotation marks (just to keep screen output organized)
    print ("-" * 34)
    print ("Original Text")
    print ("-" * 34)

    # Program shows on-screen the original text
    print (originalText)
    
    # Program shows on-screen the sentence contained within the quotation marks (just to keep screen output organized)
    print ("-" * 34)
    print ("Altered Text")
    print ("-" * 34)

    # Program shows on-screen the altered text
    # FOR loop is used to print each row of the text separately
    for row in alteredText:
        print (row)


    # Create the ateam_Altered.txt file to save the alteredText
    fileName = "Assignments\\Assignment4\\ateam_Altered.txt"
    accessMode = "w"

    with open(fileName, accessMode) as alteredFile:
        
        # FOR loop is used to added each row of the text separately and used "\n" to break line
        for row in alteredText:
            alteredFile.write (row + "\n")


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()