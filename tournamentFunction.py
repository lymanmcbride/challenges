#    Coding Challenge:    Tournament Function
#    By:                  Lyman McBride
#    Date:                4/7/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program takes an array of numbers and puts them through a 
#                         tournament. The lowest of each pair is eliminated and the higher 
#                         continues on to the next round. It returns an array of arrays of 
#                         the competition.

def tournament(array):
    final_lineUp = [array]
    while len(array) > 1:
        newArray = []
        if (len(array) % 2 != 0):
            newArray.append(array[len(array) - 1])
        for i, num in enumerate(array):
            try:
                if i % 2 == 0:
                    nextNum = array[i+1]
                    if num > nextNum:
                        newArray.append(num)
                    else:
                        newArray.append(nextNum)
            except IndexError:
                continue
        array = newArray
        final_lineUp.append(array)
        
    return final_lineUp

print(tournament([9,5,4,7,6, 5,3,8,2]))