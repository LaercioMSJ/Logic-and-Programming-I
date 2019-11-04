###########################################
# Desc: Write list functions that carry out the following tasks for
#  a list of integers. For each function, provide a test program.
# 
# 1 - Swap the first and last elements in the list.
#
# 2 - Shift all elements by one to the right and move the last element
#  into the first position. For example, 1 4 9 16 25 would be transformed
#  into 25 1 4 9 16.
#
# 3 - Replace all even elements with 0.
#
# 4 - Replace each element except the first and last by the larger of its
#  two neighbors.
#
# 5 - Remove the middle element if the list length is odd, or the middle
#  two elements if the length is even.
#
# 6 - Move all even elements to the front, otherwise preserving the order
#  of the elements.
#
# 7 - Return the second-largest element in the list.
#
# 8 - Return true if the list is currently sorted in increasing order.
#
# 9 - Return true if the list contains two adjacent duplicate elements.
#
# 10 - Return true if the list contains duplicate elements (which need
#  not be adjacent).
#
# Date: 03 November 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

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