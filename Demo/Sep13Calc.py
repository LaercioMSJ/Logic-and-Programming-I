###########################################
# Desc: Enter application description here.
#
# Author: Laercio.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # Input
    num1 = input("What is the first number? ")
    num2 = input("What is the second number? ")
    # Process
    result = float(num1) + float(num2)
    #print("Variable type is " + str(type(result)))

    # Outputlaer
    print("Result is " + str(round(result, 2)))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()