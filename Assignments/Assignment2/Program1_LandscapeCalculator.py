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
# Date: 13 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.




    def grassCost(grass):
        if grass == "fescue":
            return costPerSquareFootFescue

        elif  grass == "bentgrass":
            return costPerSquareFootBentgrass

        elif grass == "campus":
            return costPerSquareFootCampus

        else:
            print("\nThe type of grass you entered is incorrect. Try again.")
            return 0



    # Show program title and use \n to have a space line
    print("\nLandscape Calculator")


    # INPUT
    # Declaration of houseNumber variable with input of a string via keyboard and used \n to have a space line
    houseNumber = input("\nEnter House Number: ")

    # Declaration of propertyDepth variable with input of a float value via keyboard and used \n to have a space line
    propertyDepth = float(input("\nEnter property depth (feet): "))

    # Declaration of propertyWidth variable with input of a float value via keyboard and used \n to have a space line
    propertyWidth = float(input("\nEnter property width (feet): "))

    # Declaration of typeOfGrass variable with input of a string via keyboard and used \n to have a space line
    typeOfGrass = input("\nEnter type of grass (fescue, bentgrass, campus): ").lower()

    # Declaration of numberOfTrees variable with input of a integer value via keyboard and used \n to have a space line
    numberOfTrees = int(input("\nEnter the number of trees: "))


    # Declaration of baseLabourCharge variable with fixed value
    baseLabourCharge = 1000

    # Declaration of maximumSurfaceWithoutFee variable with fixed value
    maximumSurfaceWithoutFee = 5000

    # Declaration of surfaceTaxExceeded variable with fixed value
    surfaceTaxExceeded = 500

    # Declaration of costPerSquareFootFescue variable with fixed value
    costPerSquareFootFescue = 0.05

    # Declaration of costPerSquareFootBentgrass variable with fixed value
    costPerSquareFootBentgrass = 0.02

    # Declaration of costPerSquareFootCampus variable with fixed value
    costPerSquareFootCampus = 0.01

    # Declaration of costPerTree variable with fixed value
    costPerTree = 100



    # PROCESS

    totalSurface = propertyDepth * propertyWidth




    totalCost = (totalSurface * grassCost(typeOfGrass)) + (numberOfTrees * costPerTree) + baseLabourCharge



    if totalSurface > maximumSurfaceWithoutFee:
        totalCost += surfaceTaxExceeded





    # OUTPUT
    # Program shows on-screen the sentence contained within the quotation marks, the string contained in
    #  the variable houseNumber, and the value contained in the variable totalCost.
    # The format method is used to return the formatted string and used \n to have a space line.
    print("\nTotal cost for house " + houseNumber + " is: ${0:.2f}".format(totalCost))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()