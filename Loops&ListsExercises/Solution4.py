###########################################
# Desc: Write programs that read a sequence of integer inputs and print
# 
# The smallest and largest of the inputs.
# The number of even and odd inputs.
# Cumulative totals. For example, if the input is 1 7 2 9, the program should print 1 8 10 19.
# All adjacent duplicates. For example, if the input is 1 3 3 4 5 5 6 6 6 2, the program should print 3 5 6.
#
# Date: 27 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    integerInputs = []

    for counter in range(10):
        integerInputs.append (int(input("\nPlease, enter a integer number: ")))


    totalOfOddNumbers = 0
    totalOfEvenNumbers = 0

    cumulativeTotals = []
    adjacentDuplicatesNumbers = []


    # PROCESS
    for counter in range(10):
        if (integerInputs[counter] % 2) == 1:
            totalOfOddNumbers += 1

        else:
            totalOfEvenNumbers += 1

    
    cumulativeTotals.append (integerInputs[0])
    x = 1
    while (x < len(integerInputs)):
        cumulativeTotals.append (integerInputs[x] + cumulativeTotals[x-1])
        x += 1







    #X = 1
    #while x < len(adjacentDuplicatesNumbers):
    #    if adjacentDuplicatesNumbers[x] != adjacentDuplicatesNumbers[x-1]:
    #        adjacentDuplicatesNumbers.pop(x)
    #    x -= 1  
    #x += 1


    # OUTPUT
    print("\nThe smallest and largest of the inputs are " + str(min(integerInputs)) + " and " + str(max(integerInputs)))

    print("\nThe number of even and odd inputs is " + str(totalOfEvenNumbers) + " and " + str(totalOfOddNumbers))

    print("\nCumulative totals is: " + str(cumulativeTotals))

    print("\nCumulative totals is: " + str(integerInputs))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()