###########################################
# Desc: TO DO Items
# Exercise – Ottawa Baseball Fields:
# •Find the Ottawa_Ball_Diamonds.csv file on BrightSpace
# •Write an application that reads in the data from the file 
# •Ask the user what type of fields they want to list: softball, baseball, or T-Ball
# •List the FACILITYID( third column) and FIELD_NAME (6th column) of all those ball fields
#
# Date: 12 November 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

import csv

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    fileName = "InClass\\Lab11\\Ottawa_Ball_Diamonds.csv"
    accessMode = "r"

    typeOfField = input("What type of fields do you want to list? softball, baseball, or T-Ball?").upper()

    with open(fileName, accessMode) as myCSVFile:
        
        #Read the file contents
        dataFromFile = csv.reader(myCSVFile)
        
        #For loop that will run
        # #once per row
        for row in dataFromFile:
            if typeOfField == row[3].upper():
                print(row[2] + "\t" + row[5])

    # PROCESS


    # OUTPUT


#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()