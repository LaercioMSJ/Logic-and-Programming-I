###########################################
# Desc: Write a program that reads a word and prints each
#  character of the word on a separate lt "Harry",
#  the program prints:
#
# H
# a
# r
# r
# y
#
# Date: 30 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.


    # INPUT
    chosenWord = str(input("\nPlease, enter the a word: "))

    # PROCESS
 
    # OUTPUT
    for char in chosenWord:
        print("\n" + char)


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()