###########################################
# # Desc: 
#
# Date: xx October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    print("\nGrade Point Calculator")

    print("\nValid letter grades that can be entered: A, B, C, D, F")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.")

    # INPUT
    letterGrade = input("\nPlease enter a letter grade : ").upper()
    modifier = input("Please enter a modifier (+, - or nothing) : ")
    numericValue = 0

    NumericA = 4
    NumericB = 3
    NumericC = 2
    NumericD = 1
    NumericF = 0
    NumericPlus = 0.3
    NumericMinus = -0.3


    # PROCESS
    if letterGrade == "A":
        numericValue = NumericA
    elif letterGrade == "B":
        numericValue = NumericB
    elif letterGrade == "C":
        numericValue = NumericC
    elif letterGrade == "D":
        numericValue = NumericD
    elif letterGrade == "F":
        numericValue = NumericF
        modifier = ""
    else:
        print("\nYou entered an invalid letter grade.")

    if modifier == "+" and letterGrade != "A":
        numericValue += NumericPlus
    elif modifier == "-":
        numericValue += NumericMinus 

    # OUTPUT
    print("\nThe numeric value is: {0:.1f}".format(numericValue))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()