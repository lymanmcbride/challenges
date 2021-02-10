#    Coding Challenge:    Odd-one-out Challenge
#    By:                  Lyman McBride
#    Date:                2/10/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program takes an array, and returns the number that 
#                         is not equal to the other numbers

def odd_one_out(array):
    count = 0
    num1 = 0
    num2 = 0
    same_num = 0
    for i, num in enumerate(array):
        if num1 == num2:
            num1 = num
            num2 = array[i+1]
            if num == array[i+1]:
                same_num = num
                count += 1
        elif count < 1 and num == array[i+1]:
            same_num = num
            count += 1
        else:
            continue
    if same_num == num1:
        string = "The odd one out is {}".format(num2)
    else:
        string = "The odd one out is {}".format(num1)
    print(string + "\nThe other numbers are all {}".format(same_num))
            

array = [1, 2, 1, 1, 1]
odd_one_out(array)
        


