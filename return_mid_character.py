#    Coding Challenge:    Return the Middle Character of a Word
#    By:                  Lyman McBride
#    Date:                1/19/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program returns the middle character of an inputted word.
#                         If the word is even, it returns the two middle characters. 
#                         It only works for single words. 

def main(name = "", word = ""):
    name, word = get_name_word(name, word)
    characters = mid_char(word)
    print("Thank you {}! The middle character(s) of this word is/are: {}".format(name, characters))
    again(name, word)

def again(name, word):
    again = input("Do you want to do it again? (y/n)\n").lower()
    go = True
    while go:
        if again == "y":
            go=False
            main(name, word)
        elif again =="n":
            print("Thank you for running my program!")
            go=False
        else:
            print("Please enter either 'y' or 'n'.\n")

def mid_char(word):
    length = len(word)
    i = length//2
    if length%2 == 0:
        return word[i-1:i+1]
    else:
        return word[i]

#Getting Functions
def get_name_word(name="", word=""):
    if name != "":
        print("Thank you for playing again!")
    else:
        print("The object of this program is to input a word of any length\nwithout hyphens and the program will return the middle\ncharacter. In the case that there are an even \nnumber of characters, it will return the middle two.\n")
        name = input("What is your name?\n").capitalize()
    word = get_word(word)
    return name, word

def get_word(word = ""):
    word = input("\nType any word\n").lower()
    return word






if __name__ == "__main__":
    main()