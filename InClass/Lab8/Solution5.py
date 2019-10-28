###########################################
# Desc: Given a list of integers with a length of 3, figure out which is larger
#  between the first and last elements in the list, and set all the other
#  elements to be that value. Return the changed list.
#
# Sample function calls & results:
# ChangeToMax([1, 2, 3]) → [3, 3, 3]
# ChangeToMax ([11, 5, 9]) → [11, 11, 11]
# ChangeToMax ([2, 11, 3]) → [3, 3, 3]
#
# Date: 27 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def changeToMax(valueList):
    return [max(valueList[0],valueList[-1]), max(valueList[0],valueList[-1]), max(valueList[0],valueList[-1])]

    #if valueList[0] >= valueList[-1]:
    #    return [valueList[0],valueList[0],valueList[0]]

    #elif valueList[0] < valueList[-1]:
    #    return [valueList[-1],valueList[-1],valueList[-1]]


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    numberList = [6,8,5]

    # PROCESS

    result = changeToMax(numberList)

    # OUTPUT
    print("\nThe changed list is " + str(result))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()