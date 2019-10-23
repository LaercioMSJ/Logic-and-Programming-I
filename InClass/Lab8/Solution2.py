###########################################
# Desc: Given a list of 3 integers, return a new list with the elements
#  in reverse order, so [1, 2, 3] becomes [3, 2, 1]. 
#
# Sample function calls & results:
# ReverseIt([1, 2, 3]) → [3, 2, 1]
# ReverseIt([5, 11, 9]) → [9, 11, 5]
# ReverseIt([7, 0, 0]) → [0, 0, 7]
#
# Date: 23 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def reverseOrder(valueList):
    valueList.reverse()
    return valueList

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    numberList = [1,2,3]

    # PROCESS

    numberList = reverseOrder(numberList)

    # OUTPUT
    print("A new list with the elements in reverse order " + str(numberList))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()