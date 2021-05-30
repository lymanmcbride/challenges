

def addNums(string1, string2):
    finalSum = ""
    for i in range((len(string1)-1), -1, -1):
        indexDifference = (len(string1)) - i
        if indexDifference <= len(string2):
            num2 = string2[-indexDifference]
            addedNums = int(string1[i]) + int(num2)
            if addedNums < 10:
                finalSum = str(addedNums) + finalSum
        else:
            finalSum = string1[i] + finalSum
        
    print(finalSum)

addNums("123", "45")
            
