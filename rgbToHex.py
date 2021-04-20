#    Coding Challenge:    Return Hex
#    By:                  Lyman McBride
#    Date:                4/20/2021

#    Purpose:             This is a level 5 on CodeWars. The function takes in an RGB value and returns
#                         a Hex key value

#    Runtime:             O(2N) = O(N)

def rgb(r, g, b):
    #your code here :)
    originalList = [r,g,b]
    valuesList = []
    returnString = ""
    hexLetters = ("A", "B", "C", 'D', 'E', 'F')

    for num in originalList:
        if num > 255: 
            num = 255
        if num < 0:
            num = 0
        valuesList.append(num//16)
        valuesList.append(num-((num//16)*16))

    for num in valuesList:
        if num > 9:
            i = num-10
            returnString += hexLetters[i]
        else:
            returnString += str(num)
    
    return returnString

print(rgb(-20,275,125))