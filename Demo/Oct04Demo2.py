###########################################
# Desc: Write a program that allows the user to enter the number of hours they worked this week and
#  the dollar amount they make per hour.
# Use these values to calculate the amount of money they made this week.
# If the # of hours exceeds 40 in a week, include the amount of overtime pay they made in the total.
# Overtime pays time-and-a-half (1.5X) the usual hourly wage, and only apply to the # of hours worked over 40.
#
# Date: 04 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    numberOfHoursWorked = float(input("\nPlease, enter the number of hours you worked this week: "))
    regularRatePerHour = float(input("\nPlease, enter the dollar amount you make per hour: "))
    maxNumHours = 40
    overtimeRate = 1.5
    overtimeHours = 0

    # PROCESS
    if numberOfHoursWorked > maxNumHours:
        overtimeHours = numberOfHoursWorked - maxNumHours
        payment = (overtimeHours * (regularRatePerHour * overtimeRate)) + ((numberOfHoursWorked - overtimeHours) * regularRatePerHour)
    else:
        payment = numberOfHoursWorked * regularRatePerHour

    # OUTPUT
    print("\nYour payment is: ${0:.2f}".format(payment))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()