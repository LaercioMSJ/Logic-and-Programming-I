###########################################
# Desc: Write a program that initializes a list with ten
#  random integers and then prints four lines of output,
#  containing:
# 
# Every element at an even index.
# Every even element.
# All elements in reverse order.
# Only the first and last element.
#
# Date: 30 October 2019
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

    elementsInReverseOrder + listOfRandomIntegers
    elementsInReverseOrder.reverse()

    

 
    # OUTPUT
    print("\nThe list with ten random integers: " + str(listOfRandomIntegers))

    print("\nEvery element at an even index: " + str(elementsAtAnEvenIndex))

    print("\nEvery even element: " + str(evenElements))

    print("\nAll elements in reverse order: " + str(elementsInReverseOrder))

    print("\nOnly the first and last element: " + str(firstElement))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()