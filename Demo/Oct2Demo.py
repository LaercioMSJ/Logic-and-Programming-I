###########################################
# Desc: .
#
# Author: Laercio M da Silva Junior - W0433181.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # INPUT

    country = input('Where are you from? ')
    
    # PROCESS
    if country == 'CANADA':
        print('Hello')
    elif country == 'GERMANY':
        print ('Guten Tag')
    elif country == 'FRANCE':
        print('Bonjour')




    country = 'VIETNAM'
    pet = 'BEAVER'

    if country == 'CANADA' and \
        (pet == 'MOOSE' or pet == 'BEAVER'):
        print('Do you play hockey too?')
 


    monday = True
    fresh_coffee = False
    if monday:
        #you could have code here to check for fresh coffee
        
        # the if statement is nested, so this if statement
        # is only executed if the other if statement is true
        if fresh_coffee:
            print('go buy a coffee!')
        print('I hate Mondays')
    print('now you can start work')


    # OUTPUT
    # print("Hello World")

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()