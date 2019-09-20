###########################################
# Desc: Write a program to display information and alter a user-entered string value.
# Your program should prompt the user to enter a word or short phrase. Ex. My dog has fleas.
# Using the entered phrase, create output to show the following:
# Confirm the phrase the user typed, with no changes
# Display the phrase in all uppercase, then all lowercase
# Display how many lowercase o’s the phrase contains
# Display whether the phrase contains only alpha-numeric characters (Display true or false)
# Finally, change any lowercase s’s in the phrase to lowercase z’s
#
# Author: Laercio.
###########################################

def main():
    # Main function for execution of program code.
    # Make sure you tab once for every line.

    # Input
    phrase = input("Write a phrase? ")

    # Process

    # Output
    print("Your phrase is: " + phrase)
    print("Your phrase in all uppercase is: " + phrase.upper())
    print("Your phrase in all lowercase is: " + phrase.lower())
    print("How many lowercase o’s your phrase contains: " + str(phrase.count('o')))
    print("Your phrase contains only alpha-numeric characters: " + str(phrase.isalnum()))
    print("All lowercase s’s in your phrase have been changed to lowercase z’s: " + phrase.replace('s', 'z'))

#PROGRAM STARTS HERE. DO NOT CHANGE THIS CODE.
if __name__ == "__main__":
    main()