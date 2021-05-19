#    Coding Challenge:    Format Ordered List
#    By:                  Lyman McBride
#    Date:                5/19/2021

#    Purpose:             4ku Kata on Code Wars
#                         Create a function that takes a list of ascending-ordered integers
#                         Return a string formatted so that the integers are separated by commas
#                         If three or more in a row ascend by step, show a range of numbers using a dash
#                             - (5,6,7 becomes 5-7)
# 
#    Runtime:             O(N)

# original plan:
    # declare string
    # loop through args
    # add first one
    # check for adjacency
    # add num if not three adjacent, 
    # otherwise, go to end of adjacent nums and add that one with a dash.

def solution(args):
    string = "" #return string
    current_index = 0 #helps control for which index to perform operations on

    for i, num in enumerate(args):
        if i == current_index: #changes based on whether a range had been detected before
            num_range = True
            #if not on last two in list(where range is no longer possible)
            if i < len(args) - 2:
                #if the next number and the number ater are not 1 step up from each other (creating a range)
                if args[i+1] - num != 1 or args[i+2] - args[i+1] != 1: 
                    num_range = False
            #if not a range or index is in final two of list
            if not num_range or i > len(args) - 3:
                string += "{}".format(num) #add number
                current_index = i+1
            else: #otherwise make a range
                end_index = find_end_num(i, args)
                string += "{}-{}".format(num, args[end_index]) #format range
                current_index = end_index + 1
            if current_index < len(args):
                string += "," #add comma if not last number
        else:
            continue
    return string


def find_end_num(i, args):
    difference = 1
    current = i
    next = i+1
    #while loop finds where the range ends
    while difference == 1 and next < len(args):
        difference = args[next] - args[current]
        if difference == 1:
            current += 1
            next += 1
    return current

print(solution([-1, 5, 7, 8, 9, 10, 15, 18, 20]))
print(solution([-1, 0, 1, 5, 7, 8, 9, 10, 15, 18, 20]))
print(solution([-1, 5, 7, 8, 9, 10, 15, 18, 19, 20]))
print(solution([-1, 0, 1, 2, 3, 4, 5, 6]))