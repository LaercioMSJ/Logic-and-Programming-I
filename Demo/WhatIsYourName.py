###########################################
# Desc: Enter application description here.
#
# Author: Laercio.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # Input
    name = input("What is your name? ")
    birthday_day = input("What day of the month were you born? ")

    # Process
    # Result is 'You name is X and your birthday date is Y'
    result = "Your name is " + name  \
        + " and your birthday date is " + birthday_day 

    # Outputlaer
    print(result)

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()