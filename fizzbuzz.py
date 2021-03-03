#    Coding Challenge:    Odd-one-out Challenge
#    By:                  Lyman McBride
#    Date:                3/2/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program prints numbers from 1-100, replacing each multiple of 3 with fizz
#                         and each multiple of 5 with buzz. If both, with fizzbuzz.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print('fizz')
    elif i % 3 != 0 and i % 5 == 0:
        print('buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    else:
        print(i)

