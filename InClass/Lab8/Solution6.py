###########################################
# Desc: Given a list of integers with a length of 3, return a list with the
#  elements "rotated left" so [1, 2, 3] yields [2, 3, 1].
#
# Sample function calls & results:
# RotateLeft ([1, 2, 3]) → [2, 3, 1]
# RotateLeft ([5, 11, 9]) → [11, 9, 5]
# RotateLeft([7, 0, 0]) → [0, 0, 7]
#
# Date: 27 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def rotateLeft(valueList):
    return [valueList[1], valueList[2], valueList[0]]

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    numberList = [6,8,5]

    # PROCESS

    result = rotateLeft(numberList)

    # OUTPUT
    print("\nThe list with the elements rotated left is " + str(result))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()