###########################################
# Desc: Rewrite the following for loop as a while loop.
# 
# s = 0
# for i in range(1, 10):
#   s = s + i
#
# Date: 27 October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT

    # PROCESS
    s = 0
    x = 1
    while (x < 10):
        s = s + x
        x += 1


    s = 0
    for i in range(1, 10):
        s = s + i


    # OUTPUT
    print("Using While " + str(s))
    print("Using For " + str(s))



#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()