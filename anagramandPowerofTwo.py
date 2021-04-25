import re

def anagram(string1, string2):
    string1Letters = re.sub(r'[^a-zA-Z]', '', string1).lower()
    string2Letters = re.sub(r'[^a-zA-Z]', '', string2).lower()


    characters = {}
    characters2 = {}
    for char in string1Letters:
        if char in characters.keys():
            characters[char] += 1
        else:
            characters[char] = 1
        
    for char in string2Letters:
        if char in characters2.keys():
            characters2[char] += 1
        else:
            characters2[char] = 1
    
    return characters == characters2



print(anagram("words /.'',;", 'sword'))


def powerOfTwo(num):
    if num < 2:
        return False
    if num == 2:
        return True
    return powerOfTwo(num/2)

def two(num):
    while num>2:
        num = num/2
    return True if num == 2 else False

print(powerOfTwo(1427247692705959881058285969449495136382746624))
print(two(1427247692705959881058285969449495136382746624))