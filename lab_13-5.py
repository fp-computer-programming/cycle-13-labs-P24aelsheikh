#Author: Alsir Elsheikh

import lab_13_5_functions as funcs  

# Test the functions
numbers = [1, 2, 3, 4, 5]
words = ["apple", "banana", "orange", "strawberry"]
sentence = "This is a test sentence."
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Print results of function calls
print("Sum of list:", funcs.sum_of_list(numbers))
print("Number of words in sentence:", funcs.count_words(sentence))
print("Merged dictionaries:", funcs.merge_dicts(dict1, dict2))
print("Capitalized words:", funcs.capitalize_words(words))

