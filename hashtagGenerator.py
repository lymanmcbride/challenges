#    Coding Challenge:    Hashtag Generator
#    By:                  Lyman McBride
#    Date:                4/13/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program takes a string, and returns it with a # in front and 
#                         with all words together and capitalized.

import re

def hashtag(string):
    return False if len(re.sub(r'[^\w\s]', '', string).replace(" ", "")) > 140 or string == "" else "#" + re.sub(r'[^\w\s]', '', string).title().replace(" ", "") 
    # First attempt at doing a challenge all in one line. This is really wacky, here's what it does:
    # return false if it's longer than 140 characters or is an empty string, otherwise make a new string that starts with #, plus regex for substituting 
    # out the punctuation from the imput string, make every word capitalized, and replace spaces with nothing.

print(hashtag("This,.';\"'' is a roundtable coding challenge!"))
print(hashtag(""))
print(hashtag(
    "This,.';\"'' is a roundtable coding challenge!This,.';\"'' is a roundtable coding challenge!" + 
    "This,.';\"'' is a roundtable coding challenge! This,.';\"'' is a roundtable coding challenge!Th" + 
    "is,.';\"'' is a roundtable coding challenge!This,.';\"'' is a roundtable coding challenge!"
    ))
        