#    Coding Challenge:    Highest Scoring Words
#    By:                  Lyman McBride
#    Date:                4/14/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program takes a string, and returns the word with the highest 
#                         score according to the letters' position in the alphabet. I decided
#                         not to control for punctuation in this one.

def scoreWords(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    highWord = ""
    highScore = 0
    for word in string.lower().split():
        wordScore = 0
        for letter in word:
            wordScore += (alphabet.index(letter)+1)
        if wordScore > highScore: 
            highWord = word
            highScore = wordScore
    print(highWord)
    print(highScore)

scoreWords("apples xawy are waxy")
