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


def Average(listOfValues): 
    return sum(listOfValues) / len(listOfValues) 


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    listOfHoursWorked = []
    day = 1
    minimumHours = 7

    while 5 > len(listOfHoursWorked):

        enteredValue = input("Enter hours worked on Day #" + str(day) + ": ")

        if enteredValue.isnumeric():
            listOfHoursWorked.append (int(enteredValue))
            day += 1
        
        else:
            print("ERROR! Enter a valid number of hours worked on Day #" + str(day) + ".")


    # PROCESS


    # OUTPUT
    print(80 * "-")

    print("The most hours worked was on:")

    x = 0
    while x < len(listOfHoursWorked):
        if listOfHoursWorked[x] == max(listOfHoursWorked):
            print("Day #" + str(x + 1) + " when you worked " + str(max(listOfHoursWorked)) + " hours.")
        x += 1


    print(80 * "-")

    print("The total number of hours worked was: " + str(sum(listOfHoursWorked)))
    print("The average number of hours worked each day was: " + str(Average(listOfHoursWorked)))


    print(80 * "-")


    print("Days you slacked off (i.e. worked less than 7 hours):")

    x = 0
    while x < len(listOfHoursWorked):
        if listOfHoursWorked[x] < minimumHours:
            print("Day #" + str(x + 1) + ": " + str(listOfHoursWorked[x]) + " hours")
        x += 1


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()