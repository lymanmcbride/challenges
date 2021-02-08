#    Coding Challenge:    Return the amount of different characters that are repeated in a string
#    By:                  Lyman McBride
#    Date:                1/19/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program returns the amount of characters in a string that 
#                         are repeated at least once in the string. We assume there is only
#                         alpha-numeric content. 


def main_function():
    string = input("Please type in any string\n").lower()
    letters = []
    doubles = []
    for letter in string:
        if letter not in letters:
            letters.append(letter)
        else:
            if letter in doubles:
                continue
            else:
                doubles.append(letter)
    print("The amount of different characters that \nare repeated at least once is: {}".format(len(doubles)))

main_function()
