#function definitions
def main():
    greeting()
    play()

def play():
    final = ""
    num = get_number()
    final = loop_digits(num, final)
    returned(final)

def greeting():
    print("Hello, and welcome to my program!\nWhen you type in a number, the computer will take each digit and square it, then return a number where each digit has been squared. (ie: 9128 would become 811464\n")

# Play functions
def returned(final):
    print("The number returned is", final)
    again = input("Would you like to do another one? y/n").lower()
    if again == "y":
        play()
    else:
        end()

def end():
    print("Thank you for checking out this challenge!")

#getting functions and digit looping
def get_number():
    num = input("Please type in a number. For now, integers only plese!\n")
    return num

def loop_digits(num, final):
    for digit in num:
        integer = int(digit)
        squared = integer**2
        new_integer = str(squared)
        final += new_integer
    return final

main()