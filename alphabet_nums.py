alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    greeting()
    phrase = get_phrase()
    final = change_nums(phrase)
    print("Your phrase returned", final)

def greeting():
    print("Welcome to the alphabet coding challenge.\nPlease enter a sentence and the program will return a string of numbers with each letter's position in the alphabet.\nSpaces, punctuation, and other characters will be ignored")

def get_phrase():
    phrase = input("Please type your phrase below\n").lower()
    return phrase

def change_nums(phrase):
    final = ""
    for character in phrase:
        if character in alphabet:
            for i, letter in enumerate(alphabet):
                if character == letter:
                    ind = str(i+1)
                    final += ind
                else:
                    continue
        else:
            continue
    return final


main()

#Is there a way to do this without first declaring the alphabet?
#if I were to do this again I would use a dictionary instead of a list in order to lower the Big O runtime
