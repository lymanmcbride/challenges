#    Coding Challenge:    Snail Sort
#    By:                  Lyman McBride
#    Date:                5/14/2021

#    Purpose:             4ku kata on codewars. Takes a multi-dimensional array (square matrix) and sorts it
#                         by going in a clock-wise spiral.
# 
#    Runtime:             O(N)?

def snail(snail_map):
    return_array = []
    len_inner_array = len(snail_map[0])
    top_index = 0
    top_start = 0
    top_end = len_inner_array
    right_start = 1
    right_end = len(snail_map) - 1
    right_index = len_inner_array - 1
    bottom_start = len_inner_array - 1
    bottom_end = -1
    bottom_index = len(snail_map) - 1
    left_start = len(snail_map) - 2
    left_end = 0
    left_index = 0
    ## some kind of while loop
    while top_start <= top_end:
        for i in range(top_start, top_end):
            return_array.append(snail_map[top_index][i])
        top_index += 1
        top_start += 1
        top_end -= 1

        if right_start <= right_end:
            for i in range(right_start, right_end):
                return_array.append(snail_map[i][right_index])
            right_start += 1
            right_end -= 1
            right_index -= 1
        else: break

        if bottom_start >= bottom_end:
            for i in range(bottom_start, bottom_end, -1):
                return_array.append(snail_map[bottom_index][i])
            bottom_start -= 1
            bottom_end += 1
            bottom_index -= 1
        else: break

        if left_start >= left_end:
            for i in range(left_start, left_end, -1):
                return_array.append(snail_map[i][left_index])
            left_start -= 1
            left_end += 1
            left_index += 1
        else: break

    return return_array




array = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]

print(snail(array))