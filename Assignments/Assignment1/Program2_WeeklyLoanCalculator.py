###########################################
# Desc: Program 2 – Weekly Loan Calculator.
#
# Develop a short term loan calculator program as a console application
# with the following specifications. Begin by designing your solution to
# this problem in pseudocode, which will be submitted along with the program.
# If A dollars are borrowed at r% interest compounded weekly to purchase
# something with weekly payments for n years, then the weekly payment
# is given by the formula:
#
# If : i = r / 5200	
#
# Then calculate the weekly payment as: weekly payment = (i / 1 – (1 + i) exp-52n) * A
#
# Write a console application that calculates the weekly payment after
# the user gives the amount of the loan, interest rate, and number of years.

# Author: Author: Laercio M da Silva Junior - W0433181.
###########################################
#
# PSEUDOCODE:
# Request the loan amount
# Request the interest rate
# Request the number of years
# Calculate the weekly interest (the interest rate divided by 5200)
# Calculate total week number (the fixed number of weeks in a year (52) multiplied by number of years)
# Calculate weekly compound interest (the weekly interest exponentiated by the total number of weeks is divided by weekly interest)
# Calculate weekly payment (the weekly compound interest multiplied by loan amount)
# Show on screen the weekly payment
#
######################################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # Show program title and use \n to have a space line
    print("\nWeekly Loan Calculator")


    # INPUT
    # Declaration of loanAmount variable with input of a float value via keyboard and used \n to have a space line
    loanAmount = float(input("\nEnter the amount of loan: "))

    # Declaration of interestRate variable with input of a float value via keyboard
    interestRate = float(input("Enter the interest rate (%): "))

    # Declaration of numberOfYears variable with input of a float value via keyboard
    # I used float type if you need to enter years and months, for example: for a 4 years and 6 months loan the user should type '4.5'
    numberOfYears = float(input("Enter the number of years: "))


    # PROCESS
    # Weekly interest calculation
    # Where the interest rate divided by 5200 results in the desired value
    weeklyInterest = interestRate / 5200

    # Total week number calculation
    # Where the fixed number of weeks in a year (52) multiplied by number of years results in the desired value
    totalWeekNumber = 52 * numberOfYears

    # Weekly compound interest calculation
    # Where the weekly interest exponentiated by the total number of weeks is divided by weekly interest and results in the desired value
    weeklyCompoundInterest = weeklyInterest / (1 - ((1 + weeklyInterest) ** -totalWeekNumber ))

    # Weekly payment calculation
    # Where the weekly compound interest multiplied by loan amount results in the desired value
    weeklyPayment = weeklyCompoundInterest * loanAmount


    # OUTPUT
    # Program shows on-screen the sentence contained within the quotation marks and the value contained in the variable weeklyPayment
    # Used \n to have a space line
    # The format method is used to return the formatted string.
    print("\nYour weekly payment will be: ${0:.2f}".format(weeklyPayment))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()