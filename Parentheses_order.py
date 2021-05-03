#    Coding Challenge:    Parentheses 
#    By:                  Lyman McBride
#    Date:                5/3/2021

#    Purpose:             Write a function that takes a string of parentheses, 
#                         and determines if the order of the parentheses is valid. 
#                         The function should return true if the string is valid, 
#                         and false if it's invalid.

#   Runtime:              O(N)


def parentheses(string):
    print(string)
    one = "("
    close = ")"
    stack = []
    for paren in string:
        if paren == one:
            stack.append(paren)
        elif paren == close:
            if len(stack) > 0:
                stack.pop()
            else:
                return False

    return True if len(stack) == 0 else False

print(parentheses("  ("))