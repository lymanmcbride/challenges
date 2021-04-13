#    Coding Challenge:    Hashtag Generator
#    By:                  Lyman McBride
#    Date:                4/13/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program takes a string, and returns it with a # in front and 
#                         with all words together and capitalized.

import re

def hashtag(string):
    return False if len(string) > 140 or string == "" else "#" + re.sub(r'[^\w\s]', '', string).title().replace(" ", "") 

print(hashtag("This,.';\"'' is a roundtable coding challenge!"))
print(hashtag(""))
print(hashtag(
    "This,.';\"'' is a roundtable coding challenge!This,.';\"'' is a roundtable coding challenge!" + 
    "This,.';\"'' is a roundtable coding challenge! This,.';\"'' is a roundtable coding challenge!Th" + 
    "is,.';\"'' is a roundtable coding challenge!This,.';\"'' is a roundtable coding challenge!"
    ))
        