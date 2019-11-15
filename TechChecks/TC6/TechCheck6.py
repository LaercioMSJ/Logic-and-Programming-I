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
    print("Welcome to the Dungeon Attack application where none shall survive! Simply try to live as long as you can.")
    keyToQuit = input("Hit any key to continue ('Q' or 'q' to quit): ").upper()

    while keyToQuit != "Q":

        initialHitPoint = ""
        initialHitPointInt = 0
        controller = True
        while controller == True:

            try:
                initialHitPoint = input("Please enter your initial hit points (1-200): ")
                initialHitPointInt = int(initialHitPoint)

            except ValueError:
                print("You do not listen very well do you? Think you are going to survive this dungeon?")


            if (initialHitPointInt > 0 and initialHitPointInt < 201):
                controller = False
            else:
                print("You do not listen very well do you? Think you are going to survive this dungeon?")

        print("=" * 80)

        points = 0


        fileName="TC6_monsters.csv"
        accessMode="r"
        with open(fileName, accessMode) as myCSVFile:
            dataFromFile=csv.reader(myCSVFile)
            for row in dataFromFile:
                print (', '.join(row))
                print ("You were attacked by a " + str(row) + "with a " + str(row) + " attack for " + str(row) + " damage. Current hit points: " + points)



        print("Welcome to the Dungeon Attack application where none shall survive! Simply try to live as long as you can.")
        keyToQuit = input("Hit any key to continue ('Q' or 'q' to quit): ").upper()



    # OUTPUT
    


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()