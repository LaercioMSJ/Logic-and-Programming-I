###########################################
# Desc: Write a program that computes monthly insurance according to the following schedule: 
#
#  If you are ‘Male’ and your age is    #	 But less than   #  the price of the vehicle multiplied by 
#       15 or greater 	                #          25        #             25% / 12 
#       25 	                            #          40        #             17% / 12 
#       40                              #          70 	     #             10% / 12 
#  If you are ‘Female’ and your age is  #    But less than   #	the price of the vehicle multiplied by 
#       15 or greater                   #           25       #           	20% / 12 
#       25                              #        	40       #          	15% / 12 
#       40                              #       	70       #          	10% / 12 
#
# First, create a flowchart that clearly shows all of the paths of execution that will exist
#  within your designed solution to this problem. Then, write a console application that
#  will input the sex and price of vehicle, and then output the corresponding monthly insurance amount.
# Your solution must contain examples demonstrating your understanding of appropriate
#  use of functions and core assignment concepts (decision structures).
#
# Date: 17 October 2019
#
# Author: Laercio M da Silva Junior - W0433181
###########################################


# This function selects the multiplier factor based on gender and age, and returns the selected value
def multiplierFactorSelection (gender, age):
    # Declaration of variables
    # Declaration of multiplierFactorMale variables with fixed values
    multiplierFactorMale1 = 0.25
    multiplierFactorMale2 = 0.17
    multiplierFactorMale3 = 0.10

    # Declaration of multiplierFactorFemale variables with fixed values
    multiplierFactorFemale1 = 0.20
    multiplierFactorFemale2 = 0.15
    multiplierFactorFemale3 = 0.10

    # Declaration of ageRange variables with fixed values
    ageRange1 = 15
    ageRange2 = 25
    ageRange3 = 40
    ageRange4 = 70

    # Select multiplierFactor based on gender and age entered and return it
    if gender == "male":
        if age >= ageRange1 and age < ageRange2:
            return multiplierFactorMale1

        elif age >= ageRange2 and age < ageRange3:
            return multiplierFactorMale2

        elif age >= ageRange3 and age < ageRange4:
            return multiplierFactorMale3
        
        else:
            # Program shows on-screen the error message contained within the quotation marks if the age is incorrect
            print("\nThe age you entered is incorrect. Try again.")
            return 0

    # Select multiplierFactor based on gender and age entered and return it
    elif gender == "female":
        if age >= ageRange1 and age < ageRange2:
            return multiplierFactorFemale1

        elif age >= ageRange2 and age < ageRange3:
            return multiplierFactorFemale2

        elif age >= ageRange3 and age < ageRange4:
            return multiplierFactorFemale3

        else:
            # Program shows on-screen the error message contained within the quotation marks if the age is incorrect
            print("\nThe age you entered is incorrect. Try again.")
            return 0

    else:
        # Program shows on-screen the error message contained within the quotation marks if the gender is incorrect
        print("\nThe gender you entered is incorrect. Try again.")
        return 0


# This function multiplies two values and return the result
def multiplierFunction (value1, value2):
    return value1 * value2


# This function divides two values and return the result
def dividerFunction (value1, value2):
    return value1 / value2


def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.


    # Show program title and use \n to have a space line
    print("\nAuto Insurance")


    # INPUT
    # Declaration of gender variable with input of a string via keyboard and used \n to have a space line
    userGender = str(input("\nAre you 'Male' or 'Female': ").lower())
    
    # Declaration of age variable with input of a integer value via keyboard and used \n to have a space line
    userAge = int(input("\nEnter your age: "))

    # Declaration of priceOfTheVehicle variable with input of a float value via keyboard and used \n to have a space line
    priceOfTheVehicle = float(input("\nEnter the purchase price of the vehicle: "))


    # Declaration of variables
    # Declaration of months variable with 12 months
    months = 12

    # Declaration of monthlyInsurance variable with 0
    monthlyInsurance = 0


    # PROCESS
    # Call three different functions to calculate monthlyInsurance based on multiplierFactor, priceOfTheVehicle and number of months
    monthlyInsurance = dividerFunction (multiplierFunction (priceOfTheVehicle, multiplierFactorSelection (userGender, userAge)), months)


    # OUTPUT
    # Program shows on-screen the sentence contained within the quotation marks and the value contained in the variable monthlyInsurance.
    # The format method is used to return the formatted string and used \n to have a space line.
    print("\nYour monthly insurance will be ${0:.2f}" .format(monthlyInsurance))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()