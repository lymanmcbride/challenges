#    Coding Challenge:    Phone Number
#    By:                  Lyman McBride
#    Date:                4/17/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program takes an array of 10 integers and returns them in 
#                         phone number format.

#    Runtime:             O(3N) = O(N)

def phoneNumber(numbers):
    areaCode = ""
    middleThree = ""
    finalFour = ""
    for num in numbers[:3]:
        areaCode += str(num)
    for num in numbers[:3]:
        middleThree += str(num)
    for num in numbers[6:]:
        finalFour += str(num)
    return "({}) {}-{}".format(areaCode, middleThree, finalFour)

print(phoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

