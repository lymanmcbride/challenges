def average(array):
    new_array = []
    last_i = (len(array) - 1)
    for i, num in enumerate(array):
        if i < last_i:
            num2 = array[i+1]
            value = (num + num2)/2
            if (num + num2)%2 == 0:
                int_value = int(value)
                new_array.append(int_value)
            else:
                new_array.append(value)
    return new_array

nums = [5, 3, 4, 2]
print(average(nums)) 