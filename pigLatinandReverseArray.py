
def pigLatin(string):
    words = string.split()
    returnList = []
    for word in words:
        capitolize = False
        if word[0].isupper():
            capitolize = True
        
        lastcharIndex = len(word)-1
        if word[lastcharIndex].isalpha() == False:
            word = word[1:lastcharIndex] + word[0] + "ay" + word[lastcharIndex]
        else:
            word = word[1:] + word[0] + "ay"

        if capitolize:
            word = word.title()
        returnList.append(word)
        
    returnString = " ".join(returnList)

    return returnString

print(pigLatin("I Love, always and forever, to code!"))

## Handles spaces inbetween punctuation
def pig_it(text):
    #your code here
    text_array = text.split()
    return_array = []
    for word in text_array:
        if word.isalpha():
            return_array.append(word[1:] + word[0] + "ay")
        else:
            return_array.append(word[1:len(word)-1] + word[0] + "ay" + word[-1])
    return " ".join(return_array)
    

print(pig_it("I love to code!"))



def reverseArray(array):
    secondIndex = -1
    for i, item in enumerate(array):
        if i < (len(array))/2:
            temp = item
            array[i] = array[secondIndex]
            array[secondIndex] = temp
            secondIndex -= 1
        else:
            break
    return array

print(reverseArray([1,2,3,4]))
