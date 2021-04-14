#    Coding Challenge:    Return a list of integers
#    By:                  Lyman McBride
#    Date:                3/9/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program takes a list of numbers as strings and makes them 
#                         a list of integers. The function should be done in one line.

nums = lambda strings : [int(num) for num in strings]

print(nums(['1','2','3','4']))