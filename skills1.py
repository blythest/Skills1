# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    new_list = some_list[1::2]
    return new_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    new_list = some_list[::2]
    return new_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    
    new_list = []
    for i in range(len(word_list)):
        if len(word_list[i]) >= 4:
            new_list.append(word_list[i])
    return new_list


# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    min_num = some_list[0]
    for i in range(len(some_list)):
        if some_list[i] <= min_num:
            min_num = some_list[i]
    return min_num

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    max_num = some_list[0]
    for i in range(len(some_list)):
        if some_list[i] >= max_num:
            max_num = some_list[i]
    return max_num
# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    halvesies = []
    for i in range(len(some_list)):
        halvesies.append((some_list[i]/2))
    return halvesies

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    lengths = []
    for i in range(len(word_list)):
        lengths.append(len(word_list[i]))
    return lengths

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    product = 1
    for i in range(len(numbers)):
        product *= numbers[i]
    return product

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    total_str = ''
    for i in range(len(string_list)):
        total_str += string_list[i]
    return total_str
# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    total = 0
    count = 0
    for i in range(len(numbers)):
        total += numbers[i]
        count += 1
    return total/count