#    Coding Challenge:    Pangram Challenge
#    By:                  Lyman McBride
#    Date:                2/8/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program returns whether a given string is a pangram or not.
#                         A pangram is a string that contains every letter of the alphabet
#                         at least once.

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def pangram(string, abc):
    lString = string.lower()
    if all(letter in lString for letter in abc) == True:
        print("It's a pangram!")
    else:
        print("It's not a pangram!")

string = "The uick brown fox jumps over the lazy dog"

pangram(string, abc)
