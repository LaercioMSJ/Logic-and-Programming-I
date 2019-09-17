###########################################
# Desc: About 12% of the restaurants in the
#  US are pizzerias, and there are about 70,000
#  pizzerias in the US. Estimate the total number
#  of restaurants in the US. Write code in a console
#  application which calculates and then displays the
#  estimated number of restaurants.
#
# Author: Laercio.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.
    # .12x = 70,000
    # x = 70,000 / .12

    # Input
    percentage_pizzerias = input("What is the percentage of pizzeria in the US in float? ")
    pizzerias = input("How many pizzerias are there in the US? ")

    # Process
    result = float(pizzerias) / float(percentage_pizzerias)

    # Outputlaer
    print("There are " + str(round(result)) + " restaurants in the US")

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()