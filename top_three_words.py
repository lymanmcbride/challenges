#    Coding Challenge:    Top three Words
#    By:                  Lyman McBride
#    Date:                3/9/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program takes a string of text and returns an array of the 
#                         top 3 most occurring words in the string.
import re

def topThreeWords(string):
    # Line 14 has a lot going on. It starts with regex code, which gets rid of all the punctuation, 
    # then it runs two string methods to clean, including .split() which splits along spaces. It automatically 
    # gets rid of the extra space. 
    string_cleaner = re.sub(r'[^\w\s\']', '', string).lower().split()
    words = []
    occurrences = []
    for word in string_cleaner:
        if word not in words:
            words.append(word)
            occurrences.append(1)
        else:
            word_index = words.index(word)
            occurrences[word_index] += 1
    top_3_tuples = sorted(list(zip(occurrences, words)), reverse=True)[:3]
    results = []
    for t in top_3_tuples:
        results.append(t[1])
    print(results) # I need to add a way to control for if there's only an apostrophe in the string
    # The challenge asked for the program to return a list, however the below code
    # is a much better formatted way of returning the results. 
    # counter = 1
    # print("The Top words are:")
    # for word in top_3_tuples:
    #     print("{}. {}".format(counter, word[1]))
    #     counter += 1

topThreeWords("I   I        love's love's love's to sang sang I !?!")
