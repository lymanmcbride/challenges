#    CREATED FOR STEP 208 OF THE TECH ACADEMY.
#    By:                  Lyman McBride
#    Date:                5/7/2021

#    Purpose:             

            

# Coding Challenge:    Given an array of integers, write a method 
#                      to total the odd numbers.

# Runtime:             O(N)

def total_odds(array):
    count = 0
    for num in array:
        if num%2 != 0:
            count += 1
    return count

# print(total_odds([1, 3, 5, 2, 4, 6, 7, 9, 0]))


# Coding Challenge:    Given an array of integers, write a method 
#                      to sum the elements in the array, knowing that some of the 
#                      elements may be very large integers.

# Runtime:             O(N)    

def sum_array(array):
    total = 0
    for num in array:
        total += num
    return total

# print(sum_array([100, 907958574, 394747023084723, 45987450874762323, 5585874789348934]))
# Python automatically converts to bignum if needed



# Coding Challenge:    Given a string, reverse it.

# Runtime:             O(N)

def reverse_string(string):
    new_string = ""
    for i in range(len(string)-1, -1, -1):
        new_string += string[i]
    return new_string

#print(reverse_string("I love coding"))
#Not reversed in place, done quickly for simple solution.

# Coding Challenge:    Given a string, remove any repeated letters.

# Runtime:             O(N)

def remove_repeated_letters(string):
    letters = []
    return_string = ""
    for letter in string:
        if letter not in letters:
            letters.append(letter)
            return_string += letter
    return return_string

#print(remove_repeated_letters("ababcdcdeefgghihi"))

# Coding Challenge:    FizzBuzz

# Runtime:             O(1)

def fizzBuzz():
    for num in range(1, 101):
        if num%15 == 0:
            print("FizzBuzz")
        elif num%5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)

fizzBuzz()