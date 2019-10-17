###########################################
# Desc: .
#
# Date: XX October 2019
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    gender = input ("\nAre you 'Male' or 'Female': ").lower()

    age = int(input("\nEnter your age: "))

    price = float(input("\nEnter the purchase price of the vehicle: "))

    result = 0

    multiplierFactor = 0

    # PROCESS
    if gender == "male":
        if age >= 15 and age < 25:
            result = (price * 0.25) / 12

        elif age >= 25 and age < 40:
            result = (price * 0.17) / 12

        elif age >= 40 and age < 70:
            result = (price * 0.10) / 12
        
        else:
            print("\nThe age you entered is incorrect. Try again.")


    elif gender == "female":
        if age >= 15 and age < 25:
            result = (price * 0.20) / 12

        elif age >= 25 and age < 40:
            result = (price * 0.15) / 12

        elif age >= 40 and age < 70:
            result = (price * 0.10) / 12

        else:
            print("\nThe age you entered is incorrect. Try again.")

    else:
        print("\nThe gender you entered is incorrect. Try again.")



    # OUTPUT
    print("\nYour monthly insurance will be ${0:.2f}" .format(result))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()