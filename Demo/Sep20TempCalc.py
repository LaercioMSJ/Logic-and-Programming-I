###########################################
# Desc: Convert Fahrenheit to Celsius.
#
# Author: Laercio.
###########################################

"""
    Conversion formulas:
    F to C = (F - 32) * 5/9
    C to F = C * 9/5 + 32
    This program will initially convert tempInFahr
    to Celsius using the above formula.
"""

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # Input
    tempInFahr = float(input("What is the temp in Fahrenheit? "))
    tempInCelsius = 0.0

    # Process
    # F to C = (F - 32) * 5/9
    tempInCelsius = (tempInFahr - 32) * 5/9

    # Output
    print("Your temp in Celsius is {0:.2f}.".format(tempInCelsius))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()