"""
Q3. Lists can be mixed with various types. Your task for this challenge is to
sum all the number elements in the given list. Create a function that takes
a list and returns the sum of all numbers in the list.

Examples:
• numbers_sum([1,2,"13","4","645"]) → 3
• numbers_sum([True, False, "123", "75"]) → 0
• numbers_sum([1,2,3,4,5,True]) → 15
"""


def numbers_sum(my_list):
    total = 0
    for i in my_list:
        if type(i) == int:
            total += i
    return total


print(numbers_sum([1, 2, "13", "4", "645"]))
print(numbers_sum([True, False, "123", "75"]))
print(numbers_sum([1, 2, 3, 4, 5, True]))
