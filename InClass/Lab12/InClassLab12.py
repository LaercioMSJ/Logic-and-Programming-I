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

import sys

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    listOfGuests = []

    
    fileName = "PartyGuestList.csv"
    accessMode = "w"
    try:
        myFile = open(fileName, accessMode)
    except OSError as err:
	    print("OS error: {0}".format(err))
    except:
	    print("Unexpected error:", sys.exc_info()[0])


    numberOfGuests = int(input("Enter the number of guests: "))
    
    for counter in range (0, numberOfGuests):

        nameGuest = input("\nEnter the full name of guest #" + str(counter + 1) + ": ").title()

        ageGuest = ""
        while ageGuest == "":

            try:
                ageGuest = int(input("Enter " + nameGuest + "'s age: "))

            except ValueError:
                print("Could not convert data to an integer. Please enter numeric characters only.")

        listOfGuests.append (nameGuest + ", " + str(ageGuest))


    # PROCESS
    x = 0
    while x < len(listOfGuests):
        
        try: 
            myFile.write (listOfGuests [x] + "\n")
            x += 1

        except OSError as err:
            print("OS error: {0}".format(err))

        except ValueError:
	        print("Could not convert data to an integer.")

        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    myFile.close()
    print ("\nSave successfully!!!")

    # OUTPUT


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()