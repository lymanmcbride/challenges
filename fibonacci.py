#    Coding Challenge:    nth fibonacci number 
#    By:                  Lyman McBride
#    Date:                5/5/2021

#    Purpose:             Write a function that computes the nth fibonacci number

#   Runtime:              O(N)


def fibonacci(n):
    if n > 0:
        if n == 1:
            return 1
        if n == 2:
            return 1
        count = 2
        previousNum = 1
        number = 1
        next_num = 0
        while count != n:
            next_num = previousNum + number
            previousNum = number
            number = next_num
            count += 1
        return number

print(fibonacci(6))
        