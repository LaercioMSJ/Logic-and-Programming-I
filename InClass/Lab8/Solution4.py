###########################################
# Desc: Given a list of integers with a length of 3, return the sum of all the elements.
#
# Sample function calls & results:
# SumList([1, 2, 3]) → 6
# SumList ([5, 11, 2]) → 18
# SumList ([7, 0, 0]) → 7
#
# Date: 23 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    numberList1 = [1,5,3]

    # PROCESS

    sumOfAllTheElements = numberList1[0] + numberList1[1] + numberList1[2]

    # OUTPUT
    print("The sum of all the elements is " + str(sumOfAllTheElements))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()