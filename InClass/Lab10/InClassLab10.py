###########################################
# Desc: Your challenge, create a CSV file
# 
# Exercise – Party Guest List Version 2:
# 
# Ask the user to enter the names and ages of everyone attending
#  a party and store the information in a CSV file
#
# Date: 06 November 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    listOfGuests = []
    fileName = "PartyGuestList.csv"
    accessMode = "w"
    myFile = open(fileName, accessMode)


    numberOfGuests = int(input("Enter the number of guests: "))
    
    for counter in range (0, numberOfGuests):

        nameGuest = input("\nEnter the full name of guest #" + str(counter + 1) + ": ").title()

        ageGuest = input("Enter " + nameGuest + "'s age: ")

        listOfGuests.append (nameGuest + ", " + ageGuest)


    # PROCESS
    x = 0
    while x < len(listOfGuests):
        myFile.write (listOfGuests [x] + "\n")
        x += 1

    myFile.close()


    # OUTPUT
    print ("\nSave successfully!!!")

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()