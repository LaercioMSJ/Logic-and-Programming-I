###########################################
# Desc: Given an integer list of length 2, return True if it contains a 2 or a 3.
#
# Sample function calls & results:
# Has2Or3 ([2, 5]) → True
# Has2Or3 ([4, 3]) → True
# Has2Or3 ([4, 5]) → False
#
# Date: 27 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def has2Or3(valueList):
    return (2 in valueList or 3 in valueList)

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    numberList = [7,2]

    # PROCESS

    result = has2Or3(numberList)

    # OUTPUT
    print("\nThe list contains a 2 or a 3: " + str(result))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()