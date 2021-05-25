import operator

class Calculator(object):
    def evaluate(self, string):
        print(string)
        
        string = string.split(" ")
        print(string)
        level = string.count("(")
        paren_count = 0
        while level > 0:
            string = self.get_paren_results(string, paren_count, level)
            paren_count = 0
            level -= 1
        return self.get_math_done(string) 

    def get_paren_results(self, string, paren_count, level):
        for i, item in enumerate(string):
            if item == "(":
                paren_count += 1
            if paren_count == level:
                end_index=i
                for item in string[i+1:]:
                    end_index += 1
                    if string[end_index] == ")":
                        break
                temp_result = 0
                if len(string[i+1:end_index]) == 2:
                    temp_result = string[i+1:end_index]
                else:
                    temp_result = self.get_math_done(string[i+1:end_index])
                new_array = string[:i]
                new_array.append(temp_result)
                new_array = new_array + string[end_index+1:]
                return new_array

    def get_math_done(self, string):
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        non_numbers = "/*+-()"
        priority2 = "*/"
        storage=[]
        counter = 0
        for i, item in enumerate(string):
            if i == counter:
                if str(item) not in non_numbers:
                    string_operator = ""
                    if i < len(string)-1:
                        string_operator = string[i+1]
                    if i < len(string)-2 and string_operator in priority2:
                        print("{}{}{}".format(string[i], string[i+1], string[i+2]))
                        storage.append(self.operate(string, i, ops))
                        counter += 3
                    else:
                        storage.append(float(item))
                        counter += 1
                else:
                    storage.append(item)
                    counter += 1
        print(storage)
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
        num_left = float(string[i])
        num_right = float(string[i+2])
        do_math = ops[string[i+1]]
        result = do_math(num_left, num_right)
        return result


# print("your answer is {}".format(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )")))
# print("your answer is {}".format(Calculator().evaluate("4 * ( 3 * ( 2 * ( 2 * 1 ) ) )")))
print(Calculator().evaluate("2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"))

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