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

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT

    # PROCESS

    # OUTPUT
    print("Hello World")

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()