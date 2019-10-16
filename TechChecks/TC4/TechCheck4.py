###########################################
# # Desc: Tech Check 4
#
# Date: 16 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def inputGradeFunction (course):
    return input("\nPlease enter a letter grade for " + course + ": ").upper()


def inputModifierFunction ():
    return input("Please enter a modifier (+, - or nothing) : ")


def letterGradeCalculator (letter, mod):
    if letter == "A":
        numericGrade = 4.0
    elif letter == "B":
        numericGrade = 3.0
    elif letter == "C":
        numericGrade = 2.0
    elif letter == "D":
        numericGrade = 1.0
    elif letter == "F":
        numericGrade = 0.0
    else:
        print("You entered an invalid letter grade.")

    if mod == "+":
        if letter != "A" and letter != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif mod == "-":
        if letter != "F":     # Minus is not valid on F
            numericGrade -= 0.3
    
    return numericGrade



def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    print("\nGrade Point Average Calculator")

    print("\nValid letter grades that can be entered: A, B, C, D, F")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.")

    # INPUT
    letterGradePROG1700 = inputGradeFunction ("PROG1700")
    modifierPROG1700 = inputModifierFunction ()

    letterGradeNETW1700 = inputGradeFunction ("NETW1700")
    modifierNETW1700 = inputModifierFunction ()

    letterGradeOSYS1200 = inputGradeFunction ("OSYS1200")
    modifierOSYS1200 = inputModifierFunction ()

    letterGradeWEBD1000 = inputGradeFunction ("WEBD1000")
    modifierWEBD1000 = inputModifierFunction ()

    letterGradeCOMM1700 = inputGradeFunction ("COMM1700")
    modifierCOMM1700 = inputModifierFunction ()

    letterGradeDBAS1007 = inputGradeFunction ("DBAS1007")
    modifierDBAS1007 = inputModifierFunction ()


    # PROCESS

    PROG1700 = letterGradeCalculator (letterGradePROG1700, modifierPROG1700)

    NETW1700 = letterGradeCalculator (letterGradeNETW1700, modifierNETW1700)

    OSYS1200 = letterGradeCalculator (letterGradeOSYS1200, modifierOSYS1200)

    WEBD1000 = letterGradeCalculator (letterGradeWEBD1000, modifierWEBD1000)

    COMM1700 = letterGradeCalculator (letterGradeCOMM1700, modifierCOMM1700)

    DBAS1007 = letterGradeCalculator (letterGradeDBAS1007, modifierDBAS1007)

    average = (PROG1700 + NETW1700 + OSYS1200 + WEBD1000 + COMM1700 + DBAS1007) / 6


    # OUTPUT
    print("\n***************************************************")

    print("\nThe numeric value for PROG1700 is: {0:.1f}".format(PROG1700))

    print("The numeric value for NETW1700 is: {0:.1f}".format(NETW1700))

    print("The numeric value for OSYS1200 is: {0:.1f}".format(OSYS1200))

    print("The numeric value for WEBD1000 is: {0:.1f}".format(WEBD1000))

    print("The numeric value for COMM1700 is: {0:.1f}".format(COMM1700))

    print("The numeric value for DBAS1007 is: {0:.1f}".format(DBAS1007))

    print("======================================================")

    print("Your grade point average for the semester is: {0:.1f}".format(average))

    print("======================================================")

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()