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

    # PROCESS
    if letterGrade == "A":
        numericValue = 4
    elif letterGrade == "B":
        numericValue = 3
    elif letterGrade == "C":
        numericValue = 2
    elif letterGrade == "D":
        numericValue = 1
    elif letterGrade == "F":
        numericValue = 0
        modifier = ""
    else:
        print("\nYou entered an invalid letter grade.")

    if modifier == "+" and letterGrade != "A":
        numericValue += 0.3
    elif modifier == "-":
        numericValue -= 0.3 

    # OUTPUT
    print("\nThe numeric value is: {0:.1f}".format(numericValue))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()