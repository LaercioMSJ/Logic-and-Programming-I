###########################################
# Desc: Given a list of integers with a length of 3, return the sum of all the elements.
#
# Sample function calls & results:
# SumList([1, 2, 3]) → 6
# SumList ([5, 11, 2]) → 18
# SumList ([7, 0, 0]) → 7
#
# Date: 27 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def sumList(valueList):
    return valueList[0] + valueList[1] + valueList[2]

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    numberList = [7,0,1]

    # PROCESS

    sumOfAllTheElements = sumList(numberList)

    # OUTPUT
    print("\nThe sum of all the elements is " + str(sumOfAllTheElements))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()