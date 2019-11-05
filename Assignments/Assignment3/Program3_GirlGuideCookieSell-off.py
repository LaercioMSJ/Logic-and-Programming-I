###########################################
# Desc: The organizers of the annual Girl Guide cookie sale event
#  want to raise the stakes on the number of cookies sold and are
#  offering cool prizes to those guides who go above and beyond in
#  their sales efforts. The organizers want a program to print the
#  guide list and their prizes.
# 
# Your solution should demonstrate an understanding of how to apply
#  list/loop concepts in a program that should:
#
# •	Ask the user how many guides sold cookies in the current event,
# •	For each numbered guide up to the user-entered count of guides,
#  allow the user to enter a name and the number of boxes of cookies
#  that person sold.
# •	Calculate and output a list of all guide names, 
# •	Display the average sales, and the prize that each guide won,
# •	The highest selling guide gets a trip to the Girl Guide Jamboree,
#  any guides selling above average get a badge, and any guides
#  selling at least one box get to split the remaining cookies,
#  with guides selling no boxes shut out of all prizes (as they should be).
#
#  (Hint: Some potential solution ideas: Research parallel arrays or
#  two-dimensional lists)
# 
# Your solution must contain examples demonstrating your understanding
#  of appropriate use of functions and core assignment concepts (loops
#  and lists).
#
# Date: 04 November 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################


# This function selects the prize based on number of boxes sold, on average
#  of boxes sold, and on highest selling and returns the selected string
def selectPrizesWon (boxesSold, average, highestSelling):

    # Select prize type based on number of boxes sold
    if boxesSold == highestSelling:
        return "Trip to Girl Guide Jamboree in Aruba!"
        
    if boxesSold > average:
        return "Super Seller Badge"

    elif boxesSold < average and boxesSold != 0:
        return "Left over cookies"

    else:
        return ""


# This function selects the highest selling based on number of boxes sold for each guide
#  and a loop is used to compare each item in the list and returns the selected value
def largestNumberOfBoxesSold(listBoxByGuide):

    # Declaration of higherNumber variable with 0
    higherNumber = 0

    # FOR Loop is used to compare each item in the list
    for counter in range(len(listBoxByGuide)):
        
        # Select higherNumber comparing the number of boxes sold for each guide
        if listBoxByGuide [counter][1] > higherNumber:
            higherNumber = listBoxByGuide [counter][1]

    return higherNumber


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.


    # INPUT
    # Declaration of variables and lists
    # Declaration of listOfGuides list with empty
    listOfGuides = []
    # Declaration of totalOfBoxesSold variable with 0
    totalOfBoxesSold = 0


    # Declaration of numberOfGuides variable with input of a integer value via keyboard
    numberOfGuides = int(input("Enter the number of guides selling cookies: "))


    # FOR loop is used to repeat the next input section based on numberOfGuides entered
    for counter in range (0, numberOfGuides):

        # Declaration of nameOfGuide variable with input of a string via keyboard
        nameOfGuide = str(input("\nEnter the name of guide #" + str(counter + 1) + ": ").title())

        # Declaration of boxesSoldByGuide variable with input of a integer value via keyboard
        boxesSoldByGuide = int(input("Enter the number of boxes sold by " + nameOfGuide + ": "))

        # Added nameOfGuide and boxesSoldByGuide values to the list
        listOfGuides.append ([nameOfGuide, boxesSoldByGuide])


    # PROCESS
    # Declaration of x variable with 0 to use in while loop
    x = 0
    # WHILE loop is used to sum all boxes sold by the guides
    while x < len(listOfGuides):
        totalOfBoxesSold += listOfGuides[x][1]
        x += 1


    # Declaration of averageNumberOfBoxesSold variable with the result of dividing the totalOfBoxesSold by number of the guides
    averageNumberOfBoxesSold = totalOfBoxesSold / len(listOfGuides)


    # OUTPUT
    # Program shows on-screen the sentence contained within the quotation marks, the value contained in
    #  the variable averageNumberOfBoxesSold and used \n to have a space line.
    print("\n\nThe average number of boxes sold by each guide was {0:.1f}".format(averageNumberOfBoxesSold))

    # Program shows on-screen the sentence contained within the quotation marks
    # It used \n to have a space line and \t to have space between strings.
    print("\nGuide\t\tPrizes Won:")
    print(80 * "-")

    # Declaration of x variable with 0 to use in while loop
    x = 0
    # WHILE loop is used to repeat the next print section based on number of values in the list listOfGuides
    while x < len(listOfGuides):
        # Program shows on-screen the name and the prize of each guide
        # Call the selectPrizesWon function to select the prize based on number of boxes sold, on average of boxes sold, and on highest selling
        # Call the largestNumberOfBoxesSold function to select the highest selling based on number of boxes sold for each guide
        print(str(listOfGuides [x][0]) + "\t\t- " + selectPrizesWon (listOfGuides [x][1], averageNumberOfBoxesSold, largestNumberOfBoxesSold(listOfGuides)))
        x += 1



#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()
