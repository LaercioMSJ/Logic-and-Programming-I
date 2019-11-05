###########################################
# Desc: .
#
# Date: XX October 2019
#
# Author: Laercio M da Silva Junior - W0433181
###########################################

import random

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    rows = 5
    cols = 6
    
    matrix = [ ([0] * cols) for row in range(rows) ]

    # PROCESS
    for i in range(len(matrix)):
        for x in range (len(matrix[i])):
            matrix[i][x] = random.randint(1, 100)


    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col] , end = "\t")
        print()

    
    # OUTPUT

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()