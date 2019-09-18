###########################################
# Desc: Code a Python program that calculates the amount of paint you need to cover the walls in your family room.
# The salesperson at the home improvement store told you to buy 1 gallon of paint for every 150 square feet of wall you need to paint.
# Assuming that the room is rectangular in shape, the program should take in as input the width of your two sets of walls and the height of the room.
# The program should output the number of gallons required to paint the room. Paint is sold only by the gallon..
#
# Author: Laercio.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # Input
    height = input("What is the height of the room? ")  # height input via keyboard
    width1 = input("What is the first width of the room? ")  # first width input via keyboard
    width2 = input("What is the second width of the room? ")  # second width input via keyboard
    squareFeetPerGallon = 150  # input the fixed amount of 1 gallon of paint for every 150 square feet

    # Process
    gallons = ( ( (float(height) * float(width1) ) * 2) + ( ( float(height) * float(width2) ) * 2) ) / squareFeetPerGallon

    # Output
    print("{0:.0f} gallons are required to paint the room".format(gallons)) # result

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()