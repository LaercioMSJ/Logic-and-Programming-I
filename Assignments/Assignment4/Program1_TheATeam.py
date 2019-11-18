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



# list or string (originalText)? 2 d list é necessario? try error é preciso?  posso usar fileName e accessMode mais de uma vez com o mesmo nome ou usar o nome do arquivo direto?

import random

def textAlterer (text):

    newText = []
    lineOfText = ""
    lineNumber = 1
    charPerLine = 0
    charLineLimit = 20

    for char in text:

        if char != "\n":
            lineOfText += char
            charPerLine += 1

        elif (charPerLine > charLineLimit and char == "\n"):
            newText.append (str(lineNumber) + ": " + lineOfText.lower())
            lineNumber += 1
            charPerLine = 0
            lineOfText = ""

        elif (charPerLine <= charLineLimit and char == "\n"):
            newText.append (str(lineNumber) + ": " + lineOfText.upper())
            lineNumber += 1
            charPerLine = 0
            lineOfText = ""

    newText [random.randint (0, len(newText) - 1)] = ""

    return newText



def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.


    # INPUT

    fileName = "ateam_Original.txt"
    accessMode = "r"

    with open(fileName, accessMode) as originalFile:
        
        originalText = (originalFile.read() + "\n")


    # PROCESS

    alteredText = textAlterer (originalText)


    # OUTPUT
    print ("-" * 34)
    print ("Original Text")
    print ("-" * 34)

    print (originalText)
    
    print ("-" * 34)
    print ("Altered Text")
    print ("-" * 34)

    for row in alteredText:
        print (row)



    fileName = "ateam_Altered.txt"
    accessMode = "w"

    with open(fileName, accessMode) as alteredFile:
        
        for row in alteredText:
            alteredFile.write (row + "\n")


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()