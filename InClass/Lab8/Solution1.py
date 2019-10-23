###########################################
# Desc: 1.	Using a list of integers, build a function called
#  FirstOrLast7 which returns True if a 7 appears as either
#  the first or last element in the list. The list will be
#  length 1 or more. 
#
# Sample function calls & results:
# FirstOrLast7 ([1, 3, 7]) → True
# FirstOrLast7 ([7, 8, 2, 4]) → True
# FirstOrLast7 ([13, 7, 1, 5, 9]) → False
#
# Date: 23 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def FirstOrLast7(valueList):
    return "7" in str(valueList[0]) or "7" in str(valueList[len(valueList)-1])


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    numberList = [2,4,5,6,7,5,7]

    # PROCESS

    result = FirstOrLast7(numberList)

    # OUTPUT
    print("7 appears as either the first or last element in the list? " + str(result))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()