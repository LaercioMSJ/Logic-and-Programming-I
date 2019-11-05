###########################################
# Desc: Design and write a program that accepts the number of
#  hours worked on each of five work days from the user, then
#  displays different information calculated about those entries
#  as output.
# Your solution should demonstrate an understanding of how to
#  apply list and looping concepts in a program that should:
#
# •	Prompt the user to enter the five daily hours worked amounts,
#  and store them in the program.
# •	Determine the day(s) on which the most hours were worked and
#  display the day(s) and hours onscreen.
# •	Calculate and display both the total and the daily average of
#  hours worked.
# •	Display a list of all days that had insufficient hours, which
#  is defined as less than 7 hours.
# 
# Your solution must contain examples demonstrating your understanding
#  of appropriate use of functions and core assignment concepts (loops and lists).
#
# Date: 03 November 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################


# This function calculates the average of hours worked base on total of hours worked and on number of days worked, and returns a value
def Average(listOfValues): 
    return sum(listOfValues) / len(listOfValues) 


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    # Declaration of variables and lists
    # Declaration of listOfHoursWorked with empty
    listOfHoursWorked = []
    # Declaration of day variable with 1
    day = 1
    # Declaration of minimumHours variable with 7
    minimumHours = 7


    # WHILE loop is used to repeat the next section until listOfHoursWorked contains 5 values
    while 5 > len(listOfHoursWorked):

        # Declaration of enteredValue variable with input of a string via keyboard
        enteredValue = input("Enter hours worked on Day #" + str(day) + ": ")

        # Checks if it was entered a numeric value
        # If true enteredValue is added to the listOfHoursWorked
        # If false error message is showed and listOfHoursWorked doesn't receive the entered value
        if enteredValue.isnumeric():
            listOfHoursWorked.append (int(enteredValue))
            day += 1
        
        else:
            print("ERROR! Enter a valid number of hours worked on Day #" + str(day) + ".")


    # PROCESS


    # OUTPUT
    # Program shows on-screen - 80 times in sequence
    print(80 * "-")

    # Program shows on-screen the sentence contained within the quotation marks
    print("The most hours worked was on:")

    # Declaration of x variable with 0 to use in while loop
    x = 0
    # WHILE loop is used to repeat next section for each value contained in the listOfHoursWorked
    while x < len(listOfHoursWorked):

        # Checks if each value contained in the listOfHoursWorked is equal to the maximum value contained in the listOfHoursWorked
        # If true program shows on-screen next print command information
        if listOfHoursWorked[x] == max(listOfHoursWorked):

            # Program shows on-screen the sentence contained within the quotation marks,
            #  the day and the maximum value contained in the listOfHoursWorked
            print("Day #" + str(x + 1) + " when you worked " + str(max(listOfHoursWorked)) + " hours.")
        x += 1

    # Program shows on-screen - 80 times in sequence
    print(80 * "-")

    # Program shows on-screen the sentence contained within the quotation marks and
    #  the sum of the hours worked using sum method
    print("The total number of hours worked was: " + str(sum(listOfHoursWorked)))

    # Program shows on-screen the sentence contained within the quotation marks and
    #  the average of the hours worked using Average function
    print("The average number of hours worked each day was: " + str(Average(listOfHoursWorked)))

    # Program shows on-screen - 80 times in sequence
    print(80 * "-")

    # Program shows on-screen the sentence contained within the quotation marks
    print("Days you slacked off (i.e. worked less than 7 hours):")

    # Declaration of x variable with 0 to use in while loop
    x = 0
    # WHILE loop is used to repeat next section for each value contained in the listOfHoursWorked
    while x < len(listOfHoursWorked):

        # Checks if each value contained in the listOfHoursWorked is less than minimumHours (7 hours)
        # If true program shows on-screen the sentence contained within the quotation marks,
        #  the day and the number of hours worked
        if listOfHoursWorked[x] < minimumHours:
            print("Day #" + str(x + 1) + ": " + str(listOfHoursWorked[x]) + " hours")
        x += 1


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()