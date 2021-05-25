#    Coding Challenge:    Calculator
#    By:                  Lyman McBride
#    Date:                5/24/2021

#    Purpose:             3ku on Code Wars Website. 
#                         Method takes a string and returns a float. 
#                         Performs math on the input string according to 
#                         order of operations.


import operator

class Calculator(object):
    def evaluate(self, string):
        array = string.split(" ")

        # how many levels deep in Parntheses do we go
        level = array.count("(")

        #do all math inside each parens until parens are gone
        while level > 0:
            array = self.get_paren_results(array, level)
            level -= 1

        # do remaining math without parens
        return self.get_math_done(array) 

    def get_paren_results(self, array, level):
        paren_count = 0 #declare for use below
        for i, item in enumerate(array):
            if item == "(":
                paren_count += 1
            if paren_count == level: #aka, are we down to the lowest level
                end_index=i #declare end index and find below
                #finds the end_index
                for item in array[i+1:]:
                    end_index += 1
                    if array[end_index] == ")":
                        break
                
                temp_result = 0
                #if what is inside of these parens needs no math (it look like (2*) or something like that)
                if len(array[i+1:end_index]) == 2:
                    temp_result = array[i+1:end_index] #set our temporary result to this array
                else:
                    #do the math inside those parens
                    temp_result = self.get_math_done(array[i+1:end_index])
                #re-assemble the array with the result of inner parens in place
                new_array = array[:i]
                new_array.append(temp_result)
                new_array = new_array + array[end_index+1:]
                return new_array

    def get_math_done(self, array):
        #helpful operator variables
        non_numbers = "/*+-"
        priority2 = "*/"

        #do all times and divide first
        while "*" in array or "/" in array:
            for i, item in enumerate(array):
                #if the item is a number
                if str(item) not in non_numbers:
                    #find the operator
                    array_operator = ""
                    if i < len(array)-1:
                        array_operator = array[i+1]
                    # if there is potential math to do (not on final two) and it's times or divide
                    if i < len(array)-2 and array_operator in priority2:
                        #operate
                        result = self.operate(array, i)

                        #reconstruct the array
                        tempArray = array[:i]
                        tempArray.append(result)
                        if i+2 < len(array): #if there is anything after current math
                            tempArray += array[i+3:]
                        #make the array the newly constructed one
                        array = tempArray

        #do the rest of the math
        while len(array) > 1:
            #operate on first one
            result = self.operate(array, 0)

            #if there is more than just one operation to do
            if len(array) > 3:
                new_array = [result] + array[3:]
                array = new_array
            else:
                array = [result]

        #pull out the num and return it
        for num in array:
            return float(num)

    def operate(self, array, i):
        #operators
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        num_left = float(array[i])
        num_right = float(array[i+2])
        operatr = ops[array[i+1]]
        result = operatr(num_left, num_right)
        return result


print("your answer is {}".format(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )")))
print("your answer is {}".format(Calculator().evaluate("4 * ( 3 * ( 2 * ( 2 * 1 ) ) )")))
print(Calculator().evaluate("2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"))
print(Calculator().evaluate("2 / 2 + 3 * 4 - 6"), 7)
print(Calculator().evaluate("3 * 4 + 3 * 7 - 6"))
print(Calculator().evaluate('1 + 1'))
print(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )"))
print(Calculator().evaluate("( ( ( ( ( ( ( 5 ) ) ) ) ) ) )"))
print(Calculator().evaluate("2 * ( 2 * ( 2 * ( 2 * 1 ) ) )"))
print(Calculator().evaluate("3 * ( 4 + 7 ) - 6"))