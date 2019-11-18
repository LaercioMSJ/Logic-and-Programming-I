###########################################
# Desc: TechCheck6.
#
# Date: 15 November 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################


import csv

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
        
 
    # PROCESS
    print("\nWelcome to the Dungeon Attack application where none shall survive! Simply try to live as long as you can.")
    keyToQuit = input("Hit any key to continue ('Q' or 'q' to quit): ").upper()

    while keyToQuit != "Q":

        controller = True
        while controller == True:

            try:
                initialHitPoint = int(input("\nPlease enter your initial hit points (1-200): "))

            except ValueError:
                initialHitPoint = -1


            if (initialHitPoint > 0 and initialHitPoint < 201):
                controller = False
            else:
                print("You do not listen very well do you? Think you are going to survive this dungeon?")

        print("\n======================================================================================================\n")

        fileName = "TC6_monsters.csv"
        accessMode = "r"
        with open(fileName, accessMode) as myCSVFile:
            dataFromFile = csv.reader(myCSVFile)
            for row in dataFromFile:
                initialHitPoint -= int(row[2])
                
                if initialHitPoint < 0:
                    initialHitPoint = 0
                    
                print ("You were attacked by a " + str(row[0]) + " with a " + str(row[1]) + " attack for " + str(row[2]) + " damage. Current hit points: " + str(initialHitPoint))

                if initialHitPoint == 0:
                    break

        print("\nWelcome to the Dungeon Attack application where none shall survive! Simply try to live as long as you can.")
        keyToQuit = input("Hit any key to continue ('Q' or 'q' to quit): ").upper()



    # OUTPUT
    


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()