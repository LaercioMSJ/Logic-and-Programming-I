###########################################
# Desc: Given 2 lists of integers, each with a length of 3,
#  return a new list (length of 2) containing their middle elements. 

# Sample function calls & results:
# MiddleElements([1, 2, 3], [4, 5, 6]) → [2, 5]
# MiddleElements ([7, 7, 7], [3, 8, 0]) → [7, 8]
# MiddleElements ([5, 2, 9], [1, 4, 5]) → [2, 4]
#
# Date: 23 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def MidleList (valueList1, valueList2):
    mid1 = valueList1[int(len(valueList1)/2)]
    mid2 = valueList2[int(len(valueList2)/2)]
    return [mid1,mid2]

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    numberList1 = [1,2,3]
    numberList2 = [5,4,3]

    # PROCESS

    middleElementsList = MidleList (numberList1, numberList2)

    # OUTPUT
    print("MiddleElements list " + str(middleElementsList))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()