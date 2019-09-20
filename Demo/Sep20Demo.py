###########################################
# Desc: .
#
# Author: Laercio.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # Input
    statement7 = "123"
    statement6 = "ronAnODriscolliscool"
    statement5 = "ronAn O'Driscoll is \"cool\""
    statement = "ronAn O'Driscoll is \"cool\""
    statement4 = "Ronan O'Driscoll is \"cool\""
    statement2 = 'Ronan O\'Driscoll\n=============='
    statement3 = 'Ronan\t O\'Driscoll\t=============='
    name = 'Ronan O\'Driscoll'
    bill = 23.99
    output = "Mr. {0}. Your bill is ${1}."

    # Process

    # Output
    print(statement7.isnumeric())
    print(statement6.isalpha())
    print(statement.replace('Driscoll', 'Droptable'))
    print(statement.count('D'))
    print(statement5.capitalize())
    print(statement4.lower())
    print(statement.title())
    print(statement2)
    print(statement3)
    print(output.format(name, bill))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()