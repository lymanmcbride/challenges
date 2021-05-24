import operator
import re

class Calculator(object):
    def evaluate(self, string):
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }   

        string = re.sub(r'[ ]', "", string)
        non_numbers = "/*+-()"
        priority1 = "("
        priority2 = "*/"
        storage=[]
        counter = 0
        for i, item in enumerate(string):
            if i == counter:
                if item not in non_numbers:
                    string_operator = ""
                    if i < len(string)-1:
                        string_operator = string[i+1]
                    if i < len(string)-2 and string_operator in priority2:
                        storage.append(self.operate(string, i, ops))
                        counter += 3
                    else:
                        storage.append(int(item))
                        counter += 1
                else:
                    storage.append(item)
                    counter += 1
        counter = 0
        result = 0
        for i, item in enumerate(storage):
            if i == counter:
                if i == 0:
                    result = item
                    counter += 1
                else:
                    do_math = ops[item]
                    result = do_math(result, storage[i+1])
                    counter += 2

        return result

    def operate(self, string, i, ops):
        num_left = int(string[i])
        num_right = int(string[i+2])
        do_math = ops[string[i+1]]
        result = do_math(num_left, num_right)
        return result


print(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )"))

# if you're on number, and any of the three contains opern paren, append first two to bottom of list
# if you're on paren, go to the next one. 
# if you're on number and there's no paren, or a close paren in the next 4, operate.

# count open parens in string
# go that far deep, operate until down to one number
# then reset and go next level up.


# paren
# exponents
# multiply and divide
# add and subtract 