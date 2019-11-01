###########################################
# Desc: Write a program that reads numbers and adds them to a
#  list if they aren’t already contained in the list.
#  When the list contains ten numbers, the program
#  displays the contents and quits.
#
# Date: 01 November 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

import random

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.


    # INPUT
    listOfRandomIntegers = []

    for counter in range(10):
        listOfRandomIntegers.append (random.randint(1, 100))

    elementsAtAnEvenIndex = []

    evenElements = []

    elementsInReverseOrder = []

    firstElement = 0
    lastElement = 0
    

    # PROCESS
    for ctr in range(0, 10, 2):
        elementsAtAnEvenIndex.append (listOfRandomIntegers[ctr])


    for i in range(10):
        if listOfRandomIntegers[i] % 2 == 0:
            evenElements.append (listOfRandomIntegers[i])


    elementsInReverseOrder = elementsInReverseOrder + listOfRandomIntegers
    elementsInReverseOrder.reverse()


    firstElement = listOfRandomIntegers[0]
    lastElement = listOfRandomIntegers[-1]
    

 
    # OUTPUT
    print("\nThe list with ten random integers: " + str(listOfRandomIntegers))

    print("\nEvery element at an even index: " + str(elementsAtAnEvenIndex))

    print("\nEvery even element: " + str(evenElements))

    print("\nAll elements in reverse order: " + str(elementsInReverseOrder))

    print("\nOnly the first and last element: " + str(firstElement), str(lastElement))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()