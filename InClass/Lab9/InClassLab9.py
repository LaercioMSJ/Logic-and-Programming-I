###########################################
# Desc: Exercise – Random Matrix (watch out Neo)
#
# Write code that creates a 5x5 matrix and fills the matrix with random numbers between 1-100
#
# Your first line of code must be:
#
# matrix = []
# Once your matrix is created and filled, print the values to the console in the following format
# Example output...
#
# 1 4 60 3 7
# 23 5 15 3 6
# 55 1 1 7 3
# 34 77 3 99 44
# 2 88 71 35 16
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
    matrix = []
    
    # PROCESS
    for row in range(5):
        matrix.append([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])


    for counter in range(5):
        for ctr in range(1):
            print(matrix[ctr] , end = "\t")
        print()
    
    # OUTPUT


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()