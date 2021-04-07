#    Coding Challenge:    Sort string by first letter
#    By:                  Lyman McBride
#    Date:                4/7/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program takes a sentence as a string, and returns a sentence 
#                         of the same words sorted alphabetically, lowercase letters at the beginning
#                         and uppercase at the end.

import re

def main():
    sentence = input("Please enter any sentence")
    stringCleaner = re.sub(r'[^\w\s]', '', sentence)
    sortSentence(stringCleaner)

def sortSentence(sentence):
    sentenceArray = sentence.split(" ")
    uppercase = []
    lowercase = []
    for word in sentenceArray:
        if word[0].isupper():
            uppercase.append(word)
        else:
            lowercase.append(word)

    lowercase.sort()
    uppercase.sort()
    sortedArray = lowercase + uppercase
    sortedsentence = ""
    for word in sortedArray:
        sortedsentence += word + " "
    print(sortedsentence)
    
main()