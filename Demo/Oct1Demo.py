###########################################
# Desc: .
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT
    answer = input('Would you like express shipping?')

    # PROCESS
    if answer == 'yes':
        print('That will be an extra $10')



    deposit = float(input('How much would you like to deposit? ')) #input
    if deposit > 100:
        print('You get a free toaster!')
    else:
        print('Enjoy your mug!')
    print('Have a nice day')



    #Initialize the variable to fix the error
    free_toaster = False

    deposit = input('how much would you like to deposit? ') #input
        if float(deposit) > 100:
            #Set the boolean variable free_toaster to True
            free_toaster = True 

        #if the variable free_toaster is True  
        #the print statement will execute 
        if free_toaster:
            print('enjoy your toaster')


    # OUTPUT
    # print("Hello World")

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()