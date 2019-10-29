###########################################
# Desc: Write a loop that computes
# 
# The sum of all even numbers between 2 and 100 (inclusive).
# The sum of all squares between 1 and 100 (inclusive).
# The sum of all odd numbers between a and b (inclusive).
# The sum of all odd digits of n. For example, if n is 32677, the sum would be 3 + 7 + 7 = 17
#
# Date: 27 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    sumOfAllEvenNumbers = 0
    sumOfAllSquares = 0
    sumOfAllOddNumbers = 0
    A = 1
    B = 9

    sumOfAllOddDigitsOfN = 0
    N = 32677
    digit = 0


    # PROCESS
    for counter in range(2,101,2):
        sumOfAllEvenNumbers += counter


    x = 0
    while ((x * x) <= 100):
        sumOfAllSquares += (x * x)
        x +=1


    x = A
    while (x <= B):
        if (x % 2) != 0:
            sumOfAllOddNumbers += x

        x +=1


    while (N > 0):
        digit = N % 10

        if (digit % 2) != 0:
            sumOfAllOddDigitsOfN += digit

        N = int(N / 10)


    # OUTPUT
    print("\nThe sum of all even numbers between 2 and 100 (inclusive) is: " + str(sumOfAllEvenNumbers))

    print("\nThe sum of all squares between 1 and 100 (inclusive) is: " + str(sumOfAllSquares))

    print("\nThe sum of all odd numbers between a and b (inclusive) is: " + str(sumOfAllOddNumbers))

    print("\nThe sum of all odd digits of N is: " + str(sumOfAllOddDigitsOfN))


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()