#Author: Alsir Elsheikh

# Define functions that will be used in lab_13-5.py

# Function to calculate the sum of a list of numbers
def sum_of_list(lst):
    total = sum(lst)
    return total

# Function to count the number of words in a sentence
def count_words(sentence):
    words = sentence.split()
    return len(words)

# Function to merge two dictionaries
def merge_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Function to capitalize all words in a list
def capitalize_words(words):
    capitalized_words = [word.capitalize() for word in words]
    return capitalized_words

# Function to remove duplicates from a list
def remove_duplicates(lst):
    unique_lst = list(set(lst))
    return unique_lst

# Function to find the average of a list of numbers
def find_average(lst):
    avg = sum(lst) / len(lst)
    return avg

# Function to find the longest word in a list of words
def find_longest_word(words):
    longest_word = max(words, key=len)
    return longest_word

# Function to check if a word is a palindrome
def is_palindrome(word):
    reversed_word = word[::-1]
    return word.lower() == reversed_word.lower()

# Function to filter even numbers from a list
def even_numbers(lst):
    even_nums = [num for num in lst if num % 2 == 0]
    return even_nums

# Function to calculate the factorial of a number
def find_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial
