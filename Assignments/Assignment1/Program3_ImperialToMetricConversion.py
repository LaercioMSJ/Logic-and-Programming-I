###########################################
# Desc: Program 3 – Imperial to Metric Conversion.
#
# Write a console program that converts a weight given in tons (imperial),
# stones, pounds, and ounces to the metric equivalent in metric tons,
# kilograms, and grams. Begin by designing your solution to this problem
# in pseudocode, which will be submitted along with the program.
#
# After the numbers of tons, stones, pounds, and ounces are input by the user,
# the weight should be converted entirely into ounces (the lowest common denominator)
# and then divided by 35.274 to obtain the value in kilos. The Python int function
# should be used to break the total number of kilos into a whole number of metric
# tons and kilos. The number of grams should be displayed to one decimal place.
#
# Required formulas:
# total ounces = 35840 * tons + 224 * stone + 16 * pounds + ounces
# total kilos = total ounces / 35.274
# metric tons = int(kilos/1000)
#
# Author: Author: Laercio M da Silva Junior - W0433181.
###########################################
#
# PSEUDOCODE:
# Request the number of tons
# Request the number of stone
# Request the number of pounds
# Request the number of ounces
# Calculate the total of weight in ounces (35840 * tons + 224 * stone + 16 * pounds + ounces)
# Convert the total of weight in ounces to kilos (total ounces / 35.274)
# Convert the total of weight in kilos to metric tons ( int(kilos/1000) )
# Convert the total of weight in kilos to show only kilos
# Convert the total of weight in kilos to only grams
# Show on screen the metric tons, kilos, and grams
#
######################################################
#
# OBSERVATION: I converted the total weight from ounces to kilos, following what was
# requested in the announcement, but in my opinion the best would be to convert ounces
# to grams (totalWeightInOunces / 0.035274). This would facilitate the calculation of all metric units.
#
######################################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # Show program title and use \n to have a space line
    print("\nImperial To Metric Conversion")


    # INPUT
    # Declaration of imperialTons variable with input of a int value via keyboard and used \n to have a space line
    imperialTons = int(input("\nEnter the number of tons: "))
    
    # Declaration of imperialStone variable with input of a int value via keyboard
    imperialStone = int(input("Enter the number of stone: "))
    
    # Declaration of imperialPounds variable with input of a int value via keyboard
    imperialPounds = int(input("Enter the number of pounds: "))
    
    # Declaration of imperialOunces variable with input of a float value via keyboard
    imperialOunces = float(input("Enter the number of ounces: "))


    # PROCESS
    # Total of weight in ounces calculation
    # Where 35840 * tons + 224 * stone + 16 * pounds + ounces results in the desired value
    totalWeightInOunces = (35840 * imperialTons) + (224 * imperialStone) + (16 * imperialPounds) + imperialOunces
    
    # Convert the total of weight in ounces to kilos
    # Where the total of weight in ounces divided by 35.274 results in the desired value
    totalWeightInKilos = totalWeightInOunces / 35.274
    
    # Convert the total of weight in kilos to metric tons
    # Where the Python int function is used to break the total number of kilos into a whole number of metric tons
    metricTons = int (totalWeightInKilos / 1000)
    
    # Convert the total of weight in kilos to show only kilos
    # Where the Python int function and the arithmetic operator modulus (%) are used to break the total number of kilos into only 3 decimal places before the decimal point
    metricKilos = int (totalWeightInKilos % 1000)
    
    # Convert the total of weight in kilos to only grams
    # Where the arithmetic operator modulus (%) is used to break the total number of kilos into only decimal places after the decimal point
    # And multiplied by 1000 to convert to grams
    metricGrams = (totalWeightInKilos % 1) * 1000


    # OUTPUT
    # Program shows on-screen the sentence contained within the quotation marks and the value contained in the variables metricTons, metricKilos, and metricGrams
    # Used \n to have a space line
    # The format method is used to return the formatted string.
    print("\nThe metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams.".format(metricTons, metricKilos, metricGrams))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()