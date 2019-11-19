###########################################
# Desc: Design and develop a program that replicates the
#  functionality of the provided sample application, a simple
#  version of the game Battleship.
# 
# Begin by designing your solution to this problem in pseudocode,
#  which will be submitted along with the program. Your solution
#  should demonstrate an understanding of how to apply file I/O,
#  list and looping concepts, in a Battleship program that will
#  work as follows:
# 
# On application start, your code will read the contents of the
#  provided ship grid text file into a two-dimensional list in
#  your program. This ship map will be used as the “key”,
#  indicating the locations of the five ships used in the game.
#  Zeros (0) indicate empty water, while ones (1) indicate part
#  of a ship exists at that location. The ship map will remain
#  invisible to the user during gameplay. A second map (the
#  targeting map) will be displayed to the user each turn, and
#  will be used to show the targeting results of the current
#  game turn by turn. The initial display of the targeting map
#  will be blank except for the row and column indicators
#  (Columns A, B, C, Rows 1, 2, 3, etc.).
# 
# The user will be given 30 turns to attempt to sink all five ships.
#  During each turn, the user will be prompted to enter a map
#  coordinate (ex. A2, F5, B10) representing the location at which
#  they wish to fire a missile. After each missile shot attempt,
#  your program will evaluate whether the chosen coordinate is a hit
#  or a miss and notify the user of the result. The targeting map
#  will be updated to show the latest missile result and be shown
#  to the user. A message indicating the current missile count will
#  also be displayed, used to tell the player how many turns remain.
# 
# Only valid targeting coordinates are allowed to be entered. If an
#  invalid coordinate value is entered, the user will be prompted to
#  re-enter a new coordinate until a valid coordinate is entered.
# 
# The game has two ending conditions: 
# •	If the user hits every individual location in the map that contains
#  part of a ship before running out of missiles, they win the game. 
# •	If the user runs out of missiles before hitting every part of every
#  ship, they lose the game. 
# 
# Your program should track the game’s progress and display either a
#  “You win!” or “You lose!” message when either game ending condition
#  is reached.
# 
# Your solution must contain examples demonstrating your understanding
#  of appropriate use of functions and core assignment concepts
#  (file I/O, 2-d lists).
# 
# Bonus Marks: Add functionality to the game such that the user is
#  notified when a particular ship has been definitively sunk. You’ll
#  likely need to modify the contents of the map so that it stores
#  more than just ones and zeros in order to identify each ship
#  individually.
# 
# Refer to the provided sample application for guidance. Your
#  completed program should duplicate the sample game functionality
#  as closely as possible.
#
# Date: 17 November 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################
#
# PSEUDOCODE:
# Open the map.txt file and save in a 2D list
# Create a new 2D list to be the board
# Request the coordenate to the user
# Validate the coordinate,and if necessary, request the coordinate again
# Compare the coordinate entered by the user with the game coordinates
# If the coordinate is the same as a ship's coordinate, hit is incremented and "X" is added to the board.
# If different coordinates, "O" is added to the board
# The number of missiles is decreased
# Show the board updated with the last user coordinates
# Repeat the previous 7 tasks until the user hits all ships or the number of missiles goes to 0.
# Show a victory message if user hits all ships, or a game over message if missiles go to 0
#
######################################################

import csv


# This function selects a number based on letters A-F,
#  and returns the number between 1 and 11
def letterValidation (value):
    if value == "A":
        return 1
    elif value == "B":
        return 2
    elif value == "C":
        return 3
    elif value == "D":
        return 4
    elif value == "E":
        return 5
    elif value == "F":
        return 6
    elif value == "G":
        return 7
    elif value == "H":
        return 8
    elif value == "I":
        return 9
    elif value == "J":
        return 10
    else:
        return 11


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    print("\nLet's play Battleship!")

    # INPUT
    # Declaration of variables and lists
    missiles = 30
    hits = 0
    allShips = 17
    board = []
    mapOriginal = []


    # Open the map file with the coordenates of the ships, save all
    #  information on mapOriginal 2Dlist and close the file
    fileName = "map.txt"
    accessMode = "r"

    with open(fileName, accessMode) as myTXTFile:

        mapFile = csv.reader(myTXTFile)

        for row in mapFile:
            mapOriginal.append (row)


    # PROCESS AND OUTPUT
    # Program shows on-screen the sentence contained within the quotation marks
    print ("You have " + str(missiles) + " missiles to fire to sink all five ships.\n")

    # Completes the entire board with the coordinates at the beginning of each
    #  row and column, and adds empty to the rest of the board (a 2D list 11 per 11)
    for row in range(11):
        board.append(["  ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])

    board[0] = [" ", "A", "B", "C", "D","E", "F", "G", "H", "I", "J"]

    for i in range(1,11):
        board[i][0] = i


    # WHILE loop is used to repeat each turn of the game
    while True:

        # FOR loop is used to shows on-screen the entire 2D list (board) neatly and updated every turn
        for row in range (11):
            for column in range (11):
                print (board[row][column] , end = " ")
            print()
        print()

        # WHILE loop is used to take a user's target and validate it
        while True:

            # Declaration of targetList with empty
            targetList = []

            # Declaration of target variable with input of a string via keyboard
            target = str(input("Choose your target (Ex. A1): ")).upper()

            # If user input nothing or more than 3 chars, repeat the loop
            if ( (len(target)) > 3 or (len(target)) == 0 ):
                continue

            # Otherwise each char is added to targetList
            else:
                for char in target:
                    targetList.append (char)

            # If user input 3 chars, the third char is added to the second char (when user input the coordinate number 10)
            if (len(target)) == 3:
                targetList[1] += targetList[2]

            # Call the letterValidation function to select a unique number for each letter using the first char that user input
            letter = letterValidation (targetList[0])

            # Try to change string to integer using the second char that user input, and in case of error repeat the loop
            try:
                number = int(targetList[1])
            except:
                continue

            # If the first char that user input is a letter between A-F and the second char
            #  that user input is a number between 1-10, exit the loop and execute the rest of the code
            if (number > 0 and number < 11 and letter != 11):
                break


        # If the user's target is equals the coordinates of the file, so that same coordinate on the board gets "X", and the hits increment by 1 more
        if mapOriginal[number - 1][letter - 1] == "1":
            board[number][letter] = "X"
            hits += 1
            print ("HIT!!!!!")

        # Otherwise that same coordinate on the board gets "O"
        else:
            board[number][letter] = "O"
            print ("Miss")


        # If user hits the correct ship coordinate 17 times (there are 5 ships occupying 17 coordinates in this game), the game ends, and the user wins
        if hits == allShips:
            print ("YOU SANK MY ENTIRE FLEET!")
            print ("You had " + str(hits) + " of " + str(allShips) + " hits, which sank all the ships.")
            print ("You won, congratulations!")
            break


        # Each turn the number of missiles is decreased by 1
        missiles -= 1
        print ("You have " + str(missiles) + " missiles remaining")


        # When the number of missiles goes to 0 (30 turns in this game), the game ends and the user is defeated
        if missiles == 0:
            print ("GAME OVER.")
            print ("You had " + str(hits) + " of " + str(allShips) + " hits, but didn't sink all the ships.")
            print ("Better luck next time.")
            break


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()