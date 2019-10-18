###########################################
# Desc: A landscaping company needs a program that computes the price
#  of landscaping for a new housing development. Work orders are based on:
#  address, plot length and width in feet, type of grass (“fescue”,
#  “bentgrass” or “campus”), and number of trees.
#  The price is computed as follows:  
#
#	* There is a base labour charge of $1000. 
#	* If the surface (length * width) is over 5000 square feet, add $500. 
# 	* The cost is calculated per square foot. If the grass is “fescue” the
#    cost is $0.05; for “bentgrass” it is $0.02; “campus” is $0.01. 
# 	* Each tree requested has a $100 charge. 
#
# First, create a flowchart that clearly shows all the paths of execution
#  that will exist within your designed solution to this problem. Write a
#  console application that will input the address, property length and width,
#  type of grass and number of trees, and then output the corresponding price.
# Your solution must contain examples demonstrating your understanding of
#  appropriate use of functions and core assignment concepts (decision structures).
#
# Date: 17 October 2019
#
# Author: Laercio M da Silva Junior - W0433181
###########################################


# This function multiplies two values and return the result
def multiplierFunction (value1, value2):
    return value1 * value2


# This function selects the grass cost per square foot based on type of grass and returns the selected value
def grassCostSelection (grass):
    # Declaration of costPerSquareFootFescue variable with fixed value
    costPerSquareFootFescue = 0.05

    # Declaration of costPerSquareFootBentgrass variable with fixed value
    costPerSquareFootBentgrass = 0.02

    # Declaration of costPerSquareFootCampus variable with fixed value
    costPerSquareFootCampus = 0.01

    # Select grass cost per square foot based on type of grass entered
    if grass == "fescue":
        return costPerSquareFootFescue

    elif  grass == "bentgrass":
        return costPerSquareFootBentgrass

    elif grass == "campus":
        return costPerSquareFootCampus

    else:
        # Program shows on-screen the error message contained within the quotation marks if the type of grass is incorrect
        print("\nThe type of grass you entered is incorrect. Try again.")
        return 0


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.


    # Show program title and use \n to have a space line
    print("\nLandscape Calculator")


    # INPUT
    # Declaration of houseNumber variable with input of a integer value via keyboard and used \n to have a space line
    houseNumber = int(input("\nEnter House Number: "))

    # Declaration of propertyDepth variable with input of a float value via keyboard and used \n to have a space line
    propertyDepth = float(input("\nEnter property depth (feet): "))

    # Declaration of propertyWidth variable with input of a float value via keyboard and used \n to have a space line
    propertyWidth = float(input("\nEnter property width (feet): "))

    # Declaration of typeOfGrass variable with input of a string via keyboard and used \n to have a space line
    typeOfGrass = str(input("\nEnter type of grass (fescue, bentgrass, campus): ").lower())

    # Declaration of numberOfTrees variable with input of a integer value via keyboard and used \n to have a space line
    numberOfTrees = int(input("\nEnter the number of trees: "))


    # Declaration of variables
    # Declaration of baseLabourCharge variable with fixed value
    baseLabourCharge = 1000

    # Declaration of maximumSurfaceWithoutFee variable with fixed value
    maximumSurfaceWithoutFee = 5000

    # Declaration of surfaceTaxExceeded variable with fixed value
    surfaceTaxExceeded = 500

    # Declaration of costPerTree variable with fixed value
    costPerTree = 100

    # Declaration of totalSurface variable with 0
    totalSurface = 0

    # Declaration of totalCost variable with 0
    totalCost = 0


    # PROCESS
    # Call the multiplierFunction to calculate totalSurface based on propertyDepth and propertyWidth
    totalSurface = multiplierFunction (propertyDepth, propertyWidth)

    # Call the multiplierFunction twice to calculate totalCost based on totalSurface, selected grass cost, numberOfTrees and costPerTree
    totalCost = multiplierFunction (totalSurface, grassCostSelection (typeOfGrass))
    totalCost += multiplierFunction (numberOfTrees, costPerTree)

    # Add baseLabourCharge to totalCost
    totalCost += baseLabourCharge

    # Add surfaceTaxExceeded to totalCost if totalSurface greater than maximumSurfaceWithoutFee(5000)
    if totalSurface > maximumSurfaceWithoutFee:
        totalCost += surfaceTaxExceeded


    # OUTPUT
    # Program shows on-screen the sentence contained within the quotation marks, the string contained in
    #  the variable houseNumber, and the value contained in the variable totalCost.
    # The format method is used to return the formatted string and used \n to have a space line.
    print("\nTotal cost for house {0:.0f} is: ${1:.2f}".format(houseNumber, totalCost))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()